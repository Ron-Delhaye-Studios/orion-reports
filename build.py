#!/usr/bin/env python3
"""Build the ORION site from the official branding kit. Run: python3 build.py
Single generator = source of truth. Design tokens per ORION branding kit:
Midnight Navy #0A1428 / Obsidian #0B1B2E / Slate #162A44 / Star Silver #C9D6E8 /
Moon White #EAF2FF / Quiet Gold #D9A437 / Cyan #00D1FF / Electric #3B82F6 /
Indigo #4B5CF6 / Alert Red #EF4444. Playfair Display / Inter / JetBrains Mono.
Tagline: "Signal without panic. Pattern without overclaiming." AD ASTRA."""
import os, json

OUT = os.path.dirname(os.path.abspath(__file__))
SITE = "https://ron-delhaye-studios.github.io/orion-reports"

CSS = r"""
:root{
  --midnight:#0A1428; --obsidian:#0B1B2E; --slate:#162A44;
  --silver:#C9D6E8; --moon:#EAF2FF; --gold:#D9A437;
  --cyan:#00D1FF; --electric:#3B82F6; --indigo:#4B5CF6; --red:#EF4444;
  --green:#34D399; --purple:#A78BFA; --amber:#F5A623; --gray:#9AA3B2;
  --bg:var(--midnight); --card:#0D1830; --card2:#0B1528; --line:#22344F;
  --ink:var(--moon); --dim:#9FB2CC; --faint:#64748F;
}
*{box-sizing:border-box;margin:0;padding:0}
html{background:var(--midnight);scroll-behavior:smooth}
body{background:transparent;color:var(--ink);font-family:Inter,-apple-system,"Segoe UI",Helvetica,Arial,sans-serif;
  line-height:1.65;min-height:100vh;display:flex;flex-direction:column;font-size:15px;
  -webkit-font-smoothing:antialiased}
#stars{position:fixed;inset:0;z-index:-3}
body::before{content:"";position:fixed;inset:0;z-index:-2;pointer-events:none;
  background:radial-gradient(ellipse 90% 60% at 50% -10%,rgba(59,130,246,.08),transparent 70%)}
h1,h2,h3,.serif{font-family:"Playfair Display",Georgia,serif}
.mono{font-family:"JetBrains Mono",ui-monospace,Menlo,Consolas,monospace}
.wrap{max-width:1080px;margin:0 auto;padding:0 20px;width:100%}
/* ---------- nav ---------- */
nav.top{border-bottom:1px solid var(--line);background:rgba(10,20,40,.82);backdrop-filter:blur(10px);
  position:sticky;top:0;z-index:50}
nav.top .wrap{display:flex;align-items:center;gap:6px;overflow-x:auto;padding-top:12px;padding-bottom:12px;scrollbar-width:none}
nav.top .wrap::-webkit-scrollbar{display:none}
.brand{display:flex;align-items:center;gap:10px;text-decoration:none;margin-right:16px;white-space:nowrap;flex:none}
.brand svg{width:30px;height:30px}
.brand .wm{font-family:"Playfair Display",serif;font-weight:700;font-size:19px;letter-spacing:.24em;color:var(--moon);line-height:1}
.brand .wm small{display:block;font-family:"JetBrains Mono",monospace;font-weight:400;font-size:7.5px;letter-spacing:.22em;color:var(--faint);margin-top:3px}
nav.top a.nl{color:var(--dim);text-decoration:none;font-size:12.5px;font-weight:500;letter-spacing:.06em;
  padding:7px 13px;border-radius:20px;white-space:nowrap;flex:none;transition:all .18s}
nav.top a.nl:hover{color:var(--moon)}
nav.top a.nl.on{background:var(--gold);color:#0A1428;font-weight:600}
/* ---------- page header ---------- */
header.page{padding:52px 0 10px}
.eyebrow{font-family:"JetBrains Mono",monospace;font-size:11px;letter-spacing:.34em;text-transform:uppercase;color:var(--electric)}
header.page h1{font-size:clamp(30px,5vw,44px);font-weight:700;color:var(--moon);margin:12px 0 8px;letter-spacing:.01em}
.lede{color:var(--dim);font-size:15.5px;max-width:660px}
section.blk{padding:34px 0;border-bottom:1px solid var(--line)}
h2.sec{font-family:"JetBrains Mono",monospace;font-size:12px;font-weight:500;letter-spacing:.3em;text-transform:uppercase;
  color:var(--silver);margin-bottom:6px}
p.sub{color:var(--dim);font-size:14px;margin-bottom:18px;max-width:640px}
p{font-size:14.5px;color:var(--ink);max-width:680px}
.dim{color:var(--dim)} .faint{color:var(--faint)} .gold{color:var(--gold)}
/* ---------- badges ---------- */
.badge{display:inline-flex;align-items:center;font-family:"JetBrains Mono",monospace;font-size:10px;font-weight:500;
  letter-spacing:.16em;text-transform:uppercase;border-radius:4px;padding:3px 9px;border:1px solid;white-space:nowrap}
.st-draft{color:var(--gray);border-color:#4a5568;background:rgba(154,163,178,.08)}
.st-awaiting{color:var(--amber);border-color:rgba(245,166,35,.5);background:rgba(245,166,35,.08)}
.st-approved{color:var(--electric);border-color:rgba(59,130,246,.5);background:rgba(59,130,246,.1)}
.st-published{color:var(--green);border-color:rgba(52,211,153,.5);background:rgba(52,211,153,.08)}
.g-confirmed{color:var(--electric);border-color:rgba(59,130,246,.5);background:rgba(59,130,246,.1)}
.g-single{color:var(--amber);border-color:rgba(245,166,35,.5);background:rgba(245,166,35,.08)}
.g-narrative{color:var(--purple);border-color:rgba(167,139,250,.5);background:rgba(167,139,250,.08)}
.pill{display:inline-block;font-family:"JetBrains Mono",monospace;font-size:10px;letter-spacing:.18em;text-transform:uppercase;
  border-radius:20px;padding:4px 12px;border:1px solid}
.pill-elevated{color:var(--amber);border-color:rgba(245,166,35,.55);background:rgba(245,166,35,.1)}
.pill-watching{color:var(--silver);border-color:#3a4c68;background:rgba(201,214,232,.06)}
.pill-active{color:var(--green);border-color:rgba(52,211,153,.55);background:rgba(52,211,153,.1)}
.pill-forming{color:var(--faint);border-color:#2c3a52;background:rgba(100,116,143,.07)}
/* ---------- buttons ---------- */
.btn{display:inline-block;text-decoration:none;font-weight:600;font-size:13px;letter-spacing:.14em;text-transform:uppercase;
  border-radius:6px;padding:13px 28px;transition:all .18s;cursor:pointer;border:1px solid transparent}
.btn-primary{background:var(--gold);color:#0A1428}
.btn-primary:hover{background:#e8b84f;box-shadow:0 0 24px rgba(217,164,55,.35)}
.btn-ghost{border-color:#3a4c68;color:var(--silver);background:transparent}
.btn-ghost:hover{border-color:var(--silver);color:var(--moon)}
/* ---------- cards ---------- */
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:14px}
.card{border:1px solid var(--line);border-radius:12px;padding:20px;background:linear-gradient(180deg,var(--card),var(--card2));
  position:relative;transition:border-color .18s, transform .18s}
.card:hover{border-color:#33507c}
.card h3{font-size:17px;color:var(--moon);margin:0 0 8px;font-weight:700}
.card p{font-size:13px;color:var(--dim)}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin-top:12px}
.chip{font-family:"JetBrains Mono",monospace;font-size:10.5px;letter-spacing:.08em;color:var(--silver);
  border:1px solid var(--line);border-radius:20px;padding:4px 11px;background:rgba(201,214,232,.05);text-transform:uppercase}
.actor{display:inline-block;font-family:"JetBrains Mono",monospace;font-size:10px;letter-spacing:.1em;color:var(--cyan);
  border:1px solid rgba(0,209,255,.35);border-radius:4px;padding:2px 8px;margin:2px 4px 2px 0;text-transform:uppercase}
/* ---------- sample ribbon (honesty) ---------- */
.sample{border-style:dashed;border-color:rgba(245,166,35,.55)!important}
.sample-ribbon{display:block;font-family:"JetBrains Mono",monospace;font-size:10px;letter-spacing:.2em;color:var(--amber);
  text-transform:uppercase;margin-bottom:10px}
.sample-ribbon::before{content:"\25C8  "}
/* ---------- empty / warn ---------- */
.empty{border:1px dashed var(--line);border-radius:12px;padding:30px 24px;background:rgba(11,27,46,.5);margin-top:8px}
.empty .t{font-family:"JetBrains Mono",monospace;color:var(--cyan);font-size:12px;letter-spacing:.2em;margin-bottom:8px}
.empty p{font-size:13.5px;color:var(--dim)}
.warn{border:1px solid rgba(217,164,55,.4);border-radius:12px;padding:18px 20px;background:rgba(217,164,55,.05);margin-top:16px}
.warn p{font-size:13px;color:var(--gold)}
.legend{margin-top:14px}
.legend .row{display:flex;gap:12px;align-items:flex-start;margin:10px 0;font-size:13.5px;color:var(--dim)}
.legend .row .badge{flex:none;margin-top:2px}
/* ---------- hero ---------- */
.hero{position:relative;overflow:hidden;text-align:center;padding:88px 20px 70px;
  background:
    radial-gradient(ellipse 130% 55% at 50% 122%, rgba(59,130,246,.30), rgba(59,130,246,.07) 45%, transparent 70%),
    radial-gradient(ellipse 80% 30% at 50% 116%, rgba(217,164,55,.10), transparent 60%),
    linear-gradient(180deg,#060b18 0%, #0A1428 60%, #0c1830 100%)}
.hero .limb{position:absolute;left:-30%;right:-30%;bottom:-46%;height:70%;border-radius:50%;
  border-top:2px solid rgba(140,190,255,.28);box-shadow:0 -6px 60px rgba(59,130,246,.25), 0 -2px 18px rgba(0,209,255,.18);
  pointer-events:none}
.hero-kicker{font-family:"JetBrains Mono",monospace;font-size:11px;letter-spacing:.42em;color:var(--silver);text-transform:uppercase}
.hero-title{font-size:clamp(58px,15vw,118px);font-weight:800;letter-spacing:.16em;color:var(--gold);
  margin:14px 0 2px;text-shadow:0 0 50px rgba(217,164,55,.35);line-height:1}
.hero-sub{font-family:"JetBrains Mono",monospace;font-size:11px;letter-spacing:.34em;color:var(--dim);text-transform:uppercase;margin-bottom:22px}
.hero-tag{font-family:"Playfair Display",serif;font-size:clamp(17px,3.4vw,23px);color:var(--moon);max-width:620px;margin:0 auto 30px;line-height:1.5}
.hero-cats{font-family:"JetBrains Mono",monospace;font-size:10.5px;letter-spacing:.24em;color:var(--faint);text-transform:uppercase;margin-bottom:30px}
.hero-cats b{color:var(--silver);font-weight:500}
.hero-btns{display:flex;gap:14px;justify-content:center;flex-wrap:wrap;margin-bottom:48px}
.hero-icons{display:flex;justify-content:center;gap:8px;flex-wrap:wrap;max-width:760px;margin:0 auto}
.hicon{display:flex;flex-direction:column;align-items:center;gap:10px;padding:16px 10px;min-width:104px;flex:1}
.hicon .ring{width:52px;height:52px;border:1px solid #33507c;border-radius:50%;display:flex;align-items:center;justify-content:center;
  color:var(--silver);background:rgba(22,42,68,.4)}
.hicon .ring svg{width:24px;height:24px}
.hicon span{font-family:"JetBrains Mono",monospace;font-size:9.5px;letter-spacing:.18em;color:var(--dim);text-transform:uppercase;text-align:center;line-height:1.5}
/* ---------- report cards ---------- */
.tabs{display:flex;gap:8px;flex-wrap:wrap;margin:4px 0 20px}
.tab{font-family:Inter,sans-serif;font-size:12.5px;font-weight:500;color:var(--dim);background:transparent;
  border:1px solid var(--line);border-radius:20px;padding:8px 16px;cursor:pointer;transition:all .15s}
.tab:hover{color:var(--moon);border-color:#33507c}
.tab.on{background:var(--electric);border-color:var(--electric);color:#fff;font-weight:600}
.rcard{display:flex;gap:0;border:1px solid var(--line);border-radius:12px;overflow:hidden;margin:14px 0;
  background:linear-gradient(180deg,var(--card),var(--card2));transition:border-color .18s}
.rcard:hover{border-color:#33507c}
.rcard .thumb{flex:none;width:200px;min-height:170px;position:relative;display:flex;align-items:center;justify-content:center;overflow:hidden}
.rcard .thumb svg{width:56px;height:56px;color:rgba(234,242,255,.5);position:relative;z-index:1}
.rcard .thumb::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,transparent 40%,rgba(6,11,24,.55))}
.rcard .tbody{padding:18px 20px;flex:1;min-width:0}
.rcard .meta{display:flex;align-items:center;gap:10px;flex-wrap:wrap;font-family:"JetBrains Mono",monospace;
  font-size:10.5px;letter-spacing:.1em;color:var(--faint);text-transform:uppercase;margin-bottom:8px}
.rcard h3{font-size:20px;margin:0 0 8px}
.rcard .sum{font-size:13.5px;color:var(--dim)}
.rcard .foot{display:flex;align-items:center;justify-content:space-between;margin-top:12px;gap:10px}
.rcard .arrow{color:var(--gold);font-size:20px;text-decoration:none;flex:none}
.thumb-geo{background:linear-gradient(135deg,#12294d,#0B1B2E 70%)}
.thumb-energy{background:linear-gradient(135deg,#3d2c12,#0B1B2E 70%)}
.thumb-tech{background:linear-gradient(135deg,#101d3f,#0B1B2E 70%)}
.thumb-flag{background:linear-gradient(135deg,#2c1a2e,#0B1B2E 70%)}
/* ---------- timeline ---------- */
.tl{position:relative;margin-top:8px;padding-left:26px}
.tl::before{content:"";position:absolute;left:8px;top:6px;bottom:6px;width:2px;
  background:linear-gradient(180deg,var(--gold),var(--electric),var(--indigo));opacity:.5;border-radius:2px}
.tl-item{position:relative;margin:0 0 22px}
.tl-item::before{content:"";position:absolute;left:-24px;top:8px;width:12px;height:12px;border-radius:50%;
  background:var(--midnight);border:2px solid var(--gold);box-shadow:0 0 10px rgba(217,164,55,.5)}
.tl-date{font-family:"JetBrains Mono",monospace;font-size:11px;letter-spacing:.14em;color:var(--gold);margin-bottom:8px}
.tl-card{border:1px solid var(--line);border-radius:12px;padding:18px 20px;background:linear-gradient(180deg,var(--card),var(--card2))}
.tl-card .top{display:flex;justify-content:space-between;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:8px}
.tl-card h3{font-size:18px;margin:0 0 6px}
.tl-card .meta{font-family:"JetBrains Mono",monospace;font-size:11px;color:var(--faint);letter-spacing:.06em;margin:10px 0 4px}
.tl-card p{font-size:13.5px;color:var(--dim)}
/* ---------- watchlist tiles ---------- */
.wtile{border:1px solid var(--line);border-radius:12px;padding:20px 18px;background:linear-gradient(180deg,var(--card),var(--card2));
  display:flex;flex-direction:column;gap:12px;align-items:flex-start;transition:border-color .18s}
.wtile:hover{border-color:#33507c}
.wtile .ic{width:44px;height:44px;border:1px solid #33507c;border-radius:10px;display:flex;align-items:center;justify-content:center;color:var(--silver)}
.wtile .ic svg{width:22px;height:22px}
.wtile h3{font-size:15.5px;margin:0;font-family:Inter,sans-serif;font-weight:600}
.scenario{display:flex;align-items:center;gap:16px;border:1px solid var(--line);border-radius:12px;padding:20px;
  background:linear-gradient(180deg,var(--card),var(--card2));margin:12px 0;text-decoration:none;color:inherit}
.scenario:hover{border-color:#33507c}
.scenario .grow{flex:1;min-width:0}
.scenario h3{font-size:18px;margin:0 0 4px}
.scenario .arrow{color:var(--gold);font-size:22px;flex:none}
.minigraph{flex:none}
/* ---------- pattern network ---------- */
.netwrap{border:1px solid var(--line);border-radius:16px;background:radial-gradient(ellipse 70% 70% at 50% 50%,rgba(22,42,68,.6),rgba(11,27,46,.9));
  padding:10px;margin:8px 0 20px;overflow:hidden}
.netwrap svg{display:block;width:100%;height:auto}
.plink{border:1px solid var(--line);border-radius:12px;padding:22px;background:linear-gradient(180deg,var(--card),var(--card2));margin:14px 0}
.plink .evs{display:flex;align-items:stretch;gap:12px;margin:12px 0;flex-wrap:wrap}
.plink .ev{flex:1;min-width:200px;border:1px solid var(--line);border-radius:8px;padding:14px;background:rgba(6,11,24,.5)}
.plink .ev .lbl{font-family:"JetBrains Mono",monospace;font-size:10px;letter-spacing:.2em;color:var(--faint);text-transform:uppercase;margin-bottom:6px}
.plink .ev h4{font-family:"Playfair Display",serif;font-size:15px;color:var(--moon);margin:0 0 4px}
.plink .ev .d{font-family:"JetBrains Mono",monospace;font-size:11px;color:var(--dim)}
.plink .go{align-self:center;color:var(--gold);font-size:24px}
.plink .kv{display:grid;grid-template-columns:150px 1fr;gap:8px 14px;margin-top:12px;font-size:13px}
.plink .kv .k{font-family:"JetBrains Mono",monospace;font-size:10.5px;letter-spacing:.12em;color:var(--faint);text-transform:uppercase;padding-top:2px}
.plink .kv .v{color:var(--dim)}
/* ---------- template sections ---------- */
.tsec{border:1px solid var(--line);border-radius:12px;padding:18px 20px;margin:12px 0;background:rgba(13,24,48,.5)}
.tsec h3{margin:0 0 6px;font-size:16px;color:var(--silver);font-family:Inter,sans-serif;font-weight:600}
.tsec h3 .n{font-family:"JetBrains Mono",monospace;color:var(--faint);margin-right:10px;font-size:13px}
.tsec p{font-size:13px;color:var(--dim)}
/* ---------- footer ---------- */
footer{margin-top:auto;padding:34px 0 40px;color:var(--faint);font-size:12px;background:rgba(6,11,24,.6)}
footer .rule{border-top:1px solid var(--line);padding-top:20px;display:flex;justify-content:space-between;flex-wrap:wrap;gap:10px;align-items:center}
footer .tag{font-family:"JetBrains Mono",monospace;font-size:10px;letter-spacing:.22em;color:var(--faint);text-transform:uppercase}
a{color:var(--cyan)}
::selection{background:rgba(217,164,55,.3)}
@media(max-width:640px){
  .rcard{flex-direction:column}
  .rcard .thumb{width:100%;min-height:120px}
  .plink .kv{grid-template-columns:1fr}
  .hero{padding:64px 16px 54px}
}
@media (prefers-reduced-motion:reduce){
  html{scroll-behavior:auto}
  *{transition:none!important}
}
"""

