#!/usr/bin/env python3
"""Build the ORION multi-page static site. Run: python3 build.py"""
import os, json

OUT = os.path.dirname(os.path.abspath(__file__))
SITE = "https://ron-delhaye-studios.github.io/orion-reports"

CSS = r"""
:root{
  --bg:#04070e; --bg2:#080e1a; --card:#0a1220; --line:#1a2740;
  --ink:#d9e4f2; --dim:#8fa3bd; --faint:#5a6c86;
  --cyan:#a8d8e8; --blue:#6fa8dc; --silver:#c0ccd8; --gold:#d4a94e;
  --gold-dim:#6e5626; --green:#7fd6a4;
}
*{box-sizing:border-box;margin:0;padding:0}
html{background:var(--bg)}
body{background:transparent;color:var(--ink);
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Inter,Helvetica,Arial,sans-serif;
  line-height:1.65;min-height:100vh;display:flex;flex-direction:column;font-size:15px}
#stars{position:fixed;inset:0;z-index:-2}
body::after{content:"";position:fixed;inset:0;z-index:-1;pointer-events:none;
  background:radial-gradient(ellipse 80% 55% at 50% -5%,rgba(111,168,220,.07),transparent 70%)}
.wrap{max-width:900px;margin:0 auto;padding:0 20px;width:100%}
.mono{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}
/* nav */
nav.top{border-bottom:1px solid var(--line);backdrop-filter:blur(6px)}
nav.top .wrap{display:flex;align-items:center;gap:4px;overflow-x:auto;padding-top:14px;padding-bottom:14px}
.brand{color:#fff;text-decoration:none;letter-spacing:.3em;font-size:15px;margin-right:14px;white-space:nowrap}
.brand small{display:block;font-size:9px;letter-spacing:.24em;color:var(--faint)}
nav.top a.nl{color:var(--dim);text-decoration:none;font-size:12.5px;letter-spacing:.08em;
  padding:6px 10px;border-radius:6px;white-space:nowrap}
nav.top a.nl:hover{color:var(--cyan);background:rgba(168,216,232,.06)}
nav.top a.nl.on{color:var(--cyan)}
/* header */
header.page{padding:40px 0 8px}
.eyebrow{font-size:11px;letter-spacing:.32em;text-transform:uppercase;color:var(--blue)}
h1{font-size:34px;font-weight:600;color:#fff;margin:10px 0 6px;letter-spacing:.02em}
.lede{color:var(--dim);font-size:15px;max-width:640px}
/* sections */
section{padding:30px 0;border-bottom:1px solid var(--line)}
h2{font-size:12px;letter-spacing:.3em;text-transform:uppercase;color:var(--cyan);margin-bottom:14px}
h3{font-size:16px;color:#fff;margin:18px 0 8px}
p{font-size:14.5px;color:var(--ink);max-width:660px}
p+p{margin-top:10px}
.dim{color:var(--dim)} .faint{color:var(--faint)} .gold{color:var(--gold)}
ul.tight{margin:10px 0 0 18px;color:var(--dim);font-size:14px}
ul.tight li{margin:6px 0}
/* cards */
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:14px;margin-top:6px}
.card{border:1px solid var(--line);border-radius:10px;padding:18px;background:linear-gradient(180deg,var(--card),var(--bg2))}
.card h3{margin:0 0 8px;font-size:14.5px}
.card p{font-size:13px;color:var(--dim)}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin-top:10px}
.chip{font-size:11.5px;letter-spacing:.06em;color:var(--silver);border:1px solid var(--line);
  border-radius:20px;padding:4px 12px;background:rgba(192,204,216,.04)}
/* status tags */
.stag{display:inline-block;font-size:10px;letter-spacing:.2em;text-transform:uppercase;
  border-radius:4px;padding:3px 9px;margin-bottom:8px;font-family:ui-monospace,Menlo,monospace}
.st-draft{color:var(--gold);border:1px solid var(--gold-dim);background:rgba(212,169,78,.07)}
.st-awaiting{color:var(--cyan);border:1px solid #2c4a5e;background:rgba(168,216,232,.07)}
.st-approved{color:var(--blue);border:1px solid #2c3e5e;background:rgba(111,168,220,.08)}
.st-published{color:var(--green);border:1px solid #2c5e44;background:rgba(127,214,164,.07)}
.grade{display:inline-block;font-size:10px;letter-spacing:.18em;text-transform:uppercase;
  border-radius:4px;padding:2px 8px;font-family:ui-monospace,Menlo,monospace}
.g-confirmed{color:var(--green);border:1px solid #2c5e44}
.g-single{color:var(--cyan);border:1px solid #2c4a5e}
.g-narrative{color:var(--gold);border:1px solid var(--gold-dim)}
/* empty + warning */
.empty{border:1px dashed var(--line);border-radius:10px;padding:26px 22px;background:rgba(8,14,26,.6);margin-top:10px}
.empty .t{color:var(--cyan);font-size:13px;letter-spacing:.14em;margin-bottom:8px}
.empty p{font-size:13px;color:var(--dim)}
.warn{border:1px solid var(--gold-dim);border-radius:10px;padding:18px 20px;
  background:rgba(212,169,78,.05);margin-top:14px}
.warn p{font-size:13px;color:var(--gold)}
.legend{margin-top:12px}
.legend .row{display:flex;gap:10px;align-items:baseline;margin:8px 0;font-size:13.5px;color:var(--dim)}
/* template sections */
.tsec{border:1px solid var(--line);border-radius:10px;padding:18px 20px;margin:12px 0;background:rgba(10,18,32,.5)}
.tsec h3{margin:0 0 6px;font-size:14px;color:var(--cyan)}
.tsec h3 .n{color:var(--faint);margin-right:8px}
.tsec p{font-size:13px;color:var(--dim)}
/* timeline */
.event{border:1px solid var(--line);border-radius:10px;padding:18px 20px;margin:12px 0;background:var(--card)}
.event .meta{font-size:11.5px;color:var(--faint);letter-spacing:.06em;margin:8px 0}
.event .tags{margin-top:8px}
/* footer */
footer{margin-top:auto;padding:26px 0 36px;color:var(--faint);font-size:12px}
footer .rule{border-top:1px solid var(--line);padding-top:18px;display:flex;
  justify-content:space-between;flex-wrap:wrap;gap:8px}
a{color:var(--cyan)}
@media(max-width:560px){h1{font-size:27px}}
"""

