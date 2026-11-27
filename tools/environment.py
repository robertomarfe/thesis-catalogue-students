#!/usr/bin/env python3
"""Neutral runtime acceptance. No thesis data, credentials, publication or remote writes."""
from __future__ import annotations
import argparse
import hashlib
import importlib.metadata as md
import json
import os
from pathlib import Path
import platform
import secrets
import socket
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request
import venv

ROOT = Path(__file__).resolve().parents[1]
REQ = ROOT / 'tools/runtime_requirements.txt'
DEMO = ROOT / 'demo/runtime_check.ipynb'
ENV = ROOT / '.venv'
RECEIPT = ROOT / '.runtime-check/receipt.json'


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pins():
    result = {}
    for line in REQ.read_text().splitlines():
        if line.strip() and not line.startswith('#'):
            name, version = line.split('==', 1)
            result[name] = version
    return result


def check_kernel(folder):
    import nbformat
    from nbclient import NotebookClient
    from jupyter_client import KernelManager
    from jupyter_client.kernelspec import KernelSpecManager
    spec = folder / 'kernels' / 'runtime-check'
    spec.mkdir(parents=True)
    (spec / 'kernel.json').write_text(json.dumps({
        'argv': [sys.executable, '-m', 'ipykernel_launcher', '-f', '{connection_file}'],
        'display_name': 'Isolated runtime check', 'language': 'python'}))
    manager = KernelSpecManager(kernel_dirs=[str(spec.parent)], ensure_native_kernel=False)
    km = KernelManager(kernel_name='runtime-check', kernel_spec_manager=manager)
    before = sha(DEMO)
    nb = nbformat.read(DEMO, as_version=4)
    nbformat.validate(nb)
    cells = [c for c in nb.cells if c.cell_type == 'code']
    require(len(cells) == 1 and not cells[0].outputs and cells[0].execution_count is None,
            'Expected one unexecuted neutral code cell')
    try:
        NotebookClient(nb, km=km, timeout=30, resources={'metadata': {'path': str(folder)}}, allow_errors=False).execute()
    finally:
        if km.has_kernel:
            km.shutdown_kernel(now=True)
    output = ''.join(o.get('text', '') for o in cells[0].outputs if o.output_type == 'stream')
    require('RUNTIME_CHECK_PASS' in output and 'PYTHON=' + sys.executable in output,
            'Unexpected notebook result or interpreter')
    require(sha(DEMO) == before, 'Original notebook changed')
    return {'code_cells': 1, 'executed': True, 'original_sha256': before, 'correct_interpreter': True}