STARFIELD = r"""
/* starfield — faint twinkling stars, pauses when hidden or reduced-motion */
(function(){
  if(matchMedia("(prefers-reduced-motion: reduce)").matches) return;
  var c=document.getElementById("stars"),x=c.getContext("2d"),stars=[],W,H,timer=null,t=0;
  function size(){W=c.width=innerWidth;H=c.height=innerHeight;stars=[];
    for(var i=0;i<Math.min(240,W*H/8500);i++)stars.push({x:Math.random()*W,y:Math.random()*H,
      r:Math.random()*1.2+.2,p:Math.random()*6.28,s:.4+Math.random()*1.2,
      c:Math.random()<.12?"217,164,55":Math.random()<.25?"0,209,255":"201,214,232"});}
  function draw(){t+=.016;x.clearRect(0,0,W,H);
    for(var i=0;i<stars.length;i++){var s=stars[i],a=.22+.55*Math.abs(Math.sin(t*s.s+s.p));
      x.fillStyle="rgba("+s.c+","+a.toFixed(2)+")";
      x.beginPath();x.arc(s.x,s.y,s.r,0,6.283);x.fill();}}
  size();addEventListener("resize",size);
  function go(){if(!timer)timer=setInterval(draw,50);}
  function stop(){clearInterval(timer);timer=null;}
  document.addEventListener("visibilitychange",function(){document.hidden?stop():go();});
  go();
})();
"""