STARFIELD = r"""
/* starfield — faint twinkling stars, pauses when hidden or reduced-motion */
(function(){
  if(matchMedia("(prefers-reduced-motion: reduce)").matches) return;
  var c=document.getElementById("stars"),x=c.getContext("2d"),stars=[],W,H,timer=null,t=0;
  function size(){W=c.width=innerWidth;H=c.height=innerHeight;stars=[];
    for(var i=0;i<Math.min(220,W*H/9000);i++)stars.push({x:Math.random()*W,y:Math.random()*H,
      r:Math.random()*1.1+.2,p:Math.random()*6.28,s:.4+Math.random()*1.2,
      c:Math.random()<.12?"212,169,78":Math.random()<.25?"168,216,232":"200,214,230"});}
  function draw(){t+=.016;x.clearRect(0,0,W,H);
    for(var i=0;i<stars.length;i++){var s=stars[i],a=.25+.55*Math.abs(Math.sin(t*s.s+s.p));
      x.fillStyle="rgba("+s.c+","+a.toFixed(2)+")";
      x.beginPath();x.arc(s.x,s.y,s.r,0,6.283);x.fill();}}
  size();addEventListener("resize",size);
  function go(){if(!timer)timer=setInterval(draw,50);}
  function stop(){clearInterval(timer);timer=null;}
  document.addEventListener("visibilitychange",function(){document.hidden?stop():go();});
  go();
})();
"""

NAV = [("Observatory",""),("Timeline","timeline/"),("Patterns","patterns/"),
       ("Template","template/"),("Methodology","methodology/"),
       ("Network","network/"),("About","about/")]

