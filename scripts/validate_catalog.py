#!/usr/bin/env python3
"""Offline checks for source identity, bilingual entries, Markdown, and audit integrity."""
import datetime as dt
import json
import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit
from render_catalog import ROOT, render, anchor
CJK = re.compile(r'[\u3400-\u9fff]')
LINK = re.compile(r'\[[^\]]*\]\(([^\s)]+)\)')
errors = []
def check(ok, message):
    if not ok: errors.append(message)
def lines(text):
    fence = None
    for n, line in enumerate(text.splitlines(), 1):
        m = re.match(r'^\s*(`{3,}|~{3,})', line)
        if m:
            if fence is None: fence=m[1]
            elif m[1][0]==fence[0] and len(m[1])>=len(fence): fence=None
            continue
        if fence is None: yield n,line
    check(fence is None, 'Unclosed Markdown code fence')
def cells(line):
    return [s.strip() for s in re.split(r'(?<!\\)\|',line.strip().strip('|'))]
def anchors(text):
    found=set();counts=Counter()
    for _,line in lines(text):
        for value in re.findall(r'<a\s+(?:id|name)="([^"]+)"',line):
            check(value not in found,'Duplicate anchor '+value);found.add(value)
        if re.match(r'^#{1,6} ',line):
            s=re.sub(r'^#+\s+','',line)
            s=re.sub(r'<[^>]+>','',s).lower()
            s=re.sub(r'[^\w\- ]','',s).replace(' ','-')
            value=s+(f'-{counts[s]}' if counts[s] else '')
            counts[s]+=1;check(value not in found,'Duplicate anchor '+value);found.add(value)
    return found

