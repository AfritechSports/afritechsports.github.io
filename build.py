#!/usr/bin/env python3
"""Builds afritechsports.github.io: home, three pillar pages, privacy, redirects, shared assets."""
import os, json, secrets, string, shutil, html
from content import *

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "out")
SITE = "https://afritechsports.github.io/"
FONTS = open(os.path.join(ROOT, "fonts.css")).read()
EMAIL = "Advisory@afritechsports.com"
WA = "254715551506"
LI_CO = "https://www.linkedin.com/company/afritech-sports-technology-and-innovation-group-limited/"
LI_AR = "https://www.linkedin.com/in/andrew-r-b1b514"
LANGS = [("en", "English"), ("fr", "Français"), ("sw", "Kiswahili"), ("pt", "Português")]
SHEET_URL = "https://script.google.com/macros/s/AKfycbzneuWkn_1svVc7ty1YP54MT1Z-1tH3ouJGSQBXDKk32prFDXdqNXM5V_5iuCO_MfYHog/exec"
GOAT = "https://afritechsports.goatcounter.com/count"
E = html.escape

def ref():
    return "AFTS" + "".join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(8))

def write(path, s, mode="w"):
    p = os.path.join(OUT, path); os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, mode).write(s)

# ---------------------------------------------------------------- CSS
CSS = FONTS + """
:root{--navy:#1A365D;--navy2:#0F2442;--teal:#0D9488;--teal2:#14B8A6;--cta:#E8701A;--wa:#1F8F4E;--ink:#1A365D;--text:#24324a;--muted:#55627a;--bg:#F4F7FA;--card:#fff;--line:#D6DEE8;--tint:#E7F5F3}
@media (prefers-color-scheme:dark){:root{--ink:#E6EEF7;--text:#D5DEEA;--muted:#A3B1C4;--bg:#0E1726;--card:#16223A;--line:#2A3A55;--tint:#123A3A}}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%;scroll-padding-top:120px}
body{margin:0;background:var(--bg);color:var(--text);font:17px/1.55 "Source Sans 3",-apple-system,sans-serif}
a{color:var(--teal)}img{max-width:100%;display:block}
.lr{position:absolute;opacity:0;pointer-events:none}
.top{background:var(--navy2);color:#fff;position:sticky;top:0;z-index:20;padding-top:env(safe-area-inset-top)}
.top-in{max-width:1080px;margin:0 auto;padding:8px 16px;display:flex;align-items:center;gap:10px;flex-wrap:wrap}
.brand{display:flex;align-items:center;gap:10px;color:#fff;text-decoration:none;flex:1;min-width:200px}
.brand img{width:40px;height:40px;border-radius:9px;background:#fff;padding:3px}
.brand b{font:700 22px/1 "Barlow Condensed",sans-serif;letter-spacing:.3px}
.brand small{display:block;font:700 11px/1.4 "Barlow Condensed",sans-serif;letter-spacing:1.3px;opacity:.75;text-transform:uppercase}
.langs{display:flex;gap:6px}
.langs label{border:1px solid rgba(255,255,255,.35);color:#fff;border-radius:999px;padding:5px 12px;font-weight:600;font-size:14px;cursor:pointer;min-height:36px;display:inline-flex;align-items:center}
#l-en:checked~.top label[for=l-en],#l-fr:checked~.top label[for=l-fr],#l-sw:checked~.top label[for=l-sw],#l-pt:checked~.top label[for=l-pt]{background:var(--teal);border-color:var(--teal)}
.lr:focus-visible~.top .langs{outline:2px solid var(--teal2);outline-offset:3px;border-radius:8px}
.nav{background:var(--navy)}
.nav-in{max-width:1080px;margin:0 auto;padding:0 10px}
.nl{display:none;align-items:center}
.nm{display:flex;align-items:center;justify-content:space-between}
@media (min-width:900px){.nl{display:flex}.nm{display:none}}
.nav a,.nav summary,.nav .nt{color:#E6EEF7;text-decoration:none;font:700 15px/1 "Barlow Condensed",sans-serif;letter-spacing:.3px;text-transform:uppercase;padding:14px 9px;border-bottom:3px solid transparent;cursor:pointer;background:none;border-top:0;border-left:0;border-right:0;min-height:46px;display:inline-flex;align-items:center}
.nav a.on,.nav a:hover,.nav summary:hover{border-bottom-color:var(--teal2);color:#fff}
.nav summary{list-style:none}.nav summary::-webkit-details-marker{display:none}
.nl summary:after{content:" ▾";white-space:pre}
.nav .nt{margin-left:auto;background:var(--wa);color:#fff;border-radius:10px;border-bottom:0;padding:10px 14px;min-height:38px;margin-top:4px;margin-bottom:4px}
.dd{position:relative}
.ddl{position:absolute;top:100%;left:0;min-width:230px;background:var(--navy2);border-radius:0 0 12px 12px;padding:6px 0;box-shadow:0 12px 28px rgba(0,0,0,.3);z-index:30;display:flex;flex-direction:column}
.mm .ddl{left:auto;right:0;min-width:260px}
.ddl a,.ddl .nt{padding:12px 16px;border-bottom:0;width:100%}
.ddl a:hover{background:var(--navy)}
.ddl .nt{margin:8px 12px 6px;width:auto;justify-content:center}
.ds{color:var(--teal2);font:700 12px/1 "Barlow Condensed",sans-serif;letter-spacing:1.3px;text-transform:uppercase;padding:12px 16px 4px;border-top:1px solid rgba(255,255,255,.12);margin-top:6px}
.t{display:none}
#l-en:checked~* .t-en,#l-fr:checked~* .t-fr,#l-sw:checked~* .t-sw,#l-pt:checked~* .t-pt{display:inline}
#l-en:checked~* div.t-en,#l-fr:checked~* div.t-fr,#l-sw:checked~* div.t-sw,#l-pt:checked~* div.t-pt,#l-en:checked~* p.t-en,#l-fr:checked~* p.t-fr,#l-sw:checked~* p.t-sw,#l-pt:checked~* p.t-pt,#l-en:checked~* section.t-en,#l-fr:checked~* section.t-fr,#l-sw:checked~* section.t-sw,#l-pt:checked~* section.t-pt{display:block}
.hero{background:radial-gradient(120% 140% at 85% 0%,#1d4f7a 0%,var(--navy) 45%,var(--navy2) 100%);color:#fff;position:relative;overflow:hidden}
.hero:after{content:"";position:absolute;right:-120px;top:-120px;width:420px;height:420px;border:2px solid rgba(255,255,255,.08);border-radius:50%;box-shadow:0 0 0 70px rgba(255,255,255,.03)}
.hero-in{max-width:1080px;margin:0 auto;padding:30px 16px 34px;position:relative;z-index:1}
.eyebrow{font:700 14px/1 "Barlow Condensed",sans-serif;letter-spacing:2px;text-transform:uppercase;color:var(--teal2);margin:0 0 12px}
h1{font:700 38px/1.05 "Barlow Condensed",sans-serif;margin:0 0 14px;max-width:22ch}
@media (min-width:720px){h1{font-size:54px}}
.lead{margin:0;max-width:66ch;opacity:.95}
.acts{display:flex;flex-wrap:wrap;gap:10px;margin-top:20px}
.btn{display:inline-flex;align-items:center;gap:8px;min-height:48px;padding:12px 18px;border-radius:12px;font:700 17px/1.2 "Source Sans 3",sans-serif;text-decoration:none;border:0;cursor:pointer}
.btn.wa{background:var(--wa);color:#fff}.btn.wa:hover{filter:brightness(1.08)}
.btn.ghost{background:transparent;border:1.5px solid rgba(255,255,255,.6);color:#fff}
.wrap .btn.ghost,.modal .btn.ghost{border-color:var(--line);color:var(--ink)}
.btn.sm{min-height:40px;padding:8px 14px;font-size:15px}
.small{font-size:15px;opacity:.85;margin:12px 0 0}
.wrap{max-width:1080px;margin:0 auto;padding:8px 16px 24px}
h2{font:700 30px/1.15 "Barlow Condensed",sans-serif;color:var(--ink);margin:34px 0 14px}
h3{font:700 23px/1.2 "Barlow Condensed",sans-serif;color:var(--ink);margin:0 0 6px}
.cards{display:grid;gap:14px;grid-template-columns:1fr}
@media (min-width:680px){.cards{grid-template-columns:1fr 1fr}}
@media (min-width:980px){.cards.three{grid-template-columns:1fr 1fr 1fr}}
.card{display:flex;flex-direction:column;gap:6px;background:var(--card);border:1px solid var(--line);border-top:5px solid var(--teal);border-radius:14px;padding:18px;color:var(--text);text-decoration:none}
a.card:hover{border-color:var(--teal);box-shadow:0 0 0 3px rgba(13,148,136,.2)}
.tag{font:700 14px/1 "Barlow Condensed",sans-serif;letter-spacing:1.3px;text-transform:uppercase;color:var(--teal)}
.card .d{color:var(--muted);flex:1}
.card ul{margin:4px 0 0;padding-left:18px;color:var(--muted)}
.go{color:var(--cta);font-weight:700;margin-top:4px;text-decoration:none}
.row{display:flex;flex-wrap:wrap;gap:8px;margin-top:8px}
.news{display:grid;gap:12px}
.ni{display:block;background:var(--card);border:1px solid var(--line);border-left:6px solid var(--cta);border-radius:12px;padding:14px 16px;text-decoration:none;color:var(--text)}
.ni .m{font:700 13px/1 "Barlow Condensed",sans-serif;letter-spacing:1.2px;text-transform:uppercase;color:var(--teal);margin-bottom:6px}
.ni b{display:block;color:var(--ink);font-size:18px}
.proof{display:grid;gap:14px;grid-template-columns:1fr}
@media (min-width:680px){.proof{grid-template-columns:1fr 1fr}}
.pf{background:var(--tint);border-radius:14px;padding:16px 18px}
.pf b{display:block;font:700 21px/1.2 "Barlow Condensed",sans-serif;color:var(--ink);margin-bottom:4px}
.prod{display:grid;gap:0;background:var(--card);border:1px solid var(--line);border-radius:16px;overflow:hidden;margin-bottom:18px}
@media (min-width:820px){.prod{grid-template-columns:5fr 6fr}}
.prod img{width:100%;height:100%;max-height:460px;object-fit:cover;background:#fff;min-height:220px}
.prod .pb{padding:20px}
.prod dl{margin:10px 0 0}.prod dt{font:700 15px/1 "Barlow Condensed",sans-serif;letter-spacing:1px;text-transform:uppercase;color:var(--teal);margin-top:12px}.prod dd{margin:4px 0 0}
.steps{display:grid;gap:12px;grid-template-columns:1fr 1fr;counter-reset:s}
@media (min-width:820px){.steps{grid-template-columns:repeat(4,1fr)}}
.st{background:var(--tint);border-radius:14px;padding:14px 16px;counter-increment:s}
.st:before{content:counter(s);display:inline-grid;place-items:center;width:30px;height:30px;border-radius:50%;background:var(--teal);color:#fff;font-weight:700;margin-bottom:8px}
.st b{display:block;color:var(--ink);font-size:18px}
.sec{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:20px;margin-top:18px}
.sec.media{display:grid;gap:18px}
#final{border-top:6px solid var(--cta)}#final h3{font-size:32px!important}
@media (min-width:820px){.sec.media{grid-template-columns:2fr 3fr;align-items:start}}
.sec.media img{border-radius:12px;width:100%;max-height:520px;object-fit:cover;object-position:top;border:1px solid var(--line)}
.ev{display:grid;gap:12px;margin-top:14px}
@media (min-width:820px){.ev{grid-template-columns:repeat(3,1fr)}}
.evc{border:1px solid var(--line);border-radius:12px;padding:14px;background:var(--bg)}
.evc .m{font:700 13px/1.2 "Barlow Condensed",sans-serif;letter-spacing:1px;text-transform:uppercase;color:var(--muted)}
.evc .s{display:inline-block;font-size:13px;font-weight:700;border-radius:999px;padding:2px 10px;margin:6px 0}
.evc .s.past{background:var(--line);color:var(--ink)}.evc .s.next{background:var(--cta);color:#fff}
.eph{margin:16px 0 6px;font-size:17px}
.eps{list-style:none;margin:0;padding:0;display:grid;gap:6px}
.eps li{display:grid;grid-template-columns:4.2em minmax(0,1fr);gap:8px;align-items:baseline;border-top:1px solid var(--line);padding-top:6px}
.eps .ed{font-size:13px;color:var(--muted);font-weight:600}
.eps a{font-weight:600}
.pods{display:flex;flex-wrap:wrap;gap:8px;margin-top:10px}
.pods a{border:1px solid var(--line);background:var(--card);border-radius:999px;padding:8px 14px;text-decoration:none;font-weight:600;color:var(--ink)}
.band{background:var(--card);border:1px solid var(--line);border-left:6px solid var(--cta);border-radius:14px;padding:20px;margin-top:34px}
.band h2{margin-top:0}
.contact,.note{color:var(--muted);font-size:15px;margin-top:14px}
.foot{max-width:1080px;margin:0 auto;padding:18px 16px 30px;color:var(--muted);font-size:13px;text-align:center;border-top:1px solid var(--line)}
.back{display:inline-block;margin:18px 0 0;font-weight:600}
.modal{position:fixed;inset:0;background:rgba(10,20,35,.6);display:none;align-items:flex-end;justify-content:center;z-index:50}
.modal.open{display:flex}
@media (min-width:640px){.modal{align-items:center}}
.mbox{background:var(--card);color:var(--text);width:100%;max-width:520px;max-height:92vh;overflow:auto;border-radius:18px 18px 0 0;padding:20px 18px calc(18px + env(safe-area-inset-bottom))}
@media (min-width:640px){.mbox{border-radius:18px}}
.mbox h3{font-size:26px}
.f{display:block;margin-top:12px;font-weight:600;color:var(--ink);font-size:15px}
.f select,.f input[type=text]{display:block;width:100%;margin-top:5px;font:16px "Source Sans 3",sans-serif;padding:11px 12px;border:1px solid var(--line);border-radius:10px;background:var(--bg);color:var(--text)}
.ck{display:flex;gap:10px;align-items:flex-start;margin-top:14px;font-size:14px;color:var(--muted)}
.ck input{width:22px;height:22px;margin-top:2px;flex:none}
.err{color:#C0392B;font-size:14px;margin-top:10px;display:none}
.minor{background:var(--tint);border-radius:10px;padding:8px 12px;font-size:14px;margin-top:10px}
"""