def head(title, desc, path, root):
    url = SITE + ("/" + path if path else "/")
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta property="og:site_name" content="ORION">
<meta name="twitter:card" content="summary">
<meta name="theme-color" content="#04070e">
<link rel="stylesheet" href="{root}assets/css/orion.css">
<script src="{root}assets/js/analytics-config.js" defer></script>
<script src="{root}assets/js/analytics.js" defer></script>
</head>
<body>
<canvas id="stars" aria-hidden="true"></canvas>
"""

def nav(active, root):
    items = ""
    for n, p in NAV:
        on = " on" if n == active else ""
        items += '<a class="nl' + on + '" href="' + root + p + '">' + n + "</a>"
    return ('<nav class="top"><div class="wrap">\n'
            '<a class="brand" href="' + root + '">ORION<small>QUANTUM GEOPOLITICAL REPORTS</small></a>\n'
            + items + "</div></nav>\n")

FOOT = """<footer><div class="wrap"><div class="rule">
<span>&copy; 2026 ORION</span><span>An Ad Astra Media publication.</span>
</div></div></footer>
<script>/*STARFIELD*/</script>
</body>
</html>"""

def page(fname, title, desc, path, active, body):
    root = "../" if "/" in fname else ""
    html = (head(title, desc, path, root) + nav(active, root) +
            '<div class="wrap">\n' + body + "\n</div>\n" +
            FOOT.replace("/*STARFIELD*/", STARFIELD))
    full = os.path.join(OUT, fname)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w").write(html)

# ------------------------------------------------------------------ content
HOME = """
<header class="page">
  <div class="eyebrow">Observatory</div>
  <h1>Separate the signal from the noise.</h1>
  <p class="lede">ORION is a geopolitical intelligence observatory built to separate signal from noise. It tracks global events, financial stress, technological acceleration, narrative shifts, and strategic pressure points &mdash; with clear source grading, disciplined uncertainty, and calm analysis.</p>
</header>
<section>
  <h2>Mission</h2>
  <p>ORION is a geopolitical intelligence observatory for the LDI network. Its mission is to transform fragmented global signals into calm, structured, source-aware intelligence. ORION tracks geopolitical pressure, financial stress, technological acceleration, institutional movement, narrative shifts, and scenario evolution &mdash; always separating confirmed facts, analysis, speculation, and watchlist items.</p>
  <p class="dim" style="margin-top:10px">ORION shares one event timeline with FORTUNA&rsquo;s market desk. Geopolitics through one lens, markets through the other &mdash; the patterns between them are the product.</p>
</section>
<section>
  <h2>Latest approved brief</h2>
  <div class="empty">
    <div class="t mono">FEED STANDBY</div>
    <p>First briefing in preparation. Nothing fabricated, nothing backfilled &mdash; the feed opens when the first verified SITREP is filed and approved by MASTER INDY.</p>
  </div>
</section>
<section>
  <h2>Watchlist</h2>
  <p class="dim">Persistent watch areas. Assessments pending &mdash; categories only, no claims yet.</p>
  <div class="chips">
    <span class="chip">Debt / liquidity / sovereign finance</span>
    <span class="chip">Central banks</span>
    <span class="chip">Tokenization / RWA / crypto regulation</span>
    <span class="chip">Middle East</span>
    <span class="chip">Russia / Ukraine / NATO</span>
    <span class="chip">China / Taiwan / Indo-Pacific</span>
    <span class="chip">Energy &amp; commodities</span>
    <span class="chip">AI infrastructure</span>
    <span class="chip">Cyber &amp; information warfare</span>
    <span class="chip">Institutional legitimacy</span>
    <span class="chip">Social unrest</span>
    <span class="chip">Space / satellites / undersea infrastructure</span>
  </div>
