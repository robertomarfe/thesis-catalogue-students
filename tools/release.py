#!/usr/bin/env python3
"""Seal or verify a positive, approved-only Pages payload; never deploy it.
The manifest is a consistency check, not a signature or substitute for human approval.
The verify subcommand works in the separate student repository without the master.
"""
import argparse, hashlib, json, re, zipfile
from pathlib import Path
ID=re.compile(r"[AD]\d{2}\.\d{2}\.\d{2}")
FILES={"proposal.pdf","proposal.md","methods.pdf","methods.md","READING_GUIDE.md","references.bib","DATA_GUIDE.md",
       "student_start.ipynb","requirements.txt","RESEARCH_PLAN.md","README.md"}
PAGES={"index.html","proposal.html","methods.html","literature.html","data.html","python.html","plan.html"}
ROLE=FILES|{"START_HERE.html","proposal.html","methods.html","READING_GUIDE.html","DATA_GUIDE.html",
            "student_start.html","RESEARCH_PLAN.html","style.css"}
BASE={"index.html","explorer.html","all.html","guide.html","assets/catalogue.js","assets/explorer.js","assets/site.css",".nojekyll","robots.txt"}
MANIFEST="release-manifest.json"

def require(ok,msg):
    if not ok: raise ValueError(msg)

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def members(site):
    entries=list(site.rglob("*"))
    require(all(not p.is_symlink() for p in entries),"Symlink in release")
    return {p.relative_to(site).as_posix():p for p in entries if p.is_file()}

def expected(ids):
    require(isinstance(ids,list) and ids and len(ids)==len(set(ids)) and all(isinstance(i,str) and ID.fullmatch(i) for i in ids),"Nonempty unique approved ID list required")
    result=set(BASE)
    for i in ids:
        base=f"projects/{i}/"
        result.update(base+f for f in PAGES)
        result.update(base+"files/"+f for f in FILES)
        result.add(base+"workspace-files.zip")
    return result

def verify(site):
    actual=members(site)
    require(MANIFEST in actual,"No sealed release manifest")
    manifest=json.loads(actual.pop(MANIFEST).read_text(encoding="utf-8"))
    require(manifest.get("schema")==1 and manifest.get("edition")=="student","Not a sealed student release")
    ids=manifest["ids"]; hashes=manifest["sha256"]
    require(set(actual)==set(hashes)==expected(ids),"Unexpected or missing release file")
    for rel,path in actual.items():
        require(sha(path)==hashes[rel],f"Hash mismatch: {rel}")
    s=actual["assets/catalogue.js"].read_text(encoding="utf-8").strip()
    require(s.startswith("window.CATALOGUE=") and s.endswith(";"),"Unknown catalogue format")
    catalogue=json.loads(s[len("window.CATALOGUE="):-1])
    require(catalogue["mode"]=="student","Review catalogue forbidden")
    projects=catalogue["projects"]
    require(len(projects)==len(ids) and {p["id"] for p in projects}==set(ids),"Catalogue differs from selection")
    require(all(p["state"]=="integrated" and p["gate"]=="not_required" and "approval" not in p for p in projects),"Uncleared or internal project metadata")
    for rel,path in actual.items():
        if rel.endswith(".html"):
            html=path.read_text(encoding="utf-8")
            require("STUDENT EDITION" in html and "PRIVATE REVIEW" not in html,f"Nonstudent page: {rel}")
        elif rel.endswith(".ipynb"):
            cells=json.loads(path.read_text(encoding="utf-8"))["cells"]
            require(any(c["cell_type"]=="code" for c in cells) and all(not c.get("outputs") and c.get("execution_count") is None for c in cells if c["cell_type"]=="code"),f"Executed notebook: {rel}")
        elif rel.endswith("workspace-files.zip"):
            with zipfile.ZipFile(path) as z:
                require(set(z.namelist())==ROLE and len(z.namelist())==len(ROLE) and z.testzip() is None,"Unexpected original role archive member")
                for f in FILES:
                    require(z.read(f)==(path.parent/"files"/f).read_bytes(),f"Role member differs: {rel}/{f}")
    return {"edition":"student","projects":len(ids),"files":len(actual)+1,"manifest_sha256":sha(site/MANIFEST)}

def seal(root,dest,allow):
    # This import is intentionally only available in the private source repository.
    import build as b
    receipt=b.qa(dest,b.build(root,dest,"student",allow,partial=False,require_nonempty=True))
    require(receipt["projects"]==len(allow) and receipt["mode"]=="student","Invalid private build")
    found=members(dest)
    require(set(found)==expected(allow),"Unexpected build payload")
    manifest={"schema":1,"edition":"student","ids":sorted(allow),"sha256":{k:sha(p) for k,p in sorted(found.items())}}
    (dest/MANIFEST).write_text(json.dumps(manifest,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    return verify(dest)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    sub=parser.add_subparsers(dest="command",required=True)
    check=sub.add_parser("verify");check.add_argument("site",type=Path)
    prepare=sub.add_parser("seal");prepare.add_argument("--root",type=Path,required=True);prepare.add_argument("--dest",type=Path,required=True);prepare.add_argument("--allowlist",type=Path,required=True)
    a=parser.parse_args()
    result=verify(a.site) if a.command=="verify" else seal(a.root,a.dest,json.loads(a.allowlist.read_text(encoding="utf-8")))
    print(json.dumps(result,indent=2))
if __name__=="__main__":
    main()