# ---------------------------------------------------------------- JS
def js():
    picker = {"pick": {k: v for k, v in PICK.items()},
              "types": [[k, lab, t, lv] for k, lab, t, lv in TYPES],
              "teams": [[k, lab] for k, lab in TEAMS],
              "levels": [[k, lab] for k, lab in LEVELS],
              "news": NEWS, "wa": WA, "email": EMAIL, "sheet": SHEET_URL}
    return "window.AFTS=" + json.dumps(picker, ensure_ascii=False) + ";\n" + r"""
(function(){
var A=window.AFTS,ok={en:1,fr:1,sw:1,pt:1};
function lang(){var c=document.querySelector('.lr:checked');return c?c.id.slice(2):'en'}
function T(o){return o[lang()]||o.en}
function src(){var m=/[?&]src=([a-z0-9_-]+)/i.exec(location.search);return m?m[1].toLowerCase():''}
// language
try{var k=null,m=/[?&]lang=(en|fr|sw|pt)/.exec(location.search);if(m)k=m[1];if(!k){try{k=localStorage.getItem('afts-lang')}catch(e){}}
if(!k||!ok[k]){var l=(navigator.language||'').toLowerCase();k=l.indexOf('fr')===0?'fr':l.indexOf('sw')===0?'sw':l.indexOf('pt')===0?'pt':'en'}
var r=document.getElementById('l-'+k);if(r)r.checked=true;document.documentElement.lang=k;
document.querySelectorAll('.lr').forEach(function(x){x.addEventListener('change',function(){var v=this.id.slice(2);document.documentElement.lang=v;try{localStorage.setItem('afts-lang',v)}catch(e){};fillPicker()})})}catch(e){}
// keep ?src on internal links
try{var s=src();if(s)document.querySelectorAll('a[href]').forEach(function(a){var h=a.getAttribute('href');if(!h||/^(https?:|mailto:|tel:|#|data:)/i.test(h))return;var p=h.split('#');a.setAttribute('href',p[0]+(p[0].indexOf('?')<0?'?':'&')+'src='+s+(p.length>1?'#'+p[1]:''))})}catch(e){}
// news: 7 days on the home page, all items on the pillar page
try{var now=Date.now(),base=document.body.getAttribute('data-base')||'';
document.querySelectorAll('[data-news]').forEach(function(box){var mode=box.getAttribute('data-news'),list=box.querySelector('.news'),n=0;
A.news.forEach(function(it){var age=(now-Date.parse(it.date+'T00:00:00Z'))/864e5;if(age<0)return;
if(mode==='home'&&age>=7)return;if(mode!=='home'&&it.pillar!==mode)return;
var a=document.createElement(it.href?'a':'div');a.className='ni';if(it.href){var hr=typeof it.href==='string'?it.href:it.href.en;var ext=/^https?:/.test(hr);a.href=ext?hr:base+hr;if(ext){a.target='_blank';a.rel='noopener';}if(typeof it.href!=='string'){(function(a,m){a.addEventListener('click',function(){var k=(document.documentElement.lang||'en').slice(0,2);a.href=m[k]||m.en})})(a,it.href)}}
var d=new Date(it.date+'T12:00:00Z');
['en','fr','sw','pt'].forEach(function(L){var sp=document.createElement('span');sp.className='t t-'+L;sp.setAttribute('lang',L);
var ds=d.toLocaleDateString(L==='sw'?'sw-KE':L==='pt'?'pt-BR':L,{day:'numeric',month:'long',year:'numeric'});
sp.innerHTML='<div class="m"></div><b></b><span></span>';sp.querySelector('.m').textContent=ds;sp.querySelector('b').textContent=it.h[L];sp.querySelector('span').textContent=it.p[L];a.appendChild(sp)});
list.appendChild(a);n++});
if(n)box.hidden=false})}catch(e){}
// menus: one open at a time, close on outside tap
try{document.addEventListener('click',function(e){document.querySelectorAll('.nav details[open]').forEach(function(d){if(!d.contains(e.target))d.open=false})})}catch(e){}
// who-are-you picker
var M,topic=null;
function opt(sel,arr,ph){sel.innerHTML='';var o=document.createElement('option');o.value='';o.textContent=ph;sel.appendChild(o);arr.forEach(function(x){var o=document.createElement('option');o.value=x[0];o.textContent=T(x[1]);sel.appendChild(o)})}
function fillPicker(){if(!M)return;var P=A.pick;
['title','sub','consent','minor','cancel'].forEach(function(k){var e=M.querySelector('[data-p='+k+']');if(e)e.textContent=T(P[k])});
['type','team','level','country','city','org'].forEach(function(k){M.querySelector('[data-l='+k+']').firstChild.nodeValue=T(P[k])});
M.querySelector('[data-p=go_wa]').textContent=T(P.go_wa);M.querySelector('[data-p=go_mail]').textContent=T(P.go_mail);
var ty=M.querySelector('#pk-type'),v=ty.value;opt(ty,A.types,T(P.choose));ty.value=v;
var tm=M.querySelector('#pk-team'),v2=tm.value;opt(tm,A.teams,T(P.choose));tm.value=v2;
var lv=M.querySelector('#pk-level'),v3=lv.value;opt(lv,A.levels,T(P.choose));lv.value=v3;show()}
function show(){var t=M.querySelector('#pk-type').value,row=A.types.filter(function(x){return x[0]===t})[0]||[0,0,0,0];
M.querySelector('#pk-teamw').hidden=!row[2];M.querySelector('#pk-levelw').hidden=!row[3];M.querySelector('[data-p=minor]').hidden=!(t==='player'||t==='parent')}
function label(sel){var o=sel.options[sel.selectedIndex];return o&&sel.value?o.textContent:''}
function collect(){var g=function(i){return M.querySelector(i)};var ty=g('#pk-type');
return{type:ty.value,typeL:label(ty),team:g('#pk-teamw').hidden?'':label(g('#pk-team')),level:g('#pk-levelw').hidden?'':label(g('#pk-level')),
country:g('#pk-country').value.trim(),city:g('#pk-city').value.trim(),org:g('#pk-org').value.trim(),consent:g('#pk-ok').checked}}
function message(d){var P=A.pick,who=[d.typeL,d.team,d.level].filter(Boolean).join(' · '),where=[d.city,d.country].filter(Boolean).join(', ');
var c=lang()==='fr'?' : ':': ';var s=T(P.hello)+' '+T(P.iam)+c+who+(where?' ('+T(P.from)+' '+where+')':'')+(d.org?', '+d.org:'')+'. ';
if(topic)s+=T(P.about)+c+topic+'. ';return s+'['+location.pathname+(src()?' · '+src():'')+']'}
function save(d){try{if(window.goatcounter&&goatcounter.count)goatcounter.count({path:'picker/'+d.type+'/'+(d.country||'-').toLowerCase(),title:d.typeL,event:true})}catch(e){}
if(!A.sheet)return;try{var b=new URLSearchParams({type:d.typeL,team:d.team,level:d.level,country:d.country,city:d.city,org:d.org,topic:topic||'',page:location.pathname,lang:lang(),src:src(),consent:'yes'});
if(navigator.sendBeacon)navigator.sendBeacon(A.sheet,b);else fetch(A.sheet,{method:'POST',mode:'no-cors',body:b})}catch(e){}}
function submit(via){var d=collect();var err=M.querySelector('.err');if(!d.type||!d.country||!d.consent){err.textContent=T(A.pick.need);err.style.display='block';return}
err.style.display='none';save(d);var msg=message(d);
if(via==='wa')window.open('https://wa.me/'+A.wa+'?text='+encodeURIComponent(msg),'_blank','noopener');
else location.href='mailto:'+A.email+'?subject='+encodeURIComponent('Afritech Sports: '+d.typeL+(d.country?' · '+d.country:''))+'&body='+encodeURIComponent(msg);
close()}
function close(){M.classList.remove('open');document.body.style.overflow=''}
function open(t,preset){topic=t;M.classList.add('open');document.body.style.overflow='hidden';
if(preset){M.querySelector('#pk-type').value=preset;show()}setTimeout(function(){M.querySelector('#pk-type').focus()},50)}
M=document.getElementById('picker');if(M){fillPicker();
M.querySelector('#pk-type').addEventListener('change',show);
M.querySelector('[data-p=go_wa]').addEventListener('click',function(){submit('wa')});
M.querySelector('[data-p=go_mail]').addEventListener('click',function(){submit('mail')});
M.querySelector('[data-p=cancel]').addEventListener('click',close);
M.addEventListener('click',function(e){if(e.target===M)close()});
document.addEventListener('keydown',function(e){if(e.key==='Escape')close()});
if(location.hash==='#talk')setTimeout(function(){open(null,'')},300);
document.querySelectorAll('[data-pick]').forEach(function(b){b.addEventListener('click',function(e){e.preventDefault();document.querySelectorAll('.nav details[open]').forEach(function(d){d.open=false});
var tp=this.getAttribute('data-topic');var tt=null;if(tp){try{tt=JSON.parse(tp)[lang()]}catch(x){}}
open(tt,this.getAttribute('data-pick'))})})}
})();
"""