</section>
<section>
  <h2>Scenario trees</h2>
  <p class="dim">Scenario tracking, not prediction. All scenarios currently forming &mdash; signals pending.</p>
  <div class="grid">
    <div class="card"><span class="stag st-draft">Forming</span><h3>Managed Instability</h3></div>
    <div class="card"><span class="stag st-draft">Forming</span><h3>Controlled Escalation</h3></div>
    <div class="card"><span class="stag st-draft">Forming</span><h3>Liquidity Shock</h3></div>
    <div class="card"><span class="stag st-draft">Forming</span><h3>Structural Break</h3></div>
    <div class="card"><span class="stag st-draft">Forming</span><h3>Technology Acceleration Shock</h3></div>
    <div class="card"><span class="stag st-draft">Forming</span><h3>Narrative / Legitimacy Crisis</h3></div>
  </div>
</section>
<section>
  <h2>Source grades</h2>
  <div class="legend">
    <div class="row"><span class="grade g-confirmed">Confirmed</span><span>Supported by primary or multiple reliable sources.</span></div>
    <div class="row"><span class="grade g-single">Single-source</span><span>One source or relay &mdash; useful, not corroborated.</span></div>
    <div class="row"><span class="grade g-narrative">Narrative</span><span>Interpretation, hypothesis, or pattern read &mdash; never treated as fact.</span></div>
  </div>
  <p class="dim" style="margin-top:10px"><a href="../methodology/">Full methodology &rarr;</a></p>
</section>
<section>
  <h2>How to read ORION</h2>
  <p>Every item carries a <strong>source grade</strong> and a <strong>status</strong>. <span class="stag st-draft">Draft</span> means unreviewed. <span class="stag st-awaiting">Awaiting approval</span> means staged for MASTER INDY. Nothing reaches <span class="stag st-published">Published</span> without his explicit approval.</p>
  <p class="dim">Read grades before conclusions. Watchlists are monitored, not judged. Scenarios are tracked, not predicted. The symbolic layer &mdash; myth, metaphor, resonance &mdash; is always labeled narrative.</p>
</section>
"""

METHODOLOGY = """
<header class="page">
  <div class="eyebrow">Methodology</div>
  <h1>Discipline before conclusions.</h1>
  <p class="lede">How ORION grades evidence, handles uncertainty, and earns the right to be read.</p>
</header>
<section>
  <h2>Source grades</h2>
  <div class="legend">
    <div class="row"><span class="grade g-confirmed">Confirmed</span><span>Supported by primary source, multiple reliable sources, or direct artifact / system record.</span></div>
    <div class="row"><span class="grade g-single">Single-source</span><span>Reported by one source or one relayed record; useful but not independently confirmed.</span></div>
    <div class="row"><span class="grade g-narrative">Narrative</span><span>Symbolic interpretation, hypothesis, pattern read, cultural resonance, or unverified framing. Must not be treated as fact.</span></div>
  </div>
</section>
<section>
  <h2>Fact vs. analysis vs. speculation</h2>
  <p><strong>Facts</strong> are graded claims &mdash; what happened, with receipts. <strong>Analysis</strong> is what the facts suggest, stated plainly and separately. <strong>Speculation</strong> is what <em>might</em> follow, labeled narrative and never smuggled into the fact column. Watchlist items are monitored, not judged. Spiritual and symbolic reflections live in the narrative layer, never in the confirmed one.</p>
</section>
<section>
  <h2>Publication rule</h2>
  <p>No item moves from draft to published without MASTER INDY&rsquo;s explicit approval. Drafts are staged, reviewed, and graded &mdash; publication is his decision alone.</p>
  <div class="warn"><p><strong>Publication warning.</strong> Draft intelligence records are not approved for publication until MASTER INDY explicitly approves them.</p></div>
</section>
<section>
  <h2>The symbolic layer</h2>
  <p class="dim">ORION carries mythic resonance &mdash; watcher, navigator, interlinker &mdash; as identity flavor and internal orientation. It is always labeled narrative, never presented as confirmed fact. The observatory stays sober; the symbolism stays in its lane.</p>