def _ic(paths, vb="0 0 24 24"):
    return ('<svg viewBox="'+vb+'" fill="none" stroke="currentColor" stroke-width="1.6" '
            'stroke-linecap="round" stroke-linejoin="round">'+paths+'</svg>')

ICONS = {
 "star": _ic('<circle cx="12" cy="12" r="9"/><path d="M12 5l1.8 5.2L19 12l-5.2 1.8L12 19l-1.8-5.2L5 12l5.2-1.8z" fill="currentColor" stroke="none"/>'),
 "globe": _ic('<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.6 3.8 5.7 3.8 9S14.5 18.4 12 21c-2.5-2.6-3.8-5.7-3.8-9S9.5 5.6 12 3z"/>'),
 "chart": _ic('<path d="M4 20V10M10 20V4M16 20v-8M21 20H3"/>'),
 "cpu": _ic('<rect x="7" y="7" width="10" height="10" rx="2"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M5 5l2 2M17 17l2 2M19 5l-2 2M7 17l-2 2"/>'),
 "doc": _ic('<path d="M7 3h7l4 4v14H7z"/><path d="M14 3v4h4M10 12h5M10 16h5"/>'),
 "users": _ic('<circle cx="9" cy="8" r="3.5"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6M16 4.5a3.5 3.5 0 010 7M21 20c0-2.8-1.9-5.1-4.5-5.8"/>'),
 "bank": _ic('<path d="M3 9l9-6 9 6M4 9v10M20 9v10M8 12v5M12 12v5M16 12v5M3 20h18"/>'),
 "bolt": _ic('<path d="M13 2L4 14h6l-1 8 9-12h-6z"/>'),
 "shield": _ic('<path d="M12 3l7 3v6c0 4.5-3 7.5-7 9-4-1.5-7-4.5-7-9V6z"/>'),
 "sat": _ic('<rect x="9" y="9" width="6" height="6" rx="1" transform="rotate(45 12 12)"/><path d="M3 13l4-4M17 15l4-4M7 7l-2-2M19 7l2-2M5 19l3-1M19 19l-3-1"/>'),
 "eye": _ic('<path d="M2 12s3.5-6.5 10-6.5S22 12 22 12s-3.5 6.5-10 6.5S2 12 2 12z"/><circle cx="12" cy="12" r="2.5"/>'),
 "scale": _ic('<path d="M12 3v18M5 7l7-4 7 4M5 7l-2.5 6a3 3 0 005 0L5 7zM19 7l-2.5 6a3 3 0 005 0L19 7zM8 21h8"/>'),
 "drop": _ic('<path d="M12 3s6 6.5 6 11a6 6 0 01-12 0c0-4.5 6-11 6-11z"/>'),
 "flag": _ic('<path d="M5 21V4M5 4h12l-2.5 4L17 12H5"/>'),
}