def check_lab(folder):
    # Actual loopback HTTP only. Never forward a port or expose a token.
    with socket.socket() as sock:
        sock.bind(('127.0.0.1', 0))
        port = sock.getsockname()[1]
    token = secrets.token_urlsafe(32)
    env = dict(os.environ)
    for key in ('JUPYTER_CONFIG_DIR', 'JUPYTER_RUNTIME_DIR', 'JUPYTER_DATA_DIR'):
        p = folder / key.lower(); p.mkdir(); env[key] = str(p)
    env['JUPYTER_TOKEN'] = token
    class NoRedirect(urllib.request.HTTPRedirectHandler):
        def redirect_request(self, req, fp, code, msg, headers, newurl):
            return None
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}), NoRedirect())
    def request(path, auth=False):
        req = urllib.request.Request(f'http://127.0.0.1:{port}{path}',
              headers={'Authorization': 'token ' + token} if auth else {})
        try:
            with opener.open(req, timeout=2) as res:
                return res.status, res.read(2_000_000)
        except urllib.error.HTTPError as ex:
            return ex.code, b''
    cmd = [sys.executable, '-m', 'jupyterlab', '--no-browser', '--ServerApp.ip=127.0.0.1',
           '--ServerApp.port=' + str(port), '--ServerApp.port_retries=0',
           '--ServerApp.root_dir=' + str(folder), '--ServerApp.allow_remote_access=False']
    proc = subprocess.Popen(cmd, cwd=folder, env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        end = time.monotonic() + 40
        while time.monotonic() < end:
            require(proc.poll() is None, 'JupyterLab process exited before readiness')
            try:
                status, raw = request('/api/contents', True)
                if status == 200 and json.loads(raw).get('type') == 'directory':
                    break
            except (OSError, ValueError):
                pass
            time.sleep(.5)
        else:
            raise RuntimeError('JupyterLab loopback readiness check failed')
        unauth, _ = request('/api/contents')
        require(unauth in (401, 403), 'Unauthenticated API unexpectedly accessible')
        lab, body = request('/lab', True)
        require(lab == 200 and b'jupyterlab' in body.lower(), 'Authenticated Lab page unavailable')
        return {'bind': 'loopback only', 'unauthenticated_api_status': unauth,
                'authenticated_api_status': status, 'authenticated_lab_status': lab}
    finally:
        proc.terminate()
        try:
            proc.wait(timeout=10)
        except subprocess.TimeoutExpired:
            proc.kill(); proc.wait(timeout=10)


def probe(require_isolated=True, lab=True):
    require(sys.version_info[:2] == (3, 13), 'Python 3.13 required')
    if require_isolated:
        require(sys.prefix != sys.base_prefix, 'Not in a virtual environment')
        cfg = (Path(sys.prefix) / 'pyvenv.cfg').read_text().lower()
        require('include-system-site-packages = false' in cfg, 'System packages must be disabled')
    versions = {name: md.version(name) for name in pins()}
    require(versions == pins(), 'Direct dependency versions differ from pins')
    # pip check is meaningful for the freshly isolated environment only.
    if require_isolated:
        subprocess.run([sys.executable, '-m', 'pip', 'check'], check=True)
    with tempfile.TemporaryDirectory(prefix='thesis-runtime-check-') as tmp:
        folder = Path(tmp)
        k = check_kernel(folder)
        http = check_lab(folder) if lab else {'status': 'not run'}
    return {'schema': 1, 'kind': 'neutral_runtime_acceptance', 'python': platform.python_version(),
            'platform': platform.system() + ' ' + platform.machine(), 'isolated_no_system_packages': require_isolated,
            'requirements_sha256': sha(REQ), 'direct_versions': versions,
            'installed_versions': {d.metadata['Name']: d.version for d in md.distributions() if d.metadata['Name']},
            'pip_check': 'pass' if require_isolated else 'not run for reused host',
            'notebook': k, 'jupyterlab': http, 'thesis_content': False, 'published': False}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('command', choices=['setup', 'check', '_probe'])
    a = p.parse_args()
    require(sys.version_info[:2] == (3, 13), 'Select the repository Python 3.13 devcontainer')
    if a.command == '_probe':
        result = probe()
        RECEIPT.parent.mkdir(parents=True, exist_ok=True)
        tmp = RECEIPT.with_suffix('.tmp')
        tmp.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
        tmp.replace(RECEIPT)
        print('RUNTIME VERIFIED: dependency check, exact pinned versions, notebook and token-protected loopback JupyterLab.', flush=True)
        return
    py = ENV / ('Scripts/python.exe' if os.name == 'nt' else 'bin/python')
    if RECEIPT.exists():
        RECEIPT.unlink()  # Invalidate this tool's own prior receipt before any new attempt.
    if a.command == 'setup' and not ENV.exists():
        print('Creating new isolated virtual environment.', flush=True)
        venv.EnvBuilder(with_pip=True, system_site_packages=False).create(ENV)
        subprocess.run([str(py), '-m', 'pip', 'install', '--disable-pip-version-check', '-r', str(REQ)], check=True)
        fresh = True
    else:
        require(py.is_file(), 'No complete environment; use setup in a fresh Codespace')
        print('Checking existing environment; not a new clean install.', flush=True)
        fresh = False
    subprocess.run([str(py), str(Path(__file__).resolve()), '_probe'], check=True)
    result = json.loads(RECEIPT.read_text())
    result['fresh_install_this_run'] = fresh
    tmp = RECEIPT.with_suffix('.tmp')
    tmp.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
    tmp.replace(RECEIPT)
    print('Acceptance receipt: .runtime-check/receipt.json (local, not committed).', flush=True)


if __name__ == '__main__':
    main()