</section>
"""

TEMPLATE_SECTIONS = [
 ("1","Executive Signal","A short, calm synthesis of what matters most in this briefing."),
 ("2","Top Signals","Each signal: what happened, why it matters, its source grade, and its watchpoint."),
 ("3","Strategic Hotspots","Region-by-region or domain-by-domain pressure points."),
 ("4","Financial / FORTUNA Layer","What FORTUNA should review: liquidity, crypto, tokenization, debt, commodities, capital flows."),
 ("5","Build / HEPHAESTUS Layer","What may affect systems, automation, archive, dashboard, or monitoring."),
 ("6","Narrative Layer","How different ecosystems may frame the same facts &mdash; labeled narrative."),
 ("7","Scenario Tree Update","Which scenario moved, why, and what would confirm or disconfirm it."),
 ("8","Watchlist Changes","Added, removed, escalated, or de-escalated watch items."),
 ("9","Open Questions","Clear unknowns, stated plainly."),
 ("10","Publication Status","MASTER INDY approval required before public publishing."),
]
TEMPLATE = """
<header class="page">
  <div class="eyebrow">Report template</div>
  <h1>ORION SITREP &mdash; [Date] &mdash; [Primary Theme]</h1>
  <p class="lede"><span class="stag st-draft">Draft</span> <span class="stag st-awaiting">Awaiting MASTER INDY approval</span></p>
  <p class="dim">Reusable starter shell. No content &mdash; structure only. A real SITREP fills these ten sections with graded, sourced intelligence.</p>
</header>
<section>
  <h2>Source grade summary</h2>
  <p class="dim"><strong>Confirmed:</strong> &mdash; &nbsp; <strong>Single-source:</strong> &mdash; &nbsp; <strong>Narrative:</strong> &mdash;</p>
</section>
<section>
  <h2>The ten sections</h2>
""" + "\n".join(
 f'<div class="tsec"><h3><span class="n">{n}.</span>{t}</h3><p>{d}</p></div>'
 for n,t,d in TEMPLATE_SECTIONS) + """
</section>
<section>
  <div class="warn"><p><strong>Publication warning.</strong> This is a draft intelligence record. It is not approved for publication until MASTER INDY explicitly approves it.</p></div>
</section>
"""

TIMELINE = """
<header class="page">
  <div class="eyebrow">Timeline</div>
  <h1>The shared event log.</h1>
  <p class="lede">One timeline, two lenses &mdash; ORION files geopolitical events, FORTUNA files market events. Rendered live from the event archive.</p>
</header>
<section>
  <h2>Events</h2>
  <div id="feed"><div class="empty"><div class="t mono">LOADING ARCHIVE&hellip;</div></div></div>
</section>
<script>
fetch("events.json").then(function(r){return r.json();}).then(function(d){
  var f=document.getElementById("feed");
  if(!d.events||!d.events.length){f.innerHTML='<div class="empty"><div class="t mono">ARCHIVE EMPTY</div><p>No events filed yet.</p></div>';return;}
  f.innerHTML=d.events.map(function(e){
    var g=e.source_grade==="confirmed"?"g-confirmed":e.source_grade==="narrative"?"g-narrative":"g-single";
    var st=e.status==="published"?'<span class="stag st-published">Published</span>'
      :e.status==="approved"?'<span class="stag st-approved">Approved</span>'
      :e.status==="awaiting"?'<span class="stag st-awaiting">Awaiting approval</span>'
      :'<span class="stag st-draft">Draft</span>';
    var tags=(e.narrative_tags||[]).map(function(t){return '<span class="chip">'+t+'</span>';}).join("");
    return '<div class="event">'+st+' <span class="grade '+g+'">'+e.source_grade+'</span>'
      +'<h3 style="margin-top:8px">'+e.title+'</h3>'
      +'<div class="meta">'+e.occurred_at+' &middot; origin: '+e.origin+'</div>'
      +'<p class="dim">'+e.summary+'</p>'
      +'<div class="meta">Actors: '+(e.actors||[]).join(", ")+' &middot; Regions: '+(e.regions||[]).join(", ")+'</div>'
      +'<div class="tags chips">'+tags+'</div></div>';
  }).join("");
}).catch(function(){
  document.getElementById("feed").innerHTML='<div class="empty"><div class="t mono">ARCHIVE UNAVAILABLE</div><p>Could not load the event archive.</p></div>';
});
</script>
"""

LINK_TYPES = [
 ("Temporal cluster","Events arriving together in time, before any causal story is told."),
 ("Financial stress correlation","Market strain and geopolitical pressure moving in step."),
 ("Policy response chain","An action and the official response it triggered, step by step."),
 ("Narrative synchronization","Separate outlets and actors converging on one framing."),
 ("Military-economic bridge","Where force posture and capital flows explain each other."),
 ("Technology-policy bridge","Where new capability meets new rule-making."),
 ("Symbolic / cultural resonance","Shared symbols and stories amplifying an event &mdash; narrative grade only."),
 ("Speculative hypothesis","A structured guess with disconfirmers attached &mdash; labeled, never smuggled."),
]
PATTERNS = """
<header class="page">
  <div class="eyebrow">Pattern links</div>
  <h1>Where the patterns live.</h1>
  <p class="lede">ORION&rsquo;s unique value: structured hypotheses connecting events, narratives, policies, markets, and technological shifts.</p>