def main():
    data=json.loads((ROOT/'data/catalog.json').read_text())
    entries=data['entries'];cutoff=dt.date.fromisoformat(data['cutoff'])
    cats=[c['id'] for c in data['categories']]
    check(len(cats)==len(set(cats)),'Duplicate categories')
    for key in ('id','title','label'):
        values=[re.sub(r'\W','',e[key].casefold()) for e in entries]
        check(len(values)==len(set(values)),f'Duplicate normalized {key}')
    allowed={
      'Paper':{'Tool agent','Perception agent','GUI agent','Interaction component','Agent harness'},
      'Benchmark':{'Agent evaluation','Execution evaluation','Interaction evaluation','Perception diagnostic','Voice tool evaluation'},
      'Technical report':{'Supporting model','Interaction component','Agentic model and harness'},
      'System':{'Tool-capable API'}}
    for e in entries:
        key=e['id']
        check(e['category'] in cats,f'{key}: unknown category')
        check(e['kind'] in allowed and e['role'] in allowed.get(e['kind'],set()),f'{key}: invalid type/role')
        check(bool(e['authors']) and all(isinstance(n,str) and n.strip() for n in e['authors']),f'{key}: missing authors')
        check(bool(e['modalities']) and set(e['modalities'])<=set('TIAV') and len(e['modalities'])==len(set(e['modalities'])),f'{key}: modalities')
        try:
            first,revision,review=(dt.date.fromisoformat(e[k]) for k in ('first_date','revision_date','review_date'))
            check(first<=revision<=cutoff<=review,f'{key}: date/cutoff order')
            check(e['review_date']==data['review_date'],f'{key}: review date drift')
        except ValueError:check(False,f'{key}: malformed date')
        en,zh=e['summary_en'],e['summary_zh']
        check(len(en)>30 and bool(re.search('[A-Za-z]',en)) and not CJK.search(en),f'{key}: English summary')
        if e['kind']=='System':
            check(zh=='' and e['checked']=='S' and e['version']=='release',f'{key}: system language/status')
            check(e['date_basis']=='Official release announcement',f'{key}: date basis')
        else:
            check(bool(CJK.search(zh)),f'{key}: missing Chinese summary')
            nums=lambda s:re.findall(r'\d+(?:\.\d+)?',s)
            check(nums(en)==nums(zh),f'{key}: bilingual numeric mismatch')
            check(re.fullmatch(r'\d{4}\.\d{4,5}',key),f'{key}: identifier')
            check(e['source_url']=='https://arxiv.org/abs/'+key,f'{key}: canonical URL')
            check(re.fullmatch(r'v\d+',e['version']),f'{key}: version')
            check(e['reviewed_record_url']==e['source_url']+e['version'],f'{key}: pinned record')
            check(e['date_basis']=='arXiv first submission',f'{key}: date basis')
            check(e['checked'] in ('A','M'),f'{key}: evidence depth')
            check(re.fullmatch('[a-f0-9]{64}',e.get('metadata_sha256','')),f'{key}: metadata digest')
        if e['checked']=='M':
            check(e['method_url']=='https://arxiv.org/html/'+key+e['version'] and bool(e['method_sections']),f'{key}: missing versioned method evidence')
            check(re.fullmatch('[a-f0-9]{64}',e.get('method_sha256','')),f'{key}: method digest')
        elif e['checked']=='A':check(not e['method_url'] and not e['method_sections'],f'{key}: A/M scope mismatch')
        check(len(e['evidence_note'])>25,f'{key}: evidence note missing')
        for k,v in e.items():
            if k!='summary_zh' and isinstance(v,str):check(not CJK.search(v),f'{key}: non-English metadata {k}')
    for c in cats:
        subset=[e for e in entries if e['category']==c]
        check(bool(subset),f'Empty category {c}')
        check(subset==sorted(subset,key=lambda e:(e['first_date'],e['id'])),f'{c}: chronological order')
    for name,expected in render(data).items():check((ROOT/name).read_text()==expected,f'Stale generated document {name}')
    docs={p:p.read_text() for p in ROOT.rglob('*.md') if '.git' not in p.parts}
    amap={p:anchors(s) for p,s in docs.items()}
    external=set()
    for path,text in docs.items():
        width=None
        for n,line in lines(text):
            if line.startswith('|'):
                current=len(cells(line));check(width is None or current==width,f'{path.name}:{n}: table shape');width=current
            else:width=None
            if CJK.search(line):
                check(path.name=='README.md' and (line.startswith('| **') or line=='| Entry and role | First submitted / released | English | 中文 | Source | Checked |'),f'{path.name}:{n}: language outside paper rows')
            for target in LINK.findall(line):
                u=urlsplit(target)
                if u.scheme or u.netloc:
                    check(u.scheme=='https' and bool(u.netloc),f'Invalid external URL {target}');external.add(target);continue
                dest=(path.parent/unquote(u.path)).resolve() if u.path else path
                check(dest.is_file(),f'{path.name}:{n}: missing {target}')
                if u.fragment and dest in amap:check(unquote(u.fragment) in amap[dest],f'{path.name}:{n}: missing anchor {target}')
    readme=docs[ROOT/'README.md'];audit=docs[ROOT/'docs/SOURCE_AUDIT.md']
    table_entries=[cells(line) for _,line in lines(readme) if line.startswith('| **')]
    check(len(table_entries)==len(entries),'README inventory count mismatch')
    check(all(len(row)==6 for row in table_entries),'Entry table is not six columns')
    for e in entries:check(anchor(e) in amap[ROOT/'docs/SOURCE_AUDIT.md'],f'Missing audit anchor {e["id"]}')
    total=re.search(r'\*\*(\d+) entries\*\*',readme)
    check(total and int(total[1])==len(entries),'Displayed total mismatch')
    report=ROOT/'docs/LINK_CHECK.json'
    if report.exists():
        r=json.loads(report.read_text());checked={x['url'] for x in r['results']}
        check(checked==external,'Link report does not cover exact external Markdown URL set')
    if errors:
        print('\n'.join('FAIL: '+e for e in errors),file=sys.stderr);return 1
    print(f'PASS: {len(entries)} unique works, {sum(e["kind"]!="System" for e in entries)} bilingual summaries, {len(cats)} categories')
    print(f'PASS: {len(docs)} Markdown files; tables, dates/cutoff, versions, authors, evidence scope, generated audit, local links and anchors')
    print(f'PASS: {len(external)} unique external URLs enumerated; remote access is checked separately')
    print('Manual limits: source truth, semantic translation equivalence, and runtime behavior cannot be certified by these checks.')
    return 0
if __name__=='__main__':raise SystemExit(main())
