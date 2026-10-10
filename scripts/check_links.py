#!/usr/bin/env python3
"""Check catalog external Markdown links with GET; retain access failures honestly."""
import argparse
import concurrent.futures
import datetime as dt
import json
import re
import time
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import urlsplit,urldefrag
from validate_catalog import ROOT,LINK,lines

def urls():
    return sorted({u for p in ROOT.rglob('*.md') if '.git' not in p.parts
                   for _,line in lines(p.read_text()) for u in LINK.findall(line)
                   if urlsplit(u).scheme=='https'})
def fetch(url,timeout,attempts):
    history=[]
    for attempt in range(attempts):
        record={'attempt':attempt+1}
        try:
            request=urllib.request.Request(urldefrag(url)[0],headers={'User-Agent':'Awesome-Omni-Agents-LinkCheck/1.0 (public research catalog; no authentication)'})
            with urllib.request.urlopen(request,timeout=timeout) as r:
                body=r.read(65536).decode('utf-8','replace')
                title=re.search(r'<title[^>]*>(.*?)</title>',body,re.I|re.S)
                page_title=re.sub(r'\s+',' ',title[1]).strip() if title else None
                record.update(status=r.status,final_url=r.url,content_type=r.headers.get('Content-Type'),title=page_title)
                challenge=page_title and any(t in page_title.casefold() for t in ('just a moment','access denied','captcha','attention required'))
                record['result']='access_limited' if challenge else 'reachable'
        except urllib.error.HTTPError as exc:
            record.update(status=exc.code,final_url=exc.url,error=str(exc),result='http_error')
        except Exception as exc:record.update(status=None,error=str(exc),result='network_error')
        history.append(record)
        if record['result']=='reachable':break
        if attempt+1<attempts:time.sleep(1)
    return {'url':url,'result':history[-1]['result'],'attempts':history}
def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',default='docs/LINK_CHECK.json')
    p.add_argument('--workers',type=int,default=4)
    p.add_argument('--timeout',type=int,default=20)
    p.add_argument('--attempts',type=int,default=2)
    a=p.parse_args();start=dt.datetime.now(dt.timezone.utc).isoformat()
    targets=urls()
    with concurrent.futures.ThreadPoolExecutor(max_workers=a.workers) as pool:
        results=list(pool.map(lambda u:fetch(u,a.timeout,a.attempts),targets))
    counts={k:sum(r['result']==k for r in results) for k in sorted({r['result'] for r in results})}
    report={'started_at':start,'finished_at':dt.datetime.now(dt.timezone.utc).isoformat(),'method':'GET, first 65536 response bytes, redirects followed; HTTPS Markdown links outside fenced examples; fragments not remotely validated','counts':counts,'results':results}
    path=ROOT/a.output;path.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'urls':len(results),'counts':counts,'report':str(path)}))
    for r in results:
        if r['result']!='reachable':print(r['url'],r['attempts'][-1])
    return 0 if counts.get('reachable',0)==len(results) else 1
if __name__=='__main__':raise SystemExit(main())