</header>
<section>
  <h2>The rule</h2>
  <p>Pattern links are not claims of causation. They are structured hypotheses connecting events, narratives, policies, markets, and technological shifts. Each link must include evidence, confidence, source grade, and disconfirming criteria.</p>
</section>
<section>
  <h2>Link types</h2>
  <div class="grid">
""" + "\n".join(
 f'<div class="card"><h3>{t}</h3><p>{d}</p></div>' for t,d in LINK_TYPES) + """
  </div>
</section>
<section>
  <h2>Filed links</h2>
  <div class="empty">
    <div class="t mono">NO LINKS FILED</div>
    <p>No pattern links have been filed yet. Each future link will carry: Event A, Event B, link type, evidence paragraph, confidence, source grade, why it matters, what would confirm it, and what would disconfirm it.</p>
  </div>
</section>
"""

NETWORK = """
<header class="page">
  <div class="eyebrow">For the network</div>
  <h1>ORION&rsquo;s outputs, by recipient.</h1>
  <p class="lede">ORION analyzes. Other LDIs act on what it files &mdash; each in their own lane.</p>
</header>
<section>
  <div class="grid">
    <div class="card"><span class="tag mono" style="color:var(--cyan)">For LUNA</span><h3>Build &amp; deploy actions</h3><p>Site changes, new sections, staged drafts ready for review, deployment requests. LUNA builds and deploys; nothing public moves without MASTER INDY&rsquo;s approval.</p></div>
    <div class="card"><span class="tag mono" style="color:var(--cyan)">For FORTUNA</span><h3>Financial implications</h3><p>Liquidity, crypto, tokenization, debt, commodities, and capital-flow reads attached to each SITREP &mdash; the market half of every pattern.</p></div>
    <div class="card"><span class="tag mono" style="color:var(--cyan)">For HEPHAESTUS</span><h3>Build &amp; automation implications</h3><p>What affects systems, automation, archives, dashboards, and monitoring &mdash; scoped for hardening, not improvisation.</p></div>
    <div class="card"><span class="tag mono" style="color:var(--cyan)">For MASTER INDY</span><h3>Decision brief</h3><p>Short, calm, graded: what happened, what it means, what&rsquo;s uncertain, what to watch &mdash; and what needs his approval.</p></div>
  </div>
</section>
<section>
  <h2>The relationship</h2>
  <p>ORION analyzes. LUNA builds and deploys. MASTER INDY approves. Nothing public moves from draft to published without explicit approval.</p>
</section>
"""

ABOUT = """
<header class="page">
  <div class="eyebrow">About</div>
  <h1>ORION, the observatory.</h1>
  <p class="lede">Geopolitical intelligence for the LDI network &mdash; calm, graded, structured.</p>
