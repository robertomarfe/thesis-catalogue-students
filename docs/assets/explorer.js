/* No external network or framework. Canonical catalogue is generated alongside this file. */
(() => {
  "use strict";
  const data = window.CATALOGUE;
  if (!data || !Array.isArray(data.projects)) return;
  const $ = id => document.getElementById(id);
  const projects = data.projects, byId = new Map(projects.map(p => [p.id, p]));
  const gates = {"not_required":"Synthetic core","pending":"Data verification pending","conditional":"Conditional data access","blocked":"Data access warning"};
  const states = {"draft_workspace":"Complete research draft · assignment subject to confirmation"};
  const storageKey = "thesis-library-v90:" + "discovery" + ":" + location.pathname.replace(/explorer\.html$/,"");
  const normalize = s => String(s || "").normalize("NFKD").replace(/[\u0300-\u036f]/g,"").toLowerCase();
  const unique = a => [...new Set(a)].sort((a,b)=>String(a).localeCompare(String(b)));
  function readList() { try { const a=JSON.parse(localStorage.getItem(storageKey)||"[]");return new Set(Array.isArray(a)?a.filter(id=>byId.has(id)):[]); } catch { return new Set(); } }
  const saved = readList(), compared = new Set();
  let shortlistOnly=false, showComparison=false, current=1;
  const perPage=12;
  function persist(){try{localStorage.setItem(storageKey,JSON.stringify([...saved]));}catch{/* File-origin storage is not guaranteed. */}}
  function el(tag, text, cls){const n=document.createElement(tag);if(text!=null)n.textContent=text;if(cls)n.className=cls;return n;}
  function action(label,fn,pressed){const b=el("button",label);b.type="button";if(pressed!==undefined)b.setAttribute("aria-pressed",String(pressed));b.addEventListener("click",fn);return b;}
  function link(p,label){const a=el("a",label,"button secondary");a.href=p.href;return a;}
  function select(id,options){const s=$(id);s.append(new Option("All",""));for(const [v,label] of options)s.append(new Option(label,v));if(options.length===0)s.disabled=true;}
  select("area",unique(projects.map(p=>p.area)).map(x=>[x,x]));
  select("family",Object.entries(data.families||{}).map(([id,label])=>[id,id+" · "+label]));
  select("difficulty",unique(projects.map(p=>p.difficulty)).map(x=>[String(x),"Level "+x+"/3"]));
  select("gate",Object.entries(gates).filter(([id])=>projects.some(p=>p.gate===id)));
  select("method",unique(projects.flatMap(p=>p.tags||[])).map(x=>[x,x]));
  select("design",unique(projects.map(p=>p.design)).map(x=>[x,x]));
  const fields=["area","family","difficulty","gate","method","design"];
  const query=new URLSearchParams(location.search);
  for(const f of fields)if(query.has(f)&&[...$(f).options].some(o=>o.value===query.get(f)))$(f).value=query.get(f);
  if(query.has("q"))$("search").value=query.get("q");
  if(query.has("sort")&&[...$("sort").options].some(o=>o.value===query.get("sort")))$("sort").value=query.get("sort");
  if(/^[0-9]+$/.test(query.get("page")||""))current=Math.max(1,Number(query.get("page")));
  
  function showFilters(){
    const chips=[], q=$("search").value.trim();
    const add=(label,clear)=>{const chip=action(label+" ×",()=>{clear();current=1;render();$("search").focus();});chip.className="filter-chip";chip.setAttribute("aria-label","Remove filter "+label);chips.push(chip);};
    if(q)add("Search: "+q,()=>{$("search").value="";});
    for(const f of fields)if($(f).value)add($(f).selectedOptions[0].text,()=>{$(f).value="";});
    $("active-filters").replaceChildren(...chips);
    $("filter-count").textContent=fields.filter(f=>$(f).value).length?"("+fields.filter(f=>$(f).value).length+" active)":"";
  }
  function updateURL(){
    const next=new URLSearchParams();const q=$("search").value.trim();if(q)next.set("q",q);
    for(const f of fields)if($(f).value)next.set(f,$(f).value);
    if($("sort").value!=="id")next.set("sort",$("sort").value);if(current>1)next.set("page",String(current));
    try{history.replaceState(null,"",location.pathname+(next.size?"?"+next.toString():"")+location.hash);}catch{/* In-memory rendering does not have a normal origin. */}
  }
  function matches(p) {
    if(shortlistOnly&&!saved.has(p.id))return false;
    for(const f of fields){
      const v=$(f).value;if(!v)continue;
      if(f==="method"){if(!(p.tags||[]).includes(v))return false;}
      else if(String(p[f])!==v)return false;
    }
    const q=normalize($("search").value.trim());if(!q)return true;
    if(/^[ad]\d{2}\.\d{2}\.\d{2}$/.test(q))return normalize(p.id)===q;
    const hay=normalize([p.id,p.title,p.question,p.data_note,p.prereq,p.motivation,p.design,p.area,data.families[p.family],...(p.tags||[])].join(" "));
    return q.split(/\s+/).every(word=>hay.includes(word));
  }
  function card(p){
    const c=el("article",null,"topic-card");c.dataset.project=p.id;c.dataset.gate=p.gate;
    const title=el("h2"), titleLink=el("a",p.title);titleLink.href=p.href;title.append(titleLink);
    const meta=el("div",null,"meta"), status=el("span",gates[p.gate],"gate-label");status.dataset.gate=p.gate;
    meta.append(status,el("span","Level "+p.difficulty+"/3 · "+p.design,"small"));
    c.append(el("p",p.id+" · "+p.area+" · "+p.family,"small"),title,meta,el("p",p.question,"question"));
    if(p.gate==="blocked")c.append(el("p","DATA ACCESS WARNING: "+p.data_note+" Confirm feasibility before committing.","warning"));
    const tags=el("div",null,"tags");for(const t of (p.tags||[]).slice(0,4))tags.append(el("span",t,"tag"));c.append(tags);
    const actions=el("div",null,"actions");
    const save=action(saved.has(p.id)?"Saved":"Save",()=>{saved.has(p.id)?saved.delete(p.id):saved.add(p.id);persist();render();},saved.has(p.id));save.dataset.cardAction="save";save.className="secondary-action";save.setAttribute("aria-label",(saved.has(p.id)?"Remove from shortlist: ":"Save to shortlist: ")+p.title);
    const open=link(p,"Open workspace →");open.className="button";actions.append(open,save);
    const cmp=action(compared.has(p.id)?"Selected":"Compare",()=>{if(compared.has(p.id))compared.delete(p.id);else if(compared.size<3)compared.add(p.id);render();},compared.has(p.id));
    cmp.disabled=!compared.has(p.id)&&compared.size>=3;cmp.dataset.cardAction="compare";cmp.className="secondary-action";cmp.setAttribute("aria-label",(compared.has(p.id)?"Remove from comparison: ":"Compare: ")+p.title);actions.append(cmp);c.append(actions);return c;
  }
  function comparison(){
    const node=$("comparison");node.replaceChildren();node.hidden=!showComparison||compared.size===0;if(node.hidden)return;
    const list=[...compared].map(id=>byId.get(id));node.className="comparison";node.tabIndex=0;node.setAttribute("aria-label","Comparison table; scroll horizontally if needed");
    node.append(el("h2","Compare selected research topics"),el("p","Scroll horizontally on narrow screens. Compare the same research dimensions across topics.","small"));
    const table=el("table"),head=el("thead"),tr=el("tr");tr.append(el("th","Research dimension"));
    for(const p of list){const th=el("th",p.id+" — "+p.title);th.scope="col";tr.append(th);}head.append(tr);table.append(head);
    const body=el("tbody");
    for(const [label,fn] of [["Research question",p=>p.question],["Motivation",p=>p.motivation],["Prerequisites",p=>p.prereq||"See original proposal"],["Methodology",p=>(p.tags||[]).join(" · ")||"Not classified on mirror"],["Design",p=>p.design],["Difficulty",p=>p.difficulty+"/3"],["Data status",p=>gates[p.gate]],["Data requirements",p=>p.data_note],["Assignment",p=>states[p.state]]]){
      const row=el("tr"),th=el("th",label);th.scope="row";row.append(th);
      for(const p of list)row.append(el("td",fn(p)));body.append(row);
    }
    table.append(body);node.append(table);
    const controls=el("div",null,"actions");for(const p of list)controls.append(link(p,"Open "+p.id),action("Remove "+p.id,()=>{compared.delete(p.id);render();}));node.append(controls);
  }
  function render(){
    // Preserve keyboard focus when a card is replaced after Save or Compare.
    const focused=document.activeElement, kind=focused?.dataset?.cardAction, previous=kind?focused.closest(".topic-card")?.dataset.project:null;
    let result=projects.filter(matches);
    const key=$("sort").value;
    result.sort((a,b)=>key==="difficulty"?a.difficulty-b.difficulty||a.id.localeCompare(b.id):key==="title"?a.title.localeCompare(b.title)||a.id.localeCompare(b.id):a.id.localeCompare(b.id));
    const pages=Math.max(1,Math.ceil(result.length/perPage));current=Math.max(1,Math.min(current,pages));
    $("status").textContent=result.length+" of "+projects.length+" research topics"+(shortlistOnly?" · Shortlist":"")+(result.length?"":" · Try adjusting the filters.");
    $("saved").textContent="Shortlist ("+saved.size+")";$("saved").setAttribute("aria-pressed",String(shortlistOnly));
    $("compare").textContent=(showComparison?"Hide comparison":"Compare")+" ("+compared.size+"/3)";
    $("compare").setAttribute("aria-pressed",String(showComparison));$("compare").disabled=compared.size===0;$("clear-compare").disabled=compared.size===0;
    $("export").disabled=saved.size===0;
    $("results").replaceChildren(...result.slice((current-1)*perPage,current*perPage).map(card));
    for(const suffix of ["","-top"]){$("pagination"+suffix).textContent="Page "+current+" of "+pages;$("prev"+suffix).disabled=current===1;$("next"+suffix).disabled=current===pages;}
    showFilters();updateURL();
    comparison();
    if(previous&&kind){
      const card=[...$("results").querySelectorAll(".topic-card")].find(x=>x.dataset.project===previous);
      const replacement=card&&[...card.querySelectorAll("button[data-card-action]")].find(x=>x.dataset.cardAction===kind);
      if(replacement&&!replacement.disabled)replacement.focus();else $("saved").focus();
    }
  }
  $("search").addEventListener("input",()=>{current=1;render();});
  for(const f of [...fields,"sort"])$(f).addEventListener("change",()=>{current=1;render();});
  $("reset").onclick=()=>{$("search").value="";for(const f of fields)$(f).value="";$("sort").value="id";shortlistOnly=false;current=1;render();};
  $("saved").onclick=()=>{shortlistOnly=!shortlistOnly;current=1;render();};
  $("compare").onclick=()=>{showComparison=!showComparison;render();};
  $("clear-compare").onclick=()=>{compared.clear();showComparison=false;render();};
  function movePage(delta){current+=delta;render();$("status").scrollIntoView({block:"start",behavior:"instant"});}
  for(const suffix of ["","-top"]){$("prev"+suffix).onclick=()=>movePage(-1);$("next"+suffix).onclick=()=>movePage(1);}
  $("export").onclick=()=>{
    const lines=["Master’s Thesis Research Library — personal shortlist","Exploration does not constitute assignment approval.",""];
    for(const id of [...saved].sort()){const p=byId.get(id);if(p)lines.push(id+" — "+p.title,"Research question: "+p.question,"Data status: "+gates[p.gate],"Data requirements: "+p.data_note,"");}
    const url=URL.createObjectURL(new Blob([lines.join("\n")],{type:"text/plain;charset=utf-8"}));
    const a=el("a");a.href=url;a.download="thesis-shortlist.txt";document.body.append(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(url),1000);
  };
  render();
})();