# ---------------------------------------------------------------- page shell
def tri(d, tag="span", cls=""):
    """Render a {en,fr,sw} dict as three language spans; plain strings pass through."""
    if isinstance(d, str):
        return E(d)
    c = (cls + " ") if cls else ""
    return "".join(f'<{tag} class="{c}t t-{l}" lang="{l}">{d[l]}</{tag}>' for l, _ in LANGS)

import json as _json
# Google: name the site and the company "Afritech Sports" so a search for the name finds this home site (Andrew, 27 Nov 2026)
LD = "".join('<script type="application/ld+json">' + _json.dumps(x, ensure_ascii=False) + "</script>" for x in (
    {"@context": "https://schema.org", "@type": "WebSite", "name": "Afritech Sports", "alternateName": ["Afritech Sports Technology and Innovation Group", "Afritech Sports Technology and Innovation Group Limited", "afritechsports"], "url": "https://afritechsports.github.io/"},
    {"@context": "https://schema.org", "@type": "Organization", "name": "Afritech Sports", "legalName": "Afritech Sports Technology and Innovation Group Limited", "alternateName": ["Afritech Sports Technology and Innovation Group", "Afritech Sports Technology and Innovation Group Ltd"],
     "url": "https://afritechsports.github.io/", "logo": "https://afritechsports.github.io/assets/img/logo.jpg", "email": "Advisory@afritechsports.com", "telephone": "+254715551506",
     "address": {"@type": "PostalAddress", "addressLocality": "Nairobi", "addressCountry": "KE"},
     "sameAs": ["https://www.linkedin.com/company/afritech-sports-technology-and-innovation-group-limited/", "https://afritech-advisory.github.io/Afritech-Advisory-afritech-tournament-desk/"]}))