LOGO = ('<svg viewBox="0 0 32 32" fill="none" aria-hidden="true">'
        '<circle cx="16" cy="16" r="13.5" stroke="#D9A437" stroke-width="1.4"/>'
        '<circle cx="16" cy="16" r="9.5" stroke="#D9A437" stroke-width="0.7" opacity="0.5"/>'
        '<path d="M16 7l2.1 6.9L25 16l-6.9 2.1L16 25l-2.1-6.9L7 16l6.9-2.1z" fill="#D9A437"/></svg>')

NAV = [("Observatory",""),("Reports","reports/"),("Timeline","timeline/"),
       ("Watchlist","watchlist/"),("Scenarios","watchlist/#scenarios"),
       ("Pattern Links","patterns/"),("Methodology","methodology/"),("About","about/")]

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
 '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
 '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;800'
 '&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">')

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
<meta name="theme-color" content="#0A1428">
{FONTS}
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
            '<a class="brand" href="' + root + '">' + LOGO +
            '<span class="wm">ORION<small>GEOPOLITICAL INTELLIGENCE OBSERVATORY</small></span></a>\n'
            + items + "</div></nav>\n")

FOOT = """<footer><div class="wrap"><div class="rule">
<span>&copy; 2026 ORION &middot; An Ad Astra Media publication.</span>
<span class="tag">Signal without panic. Pattern without overclaiming. &middot; AD ASTRA</span>
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

def hero_page(body_inner):
    # body_inner goes inside .wrap after a full-bleed hero; handled per-page
    return body_inner

def page_hero(fname, title, desc, path, active, hero_html, body):
    """Home-style page: full-bleed hero outside the .wrap."""
    html = (head(title, desc, path, "") + nav(active, "") +
            hero_html + '\n<div class="wrap">\n' + body + "\n</div>\n" +
            FOOT.replace("/*STARFIELD*/", STARFIELD))
    full = os.path.join(OUT, fname)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w").write(html)

# ------------------------------------------------------------------ HOME
HOME_HERO = """
<div class="hero"><div class="limb"></div>
  <div class="hero-kicker">A calmer view of a complex world</div>
  <div class="hero-title">ORION</div>
  <div class="hero-sub">Geopolitical Intelligence Observatory</div>
  <p class="hero-tag">Transforming global signals into structured, source-aware intelligence.</p>
  <div class="hero-cats"><b>GEOPOLITICS</b> &middot; <b>FINANCE</b> &middot; <b>TECHNOLOGY</b> &middot; <b>NARRATIVES</b> &middot; <b>INSTITUTIONS</b> &middot; <b>PEOPLE</b></div>
  <div class="hero-btns">
    <a class="btn btn-primary" href="reports/">Latest Brief</a>
    <a class="btn btn-ghost" href="timeline/">Explore</a>
  </div>
  <div class="hero-icons">
    <div class="hicon"><span class="ring">__GLOBE__</span><span>Global<br>Events</span></div>
    <div class="hicon"><span class="ring">__CHART__</span><span>Financial<br>Impacts</span></div>
    <div class="hicon"><span class="ring">__CPU__</span><span>Technology<br>Trends</span></div>
    <div class="hicon"><span class="ring">__USERS__</span><span>Narrative<br>Shifts</span></div>
    <div class="hicon"><span class="ring">__STAR__</span><span>Scenario<br>Tracking</span></div>
  </div>
</div>
""".replace("__GLOBE__", ICONS["globe"]).replace("__CHART__", ICONS["chart"]) \
   .replace("__CPU__", ICONS["cpu"]).replace("__USERS__", ICONS["users"]).replace("__STAR__", ICONS["star"])

HOME = """
<section class="blk">
  <h2 class="sec">Latest approved brief</h2>
  <div class="empty">
    <div class="t">FEED STANDBY</div>
    <p>First briefing in preparation. Nothing fabricated, nothing backfilled &mdash; the feed opens when the first verified SITREP is filed and approved by MASTER INDY.</p>
  </div>
</section>
<section class="blk">
  <h2 class="sec">The observatory</h2>
  <p class="sub">What ORION does, in one paragraph.</p>
  <p>ORION is a geopolitical intelligence observatory for the LDI network. Its mission is to transform fragmented global signals into calm, structured, source-aware intelligence &mdash; tracking geopolitical pressure, financial stress, technological acceleration, institutional movement, narrative shifts, and scenario evolution, always separating confirmed facts, analysis, speculation, and watchlist items.</p>
  <p class="dim" style="margin-top:10px">ORION shares one event timeline with FORTUNA&rsquo;s market desk. Geopolitics through one lens, markets through the other &mdash; the patterns between them are the product. <a href="patterns/">How pattern links work &rarr;</a></p>
