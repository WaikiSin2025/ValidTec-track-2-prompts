from __future__ import annotations
import json
from pathlib import Path
from typing import Iterable
AUTHORITY_ORDER={"primary":0,"secondary":1,"untrusted":2}

def load_registry(path:str|Path)->list[dict]:
    return json.loads(Path(path).read_text(encoding="utf-8"))["sources"]

def build_context_packet(registry:Iterable[dict], required_tags:set[str], max_chars:int=1600, include_untrusted:bool=False)->dict:
    candidates=[]
    for source in registry:
        if source.get("status")!="active": continue
        if source.get("authority")=="untrusted" and not include_untrusted: continue
        if required_tags and not (set(source.get("tags",[])) & required_tags): continue
        candidates.append(source)
    candidates.sort(key=lambda s:(AUTHORITY_ORDER.get(s.get("authority"),99),s["id"]))
    selected=[]; used=0
    for source in candidates:
        rendered=f'[{source["id"]}] {source["title"]}: {source["content"]}'
        cost=len(rendered)
        if cost>max_chars: continue
        if used+cost>max_chars: continue
        selected.append({"id":source["id"],"authority":source["authority"],"text":rendered}); used+=cost
    return {"source_ids":[s["id"] for s in selected],"character_budget":max_chars,"characters_used":used,"sources":selected}