def page(path, title, desc, body, base, active=""):
    r = ref()
    url = SITE + path
    home_href = base or "./"
    prim = [(home_href, "nav_home", active == ""), *[(f"{base}{slug}/", key, slug == active) for slug, key in [("technology", "nav_tech"), ("advisory", "nav_adv"), ("innovation", "nav_inn")]]]
    desks = [(MIQ, "nav_miq"), (DESK, "nav_desk"), (CVD, "nav_cv")]
    links = "".join(f'<a href="{h}" class="{"on" if on else ""}"{" aria-current=page" if on else ""}>{tri(UI[k])}</a>' for h, k, on in prim)
    dl = "".join(f'<a href="{h}">{tri(UI[k])} ↗</a>' for h, k in desks)
    talk = f'<button type="button" class="nt" data-pick="">{tri(UI["nav_talk"])}</button>'
    nav = (f'<div class="nl">{links}<details class="dd"><summary>{tri(UI["nav_desks"])}</summary><div class="ddl">{dl}</div></details>{talk}</div>'
           f'<div class="nm"><a href="{home_href}" class="nh{" on" if active=="" else ""}">⌂ {tri(UI["nav_home"])}</a>'
           f'<details class="dd mm"><summary>☰ {tri(UI["nav_menu"])}</summary><div class="ddl">'
           + "".join(f'<a href="{h}" class="{"on" if on else ""}">{tri(UI[k])}</a>' for h, k, on in prim)
           + f'<span class="ds">{tri(UI["nav_desks"])}</span>{dl}{talk}</div></details></div>')
    langs = "".join(f'<label for="l-{l}">{n}</label>' for l, n in LANGS)
    picker = f"""<div class="modal" id="picker" role="dialog" aria-modal="true" aria-labelledby="pk-h"><div class="mbox">
<h3 id="pk-h" data-p="title"></h3><p data-p="sub" style="margin:0;color:var(--muted)"></p>
<label class="f" data-l="type"> <select id="pk-type" required></select></label>
<p class="minor" data-p="minor" hidden></p>
<label class="f" id="pk-teamw" data-l="team" hidden> <select id="pk-team"></select></label>
<label class="f" id="pk-levelw" data-l="level" hidden> <select id="pk-level"></select></label>
<label class="f" data-l="country"> <input type="text" id="pk-country" autocomplete="country-name" list="pk-countries" maxlength="60"></label>
<label class="f" data-l="city"> <input type="text" id="pk-city" autocomplete="address-level2" maxlength="60"></label>
<label class="f" data-l="org"> <input type="text" id="pk-org" autocomplete="organization" maxlength="80"></label>
<label class="ck"><input type="checkbox" id="pk-ok"><span data-p="consent"></span></label>
<p class="err" role="alert"></p>
<div class="acts"><button class="btn wa" type="button" data-p="go_wa"></button><button class="btn ghost" type="button" data-p="go_mail"></button><button class="btn ghost sm" type="button" data-p="cancel"></button></div>
<datalist id="pk-countries">{"".join(f'<option value="{c}">' for c in COUNTRIES)}</datalist></div></div>"""
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="robots" content="noai, noimageai"><meta name="afritech-ref" content="{r}">
<meta name="copyright" content="© 2026 Afritech Sports Technology and Innovation Group Limited">
<title>{E(title)}</title><meta name="description" content="{E(desc)}">
<meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:url" content="{url}"><meta property="og:type" content="website"><meta property="og:image" content="{SITE}assets/img/share.jpg">
<meta name="twitter:card" content="summary_large_image"><link rel="canonical" href="{url}">
<link rel="alternate" hreflang="en" href="{url}?lang=en"><link rel="alternate" hreflang="fr" href="{url}?lang=fr"><link rel="alternate" hreflang="sw" href="{url}?lang=sw"><link rel="alternate" hreflang="pt-BR" href="{url}?lang=pt">
{LD if path == "" else ""}<link rel="icon" href="{base}assets/img/logo.jpg"><link rel="stylesheet" href="{base}assets/site.css">
</head><body data-base="{base}"><!-- Afritech Sports reference {r} --><span aria-hidden="true" style="position:absolute;left:-10000px;width:1px;height:1px;overflow:hidden">Afritech Sports reference {r}</span>
<input type="radio" name="lang" id="l-en" class="lr" checked><input type="radio" name="lang" id="l-fr" class="lr"><input type="radio" name="lang" id="l-sw" class="lr"><input type="radio" name="lang" id="l-pt" class="lr">
<header class="top"><div class="top-in"><a class="brand" href="{base or './'}"><img src="{base}assets/img/logo.jpg" alt="Afritech Sports emblem" width="40" height="40"><b>Afritech Sports<small>Technology and Innovation Group · Nairobi</small></b></a>
<div class="langs" role="group" aria-label="Language">{langs}</div></div><nav class="nav" aria-label="Main"><div class="nav-in">{nav}</div></nav></header>
<main>{body}</main>
<footer class="foot">© 2026 Afritech Sports Technology and Innovation Group Ltd. {tri(UI['rights'])} · {EMAIL} · <a href="{base}privacy/">{tri(UI['privacy'])}</a> · <a href="{LI_CO}" target="_blank" rel="noopener">LinkedIn</a><br>{tri(UI['terms'])}</footer>
{picker}
<script src="{base}assets/site.js" defer></script>
<script data-goatcounter="{GOAT}" async src="//gc.zgo.at/count.js"></script>
</body></html>"""

def pickbtn(cls, label, preset="", topic=None):
    t = f" data-topic='{E(json.dumps(topic, ensure_ascii=False))}'" if topic else ""
    return f'<button type="button" class="btn {cls}" data-pick="{preset}"{t}>{tri(label)}</button>'

def hero(eyebrow, h1, lead, preset="", topic=None):
    return f"""<section class="hero"><div class="hero-in"><p class="eyebrow">{tri(eyebrow)}</p><h1>{tri(h1)}</h1><p class="lead">{tri(lead)}</p>