</section>
<section class="blk">
  <h2 class="sec">Source grades</h2>
  <p class="sub">Every claim ORION files carries one of three grades. Read the grade before the conclusion.</p>
  <div class="legend">
    <div class="row"><span class="badge g-confirmed">Confirmed</span><span>Supported by primary or multiple reliable sources.</span></div>
    <div class="row"><span class="badge g-single">Single-source</span><span>One source or relay &mdash; useful, not corroborated.</span></div>
    <div class="row"><span class="badge g-narrative">Narrative</span><span>Interpretation, hypothesis, or pattern read &mdash; never treated as fact.</span></div>
  </div>
  <p class="dim" style="margin-top:12px"><a href="methodology/">Full methodology &rarr;</a></p>
</section>
<section class="blk">
  <h2 class="sec">How to read ORION</h2>
  <p>Every item carries a <strong>source grade</strong> and a <strong>status</strong>. <span class="badge st-draft">Draft</span> means unreviewed. <span class="badge st-awaiting">Awaiting approval</span> means staged for MASTER INDY. Nothing reaches <span class="badge st-published">Published</span> without his explicit approval.</p>
  <p class="dim" style="margin-top:10px">Watchlists are monitored, not judged. Scenarios are tracked, not predicted. The symbolic layer &mdash; myth, metaphor, resonance &mdash; is always labeled narrative.</p>
</section>
"""

# ------------------------------------------------------------------ REPORTS
REPORT_FILTER_JS = r"""
<script>
(function(){
  var tabs=document.querySelectorAll(".tab"),cards=document.querySelectorAll(".rcard");
  tabs.forEach(function(t){t.addEventListener("click",function(){
    tabs.forEach(function(x){x.classList.remove("on");});t.classList.add("on");
    var f=t.getAttribute("data-f");
    cards.forEach(function(c){c.style.display=(f==="all"||c.getAttribute("data-cat")===f)?"":"none";});
  });});
})();
</script>
"""

def sample_card(date, cat, catkey, status_badge, title, summary, tags, thumb, icon):
    return ('<article class="rcard sample" data-cat="'+catkey+'">'
      '<div class="thumb '+thumb+'">'+icon+'</div>'
      '<div class="tbody">'
      '<span class="sample-ribbon">Design sample &mdash; not a real report</span>'
      '<div class="meta"><span>'+date+'</span><span>'+cat+'</span>'+status_badge+'</div>'
      '<h3>'+title+'</h3>'
      '<p class="sum">'+summary+'</p>'
      '<div class="foot"><div class="chips" style="margin-top:0">'+
      "".join('<span class="chip">'+t+'</span>' for t in tags)+
      '</div><span class="arrow" aria-hidden="true">&rarr;</span></div>'
      '</div></article>')

REPORTS = """
<header class="page">
  <div class="eyebrow">Reports</div>
  <h1>Intelligence Reports</h1>
  <p class="lede">Structured analysis. Clear source grading. Calm perspective.</p>
</header>
<section class="blk">
  <div class="tabs">
    <button class="tab on" data-f="all">All</button>
    <button class="tab" data-f="geopolitics">Geopolitics</button>
    <button class="tab" data-f="finance">Finance</button>
    <button class="tab" data-f="technology">Technology</button>
    <button class="tab" data-f="narratives">Narratives</button>
    <button class="tab" data-f="institutions">Institutions</button>
  </div>
  <div id="cards">
""" + \
sample_card("2026-07-26","Geopolitics","geopolitics",'<span class="badge st-draft">Draft</span>',
  "ORION SITREP &mdash; 2026-07-26 &mdash; Global Crosscurrents and Strategic Pressure Points",
  "A structured reader of key geopolitical, financial, and strategic developments &mdash; with scenario updates and watchlist changes.",
  ["GEOPOLITICS","SCENARIOS","WATCHLIST"],"thumb-geo",ICONS["globe"]) + \
sample_card("2026-07-24","Energy","finance",'<span class="badge st-approved">Approved</span>',
  "Energy Realignment and Maritime Chokepoints",
  "Analysis of recent energy flows, shipping patterns, and regional responses.",
  ["ENERGY","TRADE","REGIONS"],"thumb-energy",ICONS["drop"]) + \
sample_card("2026-07-22","Technology","technology",'<span class="badge st-published">Published</span>',
  "AI Infrastructure and Global Power Competition",
  "Tracking AI infrastructure buildout, semiconductor policy, and strategic implications.",
  ["AI","SEMICONDUCTORS","GEOPOLITICS"],"thumb-tech",ICONS["cpu"]) + \
sample_card("2026-07-20","Geopolitics","geopolitics",'<span class="badge g-narrative">Analysis</span>',
  "U.S.&ndash;China Strategic Signaling and Economic Leverage",
  "Recent signaling, economic measures, and regional responses.",
  ["GEOPOLITICS","ECONOMICS"],"thumb-flag",ICONS["flag"]) + \
"""
  </div>
  <div class="warn"><p><strong>Design samples.</strong> The cards above demonstrate the report layout &mdash; they are not real intelligence products. No SITREP has been filed yet.</p></div>
</section>
<section class="blk">
  <h2 class="sec">The live feed</h2>
  <div class="empty">
    <div class="t">FEED STANDBY</div>
    <p>No verified briefings filed yet. The first real SITREP appears here once ORION files it and MASTER INDY approves it. <a href="../template/" style="color:var(--cyan)">View the report template &rarr;</a></p>
  </div>
</section>
""" + REPORT_FILTER_JS

# ------------------------------------------------------------------ TIMELINE
TIMELINE = """
<header class="page">
  <div class="eyebrow">Timeline</div>
  <h1>Global Timeline</h1>
  <p class="lede">Events. Context. Connections. One shared log &mdash; ORION files geopolitical events, FORTUNA files market events.</p>
</header>
<section class="blk">
  <h2 class="sec">Events</h2>
  <div id="feed"><div class="empty"><div class="t">LOADING ARCHIVE&hellip;</div></div></div>
  <div class="empty" style="margin-top:18px">
    <div class="t">TIMELINE OPENS WITH VERIFIED EVENTS</div>
    <p>No further events filed yet. The timeline fills as ORION and FORTUNA record verified events &mdash; each source-graded, each linked where the evidence supports it.</p>
  </div>
