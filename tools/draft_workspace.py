#!/usr/bin/env python3
"""Copy an explicitly published research draft into an independent working directory.
This is not assignment approval. No network access, execution, or data acquisition.
"""
import argparse, hashlib, json, re, shutil, zipfile
from pathlib import Path

ROLE={'proposal.pdf','proposal.md','proposal.html','methods.pdf','methods.md','methods.html','READING_GUIDE.md','READING_GUIDE.html','references.bib','DATA_GUIDE.md','DATA_GUIDE.html','student_start.ipynb','student_start.html','requirements.txt','RESEARCH_PLAN.md','RESEARCH_PLAN.html','README.md','START_HERE.html','style.css'}

def need(ok,msg):
    if not ok: raise ValueError(msg)

def prepare(site,ident,work_root):
    need(re.fullmatch(r'[AD]\d{2}\.\d{2}\.\d{2}',ident),'Invalid thesis ID')
    site=site.resolve(strict=True);root=work_root.expanduser().resolve()
    need(not root.is_relative_to(site.parent),'Work directory must be outside distribution repository')
    manifest=json.loads((site/'draft-manifest.json').read_text(encoding='utf-8'))
    need(manifest['schema']==1 and manifest['kind']=='public_research_drafts' and manifest['assignment_approval'] is False,'Not a draft edition')
    item=manifest['archives'].get(ident);need(isinstance(item,dict) and set(item)=={'gate','sha256'} and item['gate'] in {'not_required','pending','conditional','blocked'},'Draft not published')
    archive=site/'projects'/ident/'workspace-files.zip'
    need(archive.is_file() and not archive.is_symlink() and archive.resolve().is_relative_to(site),'Unsafe archive')
    raw=archive.read_bytes();need(hashlib.sha256(raw).hexdigest()==item['sha256'],'Archive changed')
    import io
    with zipfile.ZipFile(io.BytesIO(raw)) as z:
        need(len(z.namelist())==19 and set(z.namelist())==ROLE and z.testzip() is None,'Invalid draft member set')
        members={f:z.read(f) for f in ROLE}
    cells=[c for c in json.loads(members['student_start.ipynb'])['cells'] if c['cell_type']=='code']
    need(cells and all(c.get('execution_count') is None and not c.get('outputs') for c in cells),'Executed notebook')
    root.mkdir(parents=True,exist_ok=True);dest=root/ident;dest.mkdir()
    try:
        for f,b in members.items():(dest/f).write_bytes(b)
        for f in ('local-data','results'):(dest/f).mkdir()
        (dest/'.gitignore').write_text('local-data/\nresults/\n.ipynb_checkpoints/\n.env\n')
        (dest/'DRAFT_ORIGIN.json').write_text(json.dumps({'id':ident,'gate':item['gate'],'archive_sha256':item['sha256'],'assignment_approval':False,'original_member_sha256':{f:hashlib.sha256(b).hexdigest() for f,b in members.items()}},indent=2,sort_keys=True)+'\n')
    except BaseException:
        shutil.rmtree(dest);raise
    return dest,item['gate']

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--site',type=Path,required=True);p.add_argument('--id',required=True);p.add_argument('--work-root',type=Path,required=True);a=p.parse_args()
    dest,gate=prepare(a.site,a.id,a.work_root);print('Research draft only; assignment subject to supervisor confirmation. Data status:',gate)
    if gate=='blocked':print('DATA ACCESS WARNING: not currently assignable. Verify access, coverage and permitted use first.')
    print('Open in notebook editor:',dest/'student_start.ipynb')
