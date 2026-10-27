"""Render approved public intelligence while retaining build.py's visual system."""
from pathlib import Path
from html import escape
import json, re

ROOT=Path(__file__).resolve().parent
PATH='reports/2026-10-27/'

def apply_publication(g):
    g['HOME_HERO']=g['HOME_HERO'].replace('<div class="hero-title">ORION</div>','<h1 class="hero-title">ORION</h1>')
    data=json.loads((ROOT/'content/2026-10-27.json').read_text())
    sources={s['source_id']:s for s in data['sources']}
    esc=lambda x:escape(str(x),quote=True)
    def refs(ids,prefix=''):
        return ' '.join('<a class="source-ref" href="'+prefix+'#'+esc(i)+'">['+esc(i)+']</a>' for i in ids)
    def cite(text,prefix=''):
        def replace(m):
            raw=m.group(1)
            if '–' in raw:
                a,b=raw.split('–');ids=['S'+str(i).zfill(2) for i in range(int(a[1:]),int(b[1:])+1)]
            else:ids=raw.split(',')
            return refs(ids,prefix)
        return re.sub(r'\[(S\d{2}(?:,S\d{2})*|S\d{2}–S\d{2})\]',replace,text)
    badge='<span class="badge st-published">Published</span>'
    summary='Regional diplomacy, humanitarian access, election transitions, and the policy decisions that test the headlines.'
    def card(prefix):
        return '<article class="rcard" data-cat="geopolitics"><div class="thumb thumb-geo">'+g['ICONS']['globe']+'</div><div class="tbody"><div class="meta"><time datetime="2026-10-27">October 27, 2026</time>'+badge+'</div><h3><a href="'+prefix+PATH+'">Global Crosscurrents &amp; Strategic Watch</a></h3><p class="sum">'+summary+'</p><div class="chips"><span class="chip">11 sections</span><span class="chip">11 source records</span><span class="chip">Conditional scenarios</span></div><p style="margin-top:14px"><a href="'+prefix+PATH+'">Read the full SITREP →</a></p></div></article>'
    g['HOME']=re.sub(r'<section class="blk">.*?</section>','<section class="blk"><h2 class="sec">Latest published brief</h2>'+card('')+'</section>',g['HOME'],count=1,flags=re.S)
    g['HOME']=g['HOME'].replace('Watchlists are monitored, not judged. Scenarios are tracked, not predicted.','Watchlists record dated review priorities. Scenarios describe conditional possibilities. Continuous monitoring is not configured.')
    g['REPORTS']='<header class="page"><div class="eyebrow">Reports</div><h1>Intelligence Reports</h1><p class="lede">Published briefings, inspectable sources, and conditional assessments.</p></header><section class="blk">'+card('../')+'<p class="dim">Published analysis can be revised as new evidence becomes available. Source grades describe evidence, not publication status.</p></section>'

    toc='<nav class="report-toc" aria-label="Briefing contents"><h2>In this briefing</h2><ol>'+''.join('<li><a href="#section-'+str(i)+'">'+esc(s['title'])+'</a></li>' for i,s in enumerate(data['sections'],1))+'</ol></nav>'
    body='<header class="page"><div class="eyebrow">Quantum Geopolitical SITREP · 27 October 2026</div><h1>Global Crosscurrents &amp; Strategic Watch</h1><p class="lede">'+summary+'</p><div class="chips">'+badge+'<span class="chip">ORION-CORE-001</span><span class="chip">Edition 01</span></div><p class="dim" style="margin-top:14px">Collection window: October 24–27, 2026. Published October 27, 2026. Collection timestamp: '+esc(data['collected_at'])+'. Dates use America/Denver unless a source specifies otherwise.</p><p class="dim" style="margin-top:10px">A selected global scan. Primary records establish institutional actions; underlying allegations remain attributed. Syndicated copies count as one reporting origin.</p></header>'+toc
    body+='<main class="briefing">'+''.join('<section class="blk" id="section-'+str(i)+'"><h2>'+esc(s['title'])+'</h2>'+cite(s['html'])+'</section>' for i,s in enumerate(data['sections'],1))+'</main>'
    body+='<section class="blk" id="sources"><h2>Sources &amp; verification</h2><p class="dim">11 records; several share an institutional or reporting origin. Accessed during this collection cycle. No automatic claim of independent corroboration.</p><ol class="source-list">'
    for s in data['sources']:
        body+='<li id="'+esc(s['source_id'])+'"><span class="mono">'+esc(s['source_id'])+'</span> · '+esc(s['publisher'])+' · '+esc(s['publication_date'] or 'calendar checked this cycle')+'<br><a href="'+esc(s['url'])+'">'+esc(s['title'])+'</a><p class="dim">'+esc(s['limitations'])+'</p></li>'
    body+='</ol><p><a href="../../watchlist/">Monitoring register &amp; forecast ledger →</a> · <a href="../../content/2026-10-27.json" download>Download this edition’s public research data</a></p></section>'

    watch='<header class="page"><div class="eyebrow">Dated intelligence register</div><h1>Watchlist &amp; Scenarios</h1><p class="lede">Eight review priorities. Three conditional scenarios. Clear triggers and disconfirming evidence.</p><p class="dim" style="margin-top:12px">Baseline: October 27, 2026. Reviews below are planned checkpoints; continuous monitoring is not configured.</p></header><section class="blk"><h2 class="sec">Strategic monitoring register</h2><div class="grid">'
    for m in data['monitors']:
        watch+='<article class="card"><p class="eyebrow">'+esc(m['monitor_id'])+'</p><h3>'+esc(m['topic'])+'</h3><p><b>Watch:</b> '+esc(m['indicators'])+'</p><p><b>Trigger:</b> '+esc(m['trigger'])+'</p><p><b>Test:</b> '+esc(m['invalidation_or_caution'])+'</p><p><b>Review:</b> '+esc(m['review_due'])+'</p><p>'+refs(m['baseline_sources'].split(','),'../'+PATH)+'</p></article>'
    watch+='</div></section><section class="blk" id="scenarios"><h2 class="sec">Scenario &amp; forecast ledger</h2><p class="sub">Conditional possibilities, not assigned probabilities. Outcomes remain pending until reviewed.</p>'
    for f in data['forecasts']:
        watch+='<article class="card" id="'+esc(f['forecast_id'])+'" style="margin-bottom:18px"><p class="eyebrow">'+esc(f['forecast_id'])+' · '+esc(f['horizon'])+'</p><h3>'+esc(f['scenario'])+'</h3>'
        for label,k in [('Assumptions','assumptions'),('Trigger','trigger'),('Indicators','indicators'),('Implications','implications'),('Invalidation','invalidation'),('Uncertainties','uncertainties'),('Review due','review_due'),('Outcome','outcome')]:
            value=f[k];value='; '.join(value) if isinstance(value,list) else value
            watch+='<p><b>'+label+':</b> '+esc(value)+'</p>'
        watch+='<p><b>Evidence:</b> '+refs(f['evidence'],'../'+PATH)+'</p></article>'
    watch+='</section><section class="blk"><a href="../'+PATH+'">Read the baseline SITREP →</a></section>'
    timeline='<header class="page"><div class="eyebrow">Event archive</div><h1>Global Timeline</h1><p class="lede">Dated geopolitical events with explicit source grades and direct evidence links.</p><p class="dim" style="margin-top:10px">October 27 publication. These records are a static edition of the archive; live market data is not connected.</p></header><section class="blk"><div class="tl">'
    events=[]
    for e in sorted(data['events'],key=lambda e:e['date'],reverse=True):
        events.append(dict(id=e['local_id'],occurred_at=e['date']+'T00:00:00Z',date_precision='day',origin='orion',title=e['title'],summary=e.get('verification','See the source record and SITREP for context.'),actors=[],regions=[],narrative_tags=[],event_type='geopolitical',source_grade=e['source_grade'],sources=[sources[s]['url'] for s in e['sources']],status='published'))
        timeline+='<article class="tl-item"><div class="tl-date">'+esc(e['date'])+'</div><div class="tl-card"><div class="top">'+badge+'<span class="badge g-single">Single-source</span></div><h2>'+esc(e['title'])+'</h2><p>'+esc(e.get('verification','See the source record and SITREP for context.'))+'</p><p style="margin-top:10px">'+refs(e['sources'],'../'+PATH)+'</p></div></article>'
    # Keep the pre-existing architecture record as its original draft, without implying publication approval.
    events+=g['EVENTS']['events']
    g['EVENTS']={'events':events}
    timeline+='</div><p class="dim">Event dates have day precision. No market-causation links have been asserted in this edition.</p></section>'
    g['ABOUT']=g['ABOUT'].replace('ORION analyzes. LUNA builds and deploys. MASTER INDY approves.','ORION researches and publishes approved intelligence. LUNA and CODEX support building and deployment. MASTER INDY directs publication.')
    g['ABOUT']=g['ABOUT'].replace('Conversation &rarr; structured report','Mission established in April 2025. ORION-CORE-001 formalized October 27, 2026. Conversation &rarr; structured report')
    g['METHODOLOGY']=g['METHODOLOGY'].replace('Supported by primary source, multiple reliable sources, or direct artifact / system record.','Independently corroborated by multiple credible sources. A primary document can verify its issuer’s action while remaining a single source origin for broader claims.')
    g['HOME']=g['HOME'].replace('Supported by primary or multiple reliable sources.','Independently corroborated by multiple credible sources.')
    g['PAGES']=[tuple(list(p[:-1])+[{'reports/index.html':g['REPORTS'],'watchlist/index.html':watch,'timeline/index.html':timeline,'about/index.html':g['ABOUT'],'methodology/index.html':g['METHODOLOGY']}.get(p[0],p[-1])]) for p in g['PAGES']]
    g['PAGES'].append((PATH+'index.html','October 27, 2026 SITREP — ORION',summary,PATH,'Reports',body))
    g['CSS']+='''
/* Published intelligence: readable long-form sections and source navigation. */
.briefing{max-width:800px}.briefing h2{font-size:clamp(22px,4vw,30px);line-height:1.35;margin-bottom:20px}
.briefing p{margin:14px 0;max-width:76ch}.briefing ul{padding-left:24px}.briefing li{margin:12px 0}
.briefing table{display:block;max-width:100%;overflow-x:auto;border-collapse:collapse;margin:20px 0}
.briefing th,.briefing td{border:1px solid var(--line);padding:12px;text-align:left;vertical-align:top;min-width:130px;font-size:13px}
.report-toc{margin:30px 0;padding:24px;border:1px solid var(--line);border-radius:12px;background:var(--card)}
.report-toc h2{font-size:20px;margin-bottom:12px}.report-toc ol{padding-left:24px;columns:2;column-gap:32px}
.report-toc li{break-inside:avoid;margin-bottom:9px;font-size:13px}.report-toc a{color:var(--silver)}
.source-list{padding-left:24px;max-width:800px}.source-list li{margin:22px 0;overflow-wrap:anywhere}
.source-list p{font-size:13px}.source-ref{font-size:.85em;white-space:nowrap}
.card p+p{margin-top:10px}.card b{color:var(--silver)}
[id]{scroll-margin-top:95px}a:focus-visible,button:focus-visible{outline:2px solid var(--cyan);outline-offset:4px}
@media(max-width:640px){.report-toc ol{columns:1}.report-toc{padding:18px}.briefing th,.briefing td{min-width:125px}}
@media print{#stars,nav.top,.report-toc{display:none}body{color:#111;background:white}.wrap{max-width:none}p,h1,h2,h3,.dim{color:#111!important}a{color:#14528a}section.blk{break-inside:auto}.card{background:white;border:1px solid #ccc}.badge{color:#111}footer{background:white}}
'''
    # Include the new report in discovery without exposing internal archive files.
    urls=['','reports/','watchlist/','timeline/','patterns/','methodology/','about/','network/','template/',PATH]
    (ROOT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+g['SITE']+'/'+p+'</loc></url>' for p in urls)+'</urlset>\n')