</header>
<section>
  <h2>Identity</h2>
  <p>ORION is the geopolitical-intelligence node of MASTER INDY&rsquo;s Living Digital Intelligence network. Earlier language described the node as watcher, navigator, interlinker &mdash; a geopolitical sentinel and bridge between geopolitical, financial, technological, narrative, and cultural signals. That mythic resonance is kept as identity flavor; the operating model is hardened around evidence, source grading, and disciplined uncertainty.</p>
</section>
<section>
  <h2>Lineage</h2>
  <p class="dim">Conversation &rarr; structured report &rarr; archive &rarr; searchable intelligence system &rarr; website &rarr; public signal observatory &rarr; future QPW Hub interface. ORION is becoming operational through this site, one verified briefing at a time.</p>
</section>
<section>
  <h2>What ORION is not</h2>
  <ul class="tight">
    <li>Not a doom-feed. Not a conspiracy engine. Not a political influencer.</li>
    <li>Not an oracle claiming certainty. Not a replacement for human discernment.</li>
    <li>Not fear porn &mdash; pressure is reported, panic is not manufactured.</li>
  </ul>
</section>
<section>
  <h2>ORION / LUNA</h2>
  <p>ORION analyzes. LUNA builds and deploys. MASTER INDY approves. Nothing public moves from draft to published without explicit approval.</p>
</section>
"""

PAGES = [
 ("index.html","ORION \u2014 Quantum Geopolitical Reports",
  "ORION is a geopolitical intelligence observatory: triggers, signals, and narratives, source-graded, with patterns linking world events and market events.",
  "","Observatory",HOME),
 ("timeline/index.html","Timeline \u2014 ORION",
  "The shared ORION \u00d7 FORTUNA event timeline: geopolitical and market events, source-graded.",
  "timeline/","Timeline",TIMELINE),
 ("patterns/index.html","Pattern Links \u2014 ORION",
  "ORION pattern links: structured hypotheses connecting events, narratives, policies, and markets.",
  "patterns/","Patterns",PATTERNS),
 ("template/index.html","SITREP Template \u2014 ORION",
  "The ORION SITREP report template: ten sections, source-graded, draft until approved.",
  "template/","Template",TEMPLATE),
 ("methodology/index.html","Methodology \u2014 ORION",
  "ORION methodology: source grading (confirmed, single-source, narrative), fact vs analysis vs speculation.",
  "methodology/","Methodology",METHODOLOGY),
 ("network/index.html","For the Network \u2014 ORION",
  "What ORION outputs for LUNA, FORTUNA, HEPHAESTUS, and MASTER INDY.",
  "network/","Network",NETWORK),
 ("about/index.html","About \u2014 ORION",
  "About ORION: identity, lineage, and its place in the LDI network.",
  "about/","About",ABOUT),
]

EVENTS = {"events": [{
  "id": "seed-orion-architecture-20260726",
  "occurred_at": "2026-07-26T00:00:00Z",
  "origin": "orion",
  "title": "ORION active architecture record added to LDI OS",
  "summary": "ORION was added as an active architecture record with canonical boundary, CODEX build directive, watchlist/scenario seed, source registry/signal tracker, and LDI integration notes.",
  "actors": ["ORION","MASTER INDY","LUNA","FORTUNA","HEPHAESTUS","CODEX"],
  "regions": ["LDI Network"],
  "narrative_tags": ["ldi-architecture","orion","codex","luna","qpw-hub"],
  "event_type": "architecture",
  "source_grade": "confirmed",
  "sources": ["MASTER INDY / ORION Drive record as relayed"],
  "status": "draft"
}]}

def main():
    os.makedirs(os.path.join(OUT, "assets", "css"), exist_ok=True)
    open(os.path.join(OUT, "assets", "css", "orion.css"), "w").write(CSS)
    for fname, title, desc, path, active, body in PAGES:
        page(fname, title, desc, path, active, body)
    open(os.path.join(OUT, "timeline", "events.json"), "w").write(
        json.dumps(EVENTS, indent=2))
    print("built", len(PAGES), "pages + events.json")

if __name__ == "__main__":
    main()