<div class="acts">{pickbtn("wa", UI['talk'], preset, topic)}<a class="btn ghost" href="mailto:{EMAIL}">{tri(UI['email'])}</a></div>
<p class="small">{tri(UI['reply'])}</p></div></section>"""

def band(preset="", topic=None):
    return f"""<section class="band" id="contact"><h2>{tri(UI['cta_h'])}</h2><p style="margin:0">{tri(UI['reply'])}</p>
<div class="acts">{pickbtn("wa", UI['talk'], preset, topic)}<a class="btn ghost" href="mailto:{EMAIL}">{tri(UI['email'])}</a></div>
<p class="contact">{tri(UI['addr'])}<br>{EMAIL} · {tri(UI['phone'])}: +254 715 551 506<br><a href="{LI_CO}" target="_blank" rel="noopener">Afritech Sports on LinkedIn</a> · <a href="{LI_AR}" target="_blank" rel="noopener">Andrew Rukidi on LinkedIn</a></p></section>"""

def newsbox(mode, heading):
    return f'<section data-news="{mode}" hidden><h2>{tri(heading)}</h2><div class="news"></div></section>'

EYEBROW = L("Afritech Sports · Nairobi, Kenya", "Afritech Sports · Nairobi, Kenya", "Afritech Sports · Nairobi, Kenya")
COUNTRIES = ["Kenya","Uganda","Tanzania","Rwanda","Burundi","South Sudan","Ethiopia","Somalia","DR Congo","Congo","Zambia","Zimbabwe","Malawi","Mozambique","South Africa","Botswana","Namibia","Eswatini","Lesotho","Angola","Madagascar","Nigeria","Ghana","Senegal","Côte d'Ivoire","Cameroon","Mali","Burkina Faso","Guinea","Benin","Togo","Niger","Sierra Leone","Liberia","Gambia","Gabon","Morocco","Algeria","Tunisia","Egypt","Libya","Sudan","United Kingdom","United States","France","Spain","Portugal","Netherlands","Belgium","Germany","Brazil","United Arab Emirates","Qatar","Saudi Arabia"]

# ---------------------------------------------------------------- pages
def build_home():
    b = [hero(HOME["eyebrow"], HOME["h1"], HOME["lead"]), '<div class="wrap">', newsbox("home", UI["news_h"])]
    b.append(f'<h2>{tri(HOME["pillars_h"])}</h2><div class="cards three">')
    for slug, key, line, items in PILLARS:
        lis = "".join(f"<li>{tri(i)}</li>" for i in items)
        b.append(f'<a class="card" href="{slug}/"><span class="tag">{tri(UI[key])}</span><span class="d">{tri(line)}</span><ul>{lis}</ul><span class="go">{tri(UI["open"])} →</span></a>')
    b.append(f'</div><h2>{tri(HOME["who_h"])}</h2><div class="cards three">')
    for title, line, link, preset in WHO:
        b.append(f'<div class="card"><h3>{tri(title)}</h3><span class="d">{tri(line)}</span><div class="row"><a class="btn ghost sm" href="{link}">{tri(UI["see"])}</a>{pickbtn("wa sm", UI["msg"], preset)}</div></div>')
    b.append(f'</div><h2>{tri(HOME["proof_h"])}</h2><div class="proof">')
    for t, p in PROOF:
        b.append(f'<div class="pf"><b>{tri(t)}</b>{tri(p)}</div>')
    b.append("</div>" + band() + "</div>")
    write("index.html", page("", HOME["title"], HOME["desc"], "".join(b), ""))

def build_tech():
    b = [hero(EYEBROW, TECH["h1"], TECH["lead"], "club", L("sports technology", "la technologie sportive", "teknolojia ya michezo")), '<div class="wrap">', newsbox("technology", UI["latest"]), '<div style="height:22px"></div>']
    for p in PRODUCTS:
        alt = p["alt"]["en"]
        b.append(f"""<article class="prod" id="{p['id']}"><img src="../assets/img/{p['img']}" alt="{E(alt)}" loading="lazy" width="660" height="360"><div class="pb">
