# Shared header + full-screen menu for every page (v4). Run: python3 tools/site_chrome.py
import re, pathlib
R = pathlib.Path(__file__).resolve().parent.parent
L = ['en', 'fr', 'sw', 'pt']
def t(*a, tag='span'):
    return ''.join(f'<{tag} class="t t-{k}" lang="{k}">{v}</{tag}>' for k, v in zip(L, a))
DESK = 'https://afritech-advisory.github.io/Afritech-Advisory-afritech-tournament-desk/'
ITEMS = [
 ('', ('Home', 'Accueil', 'Nyumbani', 'Início')),
 ('technology/', ('Sports Technology', 'Technologie sportive', 'Teknolojia ya Michezo', 'Tecnologia Esportiva')),
 ('advisory/', ('Advisory Services', 'Services de conseil', 'Huduma za Ushauri', 'Consultoria')),
 ('innovation/', ('Innovation', 'Innovation', 'Ubunifu', 'Inovação')),
 ('about/', ('About us', 'À propos', 'Kuhusu sisi', 'Sobre nós')),
]
DESKS = [('https://afritech-advisory.github.io/afritech-matchiq/', 'MatchIQ'),
         (DESK, ('Tournament Desk', 'Desk Tournoi', 'Dawati la Mashindano', 'Mesa do Torneio')),
         ('https://afritech-advisory.github.io/afritech-sports-cv-desk/', ('CV Desk', 'Bureau CV', 'Dawati la CV', 'Mesa de Currículos'))]

def header(base, active):
    li = ''
    for i, (href, names) in enumerate(ITEMS, 1):
        on = ' aria-current="page" class="on"' if href == active else ''
        li += f'<li><a href="{base}{href}"{on}><span class="mn">0{i}</span><span class="ml">{t(*names)}</span></a></li>'
    li += f'<li><button type="button" data-pick=""><span class="mn">0{len(ITEMS)+1}</span><span class="ml">{t("Contact", "Contact", "Wasiliana", "Contato")}</span></button></li>'
    dk = ''.join(f'<a href="{u}" target="_blank" rel="noopener">{n if isinstance(n, str) else t(*n)} ↗</a>' for u, n in DESKS)
    return f'''<header class="top"><div class="top-in"><a class="brand" href="{base or './'}"><img src="{base}assets/img/logo.jpg" alt="Afritech Sports logo" width="44" height="44"><b>Afritech Sports<small>Technology &amp; Innovation Group · Nairobi</small></b></a>
<a class="live" href="{DESK}qatar-u17-2026/" target="_blank" rel="noopener"><i></i>{t('Live: U-17 Tournament Desk', 'En direct : Desk U-17', 'Moja kwa moja: Dawati la U-17', 'Ao vivo: Mesa Sub-17')}</a>
<div class="langs" role="group" aria-label="Language"><label for="l-en" title="English">EN</label><label for="l-fr" title="Français">FR</label><label for="l-sw" title="Kiswahili">SW</label><label for="l-pt" title="Português">PT</label></div>
<button type="button" class="btn go1 talk" data-pick="">{t("Let’s talk", "Parlons-en", "Tuongee", "Vamos conversar")}</button>
<button type="button" class="menu-btn" aria-expanded="false" aria-controls="menu"><span class="mb-l">{t('Menu', 'Menu', 'Menyu', 'Menu')}</span><span class="mb-i" aria-hidden="true"><i></i><i></i></span></button></div></header>
<nav class="menu" id="menu" aria-label="Main" aria-hidden="true"><div class="menu-in"><ol class="mlist">{li}</ol>
<aside class="maside"><p class="mk">{t('Our live desks', 'Nos desks en ligne', 'Madawati yetu hewani', 'Nossas mesas no ar')}</p><div class="mdesks">{dk}</div>
<p class="mk">{t('Language', 'Langue', 'Lugha', 'Idioma')}</p><div class="mlangs"><label for="l-en">English</label><label for="l-fr">Français</label><label for="l-sw">Kiswahili</label><label for="l-pt">Português</label></div>
<p class="mk">{t('Talk to us', 'Contact', 'Wasiliana nasi', 'Fale com a gente')}</p><a href="mailto:Advisory@afritechsports.com">Advisory@afritechsports.com</a><a href="tel:+254715551506">+254 715 551 506</a>
<p class="mk">{t('Follow', 'Suivre', 'Fuatilia', 'Siga')}</p><a href="https://www.linkedin.com/company/afritech-sports-technology-and-innovation-group-limited/" target="_blank" rel="noopener">LinkedIn ↗</a></aside></div></nav>'''

PAGES = {'index.html': ('', ''), 'technology/index.html': ('../', 'technology/'), 'advisory/index.html': ('../', 'advisory/'),
         'innovation/index.html': ('../', 'innovation/'), 'privacy/index.html': ('../', ''), 'about/index.html': ('../', 'about/')}
if __name__ == '__main__':
    for f, (base, act) in PAGES.items():
        p = R / f
        if not p.exists(): continue
        s = p.read_text(encoding='utf-8')
        a = s.index('<header class="top">')
        b = s.index('</nav>', a) + 6
        s = s[:a] + header(base, act) + s[b:]
        p.write_text(s, encoding='utf-8'); print('header ->', f)
