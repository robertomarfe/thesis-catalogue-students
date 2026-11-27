/* Descriptive detail page. Only public, allowlisted fields. */
(() => {
  "use strict";
  const box=document.getElementById("topic-detail"), data=window.CATALOGUE;
  if(!box||!data||data.mode!=="student_drafts")return;
  const id=new URLSearchParams(location.search).get("id");
  const p=data.projects.find(x=>x.id===id);
  function el(tag,text,cls){const n=document.createElement(tag);n.textContent=text;if(cls)n.className=cls;return n;}
  box.replaceChildren();
  if(!p){box.append(el("h1","Topic not found"),el("p","Return to the explorer and choose a research proposal."));return;}
  document.title=p.title+" | Master’s Thesis Research Library";
  const labels={"not_required":"Synthetic core","pending":"Data verification pending","conditional":"Conditional data access","blocked":"Data access warning"};
  const open=el("a","Open complete research workspace →","button");open.href=p.href;box.append(open);
  box.append(el("p",p.id+" · "+p.area+" · "+data.families[p.family],"eyebrow"),el("h1",p.title),el("p",labels[p.gate]+" · Level "+p.difficulty+"/3",p.gate==="blocked"?"warning":"small"));
  if(p.gate==="blocked")box.append(el("p","Data access warning: the required datasets may be difficult or costly to obtain. Verify availability, coverage and permitted use with your supervisor before committing. This topic is not currently ready for assignment.","warning"));
  for(const [label,value] of [["Research question",p.question],["Motivation",p.motivation],["Prerequisites",p.prereq],["Research design",p.design],["Methods",p.tags.join(" · ")],["Data requirements",p.data_note]])box.append(el("h2",label),el("p",value));
  box.append(el("p","Research proposals for exploration, not confirmed assignments. Agree scope, data access and supervision before starting. Complete student research drafts are available for consultation; assignment still requires confirmation.","notice"));
})();