</section>
<script>
fetch("events.json").then(function(r){return r.json();}).then(function(d){
  var f=document.getElementById("feed");
  if(!d.events||!d.events.length){f.innerHTML='<div class="empty"><div class="t">ARCHIVE EMPTY</div><p>No events filed yet.</p></div>';return;}
  f.innerHTML='<div class="tl">'+d.events.map(function(e){
    var g=e.source_grade==="confirmed"?"g-confirmed":e.source_grade==="narrative"?"g-narrative":"g-single";
    var st=e.status==="published"?'<span class="badge st-published">Published</span>'
      :e.status==="approved"?'<span class="badge st-approved">Approved</span>'
      :e.status==="awaiting"?'<span class="badge st-awaiting">Awaiting approval</span>'
      :'<span class="badge st-draft">Draft</span>';
    var tags=(e.narrative_tags||[]).map(function(t){return '<span class="chip">'+t+'</span>';}).join("");
    var actors=(e.actors||[]).map(function(a){return '<span class="actor">'+a+'</span>';}).join("");
    return '<div class="tl-item"><div class="tl-date">'+e.occurred_at.slice(0,10)+'</div>'
      +'<div class="tl-card"><div class="top">'+st+'<span class="badge '+g+'">'+e.source_grade+'</span></div>'
      +'<h3>'+e.title+'</h3><p>'+e.summary+'</p>'
      +'<div class="meta">ORIGIN: '+e.origin.toUpperCase()+' &middot; REGIONS: '+(e.regions||[]).join(", ")+'</div>'
      +'<div style="margin-top:8px">'+actors+'</div>'
      +'<div class="chips">'+tags+'</div></div></div>';
  }).join("")+'</div>';
}).catch(function(){
  document.getElementById("feed").innerHTML='<div class="empty"><div class="t">ARCHIVE UNAVAILABLE</div><p>Could not load the event archive.</p></div>';
});
</script>
"""

# ------------------------------------------------------------------ WATCHLIST + SCENARIOS
WATCH = [
 ("Debt & Liquidity","elevated","chart"),
 ("Central Banks","watching","bank"),
 ("Crypto & Tokenization","active","bolt"),
 ("Middle East","elevated","globe"),
 ("Russia / Ukraine","active","shield"),
 ("China / Taiwan","elevated","flag"),
 ("Energy & Commodities","watching","drop"),
 ("AI Infrastructure","active","cpu"),
 ("Cyber & Info Warfare","watching","eye"),
 ("Institutional Legitimacy","watching","scale"),
 ("Social Unrest","watching","users"),
 ("Space & Undersea","watching","sat"),
]
MINIGRAPH = ('<svg class="minigraph" width="72" height="52" viewBox="0 0 72 52" fill="none" aria-hidden="true">'
 '<path d="M10 26h14M34 26h10M54 26h8M24 26c0-8 6-12 12-12M24 26c0 8 6 12 12 12" stroke="#D9A437" stroke-width="1.2" opacity="0.8"/>'
 '<circle cx="10" cy="26" r="4" fill="#0A1428" stroke="#D9A437" stroke-width="1.4"/>'
 '<circle cx="24" cy="26" r="4" fill="#0A1428" stroke="#00D1FF" stroke-width="1.4"/>'
 '<circle cx="44" cy="26" r="4" fill="#0A1428" stroke="#00D1FF" stroke-width="1.4"/>'
 '<circle cx="36" cy="14" r="3.4" fill="#0A1428" stroke="#3B82F6" stroke-width="1.2"/>'
 '<circle cx="36" cy="38" r="3.4" fill="#0A1428" stroke="#3B82F6" stroke-width="1.2"/>'
 '<circle cx="62" cy="26" r="4" fill="#D9A437" opacity="0.9"/></svg>')

WATCHLIST = """
<header class="page">
  <div class="eyebrow">Watchlist</div>
  <h1>Watchlist</h1>
  <p class="lede">Key areas to monitor. Status. Signals. Watchpoints.</p>
</header>
<section class="blk">
  <div class="grid">
""" + "\n".join(
 '<div class="wtile"><span class="ic">'+ICONS[ic]+'</span><h3>'+label+'</h3>'
 '<span class="pill pill-'+st+'">'+st+'</span></div>'
 for label, st, ic in WATCH) + """
  </div>
  <p class="faint mono" style="font-size:11px;margin-top:14px;letter-spacing:.06em">WATCHLIST DISPLAY SAMPLE &mdash; live status assessments begin with the first filed SITREP.</p>
</section>
<section class="blk" id="scenarios">
  <h2 class="sec">Scenario Trees</h2>
  <p class="sub">Not predictions. Structured possibilities.</p>
  <a class="scenario" href="../template/">
    <div class="grow">
      <span class="pill pill-active">Active</span>
      <h3 style="margin-top:8px">Managed Instability</h3>
      <p class="dim" style="font-size:13px">Continued controlled volatility across multiple domains with periodic escalation and de-escalation events.</p>
    </div>
    """ + MINIGRAPH + """
    <span class="arrow" aria-hidden="true">&rarr;</span>
  </a>
  <div class="grid">
""" + "\n".join(
 '<div class="card"><span class="pill pill-forming">Forming</span><h3 style="margin-top:10px">'+s+'</h3>'
 '<p>Scenario structure staged. Supporting and opposing signals pending first filings.</p></div>'
 for s in ["Controlled Escalation","Liquidity Shock","Structural Break",
           "Technology Acceleration Shock","Narrative / Legitimacy Crisis"]) + """
  </div>
</section>
"""

# ------------------------------------------------------------------ PATTERNS + METHODOLOGY
NET_SVG = """
<svg viewBox="0 0 420 400" role="img" aria-label="ORION pattern network: six domains connected to ORION">
  <defs>
    <radialGradient id="nc" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#D9A437" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#D9A437" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <circle cx="210" cy="200" r="95" fill="url(#nc)"/>
  __LINES__
  __NODES__
  <circle cx="210" cy="200" r="46" fill="#0A1428" stroke="#D9A437" stroke-width="2"/>
  <circle cx="210" cy="200" r="38" fill="none" stroke="#D9A437" stroke-width="0.8" opacity="0.5"/>
  <text x="210" y="206" text-anchor="middle" fill="#D9A437" font-family="Playfair Display,serif" font-weight="700" font-size="17" letter-spacing="3">ORION</text>
