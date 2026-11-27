#!/usr/bin/env python3
"""Prepare an independent thesis working directory from a sealed student site.
Install the student runtime in a separate repository, never in the private master.
No network calls, data acquisition or automatic notebook execution.
"""
from __future__ import annotations
import argparse, hashlib, json, os, shutil, subprocess, sys, zipfile
from pathlib import Path
from release import verify, ROLE, ID, sha, require


def prepare(site, thesis_id, work_root):
    require(isinstance(thesis_id,str) and ID.fullmatch(thesis_id),'Invalid thesis ID')
    site=site.resolve(strict=True)
    result=verify(site)
    manifest=json.loads((site/'release-manifest.json').read_text(encoding='utf-8'))
    require(thesis_id in manifest['ids'],'Thesis not in the authorized student edition')
    root=work_root.expanduser().resolve()
    require(not root.is_relative_to(site.parent),'Work directory must be outside the student repository')
    root.mkdir(parents=True,exist_ok=True)
    dest=root/thesis_id
    archive=site/'projects'/thesis_id/'workspace-files.zip'
    expected=manifest['sha256'][archive.relative_to(site).as_posix()]
    require(sha(archive)==expected,'Archive hash changed')
    # Read once, validate before creating any files. No extractall or user-controlled paths.
    with zipfile.ZipFile(archive) as z:
        require(set(z.namelist())==ROLE and len(z.namelist())==len(ROLE),'Unexpected archive contents')
        members={f:z.read(f) for f in sorted(ROLE)}
    n=json.loads(members['student_start.ipynb'].decode('utf-8'))
    require(any(c['cell_type']=='code' for c in n['cells']) and all(not c.get('outputs') and c.get('execution_count') is None for c in n['cells'] if c['cell_type']=='code'),'Starter notebook already executed')
    # mkdir without exist_ok prevents overwrite even if the destination appears concurrently.
    dest.mkdir()
    try:
        for f,raw in members.items():
            (dest/f).write_bytes(raw)
            require(hashlib.sha256((dest/f).read_bytes()).digest()==hashlib.sha256(raw).digest(),'Copy failed')
        for sub in ('local-data','results'):
            (dest/sub).mkdir()
        origin={'thesis_id':thesis_id,'manifest_sha256':result['manifest_sha256'],'archive_sha256':expected,
                'original_members_sha256':{f:hashlib.sha256(raw).hexdigest() for f,raw in members.items()}}
        (dest/'WORKSPACE_ORIGIN.json').write_text(json.dumps(origin,indent=2,sort_keys=True)+'\n',encoding='utf-8')
        (dest/'.gitignore').write_text('local-data/\nresults/\n.ipynb_checkpoints/\n',encoding='utf-8')
    except BaseException:
        shutil.rmtree(dest)
        raise
    return dest


def launch_command(folder,port=8888,codespace=False):
    require(1024<=port<=65535,'Port must be between 1024 and 65535')
    require(not codespace or os.environ.get('CODESPACES')=='true','Codespaces mode requires an actual Codespace')
    folder=folder.resolve(strict=True)
    require((folder/'WORKSPACE_ORIGIN.json').is_file() and (folder/'student_start.ipynb').is_file(),'Not a prepared workspace')
    return [sys.executable,'-m','jupyterlab','--no-browser',
            '--ServerApp.ip='+('0.0.0.0' if codespace else '127.0.0.1'),
            '--ServerApp.port='+str(port),'--ServerApp.port_retries=0','--ServerApp.root_dir='+str(folder)]


def main():
    p=argparse.ArgumentParser(description=__doc__);sub=p.add_subparsers(dest='command',required=True)
    a=sub.add_parser('prepare');a.add_argument('--site',type=Path,required=True);a.add_argument('--id',required=True);a.add_argument('--work-root',type=Path,default=Path.home()/'thesis-research')
    b=sub.add_parser('lab');b.add_argument('--workspace',type=Path,required=True);b.add_argument('--port',type=int,default=8888);b.add_argument('--codespace-private',action='store_true')
    args=p.parse_args()
    if args.command=='prepare':
        dest=prepare(args.site,args.id,args.work_root)
        print('Workspace created:',dest)
        print('Read DATA_GUIDE.md before obtaining any authorized inputs. Do not commit raw data or results.')
    else:
        cmd=launch_command(args.workspace,args.port,args.codespace_private)
        if args.codespace_private:print('Check port visibility is Private in the Ports panel. Keep Jupyter token authentication enabled.',flush=True)
        subprocess.run(cmd,check=True)


if __name__=='__main__':main()