<span class="tag">{tri(UI['nav_tech'])}</span><h3 style="font-size:28px">{p['name']}</h3><p style="margin:6px 0 0">{tri(p['what'])}</p>
<dl><dt>{tri(p['sees_h'])}</dt><dd>{tri(p['sees'])}</dd><dt>{tri(p['suits_h'])}</dt><dd>{tri(p['suits'])}</dd></dl>
<div class="acts">{pickbtn("wa sm", UI['quote'], "club", {l: p['name'] for l, _ in LANGS})}</div></div></article>""")
    b.append(f'<h2>{tri(TECH["how_h"])}</h2><div class="steps">')
    for t, p in TECH["how"]:
        b.append(f'<div class="st"><b>{tri(t)}</b>{tri(p)}</div>')
    b.append("</div>" + band("club", L("sports technology", "la technologie sportive", "teknolojia ya michezo")) + f'<a class="back" href="../">{tri(UI["home"])}</a></div>')
    write("technology/index.html", page("technology/", TECH["title"], TECH["desc"], "".join(b), "../", "technology"))

def build_adv():
    b = [hero(EYEBROW, ADV["h1"], ADV["lead"]), '<div class="wrap">', newsbox("advisory", UI["latest"])]
    for s in ADV_SECTIONS:
        link = f'<a class="btn ghost sm" href="{s["link"][0]}" target="_blank" rel="noopener">{tri(s["link"][1])} →</a>' if s["link"] else ""
        extra = ""
        if s["id"] == "education":
            cards = []
            for ev in EVENTS:
                st = PAST if ev["status"] == "past" else NEXT
                act = pickbtn("wa sm", UI["interest"], "", ev["h"] if isinstance(ev["h"], dict) else {l: ev["h"] for l, _ in LANGS}) if ev["status"] == "next" else ""
                cards.append(f'<div class="evc"><div class="m">{tri(ev["date"])} · {tri(ev["kind"])}</div><span class="s {ev["status"]}">{tri(st)}</span><h3>{tri(ev["h"])}</h3><div class="m" style="text-transform:none;letter-spacing:0">{ev["with"]}</div><p style="margin:8px 0">{tri(ev["p"])}</p>{act}</div>')
            extra = f'<div class="ev">{"".join(cards)}</div><p class="note">{tri(CONF)}</p>'
        inner = f'<span class="tag">{tri(s["tag"])}</span><h3 style="font-size:28px;margin-top:6px">{tri(s["h"])}</h3><p style="margin:6px 0 0">{tri(s["p"])}</p>{extra}<div class="acts">{link}{pickbtn("wa sm", UI["msg"], "", s["topic"])}</div>'
        if s.get("img"):
            b.append(f'<section class="sec media" id="{s["id"]}"><img src="../assets/img/{s["img"][0]}" alt="{E(s["img"][1])}" loading="lazy"><div>{inner}</div></section>')
        else:
            b.append(f'<section class="sec" id="{s["id"]}">{inner}</section>')
    b.append(band() + f'<a class="back" href="../">{tri(UI["home"])}</a></div>')
    write("advisory/index.html", page("advisory/", ADV["title"], ADV["desc"], "".join(b), "../", "advisory"))

def episodes():
    """Every podcast episode in NEWS, newest first, listed permanently in the Podcast section.
    The daily News sync adds episodes to NEWS, so this list updates itself."""
    import datetime
    rows = []
    for it in NEWS:
        h = it.get("href")
        en = h.get("en", "") if isinstance(h, dict) else (h or "")
        if "spotify.com/episode" not in en and "spotify.com/show" not in en:
            continue
        if "podcast" not in it["h"]["en"].lower():
            continue
        d = datetime.date.fromisoformat(it["date"])
        links = ""
        for l, _ in LANGS:
            title = it["h"][l].split(":", 1)[-1].strip() if ":" in it["h"][l] else it["h"][l]
            url = h[l] if isinstance(h, dict) else h
            links += f'<a class="t t-{l}" lang="{l}" href="{url}" target="_blank" rel="noopener">{title}</a>'
        rows.append(f'<li><span class="ed">{d.day} {d.strftime("%b")}</span>{links}</li>')
    if not rows:
        return ""
    head = tri(L("Latest episodes", "Derniers épisodes", "Vipindi vya hivi karibuni"))
    return f'<h4 class="eph">{head}</h4><ol class="eps">{"".join(rows)}</ol>'


def build_inn():
    pods = "".join(f'<a href="{u}" target="_blank" rel="noopener">{n}</a>' for n, u in POD)
    b = [hero(EYEBROW, INN["h1"], INN["lead"]), '<div class="wrap">', newsbox("innovation", UI["latest"]),
         f'<section class="sec media" id="desk"><img src="../assets/img/desk.jpg" alt="Afritech Tournament Desk, FIFA U-17 World Cup Qatar 2026" loading="lazy"><div><span class="tag">{tri(INN["desk_tag"])}</span><h3 style="font-size:28px;margin-top:6px">{tri(INN["desk_h"])}</h3><p style="margin:6px 0 0">{tri(INN["desk_p"])}</p><div class="acts"><a class="btn ghost sm" href="{DESK}" target="_blank" rel="noopener">{tri(INN["desk_open"])} →</a>{pickbtn("wa sm", UI["msg"], "", INN["desk_topic"])}</div></div></section>',
         f'<section class="sec media" id="podcast"><img src="../assets/img/podcast.jpg" alt="Deep Dive Into Soccer podcast: 5,000 streams and downloads" loading="lazy"><div><span class="tag">{tri(INN["pod_tag"])}</span><h3 style="font-size:28px;margin-top:6px">{INN["pod_h"]}</h3><p style="margin:6px 0 0">{tri(INN["pod_p"])}</p><div class="pods">{pods}</div>{episodes()}<div class="acts">{pickbtn("wa sm", UI["msg"], "media", INN["pod_topic"])}</div></div></section>',
         band() + f'<a class="back" href="../">{tri(UI["home"])}</a></div>']
    write("innovation/index.html", page("innovation/", INN["title"], INN["desc"], "".join(b), "../", "innovation"))

def build_privacy():
    b = f'<div class="wrap"><h2>{tri(PRIV["h1"])}</h2>{tri(PRIV["body"], "div")}<a class="back" href="../">{tri(UI["home"])}</a></div>'
    write("privacy/index.html", page("privacy/", PRIV["title"], "How Afritech Sports handles visitor details.", b, "../"))

REDIRECTS = {"clubs/": "advisory/", "talent/": "advisory/#cv", "agents/": "advisory/#scouting", "federations/": "advisory/#analytics"}
def build_redirects():
    for old, new in REDIRECTS.items():
        to = SITE + new
        write(old + "index.html", f'<!doctype html><html><head><meta charset="utf-8"><meta name="robots" content="noindex"><link rel="canonical" href="{to}"><meta http-equiv="refresh" content="0; url={to}"><script>location.replace("{to.split("#")[0]}"+location.search+"{("#"+to.split("#")[1]) if "#" in to else ""}")</script></head><body><a href="{to}">Afritech Sports</a></body></html>')

ROBOTS = "# Afritech Sports. Content may not be used to train AI models.\n" + "".join(f"User-agent: {b}\nDisallow: /\n" for b in ["GPTBot","ChatGPT-User","CCBot","ClaudeBot","anthropic-ai","Google-Extended","Applebot-Extended","PerplexityBot","Bytespider","Meta-ExternalAgent","Amazonbot","cohere-ai","AhrefsBot","SemrushBot","MJ12bot","DotBot","PetalBot"]) + f"User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n"

if __name__ == "__main__":
    shutil.rmtree(OUT, ignore_errors=True)
    os.makedirs(os.path.join(OUT, "assets/img"))
    write("assets/site.css", CSS); write("assets/site.js", js())
    for f in sorted(os.listdir(os.path.join(ROOT, "img"))):
        shutil.copy(os.path.join(ROOT, "img", f), os.path.join(OUT, "assets/img", f))
    build_home(); build_tech(); build_adv(); build_inn(); build_privacy(); build_redirects()
    write("robots.txt", ROBOTS)
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + "".join(f"<url><loc>{SITE}{p}</loc></url>" for p in ["", "technology/", "advisory/", "innovation/", "privacy/"]) + "</urlset>\n")
    write("README.md", "# Afritech Sports\n\nHome site of Afritech Sports Technology and Innovation Group Limited, Nairobi: https://afritechsports.github.io/\n\n© 2026 Afritech Sports Technology and Innovation Group Ltd. All rights reserved. The text, forms and design in this repository may not be copied or republished without written permission. Contact: Advisory@afritechsports.com\n")
    write(".nojekyll", "")
    # Google Search Console ownership file (Andrew, 27 Nov 2026): must stay, or the property loses verification
    write("google8651b71c765154ef.html", "google-site-verification: google8651b71c765154ef.html")
    print("built")