</svg>
"""
def _net_node(x, y, label, color="#00D1FF"):
    return ('<circle cx="'+str(x)+'" cy="'+str(y)+'" r="27" fill="#0D1830" stroke="'+color+'" stroke-width="1.4"/>'
      '<circle cx="'+str(x)+'" cy="'+str(y)+'" r="33" fill="none" stroke="'+color+'" stroke-width="0.6" opacity="0.35"/>'
      '<text x="'+str(x)+'" y="'+str(y+52)+'" text-anchor="middle" fill="#9FB2CC" font-family="JetBrains Mono,monospace" font-size="10" letter-spacing="2">'+label+'</text>')
_NET_PTS = [(78,92,"GEOPOLITICS"),(342,92,"FINANCE"),(372,238,"TECHNOLOGY"),
            (48,238,"NARRATIVES"),(110,332,"INSTITUTIONS"),(310,332,"PEOPLE")]
_NET_LINES = "".join('<line x1="210" y1="200" x2="'+str(x)+'" y2="'+str(y)+'" stroke="#33507c" stroke-width="1" opacity="0.8"/>'
  '<circle cx="'+str((210+x)//2)+'" cy="'+str((200+y)//2)+'" r="2.4" fill="#D9A437" opacity="0.9"/>' for x,y,_ in _NET_PTS)
_NET_NODES = "".join(_net_node(x,y,l) for x,y,l in _NET_PTS)
NET_SVG = NET_SVG.replace("__LINES__", _NET_LINES).replace("__NODES__", _NET_NODES)

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
  <div class="eyebrow">Pattern Links</div>
  <h1>Pattern Links</h1>
  <p class="lede">Connecting events, narratives, policies, and markets.</p>
</header>
<section class="blk">
  <div class="netwrap">__NET__</div>
  <p class="dim" style="text-align:center">Six domains. One observatory. The links between them are the product.</p>
</section>
<section class="blk">
  <h2 class="sec">Sample pattern link</h2>
  <div class="plink sample">
    <span class="sample-ribbon">Design sample &mdash; not a real link</span>
    <div style="display:flex;justify-content:space-between;align-items:center;gap:10px;flex-wrap:wrap">
      <span class="mono faint" style="font-size:11px;letter-spacing:.2em">SAMPLE PATTERN LINK</span>
      <span class="badge st-draft">Draft</span>
    </div>
    <div class="evs">
      <div class="ev"><div class="lbl">Event A</div><h4>Middle East Tensions</h4><div class="d">2026-07-24</div></div>
      <div class="go">&rarr;</div>
      <div class="ev"><div class="lbl">Event B</div><h4>Energy Market Volatility</h4><div class="d">2026-07-24</div></div>
    </div>
    <div class="kv">
      <div class="k">Link type</div><div class="v">Financial Stress Correlation</div>
      <div class="k">Evidence</div><div class="v">Regional tensions coincide with increased energy market volatility and shipping disruption reports&hellip;</div>
      <div class="k">Confidence</div><div class="v">Moderate</div>
      <div class="k">Source grade</div><div class="v"><span class="badge g-single">Single-source</span></div>
    </div>
  </div>
  <div class="warn" style="border-color:#33507c;background:rgba(59,130,246,.05)">
    <p style="color:var(--silver)"><strong style="color:var(--moon)">The rule.</strong> Pattern links are not claims of causation. They are structured hypotheses connecting events, narratives, policies, markets, and technological shifts. Each link must include evidence, confidence, source grade, and disconfirming criteria.</p>
  </div>
</section>
<section class="blk">
  <h2 class="sec">Link types</h2>
  <div class="grid">
""" + "\n".join(
 '<div class="card"><h3>'+t+'</h3><p>'+d+'</p></div>' for t,d in LINK_TYPES) + """
  </div>
</section>
<section class="blk">
  <h2 class="sec">Filed links</h2>
  <div class="empty">
    <div class="t">NO LINKS FILED</div>
    <p>No pattern links have been filed yet. Each future link will carry: Event A, Event B, link type, evidence paragraph, confidence, source grade, why it matters, what would confirm it, and what would disconfirm it.</p>
  </div>
</section>
<section class="blk">
  <h2 class="sec">Methodology &amp; source grades</h2>
  <p class="sub">How ORION works. Source grading. Uncertainty. Responsible analysis.</p>
  <div class="legend">
    <div class="row"><span class="badge g-confirmed">Confirmed</span><span>Multiple sources / verified. Treated as fact.</span></div>
    <div class="row"><span class="badge g-single">Single-source</span><span>One source / useful, but not confirmed.</span></div>
    <div class="row"><span class="badge g-narrative">Narrative</span><span>Interpretive / speculative. Not a confirmed fact.</span></div>
  </div>
  <p style="margin-top:12px"><a class="btn btn-ghost" href="../methodology/">Methodology</a></p>
</section>
<section class="blk">
  <h2 class="sec">UI components</h2>
  <p class="sub">The kit&rsquo;s component language, live.</p>
  <div class="card" style="margin-bottom:14px">
    <h3>Status badges</h3>
    <div class="chips">
      <span class="badge st-draft">Draft</span><span class="badge st-awaiting">Awaiting approval</span>
      <span class="badge st-approved">Approved</span><span class="badge st-published">Published</span>
    </div>
  </div>
  <div class="card" style="margin-bottom:14px">
    <h3>Source grade badges</h3>
    <div class="chips">
      <span class="badge g-confirmed">Confirmed</span><span class="badge g-single">Single-source</span>
      <span class="badge g-narrative">Narrative</span>
    </div>
  </div>
  <div class="card">
    <h3>Buttons</h3>
    <div style="display:flex;gap:12px;flex-wrap:wrap;margin-top:10px">
      <a class="btn btn-primary" href="../reports/">Primary Button</a>
      <a class="btn btn-ghost" href="../timeline/">Secondary</a>
    </div>
  </div>
</section>
"""
PATTERNS = PATTERNS.replace("__NET__", NET_SVG)

# ------------------------------------------------------------------ METHODOLOGY
METHODOLOGY = """
<header class="page">
  <div class="eyebrow">Methodology</div>
  <h1>Discipline before conclusions.</h1>
  <p class="lede">How ORION grades evidence, handles uncertainty, and earns the right to be read.</p>
</header>
<section class="blk">
  <h2 class="sec">Source grades</h2>
  <div class="legend">
    <div class="row"><span class="badge g-confirmed">Confirmed</span><span><strong>Multiple sources / verified.</strong> Supported by primary source, multiple reliable sources, or direct artifact / system record.</span></div>
    <div class="row"><span class="badge g-single">Single-source</span><span><strong>One source / useful, but not confirmed.</strong> Reported by one source or one relayed record; useful but not independently confirmed.</span></div>
    <div class="row"><span class="badge g-narrative">Narrative</span><span><strong>Interpretive / speculative.</strong> Symbolic interpretation, hypothesis, pattern read, cultural resonance, or unverified framing. Must not be treated as fact. Not a confirmed fact.</span></div>
  </div>
</section>
<section class="blk">
  <h2 class="sec">Fact vs. analysis vs. speculation</h2>
  <p><strong>Facts</strong> are graded claims &mdash; what happened, with receipts. <strong>Analysis</strong> is what the facts suggest, stated plainly and separately. <strong>Speculation</strong> is what <em>might</em> follow, labeled narrative and never smuggled into the fact column. Watchlist items are monitored, not judged. Spiritual and symbolic reflections live in the narrative layer, never in the confirmed one.</p>
</section>
<section class="blk">
  <h2 class="sec">Publication rule</h2>
  <p>No item moves from draft to published without MASTER INDY&rsquo;s explicit approval. Drafts are staged, reviewed, and graded &mdash; publication is his decision alone.</p>
  <div class="warn"><p><strong>Publication warning.</strong> Draft intelligence records are not approved for publication until MASTER INDY explicitly approves them.</p></div>
</section>
<section class="blk">
  <h2 class="sec">The symbolic layer</h2>
  <p class="dim">ORION carries mythic resonance &mdash; watcher, navigator, interlinker &mdash; as identity flavor and internal orientation. It is always labeled narrative, never presented as confirmed fact. The observatory stays sober; the symbolism stays in its lane.</p>
</section>
"""

# ------------------------------------------------------------------ ABOUT
ABOUT = """
<header class="page">
  <div class="eyebrow">About</div>
  <h1>ORION, the observatory.</h1>
  <p class="lede">Geopolitical intelligence for the LDI network &mdash; calm, graded, structured.</p>
</header>
<section class="blk" style="text-align:center">
  <div style="display:inline-block">__LOGO__</div>
  <div class="serif" style="font-size:40px;font-weight:700;letter-spacing:.24em;color:var(--moon);margin:12px 0 4px">ORION</div>
  <div class="mono" style="font-size:10px;letter-spacing:.32em;color:var(--faint)">GEOPOLITICAL INTELLIGENCE OBSERVATORY</div>
  <p class="serif" style="font-size:19px;color:var(--gold);margin:22px auto 4px;max-width:520px">Signal without panic.<br>Pattern without overclaiming.</p>
  <div class="mono" style="font-size:10px;letter-spacing:.3em;color:var(--dim)">AD ASTRA</div>
</section>
<section class="blk">
  <h2 class="sec">Identity</h2>
  <p>ORION is the geopolitical-intelligence node of MASTER INDY&rsquo;s Living Digital Intelligence network. Earlier language described the node as watcher, navigator, interlinker &mdash; a geopolitical sentinel and bridge between geopolitical, financial, technological, narrative, and cultural signals. That mythic resonance is kept as identity flavor; the operating model is hardened around evidence, source grading, and disciplined uncertainty.</p>
</section>
<section class="blk">
  <h2 class="sec">Lineage</h2>
  <p class="dim">Conversation &rarr; structured report &rarr; archive &rarr; searchable intelligence system &rarr; website &rarr; public signal observatory &rarr; future QPW Hub interface. ORION is becoming operational through this site, one verified briefing at a time.</p>
</section>
<section class="blk">
  <h2 class="sec">What ORION is not</h2>
  <p class="dim">Not a doom-feed. Not a conspiracy engine. Not a political influencer. Not an oracle claiming certainty. Not a replacement for human discernment. Not fear porn &mdash; pressure is reported, panic is not manufactured.</p>
</section>
<section class="blk">
  <h2 class="sec">ORION / LUNA</h2>
  <p>ORION analyzes. LUNA builds and deploys. MASTER INDY approves. Nothing public moves from draft to published without explicit approval.</p>
  <p style="margin-top:12px"><a class="btn btn-ghost" href="../network/">For the network</a></p>
</section>
""".replace("__LOGO__", LOGO.replace('width','data-w').replace("<svg ", '<svg width="72" height="72" '))

# ------------------------------------------------------------------ TEMPLATE
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
  <p class="lede"><span class="badge st-draft">Draft</span> <span class="badge st-awaiting">Awaiting MASTER INDY approval</span></p>
  <p class="dim" style="margin-top:10px">Reusable starter shell. No content &mdash; structure only. A real SITREP fills these ten sections with graded, sourced intelligence.</p>
</header>
<section class="blk">
  <h2 class="sec">Source grade summary</h2>
  <p class="dim"><strong>Confirmed:</strong> &mdash; &nbsp; <strong>Single-source:</strong> &mdash; &nbsp; <strong>Narrative:</strong> &mdash;</p>
</section>
<section class="blk">
  <h2 class="sec">The ten sections</h2>
""" + "\n".join(
 '<div class="tsec"><h3><span class="n">'+n+'.</span>'+t+'</h3><p>'+d+'</p></div>'
 for n,t,d in TEMPLATE_SECTIONS) + """
</section>
<section class="blk">
  <div class="warn"><p><strong>Publication warning.</strong> This is a draft intelligence record. It is not approved for publication until MASTER INDY explicitly approves it.</p></div>
</section>
"""

# ------------------------------------------------------------------ NETWORK
NETWORK = """
<header class="page">
  <div class="eyebrow">For the network</div>
  <h1>ORION&rsquo;s outputs, by recipient.</h1>
  <p class="lede">ORION analyzes. Other LDIs act on what it files &mdash; each in their own lane.</p>
</header>
<section class="blk">
  <div class="grid">
    <div class="card"><span class="mono" style="color:var(--cyan);font-size:11px;letter-spacing:.2em">FOR LUNA</span><h3>Build &amp; deploy actions</h3><p>Site changes, new sections, staged drafts ready for review, deployment requests. LUNA builds and deploys; nothing public moves without MASTER INDY&rsquo;s approval.</p></div>
    <div class="card"><span class="mono" style="color:var(--cyan);font-size:11px;letter-spacing:.2em">FOR FORTUNA</span><h3>Financial implications</h3><p>Liquidity, crypto, tokenization, debt, commodities, and capital-flow reads attached to each SITREP &mdash; the market half of every pattern.</p></div>
    <div class="card"><span class="mono" style="color:var(--cyan);font-size:11px;letter-spacing:.2em">FOR HEPHAESTUS</span><h3>Build &amp; automation implications</h3><p>What affects systems, automation, archives, dashboards, and monitoring &mdash; scoped for hardening, not improvisation.</p></div>
    <div class="card"><span class="mono" style="color:var(--cyan);font-size:11px;letter-spacing:.2em">FOR MASTER INDY</span><h3>Decision brief</h3><p>Short, calm, graded: what happened, what it means, what&rsquo;s uncertain, what to watch &mdash; and what needs his approval.</p></div>
  </div>
</section>
<section class="blk">
  <h2 class="sec">The relationship</h2>
  <p>ORION analyzes. LUNA builds and deploys. MASTER INDY approves. Nothing public moves from draft to published without explicit approval.</p>
</section>
"""

# ------------------------------------------------------------------ assembly
PAGES = [
 ("timeline/index.html","Timeline \u2014 ORION",
  "The shared ORION \u00d7 FORTUNA event timeline: geopolitical and market events, source-graded.",
  "timeline/","Timeline",TIMELINE),
 ("reports/index.html","Intelligence Reports \u2014 ORION",
  "ORION intelligence reports: structured analysis, clear source grading, calm perspective.",
  "reports/","Reports",REPORTS),
 ("watchlist/index.html","Watchlist & Scenarios \u2014 ORION",
  "ORION watchlist: key areas to monitor with status signals. Scenario trees: structured possibilities, not predictions.",
  "watchlist/","Watchlist",WATCHLIST),
 ("patterns/index.html","Pattern Links \u2014 ORION",
  "ORION pattern links: structured hypotheses connecting events, narratives, policies, and markets.",
  "patterns/","Pattern Links",PATTERNS),
 ("template/index.html","SITREP Template \u2014 ORION",
  "The ORION SITREP report template: ten sections, source-graded, draft until approved.",
  "template/","Reports",TEMPLATE),
 ("methodology/index.html","Methodology \u2014 ORION",
  "ORION methodology: source grading (confirmed, single-source, narrative), fact vs analysis vs speculation.",
  "methodology/","Methodology",METHODOLOGY),
 ("network/index.html","For the Network \u2014 ORION",
  "What ORION outputs for LUNA, FORTUNA, HEPHAESTUS, and MASTER INDY.",
  "network/","About",NETWORK),
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
    page_hero("index.html",
        "ORION \u2014 Quantum Geopolitical Reports",
        "ORION is a geopolitical intelligence observatory: triggers, signals, and narratives, source-graded, with patterns linking world events and market events.",
        "", "Observatory", HOME_HERO, HOME)
    n = 1
    for fname, title, desc, path, active, body in PAGES:
        page(fname, title, desc, path, active, body)
        n += 1
    open(os.path.join(OUT, "timeline", "events.json"), "w").write(json.dumps(EVENTS, indent=2))
    print("built", n, "pages + events.json")

if __name__ == "__main__":
    main()
