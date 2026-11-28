# Builds index.html (home v2). Keeps the existing header, nav, picker and scripts from the current page.
import re, pathlib, html as H
R = pathlib.Path(__file__).resolve().parent.parent
src = (R / 'index.html').read_text(encoding='utf-8')
L = ['en', 'fr', 'sw', 'pt']

def t(en, fr, sw, pt, tag='span'):
    out = ''
    for k, v in zip(L, (en, fr, sw, pt)):
        out += f'<{tag} class="t t-{k}" lang="{k}">{v}</{tag}>'
    return out

def tp(*a): return t(*a, tag='p')

import json
topic = lambda *a: H.escape(json.dumps(dict(zip(L, a)), ensure_ascii=False), quote=True)

def ctl(line, btn, pick='', topic_json='', href=None, ghost=False):
    cls = 'btn ghost' if ghost else 'btn go1'
    if href:
        ext = ' target="_blank" rel="noopener"' if href.startswith('http') else ''
        b = f'<a class="{cls}" href="{href}"{ext}>{t(*btn)} <span class="ar" aria-hidden="true">→</span></a>'
    else:
        tp_ = f" data-topic='{topic_json}'" if topic_json else ''
        b = f'<button type="button" class="{cls}" data-pick="{pick}"{tp_}>{t(*btn)} <span class="ar" aria-hidden="true">→</span></button>'
    return f'<div class="cta-line">{tp(*line)}{b}</div>'


head = src[:src.index('<header class="top">')]
header = src[src.index('<header class="top">'):src.index('<main>')]
tail = src[src.index('<div class="modal" id="picker"'):]
foot = re.search(r'<footer class="foot">.*?</footer>', src, re.S).group(0)

DESK = 'https://afritech-advisory.github.io/Afritech-Advisory-afritech-tournament-desk/'
MIQ_URL = 'https://afritech-advisory.github.io/afritech-matchiq/matches/2026-11-07-japan-nigeria-u17w-final/'
MIQ = 'https://afritech-advisory.github.io/afritech-matchiq/matches/2026-11-07-japan-nigeria-u17w-final/'
CVD = 'https://afritech-advisory.github.io/afritech-sports-cv-desk/'

# live pill in header
live = f'<a class="live" href="{DESK}qatar-u17-2026/" target="_blank" rel="noopener"><i></i>' + t('Live: U-17 Tournament Desk', 'En direct : Desk U-17', 'Moja kwa moja: Dawati la U-17', 'Ao vivo: Mesa Sub-17') + '</a>'
if 'class="live"' not in header:
    header = header.replace('<div class="langs"', live + '<div class="langs"', 1)

arrow = '<span class="ar" aria-hidden="true">→</span>'
SND = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 9v6h4l5 4V5L7 9H3zm13.5 3a4.5 4.5 0 0 0-2.5-4v8a4.5 4.5 0 0 0 2.5-4zM14 3.2v2.1a7 7 0 0 1 0 13.4v2.1a9 9 0 0 0 0-17.6z"/></svg>' + t('Tap for sound', 'Activer le son', 'Gusa kupata sauti', 'Toque para ouvir')
PROJ = [
 dict(k='miq', href=MIQ_URL, d='assets/work/miq-desktop.webp', m='assets/work/miq-phone.webp',
      lab=('Match report','Rapport de match','Ripoti ya mechi','Relatório de partida'),
      h=('MatchIQ · U-17 World Cup final','MatchIQ · finale Coupe du monde U-17','MatchIQ · fainali Kombe la Dunia U-17','MatchIQ · final da Copa Sub-17'),
      p=('Nigeria 2–1 Japan, read goal by goal: radars, phase reads and five dated next steps.','Nigeria 2–1 Japon, but par but : radars, lectures de phases et cinq étapes datées.','Nigeria 2–1 Japan, bao kwa bao: rada, uchambuzi wa awamu na hatua tano zenye tarehe.','Nigéria 2–1 Japão, gol a gol: radares, leitura das fases e cinco passos com data.')),
 dict(k='analysis', href='#video-analysis', d='assets/work/analysis-desktop.webp', m='assets/work/analysis-phone.webp',
      lab=('Video analysis','Analyse vidéo','Uchambuzi wa video','Análise de vídeo'),
      h=('Kenya 1–2 South Africa','Kenya 1–2 Afrique du Sud','Kenya 1–2 Afrika Kusini','Quênia 1–2 África do Sul'),
      p=('Post-match coaching review with tactical reconstruction and xT.','Revue d’après-match avec reconstruction tactique et xT.','Mapitio ya kocha baada ya mechi, na uundaji upya wa mbinu na xT.','Revisão pós-jogo com reconstrução tática e xT.')),
 dict(k='dossier', href='https://afritech-advisory.github.io/afritech-sports-cv-desk/scouts/alen-suljic/#verified', d='assets/work/dossier-desktop.webp', m='assets/work/dossier-phone.webp',
      lab=('Scouting dossier','Dossier de recrutement','Ripoti ya uskauti','Dossiê de scouting'),
      h=('Scouting dossiers','Dossiers de recrutement','Ripoti za uskauti','Dossiês de scouting'),
      p=('One player, eleven checks, one clear verdict a club or agent can act on.','Un joueur, onze vérifications, un avis clair pour agir.','Mchezaji mmoja, ukaguzi kumi na moja, uamuzi mmoja wa wazi.','Um jogador, onze verificações, uma recomendação clara.')),
 dict(k='desk', href=DESK + 'qatar-u17-2026/', d='assets/work/desk-desktop.webp', m='assets/work/desk-phone.webp',
      lab=('Live desk','Desk en direct','Dawati hewani','Mesa ao vivo'),
      h=('Tournament Desk · Qatar 2026','Desk Tournoi · Qatar 2026','Dawati la Mashindano · Qatar 2026','Mesa do Torneio · Catar 2026'),
      p=('Africa’s ten nations at the U-17 World Cup, match by match, players scored.','Les dix nations africaines à la Coupe du monde U-17, match par match, joueurs notés.','Mataifa kumi ya Afrika Kombe la Dunia U-17, mechi kwa mechi, wachezaji wakipewa alama.','As dez seleções africanas na Copa Sub-17, jogo a jogo, jogadores avaliados.')),
 dict(k='cv', href=CVD, d='assets/work/cv-desktop.webp', m='assets/work/scout-phone.webp',
      lab=('CV Desk','Bureau CV','Dawati la CV','Mesa de Currículos'),
      h=('Football CVs','CV football','CV za soka','Currículos de futebol'),
      p=('Players, coaches, scouts and analysts, built to our standard so clubs can find them.','Joueurs, entraîneurs, recruteurs et analystes, à notre standard pour être trouvés.','Wachezaji, makocha, maskauti na wachambuzi, kwa kiwango chetu ili klabu ziwapate.','Jogadores, treinadores, olheiros e analistas, no nosso padrão para serem encontrados.')),
 dict(k='insait', href='technology/', d='assets/work/insait-desktop.webp', m='assets/work/insait-phone.webp',
      lab=('Sports technology','Technologie sportive','Teknolojia ya michezo','Tecnologia esportiva'),
      h=('INSAIT JOY smart shin guards','Protège-tibias connectés INSAIT JOY','Vilinda-muundi janja vya INSAIT JOY','Caneleiras inteligentes INSAIT JOY'),
      p=('Every run, touch and kick, on the coach’s phone after the session.','Chaque course, touche et frappe, sur le téléphone du coach après la séance.','Kila mbio, mguso na teke, kwenye simu ya kocha baada ya mazoezi.','Cada corrida, toque e chute, no celular do treinador após o treino.')),
 dict(k='soccerbee', href='technology/#soccerbee', d='assets/work/soccerbee-desktop.webp', m='assets/work/soccerbee-phone.webp',
      lab=('Sports technology','Technologie sportive','Teknolojia ya michezo','Tecnologia esportiva'),
      h=('Soccerbee GPS tracking','Suivi GPS Soccerbee','Ufuatiliaji wa GPS wa Soccerbee','Monitoramento GPS Soccerbee'),
      p=('Top speed and high-speed running, benchmarked against players of the same age.','Vitesse max et course à haute intensité, comparées aux joueurs du même âge.','Kasi ya juu na mbio za kasi, zikilinganishwa na wachezaji wa umri sawa.','Velocidade máxima e corrida intensa, comparadas com jogadores da mesma idade.')),
]

pitch_svg = """<div class="fx" aria-hidden="true"><svg viewBox="0 0 1200 700" preserveAspectRatio="xMidYMid slice"><defs><linearGradient id="gp" x1="0" x2="1"><stop offset="0" stop-color="#49C6F0" stop-opacity="0"/><stop offset=".6" stop-color="#5EE08A"/><stop offset="1" stop-color="#E9FFF0"/></linearGradient><linearGradient id="go" x1="0" x2="1"><stop offset="0" stop-color="#1F7FC4"/><stop offset=".5" stop-color="#5EE08A"/><stop offset="1" stop-color="#1F7FC4" stop-opacity=".2"/></linearGradient></defs>
<g class="pitchlines"><rect x="40" y="40" width="1120" height="620"/><path d="M600 40V660"/><circle cx="600" cy="350" r="92"/><rect x="40" y="200" width="150" height="300"/><rect x="1010" y="200" width="150" height="300"/></g>
<g class="orb"><ellipse cx="880" cy="350" rx="330" ry="120" fill="none" stroke="url(#go)" stroke-width="10" opacity=".55" transform="rotate(-24 880 350)"/></g>
<g class="orb b"><ellipse cx="880" cy="350" rx="300" ry="300" fill="none" stroke="#5EE08A" stroke-width="1.5" stroke-dasharray="4 14" opacity=".45"/></g>
<path class="trace" d="M0 560H180L230 510H420L470 460H560"/><path class="pulse" d="M0 560H180L230 510H420L470 460H560"/>
<path class="trace" d="M0 150H120L170 200H330L380 150H520"/><path class="pulse p2" d="M0 150H120L170 200H330L380 150H520"/>
<path class="trace" d="M1200 620H1040L990 570H860L820 610H700"/><path class="pulse p3" d="M1200 620H1040L990 570H860L820 610H700"/>
<path class="trace" d="M1200 90H1080L1030 140H930L890 100H780"/><path class="pulse p4" d="M1200 90H1080L1030 140H930L890 100H780"/>
<circle class="node" cx="560" cy="460" r="4"/><circle class="node" cx="520" cy="150" r="4"/><circle class="node" cx="700" cy="610" r="4"/><circle class="node" cx="780" cy="100" r="4"/>
<g>""" + ''.join(f'<rect class="bit" x="{980+i*23%140}" y="{230+i*37%150}" width="{4+i%3*2}" height="{4+i%3*2}" style="animation-delay:-{i*0.55:.2f}s"/>' for i in range(14)) + """</g></svg></div>"""

hero = f'''<section class="h-hero">{pitch_svg}<div class="h-in"><div>
<p class="eyebrow">{t('Football scouting, match analysis and player data · Africa', 'Recrutement, analyse de match et données joueurs · Afrique', 'Uskauti wa soka, uchambuzi wa mechi na data za wachezaji · Afrika', 'Scouting, análise de partidas e dados de jogadores · África')}</p>
<h1>{t('<span class="ln"><span>Find the <mark>talent.</mark></span></span><span class="ln"><span>Read the <em>game.</em></span></span><span class="ln"><span>Run the <em>tech.</em></span></span>',
       '<span class="ln"><span>Trouver le <mark>talent.</mark></span></span><span class="ln"><span>Lire le <em>jeu.</em></span></span><span class="ln"><span>Faire tourner la <em>tech.</em></span></span>',
       '<span class="ln"><span>Pata <mark>vipaji.</mark></span></span><span class="ln"><span>Soma <em>mchezo.</em></span></span><span class="ln"><span>Endesha <em>teknolojia.</em></span></span>',
       '<span class="ln"><span>Encontre o <mark>talento.</mark></span></span><span class="ln"><span>Leia o <em>jogo.</em></span></span><span class="ln"><span>Faça a <em>tecnologia</em> funcionar.</span></span>')}</h1>
{'<div class="lead">' + tp('Match reports, scouting dossiers, football CVs and player tracking for clubs, academies, agents and federations across Africa. Built in Nairobi, made to open on any phone, even with no signal.', 'Rapports de match, dossiers de recrutement, CV football et suivi des joueurs pour les clubs, académies, agents et fédérations d’Afrique. Conçus à Nairobi, lisibles sur n’importe quel téléphone, même sans réseau.', 'Ripoti za mechi, ripoti za uskauti, CV za soka na ufuatiliaji wa wachezaji kwa klabu, akademia, mawakala na mashirikisho kote Afrika. Zimetengenezwa Nairobi, zinafunguka kwenye simu yoyote, hata bila mtandao.', 'Relatórios de partida, dossiês de scouting, currículos de futebol e monitoramento de jogadores para clubes, academias, agentes e federações da África. Feitos em Nairóbi, abrem em qualquer celular, mesmo sem sinal.') + '</div>'}
<div class="acts"><a class="btn go1" href="#first-move">{t('Pick your first move', 'Choisissez votre premier pas', 'Chagua hatua yako ya kwanza', 'Escolha seu primeiro passo')} {arrow}</a><a class="btn ghost" href="#work">{t('See the work', 'Voir le travail', 'Ona kazi yetu', 'Veja o trabalho')}</a></div>
<div class="h-meta"><span>{t('<b>EN · FR · SW · PT</b> four languages', '<b>EN · FR · SW · PT</b> quatre langues', '<b>EN · FR · SW · PT</b> lugha nne', '<b>EN · FR · SW · PT</b> quatro idiomas')}</span><span>{t('<b>Works offline</b> on any phone', '<b>Hors ligne</b> sur tout téléphone', '<b>Bila mtandao</b> kwenye simu yoyote', '<b>Funciona offline</b> em qualquer celular')}</span></div>
</div>
{f'''<div class="show" data-show>{"".join(f'<span hidden></span>' for _ in [])}
<div class="dev"><div class="mon"><div class="mon-scr">{''.join(f'<img class="sl{" on" if n==0 else ""}" {"src" if n==0 else "data-src"}="{x["d"]}" alt="" width="1400" height="875">' for n,x in enumerate(PROJ))}</div><i class="mon-stand"></i></div>
<div class="ph"><div class="ph-scr">{''.join(f'<img class="sl{" on" if n==0 else ""}" {"src" if n==0 else "data-src"}="{x["m"]}" alt="" width="560" height="1212">' for n,x in enumerate(PROJ))}</div></div></div>
<div class="show-meta">{''.join(f'<a class="smeta{" on" if n==0 else ""}" href="{x["href"]}"{" target=_blank rel=noopener" if x["href"].startswith("http") else ""}><span class="lbl"><i></i>{t(*x["lab"])} · 0{n+1}/0{len(PROJ)}</span><b>{t(*x["h"])}</b>{t(*x["p"])}</a>' for n,x in enumerate(PROJ))}</div>
<div class="show-ctl"><button type="button" class="pp" data-show-pp aria-label="Pause the showcase"><svg viewBox="0 0 14 14"><rect x="2" y="1" width="3.5" height="12"/><rect x="8.5" y="1" width="3.5" height="12"/></svg></button><div class="dots">{''.join(f'<button type="button" aria-label="Project {n+1}"{" class=on" if n==0 else ""}></button>' for n in range(len(PROJ)))}</div></div>
</div>'''}
</div></section>'''

tick_items = [('Match analysis','Analyse de match','Uchambuzi wa mechi','Análise de partidas'),('Scouting dossiers','Dossiers de recrutement','Ripoti za uskauti','Dossiês de scouting'),('Football CVs','CV football','CV za soka','Currículos de futebol'),('INSAIT JOY','INSAIT JOY','INSAIT JOY','INSAIT JOY'),('Soccerbee GPS','Soccerbee GPS','Soccerbee GPS','Soccerbee GPS'),('Contracts & transfers','Contrats & transferts','Mikataba na uhamisho','Contratos e transferências'),('Workshops','Ateliers','Warsha','Workshops'),('Tournament Desk','Desk Tournoi','Dawati la Mashindano','Mesa do Torneio')]
BALL = '<svg class="ball" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10.5"/><path d="M12 7.2l3.6 2.6-1.4 4.2H9.8L8.4 9.8z"/><path d="M12 1.5v5.7M15.6 9.8l5.2-1.6M14.2 14l3.2 4.6M9.8 14l-3.2 4.6M8.4 9.8L3.2 8.2"/></svg>'
tk = ''.join(f'<span class="{"o" if n%2 else ""}">' + t(*i) + '</span>' + BALL for n,i in enumerate(tick_items))
tk2 = ''.join(f'<span class="{"" if n%2 else "o"}">' + t(*i) + '</span>' + BALL for n,i in enumerate(reversed(tick_items)))
ticker = f'<div class="ticks" aria-hidden="true"><div class="tick t1"><div class="tick-in">{tk}{tk}</div></div><div class="tick t2"><div class="tick-in rev">{tk2}{tk2}</div></div></div>'

reality = f'''<section class="sx dark" id="reality"><div class="in"><div class="reality">
<div><p class="kick">{t('The reality', 'La réalité', 'Ukweli', 'A realidade')}</p>
<h2>{t('Africa develops the talent. <em>Evidence</em> decides who gets paid.', 'L’Afrique forme les talents. Les <em>preuves</em> décident qui est payé.', 'Afrika inakuza vipaji. <em>Ushahidi</em> unaamua nani analipwa.', 'A África forma o talento. As <em>evidências</em> decidem quem recebe.')}</h2>
{tp('Every weekend, players across Africa perform in front of no scouts, no cameras and no data. When one of them moves abroad, FIFA pays training rewards to every club that developed him from age 12. But only if that club can prove it: registration, player passport, match video, numbers. No records, no money.', 'Chaque week-end, des joueurs partout en Afrique jouent sans recruteurs, sans caméras et sans données. Quand l’un d’eux part à l’étranger, la FIFA verse des indemnités de formation à chaque club qui l’a formé dès 12 ans. À condition de le prouver : enregistrement, passeport du joueur, vidéo, chiffres. Pas de dossier, pas d’argent.', 'Kila wikendi, wachezaji kote Afrika wanacheza bila maskauti, bila kamera na bila data. Mmoja wao anapohamia nje, FIFA inalipa fidia ya mafunzo kwa kila klabu iliyomkuza tangu miaka 12. Lakini tu kama klabu inaweza kuthibitisha: usajili, pasipoti ya mchezaji, video ya mechi, takwimu. Hakuna kumbukumbu, hakuna pesa.', 'Todo fim de semana, jogadores de toda a África jogam sem olheiros, sem câmeras e sem dados. Quando um deles vai para o exterior, a FIFA paga compensações de formação a cada clube que o formou desde os 12 anos. Mas só se o clube provar: registro, passaporte do jogador, vídeo, números. Sem registros, sem dinheiro.')}
<p class="src">{t('Source: FIFA Clearing House media release, July 2026', 'Source : communiqué FIFA Clearing House, juillet 2026', 'Chanzo: taarifa ya FIFA Clearing House, Julai 2026', 'Fonte: comunicado da FIFA Clearing House, julho de 2026')}</p></div>
<div><div class="big">$1<small>BN</small></div>
{tp('in training rewards generated through FIFA’s Clearing House since November 2022, with USD 639 million already paid to clubs that could prove their part.', 'd’indemnités de formation générées par la Clearing House de la FIFA depuis novembre 2022, dont 639 millions USD déjà versés aux clubs qui ont pu prouver leur rôle.', 'za fidia ya mafunzo zimezalishwa kupitia Clearing House ya FIFA tangu Novemba 2022, na dola milioni 639 tayari zimelipwa kwa klabu zilizothibitisha mchango wao.', 'em compensações de formação geradas pela Clearing House da FIFA desde novembro de 2022, com USD 639 milhões já pagos aos clubes que provaram sua parte.')}
<div class="sline"><div><b>639M</b>{t('USD paid out so far', 'USD déjà versés', 'USD zimelipwa hadi sasa', 'USD já pagos')}</div><div><b>12–23</b>{t('the ages a club is paid for', 'les âges pour lesquels un club est payé', 'umri ambao klabu inalipwa', 'as idades pelas quais o clube recebe')}</div></div></div>
</div>
{ctl(('Is your club owed money for a player it developed?', 'Votre club a-t-il droit à de l’argent pour un joueur formé chez lui ?', 'Je, klabu yako inadai pesa kwa mchezaji iliyemkuza?', 'Seu clube tem dinheiro a receber por um jogador que formou?'), ('Check your training rewards', 'Vérifiez vos indemnités', 'Kagua fidia yako ya mafunzo', 'Verifique suas compensações'), 'club', topic('Training rewards check','Vérification des indemnités de formation','Ukaguzi wa fidia ya mafunzo','Verificação de compensações de formação'))}
</div></section>'''

nums = f'''<section class="sx"><div class="in">
<p class="kick">{t('The scoreboard', 'Le tableau d’affichage', 'Ubao wa matokeo', 'O placar')}</p>
<div class="nums rv">
<div class="num"><b data-count="120">120</b><span>{t('countries where our podcast is heard', 'pays où notre podcast est écouté', 'nchi ambako podikasti yetu inasikilizwa', 'países onde nosso podcast é ouvido')}</span></div>
<div class="num"><b><span data-count="5">5</span>K<small>+</small></b><span>{t('streams and downloads, March 2026', 'écoutes et téléchargements, mars 2026', 'usikilizaji na upakuaji, Machi 2026', 'reproduções e downloads, março de 2026')}</span></div>
<div class="num"><b data-count="10">10</b><span>{t('African nations followed at the U-17 World Cup', 'nations africaines suivies à la Coupe du monde U-17', 'mataifa ya Afrika tunayofuatilia Kombe la Dunia U-17', 'seleções africanas acompanhadas na Copa Sub-17')}</span></div>
<div class="num"><b data-count="4">4</b><span>{t('languages on every page and every form', 'langues sur chaque page et chaque formulaire', 'lugha kwenye kila ukurasa na kila fomu', 'idiomas em cada página e cada formulário')}</span></div>
<div class="num"><b data-count="3">3</b><span>{t('live desks you can open today', 'desks en ligne à ouvrir aujourd’hui', 'madawati yaliyo hewani unayoweza kufungua leo', 'mesas no ar para abrir hoje')}</span></div>
</div>
<div class="partners rv"><span>{t('Working with', 'Avec', 'Tunafanya kazi na', 'Trabalhando com')}</span><strong>FootLab</strong><strong>INSAIT JOY</strong><strong>Soccerbee</strong></div>
</div></section>'''

news = re.search(r'<section data-news="home" hidden>.*?</section>', src, re.S).group(0)
news = f'<div class="wrap" style="padding-bottom:0">{news}</div>'

def wk(cls, href, frame, label, live_, h, p):
    ext = ' target="_blank" rel="noopener"' if href.startswith('http') else ''
    return f'<a class="wk rv {cls}" href="{href}"{ext}><div class="frame {frame[0]}"><span class="lbl{"" if live_ else " s"}"><i></i>{label}</span>{frame[1]}</div><h3>{h}{arrow}</h3><p>{p}</p></a>'

def mini(v, poster, alt):
    return f'<div class="mini"><div class="screen"><video data-src="{v}" poster="{poster}" muted loop playsinline preload="none" aria-label="{alt}"></video></div></div>'

LIVE = t('Live', 'En ligne', 'Hewani', 'No ar')
FLIP_BUL = {
 'miq': [('Goals and key moments, clip by clip','Buts et moments clés, séquence par séquence','Mabao na matukio muhimu, kipande kwa kipande','Gols e lances-chave, clipe a clipe'),('Player radars for both squads','Radars des joueuses des deux effectifs','Rada za wachezaji wa vikosi vyote','Radares das jogadoras dos dois elencos'),('Opens on any phone, offline','S’ouvre sur tout téléphone, hors ligne','Inafunguka kwenye simu yoyote, bila mtandao','Abre em qualquer celular, offline')],
 'dossier': [('Ratings, strengths, video evidence','Notes, points forts, preuves vidéo','Alama, uwezo, ushahidi wa video','Avaliações, pontos fortes, vídeo'),('Compared with players in the same position','Comparé aux joueurs du même poste','Ikilinganishwa na wa nafasi hiyo','Comparado com a mesma posição'),('Eleven checks before any verdict','Onze vérifications avant tout avis','Ukaguzi 11 kabla ya uamuzi','Onze verificações antes do veredito')],
 'desk': [('Every African squad, every match','Chaque sélection africaine, chaque match','Kila timu ya Afrika, kila mechi','Cada seleção africana, cada jogo'),('Players to watch, scored the same way','Joueurs à suivre, notés de la même façon','Wachezaji wa kufuatilia, kwa alama sawa','Jogadores a acompanhar, avaliados igual'),('Commission one for your competition','Commandez-en un pour votre compétition','Agiza moja kwa mashindano yako','Encomende uma para sua competição')],
 'cv': [('A short form on your phone','Un court formulaire sur téléphone','Fomu fupi kwenye simu','Um formulário curto no celular'),('Reviewed before anything is shared','Relu avant tout partage','Inapitiwa kabla ya kushirikishwa','Revisado antes de compartilhar'),('Four languages, four desks','Quatre langues, quatre desks','Lugha nne, madawati manne','Quatro idiomas, quatro mesas')],
 'insait': [('Sensor in each shin guard','Un capteur dans chaque protège-tibia','Kihisi ndani ya kila kilinda-muundi','Sensor em cada caneleira'),('Distance, sprints, kicks, foot use','Distance, sprints, frappes, pied utilisé','Umbali, mbio, mateke, mguu unaotumika','Distância, sprints, chutes, pé usado'),('Set up at your ground, staff trained','Installé chez vous, staff formé','Tunasimika uwanjani, tunafunza wafanyakazi','Instalado no seu campo, equipe treinada')],
 'soccerbee': [('GPS pod in a light vest','Boîtier GPS dans un gilet léger','Kifaa cha GPS ndani ya fulana nyepesi','Sensor GPS em colete leve'),('Benchmarked against peers','Comparé aux pairs','Ikilinganishwa na wenzao','Comparado com os pares'),('Built for youth and academy squads','Conçu pour les jeunes et les académies','Kwa vikosi vya vijana na akademia','Feito para base e academias')]}
FLIP_CTA = {'miq':(('Get your match read','Faites lire votre match','Chambuliwa mechi yako','Analise sua partida'),'club'),'dossier':(('Ask about a player','Demander pour un joueur','Uliza kuhusu mchezaji','Pergunte sobre um jogador'),'agent'),'desk':(('Commission a desk','Commander un desk','Agiza dawati','Encomende uma mesa'),'federation'),'cv':(('Start your CV','Commencer votre CV','Anza CV yako','Comece seu currículo'),'player'),'insait':(('Get a kit quote','Demander un devis','Pata bei ya vifaa','Peça um orçamento'),'club'),'soccerbee':(('Get a kit quote','Demander un devis','Pata bei ya vifaa','Peça um orçamento'),'club')}
def flip(n, x):
    ext = ' target="_blank" rel="noopener"' if x['href'].startswith('http') else ''
    bl = ''.join('<li>' + t(*b) + '</li>' for b in FLIP_BUL[x['k']])
    c = FLIP_CTA[x['k']]
    return f'''<div class="fc rv" tabindex="0"><div class="fc-in"><div class="fc-f"><div class="fc-img"><img src="{x['d']}" alt="" loading="lazy" width="1400" height="875"><div class="fc-ph"><img src="{x['m']}" alt="" loading="lazy" width="560" height="1212"></div></div><div class="fc-cap"><span class="lbl"><i></i>{t(*x['lab'])}</span><h3>{t(*x['h'])}</h3><span class="fc-hint">{t('Hover to flip', 'Survolez pour retourner', 'Gusa kugeuza', 'Passe o mouse para virar')} ↻</span></div></div>
<div class="fc-b"><span class="fc-n">0{n+1}</span><h3>{t(*x['h'])}</h3>{t(*x['p'], tag='p')}<ul>{bl}</ul><div class="acts"><button type="button" class="btn go1 sm" data-pick="{c[1]}" data-topic='{topic(*x['h'])}'>{t(*c[0])}</button><a class="btn ghost sm" href="{x['href']}"{ext}>{t('See it live', 'Voir en ligne', 'Ona hewani', 'Ver ao vivo')}</a></div></div></div></div>'''

work = f'''<section class="sx band-mint" id="work"><div class="in">
<div class="shead"><div><p class="kick">{t('Selected work', 'Travaux choisis', 'Kazi teule', 'Trabalhos selecionados')}</p><h2>{t('Work you can <em>open</em> today.', 'Du travail à <em>ouvrir</em> aujourd’hui.', 'Kazi unayoweza <em>kufungua</em> leo.', 'Trabalho para <em>abrir</em> hoje.')}</h2></div>
{tp('Every piece below is live and public. No mock-ups, no stock photos: the same reports, desks and CVs our clients receive.', 'Tout ce qui suit est en ligne et public. Pas de maquettes, pas de photos de banque d’images : les mêmes rapports, desks et CV que reçoivent nos clients.', 'Kila kazi hapa chini iko hewani na wazi kwa umma. Hakuna picha za kuigiza: ni ripoti, madawati na CV zile zile wanazopokea wateja wetu.', 'Tudo abaixo está no ar e é público. Sem maquetes, sem fotos de banco: os mesmos relatórios, mesas e currículos que nossos clientes recebem.')}</div>
<div class="flips">{"".join(flip(n,x) for n,x in enumerate([p for p in PROJ if p["k"]!="analysis"]))}</div>
{ctl(('Want your club’s next match to look like this?', 'Vous voulez que votre prochain match ressemble à ça ?', 'Ungependa mechi ijayo ya klabu yako ionekane hivi?', 'Quer que a próxima partida do seu clube fique assim?'), ('Send us your next match', 'Envoyez-nous votre prochain match', 'Tutumie mechi yako ijayo', 'Envie sua próxima partida'), 'club', topic('Match report','Rapport de match','Ripoti ya mechi','Relatório de partida'))}
</div></section>'''

svc_items = [
 ('Match analysis & MatchIQ','Analyse de match & MatchIQ','Uchambuzi wa mechi na MatchIQ','Análise de partidas e MatchIQ','advisory/#analytics',
  ('Know what happened, and what to do on Monday.','Savoir ce qui s’est passé, et quoi faire lundi.','Jua kilichotokea, na la kufanya Jumatatu.','Saiba o que aconteceu e o que fazer na segunda-feira.'),
  [('Pre-match briefs and post-match reports','Briefings d’avant-match et rapports d’après-match','Muhtasari kabla ya mechi na ripoti baada ya mechi','Briefings pré-jogo e relatórios pós-jogo'),('Interactive dashboards that open with no signal','Tableaux de bord qui s’ouvrent sans réseau','Dashibodi zinazofunguka bila mtandao','Painéis que abrem sem sinal'),('Video tagging: every pass, shot and duel logged in Nairobi','Annotation vidéo : chaque passe, tir et duel relevé à Nairobi','Kuwekea video alama: kila pasi, shuti na pambano, Nairobi','Marcação de vídeo: cada passe, finalização e duelo, em Nairóbi')]),
 ('Scouting dossiers','Dossiers de recrutement','Ripoti za uskauti','Dossiês de scouting','advisory/#scouting',
  ('One player, one file, one clear verdict.','Un joueur, un dossier, un avis clair.','Mchezaji mmoja, faili moja, uamuzi mmoja wa wazi.','Um jogador, um arquivo, uma recomendação clara.'),
  [('Ratings, strengths and video evidence','Notes, points forts et preuves vidéo','Alama, uwezo na ushahidi wa video','Avaliações, pontos fortes e evidências em vídeo'),('Compared with players in the same position','Comparé aux joueurs du même poste','Ikilinganishwa na wachezaji wa nafasi hiyo','Comparado com jogadores da mesma posição'),('Eleven checks before a recruitment decision','Onze vérifications avant une décision','Ukaguzi kumi na moja kabla ya uamuzi','Onze verificações antes de uma decisão')]),
 ('CV Desk','Bureau CV','Dawati la CV','Mesa de Currículos','advisory/#cv',
  ('Be found by the clubs that matter.','Être trouvé par les clubs qui comptent.','Onekana na klabu zinazohusika.','Seja encontrado pelos clubes que importam.'),
  [('Players, coaches, scouts and analysts','Joueurs, entraîneurs, recruteurs et analystes','Wachezaji, makocha, maskauti na wachambuzi','Jogadores, treinadores, olheiros e analistas'),('A short form on your phone, in four languages','Un court formulaire sur téléphone, en quatre langues','Fomu fupi kwenye simu, kwa lugha nne','Um formulário curto no celular, em quatro idiomas'),('Parents fill in the form for players under 18','Les parents remplissent pour les moins de 18 ans','Wazazi wanajaza fomu kwa walio chini ya miaka 18','Os pais preenchem para menores de 18 anos')]),
 ('Player tracking','Suivi des joueurs','Ufuatiliaji wa wachezaji','Monitoramento de jogadores','technology/',
  ('See how far and how fast your players really run.','Voir jusqu’où et à quelle vitesse vos joueurs courent vraiment.','Ona umbali na kasi halisi ya wachezaji wako.','Veja quanto e quão rápido seus jogadores realmente correm.'),
  [('INSAIT JOY smart shin guards','Protège-tibias connectés INSAIT JOY','Vilinda-muundi janja vya INSAIT JOY','Caneleiras inteligentes INSAIT JOY'),('Soccerbee GPS vests, benchmarked against peers','Gilets GPS Soccerbee, comparés aux pairs','Fulana za GPS za Soccerbee, zikilinganishwa na wenzao','Coletes GPS Soccerbee, comparados com pares'),('Chosen with you, set up at your ground, staff trained','Choisis avec vous, installés chez vous, staff formé','Tunachagua nawe, tunasimika uwanjani, tunafunza wafanyakazi','Escolhidos com você, instalados no seu campo, equipe treinada')]),
 ('Contracts, registration & transfers','Contrats, enregistrement & transferts','Mikataba, usajili na uhamisho','Contratos, registro e transferências','advisory/#legal',
  ('Get paid for the players you develop.','Être payé pour les joueurs que vous formez.','Lipwa kwa wachezaji unaowakuza.','Seja pago pelos jogadores que você forma.'),
  [('Guidance from our sports lawyer','Les conseils de notre avocat du sport','Ushauri kutoka kwa mwanasheria wetu wa michezo','Orientação do nosso advogado esportivo'),('Player contracts and registration','Contrats et enregistrement des joueurs','Mikataba na usajili wa wachezaji','Contratos e registro de jogadores'),('Claiming FIFA training rewards','Réclamer les indemnités de formation FIFA','Kudai fidia ya mafunzo ya FIFA','Receber as compensações de formação da FIFA')]),
 ('Workshops & webinars','Ateliers & webinaires','Warsha na semina','Workshops e webinars','advisory/#education',
  ('Your staff, reading the numbers themselves.','Votre staff, qui lit les chiffres lui-même.','Wafanyakazi wako, wakisoma takwimu wenyewe.','Sua equipe lendo os números por conta própria.'),
  [('Free webinars for coaches, analysts and scouts','Webinaires gratuits pour entraîneurs, analystes et recruteurs','Semina za bure kwa makocha, wachambuzi na maskauti','Webinars gratuitos para treinadores, analistas e olheiros'),('Hands-on tagging and coding with FootLab','Annotation et codage pratiques avec FootLab','Mafunzo ya vitendo ya kuwekea alama pamoja na FootLab','Marcação e codificação na prática com a FootLab'),('Men’s and women’s game, across sub-Saharan Africa','Football masculin et féminin, en Afrique subsaharienne','Soka la wanaume na wanawake, Afrika kusini mwa Sahara','Futebol masculino e feminino, na África subsaariana')]),
 ('Tournament Desk','Desk Tournoi','Dawati la Mashindano','Mesa do Torneio','innovation/#desk',
  ('Your competition, covered like a World Cup.','Votre compétition, couverte comme une Coupe du monde.','Mashindano yako, yakifuatiliwa kama Kombe la Dunia.','Sua competição, coberta como uma Copa do Mundo.'),
  [('Every squad, every match, players scored','Chaque effectif, chaque match, joueurs notés','Kila kikosi, kila mechi, wachezaji wakipewa alama','Cada elenco, cada jogo, jogadores avaliados'),('Commission a desk at any level','Commandez un desk à tout niveau','Agiza dawati kwa kiwango chochote','Encomende uma mesa em qualquer nível'),('Live now for the FIFA U-17 World Cup','En direct pour la Coupe du monde U-17','Hewani sasa kwa Kombe la Dunia U-17','No ar agora para a Copa Sub-17')]),
]
svc_cta = [
 (('Book a match read','Réserver une analyse de match','Agiza uchambuzi wa mechi','Agendar uma análise'),'club'),
 (('Ask about a player','Demander pour un joueur','Uliza kuhusu mchezaji','Pergunte sobre um jogador'),'agent'),
 (('Start your CV','Commencer votre CV','Anza CV yako','Comece seu currículo'),'player'),
 (('Get a kit quote','Demander un devis matériel','Pata bei ya vifaa','Peça um orçamento'),'club'),
 (('Check your training rewards','Vérifier vos indemnités','Kagua fidia yako','Verifique suas compensações'),'club'),
 (('Join the next workshop','Rejoindre le prochain atelier','Jiunge na warsha ijayo','Participe do próximo workshop'),'coach'),
 (('Commission a desk','Commander un desk','Agiza dawati','Encomende uma mesa'),'federation')]
det = ''
for i, s in enumerate(svc_items, 1):
    lis = ''.join('<li>' + t(*b) + '</li>' for b in s[6])
    det += f'''<details{" open" if i == 1 else ""}><summary><span class="n">0{i}</span><span class="sn">{t(*s[:4])}</span><span class="pl" aria-hidden="true"></span></summary><div class="body"><div>{tp(*s[5])}<div class="acts"><button type="button" class="btn go1 sm" data-pick="{svc_cta[i-1][1]}" data-topic='{topic(*s[:4])}'>{t(*svc_cta[i-1][0])} {arrow}</button><a class="btn ghost sm" href="{s[4]}">{t('Read more', 'En savoir plus', 'Soma zaidi', 'Saiba mais')}</a></div></div><ul>{lis}</ul></div></details>'''
services = f'''<section class="sx deep" id="services"><div class="in">
<div class="shead"><div><p class="kick">{t('What we do', 'Ce que nous faisons', 'Tunachofanya', 'O que fazemos')}</p><h2>{t('Seven ways we <em>help</em> you win.', 'Sept façons de vous <em>aider</em> à gagner.', 'Njia saba za <em>kukusaidia</em> kushinda.', 'Sete formas de <em>ajudar</em> você a vencer.')}</h2></div>
{tp('Evidence for every football decision, from the first scouting trip to the transfer paperwork.', 'Des preuves pour chaque décision football, du premier déplacement de recrutement aux papiers du transfert.', 'Ushahidi kwa kila uamuzi wa soka, kuanzia safari ya kwanza ya uskauti hadi nyaraka za uhamisho.', 'Evidências para cada decisão no futebol, da primeira viagem de scouting à papelada da transferência.')}</div>
<div class="svc">{det}</div></div></section>'''

def mv(no, tag, price, h, items, btn, fine, feat=False, pick=None, href=None):
    lis = ''.join('<li>' + t(*x) + '</li>' for x in items)
    b = f'<button type="button" class="btn {"go1" if feat else "ghost"}" data-pick="{pick or ""}" data-topic=\'{btn[1]}\'>{t(*btn[0])} {arrow}</button>' if href is None else f'<a class="btn {"go1" if feat else "ghost"}" href="{href}">{t(*btn[0])} {arrow}</a>'
    return f'<div class="mv rv{" feat" if feat else ""}"><div class="no"><span>{no}</span><span>{t(*tag)}</span></div><div class="price">{t(*price)}</div><h3>{t(*h)}</h3><ul>{lis}</ul>{b}<p class="fine">{t(*fine)}</p></div>'

moves = f'''<section class="sx dark" id="first-move"><div class="in">
<div class="shead"><div><p class="kick">{t('Three ways to start', 'Trois façons de commencer', 'Njia tatu za kuanza', 'Três formas de começar')}</p><h2>{t('Pick your first <em>move.</em>', 'Votre premier <em>pas.</em>', 'Chagua hatua ya <em>kwanza.</em>', 'Escolha o primeiro <em>passo.</em>')}</h2></div>
{tp('All three are low risk. See our work on your own match first, learn with us for free, or put one player under the microscope.', 'Les trois sont sans risque. Voyez notre travail sur votre propre match, apprenez gratuitement avec nous, ou passez un joueur au microscope.', 'Zote tatu hazina hatari. Ona kazi yetu kwenye mechi yako kwanza, jifunze nasi bure, au mchunguze mchezaji mmoja kwa kina.', 'As três têm baixo risco. Veja nosso trabalho na sua própria partida, aprenda com a gente de graça ou coloque um jogador no microscópio.')}</div>
<div class="moves">
{mv('01', ('Clubs · academies','Clubs · académies','Klabu · akademia','Clubes · academias'), ('Free','Gratuit','Bure','Grátis'), ('Your match, read','Votre match, analysé','Mechi yako, imechambuliwa','Sua partida, analisada'),
    [('Send us the video of one of your matches','Envoyez-nous la vidéo d’un de vos matchs','Tutumie video ya mechi yako moja','Envie o vídeo de uma das suas partidas'),('We send back a MatchIQ preview: key moments and three players to watch','Nous renvoyons un aperçu MatchIQ : moments clés et trois joueurs à suivre','Tunakurudishia muhtasari wa MatchIQ: matukio muhimu na wachezaji watatu wa kufuatilia','Devolvemos uma prévia MatchIQ: lances decisivos e três jogadores para acompanhar'),('Opens on any phone, no app, no signal needed','S’ouvre sur tout téléphone, sans appli ni réseau','Inafunguka kwenye simu yoyote, bila programu wala mtandao','Abre em qualquer celular, sem app e sem sinal')],
    (('Send us a match','Envoyez un match','Tutumie mechi','Envie uma partida'), topic('Free match read','Lecture de match gratuite','Uchambuzi wa mechi bure','Leitura de partida grátis')),
    ('One per club · within 5 working days','Une par club · sous 5 jours ouvrés','Moja kwa kila klabu · ndani ya siku 5 za kazi','Uma por clube · em até 5 dias úteis'), feat=True, pick='club')}
{mv('02', ('Coaches · analysts · scouts','Entraîneurs · analystes · recruteurs','Makocha · wachambuzi · maskauti','Treinadores · analistas · olheiros'), ('Free','Gratuit','Bure','Grátis'), ('Learn it with us','Apprenez avec nous','Jifunze nasi','Aprenda com a gente'),
    [('Live webinars with FootLab (Morocco)','Webinaires en direct avec FootLab (Maroc)','Semina za moja kwa moja na FootLab (Morocco)','Webinars ao vivo com a FootLab (Marrocos)'),('Real African matches tagged in front of you','De vrais matchs africains annotés devant vous','Mechi halisi za Afrika zikiwekewa alama mbele yako','Partidas africanas reais marcadas na sua frente'),('Recordings of past sessions','Les enregistrements des sessions passées','Rekodi za vipindi vilivyopita','Gravações das sessões anteriores')],
    (('See the workshops','Voir les ateliers','Ona warsha','Ver os workshops'),''), ('Open link · no sign-up','Lien ouvert · sans inscription','Kiungo wazi · bila kujisajili','Link aberto · sem cadastro'), href='advisory/#education')}
{mv('03', ('Clubs · agents','Clubs · agents','Klabu · mawakala','Clubes · agentes'), ('1 player','1 joueur','Mchezaji 1','1 jogador'), ('One scouting dossier','Un dossier de recrutement','Ripoti moja ya uskauti','Um dossiê de scouting'),
    [('Ratings, strengths and video evidence','Notes, points forts et preuves vidéo','Alama, uwezo na ushahidi wa video','Avaliações, pontos fortes e evidências em vídeo'),('Eleven checks: pathway, records, fit, verification','Onze vérifications : parcours, dossiers, adéquation, vérification','Ukaguzi 11: njia, kumbukumbu, ufanisi, uthibitisho','Onze verificações: trajetória, registros, encaixe, verificação'),('A clear verdict you can act on','Un avis clair sur lequel agir','Uamuzi wa wazi unaoweza kuufanyia kazi','Uma recomendação clara para agir')],
    (('Ask about a player','Demander pour un joueur','Uliza kuhusu mchezaji','Pergunte sobre um jogador'), topic('Scouting dossier','Dossier de recrutement','Ripoti ya uskauti','Dossiê de scouting')),
    ('Credited in full to a season package booked within 30 days','Déduit en totalité d’un forfait saison réservé sous 30 jours','Inahesabiwa kikamilifu kwenye kifurushi cha msimu ndani ya siku 30','Abatido integralmente de um pacote de temporada fechado em 30 dias'), pick='agent')}
</div></div></section>'''

aud = [('Clubs and academies','Clubs et académies','Klabu na akademia','Clubes e academias','Find players and staff, read your matches, track your squad.','Trouvez joueurs et staff, analysez vos matchs, suivez votre effectif.','Pata wachezaji na wafanyakazi, chambua mechi zako, fuatilia kikosi chako.','Encontre jogadores e comissão técnica, entenda suas partidas, monitore seu elenco.','advisory/','club'),
 ('Players, coaches, scouts','Joueurs, entraîneurs, recruteurs','Wachezaji, makocha, maskauti','Jogadores, treinadores, olheiros','Get a football CV built to our standard so clubs can find you.','Obtenez un CV football à notre standard pour que les clubs vous trouvent.','Pata CV ya soka iliyoandaliwa kwa kiwango chetu ili klabu zikupate.','Tenha um currículo de futebol no nosso padrão para os clubes encontrarem você.','advisory/#cv','coach'),
 ('Parents and schools','Parents et écoles','Wazazi na shule','Pais e escolas','Player records, CVs and tracking for young players and student teams.','Dossiers, CV et suivi pour les jeunes joueurs et les équipes scolaires.','Kumbukumbu, CV na ufuatiliaji kwa wachezaji vijana na timu za wanafunzi.','Históricos, currículos e monitoramento para jovens jogadores e equipes estudantis.','advisory/#cv','parent'),
 ('Agents','Agents','Mawakala','Agentes','Scouting dossiers and match reports that help you place a player.','Dossiers de recrutement et rapports de match pour placer un joueur.','Ripoti za uskauti na za mechi zinazokusaidia kumpatia mchezaji klabu.','Dossiês de scouting e relatórios de partida que ajudam a colocar um jogador.','advisory/#scouting','agent'),
 ('Federations and leagues','Fédérations et ligues','Mashirikisho na ligi','Federações e ligas','Match intelligence, match data and technology for teams and competitions.','Analyse, données de match et technologie pour sélections et compétitions.','Uchambuzi, data za mechi na teknolojia kwa timu na mashindano.','Inteligência de jogo, dados e tecnologia para equipes e competições.',DESK + 'commission/','federation'),
 ('Tech buyers','Acheteurs de technologie','Wanunuzi wa teknolojia','Compradores de tecnologia','Smart shin guards and GPS vests, chosen with you and set up.','Protège-tibias connectés et gilets GPS, choisis avec vous et installés.','Vilinda-muundi janja na fulana za GPS, tunavichagua pamoja nawe na kuvisimika.','Caneleiras inteligentes e coletes GPS, escolhidos com você e instalados.','technology/','club')]
aud_cta = [('Talk to our club desk','Parler à notre desk clubs','Ongea na dawati la klabu','Fale com nosso time de clubes'),('Start my CV','Créer mon CV','Anza CV yangu','Criar meu currículo'),('Ask about my child’s record','Demander pour le dossier de mon enfant','Uliza kuhusu kumbukumbu za mtoto wangu','Pergunte sobre o histórico do meu filho'),('Request a dossier','Demander un dossier','Omba ripoti ya uskauti','Peça um dossiê'),('Commission a desk','Commander un desk','Agiza dawati','Encomende uma mesa'),('Get a kit quote','Demander un devis','Pata bei ya vifaa','Peça um orçamento')]
rows = ''
for i, a in enumerate(aud, 1):
    ext = ' target="_blank" rel="noopener"' if a[8].startswith('http') else ''
    rows += f'''<div class="au rv"><span class="n">0{i}</span><h3>{t(*[f'<span class="hl">{x}</span>' for x in a[:4]])}</h3>{tp(*a[4:8])}<div class="row"><a class="btn ghost sm" href="{a[8]}"{ext}>{t('What we offer','Notre offre','Tunachotoa','O que oferecemos')}</a><button type="button" class="btn go1 sm" data-pick="{a[9]}">{t(*aud_cta[i-1])}</button></div></div>'''
audiences = f'''<section class="sx" id="who"><div class="in">
<div class="shead"><div><p class="kick">{t('Who we help', 'Pour qui', 'Tunaowasaidia', 'Quem ajudamos')}</p><h2>{t('Who are <em>you?</em>', 'Qui êtes-<em>vous ?</em>', 'Wewe ni <em>nani?</em>', 'Quem é <em>você?</em>')}</h2></div>
{tp('Tell us who you are and the right person at Afritech Sports replies, on WhatsApp or by email.', 'Dites-nous qui vous êtes et la bonne personne chez Afritech Sports vous répond, sur WhatsApp ou par e-mail.', 'Tuambie wewe ni nani na mtu sahihi wa Afritech Sports atakujibu, kwa WhatsApp au barua pepe.', 'Conte quem você é e a pessoa certa da Afritech Sports responde, no WhatsApp ou por e-mail.')}</div>
<div class="aud">{rows}</div></div></section>'''

chk = [('ST','Club'),('LW','Agent'),('RW','Federation'),('LCM','Functional role'),('RCM','Game-model fit'),('CM','Pathway'),('LB','Live scouting'),('RB','Player records'),('LCB','Full-match video'),('RCB','EPTS data'),('GK','Verification')]
method = f'''<section class="sx ink" id="method"><div class="in"><div class="meth">
<a class="poster rv" href="assets/media/beyond-the-scoreboard.jpg" target="_blank" rel="noopener"><img src="assets/media/beyond-the-scoreboard.jpg" alt="Afritech scouting method: Beyond the Scoreboard, 11 checks before a recruitment decision, laid out as a 4-3-3" loading="lazy" width="1080" height="1350"></a>
<div><p class="kick" style="color:var(--lime)">{t('Our scouting method', 'Notre méthode', 'Mbinu yetu ya uskauti', 'Nosso método')}</p>
<h2>{t('Beyond the <em>scoreboard.</em>', 'Au-delà du <em>score.</em>', 'Zaidi ya <em>matokeo.</em>', 'Além do <em>placar.</em>')}</h2>
{tp('A strong performance tells you something. It does not tell you everything. Before we recommend a player, we run eleven checks, lined up like a team.', 'Une belle performance dit quelque chose. Elle ne dit pas tout. Avant de recommander un joueur, nous faisons onze vérifications, alignées comme une équipe.', 'Mchezo mzuri unakueleza kitu. Haukuelezi kila kitu. Kabla ya kupendekeza mchezaji, tunafanya ukaguzi kumi na moja, uliopangwa kama timu.', 'Uma grande atuação diz alguma coisa. Não diz tudo. Antes de recomendar um jogador, fazemos onze verificações, escaladas como um time.')}
<div class="checks">{''.join(f'<div><i>{p}</i>{n}</div>' for p, n in chk)}</div>
{ctl(('Got a player you’re unsure about?', 'Un joueur vous fait hésiter ?', 'Una mchezaji unayemtilia shaka?', 'Tem um jogador que gera dúvida?'), ('Run the 11 checks', 'Lancer les 11 vérifications', 'Mfanyie ukaguzi 11', 'Faça as 11 verificações'), 'agent', topic('Scouting dossier','Dossier de recrutement','Ripoti ya uskauti','Dossiê de scouting'))}
</div></div></div></section>'''

listen = f'''<section class="sx band-mint" id="listen"><div class="in"><div class="listen">
<div class="cover rv"><img src="assets/img/podcast.jpg" alt="Deep Dive Into Soccer podcast: 5,000 streams and downloads" loading="lazy"><div class="eq" aria-hidden="true"><i></i><i></i><i></i><i></i></div></div>
<div><p class="kick">{t('Listen', 'Écouter', 'Sikiliza', 'Ouça')}</p>
<h2>{t('Deep Dive Into <em>Soccer.</em>', 'Deep Dive Into <em>Soccer.</em>', 'Deep Dive Into <em>Soccer.</em>', 'Deep Dive Into <em>Soccer.</em>')}</h2>
{tp('Our podcast takes African football apart, in your language: a separate episode in English, French, Swahili and Portuguese.', 'Notre podcast décortique le football africain dans votre langue : un épisode distinct en anglais, français, swahili et portugais.', 'Podikasti yetu inachambua soka la Afrika kwa lugha yako: kipindi tofauti kwa Kiingereza, Kifaransa, Kiswahili na Kireno.', 'Nosso podcast destrincha o futebol africano no seu idioma: um episódio próprio em inglês, francês, suaíli e português.')}
<div class="player" data-player><div class="pb"><button class="playb" type="button" aria-label="Play the latest episode"><svg viewBox="0 0 14 16"><path d="M0 0l14 8-14 8z"/></svg></button><div class="ep"><small>{t('Latest episode', 'Dernier épisode', 'Kipindi kipya', 'Último episódio')}</small><span data-ep></span></div></div></div>
<div class="pods"><a href="innovation/#podcast">{t('All episodes', 'Tous les épisodes', 'Vipindi vyote', 'Todos os episódios')} →</a></div>
{ctl(('Have a story African football needs to hear?', 'Une histoire que le football africain doit entendre ?', 'Una hadithi ambayo soka la Afrika linahitaji kusikia?', 'Tem uma história que o futebol africano precisa ouvir?'), ('Pitch us an episode', 'Proposez-nous un épisode', 'Tupendekezee kipindi', 'Sugira um episódio'), 'media', topic('Podcast','Podcast','Podikasti','Podcast'), ghost=True)}
</div></div></div></section>'''

founder = f'''<section class="sx" id="about" style="padding-top:0"><div class="in"><div class="half" style="margin:0 0 clamp(64px,9vw,120px)"></div><div class="fd solo">
<div><p class="kick">{t('Why Afritech', 'Pourquoi Afritech', 'Kwa nini Afritech', 'Por que a Afritech')}</p>
<blockquote>{t('Africa doesn’t have a talent problem. It has an evidence problem. Our players are seen by too few scouts, measured by too little data, and the clubs that raise them too often can’t prove it when the money moves. We build the video, the numbers and the records that change that.', 'L’Afrique n’a pas un problème de talent. Elle a un problème de preuves. Nos joueurs sont vus par trop peu de recruteurs, mesurés par trop peu de données, et les clubs qui les forment peinent trop souvent à le prouver quand l’argent circule. Nous produisons la vidéo, les chiffres et les dossiers qui changent cela.', 'Afrika haina tatizo la vipaji. Ina tatizo la ushahidi. Wachezaji wetu wanaonekana na maskauti wachache mno, wanapimwa kwa data kidogo mno, na klabu zinazowakuza mara nyingi hazina njia ya kuthibitisha pesa zinapohama. Tunatengeneza video, takwimu na kumbukumbu zinazobadilisha hilo.', 'A África não tem um problema de talento. Tem um problema de evidências. Nossos jogadores são vistos por poucos olheiros, medidos por poucos dados, e os clubes que os formam muitas vezes não conseguem provar isso quando o dinheiro circula. Nós produzimos o vídeo, os números e os registros que mudam isso.')}</blockquote>
<div class="sig"><div><b>Andrew Rukidi</b><span>{t('Founder · Football intelligence & sports technology', 'Fondateur · Intelligence football & technologie sportive', 'Mwanzilishi · Ujasusi wa soka na teknolojia ya michezo', 'Fundador · Inteligência de futebol e tecnologia esportiva')}</span></div></div>
{ctl(('Want to talk it through with us directly?', 'Vous voulez en parler directement avec nous ?', 'Ungependa kuzungumza nasi moja kwa moja?', 'Quer conversar diretamente com a gente?'), ('Message Afritech Sports on WhatsApp', 'Écrire à Afritech Sports sur WhatsApp', 'Tumia Afritech Sports ujumbe WhatsApp', 'Fale com a Afritech Sports no WhatsApp'), '')}
<div class="facts"><div><b>NBO</b><span>{t('Based in Nairobi, on the ground in Kenya', 'Basés à Nairobi, sur le terrain au Kenya', 'Tuko Nairobi, uwanjani Kenya', 'Em Nairóbi, presentes no Quênia')}</span></div><div><b>4</b><span>{t('Lawyer, coaches, finance, sports tech', 'Avocat, entraîneurs, finance, tech sportive', 'Mwanasheria, makocha, fedha, teknolojia', 'Advogado, treinadores, finanças, tecnologia')}</span></div><div><b>4</b><span>{t('Languages: English, French, Swahili, Portuguese', 'Langues : anglais, français, swahili, portugais', 'Lugha: Kiingereza, Kifaransa, Kiswahili, Kireno', 'Idiomas: inglês, francês, suaíli, português')}</span></div></div>
</div></div></div></section>'''

steps = [(('Tell <em>us</em>','Parlez-<em>nous</em>','<em>Tuambie</em>','<em>Conte</em> pra gente'),('Who you are and what you need, on WhatsApp or email.','Qui vous êtes et ce dont vous avez besoin, sur WhatsApp ou par e-mail.','Wewe ni nani na unahitaji nini, kwa WhatsApp au barua pepe.','Quem você é e o que precisa, no WhatsApp ou por e-mail.')),
 (('The <em>plan</em>','Le <em>plan</em>','<em>Mpango</em>','O <em>plano</em>'),('A clear scope, a price and a date before any work starts.','Un cadre clair, un prix et une date avant tout travail.','Mpango wa wazi, bei na tarehe kabla ya kazi kuanza.','Escopo claro, preço e data antes de começar.')),
 (('The <em>delivery</em>','La <em>livraison</em>','<em>Uwasilishaji</em>','A <em>entrega</em>'),('Reports, dossiers, CVs or kit, on your phone, in your language.','Rapports, dossiers, CV ou matériel, sur votre téléphone, dans votre langue.','Ripoti, CV au vifaa, kwenye simu yako, kwa lugha yako.','Relatórios, dossiês, currículos ou equipamento, no seu celular.')),
 (('The <em>season</em>','La <em>saison</em>','<em>Msimu</em>','A <em>temporada</em>'),('We stay with you through the season, not just the handover.','Nous restons à vos côtés toute la saison.','Tunabaki nawe msimu mzima, si siku ya kukabidhi tu.','Ficamos com você a temporada toda.'))]
proc = ''.join(f'<div class="step rv"><span class="sn">0{n}</span><h3>{t(*a)}</h3>{t(*b, tag="p")}</div>' for n,(a,b) in enumerate(steps,1))
process = f'''<section class="sx steps4" id="process"><div class="in"><div class="shead"><div><p class="kick">{t('How we work', 'Notre façon de travailler', 'Jinsi tunavyofanya kazi', 'Como trabalhamos')}</p><h2>{t('Four steps. <em>No surprises.</em>', 'Quatre étapes. <em>Aucune surprise.</em>', 'Hatua nne. <em>Hakuna mshangao.</em>', 'Quatro passos. <em>Sem surpresas.</em>')}</h2></div>{tp('From the first message to the last match of the season, you always know what happens next.', 'Du premier message au dernier match de la saison, vous savez toujours ce qui suit.', 'Kuanzia ujumbe wa kwanza hadi mechi ya mwisho ya msimu, unajua kinachofuata.', 'Da primeira mensagem ao último jogo da temporada, você sempre sabe o que vem depois.')}</div>
<div class="steps-g">{proc}</div>
{ctl(('Ready for step one?', 'Prêt pour la première étape ?', 'Uko tayari kwa hatua ya kwanza?', 'Pronto para o primeiro passo?'), ('Tell us what you need', 'Dites-nous ce qu’il vous faut', 'Tuambie unachohitaji', 'Conte o que precisa'), '')}
</div></section>'''

final = f'''<section class="sx final grad" id="contact"><div class="in">
<p class="kick">{t('Kick-off', 'Coup d’envoi', 'Mwanzo wa mchezo', 'Pontapé inicial')}</p>
<h2>{t('Your next decision deserves <em>evidence.</em>', 'Votre prochaine décision mérite des <em>preuves.</em>', 'Uamuzi wako ujao unastahili <em>ushahidi.</em>', 'Sua próxima decisão merece <em>evidências.</em>')}</h2>
<div class="acts"><button type="button" class="btn wa" data-pick="">{t('Message us on WhatsApp', 'Écrivez-nous sur WhatsApp', 'Tutumie ujumbe WhatsApp', 'Fale com a gente no WhatsApp')} {arrow}</button><a class="btn ghost" href="mailto:Advisory@afritechsports.com">{t('Email us', 'Envoyez-nous un e-mail', 'Tutumie barua pepe', 'Mande um e-mail')}</a></div>
<div class="ftr"><div><b>{t('Office', 'Bureau', 'Ofisi', 'Escritório')}</b>Afritech Sports Technology and Innovation Group Limited<br>{t('Advisory Services, Nairobi, Kenya', 'Services de conseil, Nairobi, Kenya', 'Huduma za Ushauri, Nairobi, Kenya', 'Consultoria, Nairóbi, Quênia')}</div>
<div><b>{t('Talk to us', 'Contact', 'Wasiliana nasi', 'Fale com a gente')}</b><a href="mailto:Advisory@afritechsports.com">Advisory@afritechsports.com</a><br><a href="tel:+254715551506">+254 715 551 506</a></div>
<div><b>{t('Follow', 'Suivre', 'Fuatilia', 'Siga')}</b><a href="https://www.linkedin.com/company/afritech-sports-technology-and-innovation-group-limited/" target="_blank" rel="noopener">Afritech Sports · LinkedIn</a><br><a href="https://www.linkedin.com/in/andrew-r-b1b514" target="_blank" rel="noopener">Andrew Rukidi · LinkedIn</a><br><a href="innovation/#podcast">{t('Podcast', 'Podcast', 'Podikasti', 'Podcast')}</a></div></div>
</div></section>'''

miq = f"""<section class="sx" id="matchiq"><div class="in"><div class="miq">
<div class="vframe portrait rv"><button class="sound" type="button" data-sound>{SND}</button><video data-lv data-auto controls playsinline muted preload="metadata" poster="assets/media/matchiq-promo-en.jpg" aria-label="Afritech MatchIQ: from football footage to insight">
<source src="assets/media/matchiq-promo-en.mp4" type="video/mp4"></video></div>
<div><p class="kick">MatchIQ</p>
<h2>{t('We don’t just watch the game. We <em>decode</em> it.', 'Nous ne regardons pas seulement le match. Nous le <em>décodons.</em>', 'Hatutazami mchezo tu. Tunau<em>chambua.</em>', 'Não só assistimos ao jogo. Nós o <em>decodificamos.</em>')}</h2>
{tp('Every match we analyse becomes a MatchIQ dashboard: the replay, the tactical reconstruction, the runs that open space and the moments that change a game. One file that opens on any phone, even with no signal.', 'Chaque match analysé devient un tableau de bord MatchIQ : le replay, la reconstruction tactique, les courses qui ouvrent l’espace et les moments qui font basculer un match. Un seul fichier, lisible sur n’importe quel téléphone, même sans réseau.', 'Kila mechi tunayochambua inakuwa dashibodi ya MatchIQ: marudio, uundaji upya wa mbinu, mbio zinazofungua nafasi na matukio yanayobadilisha mchezo. Faili moja linalofunguka kwenye simu yoyote, hata bila mtandao.', 'Cada partida que analisamos vira um painel MatchIQ: o replay, a reconstrução tática, as corridas que abrem espaço e os lances que mudam o jogo. Um arquivo que abre em qualquer celular, mesmo sem sinal.')}
<div class="miq-f"><div><b>{t('Replay', 'Replay', 'Marudio', 'Replay')}</b>{t('real speed and freeze-frame', 'vitesse réelle et arrêt sur image', 'kasi halisi na picha iliyosimamishwa', 'velocidade real e quadro congelado')}</div><div><b>{t('Reconstruction', 'Reconstruction', 'Uundaji upya', 'Reconstrução')}</b>{t('heat, runs and expected threat (xT)', 'chaleur, courses et menace attendue (xT)', 'joto, mbio na tishio linalotarajiwa (xT)', 'calor, corridas e ameaça esperada (xT)')}</div><div><b>{t('Your language', 'Votre langue', 'Lugha yako', 'Seu idioma')}</b>{t('English, French, Swahili', 'anglais, français, swahili', 'Kiingereza, Kifaransa, Kiswahili', 'inglês, francês, suaíli')}</div></div>
<div class="acts"><a class="btn go1" href="https://afritech-advisory.github.io/afritech-matchiq/" target="_blank" rel="noopener">{t('Open the MatchIQ library', 'Ouvrir la bibliothèque MatchIQ', 'Fungua maktaba ya MatchIQ', 'Abrir a biblioteca MatchIQ')} {arrow}</a><button type="button" class="btn ghost" data-pick="club" data-topic='{topic("MatchIQ","MatchIQ","MatchIQ","MatchIQ")}'>{t('Send us your last match', 'Envoyez-nous votre dernier match', 'Tutumie mechi yako ya mwisho', 'Envie sua última partida')}</button></div>
</div></div></div></section>"""

va_types = [('Post-match coaching review','Revue d’après-match pour le staff','Mapitio ya kocha baada ya mechi','Revisão pós-jogo para a comissão',"Possession, shots and the moments that decided it, cut for Monday's session.","Possession, tirs et moments décisifs, montés pour la séance du lundi.","Umiliki wa mpira, mashuti na matukio yaliyoamua mechi, kwa mazoezi ya Jumatatu.","Posse, finalizações e os lances decisivos, editados para o treino de segunda."),
 ('Goal and key-moment breakdown','Analyse des buts et moments clés','Uchambuzi wa mabao na matukio muhimu','Análise de gols e lances-chave','Every goal traced back: the run, the pass, the space, the mistake.','Chaque but décortiqué : la course, la passe, l’espace, l’erreur.','Kila bao linafuatiliwa: mbio, pasi, nafasi, kosa.','Cada gol rastreado: a corrida, o passe, o espaço, o erro.'),
 ('Tactical reconstruction','Reconstruction tactique','Uundaji upya wa mbinu','Reconstrução tática','Clips rebuilt on a 3D pitch with heat maps and expected threat (xT).','Séquences reconstruites sur un terrain 3D avec cartes de chaleur et menace attendue (xT).','Vipande vinajengwa upya kwenye uwanja wa 3D na ramani za joto na xT.','Lances reconstruídos em campo 3D com mapas de calor e ameaça esperada (xT).'),
 ('Full-match tagging','Annotation du match complet','Kuwekea alama mechi nzima','Marcação da partida completa','Every pass, shot, carry, duel and press logged by our Nairobi analysts.','Chaque passe, tir, conduite, duel et pressing relevé par nos analystes de Nairobi.','Kila pasi, shuti, ubebaji, pambano na kubana, Nairobi.','Cada passe, finalização, condução, duelo e pressão, registrado em Nairóbi.'),
 ('Opposition scouting','Analyse de l’adversaire','Kuchunguza mpinzani','Análise do adversário','How the next opponent builds, presses and defends set pieces.','Comment le prochain adversaire construit, presse et défend les coups de pied arrêtés.','Jinsi mpinzani ajaye anavyojenga, anavyobana na kulinda mipira ya adhabu.','Como o próximo adversário constrói, pressiona e defende bolas paradas.'),
 ('Player clip reels','Montages vidéo de joueurs','Video fupi za mchezaji','Vídeos de jogadores','Each player’s actions in one reel, for coaching, scouting dossiers and CVs.','Les actions d’un joueur dans un montage, pour le coaching, les dossiers et les CV.','Matendo ya mchezaji katika video moja, kwa ukocha, ripoti za uskauti na CV.','As ações de cada jogador num vídeo, para treino, dossiês e currículos.'),
 ('Tournament and squad packages','Forfaits tournoi et sélection','Vifurushi vya mashindano na timu za taifa','Pacotes de torneio e seleção','For federations: every match of a squad or competition, in four languages.','Pour les fédérations : chaque match d’une sélection ou d’une compétition, en quatre langues.','Kwa mashirikisho: kila mechi ya timu au mashindano, kwa lugha nne.','Para federações: cada jogo de uma seleção ou competição, em quatro idiomas.')]
va_rows = ''.join(f'<li><span class="n">{i:02d}</span><div><b>{t(*v[:4])}</b>{t(*v[4:])}</div></li>' for i, v in enumerate(va_types, 1))
video = f"""<section class="sx band-sky" id="video-analysis"><div class="in">
<div class="shead"><div><p class="kick">{t('Video analysis · Kenya 1–2 South Africa', 'Analyse vidéo · Kenya 1–2 Afrique du Sud', 'Uchambuzi wa video · Kenya 1–2 Afrika Kusini', 'Análise de vídeo · Quênia 1–2 África do Sul')}</p><h2>{t('One match. Every <em>angle.</em>', 'Un match. Tous les <em>angles.</em>', 'Mechi moja. Kila <em>pembe.</em>', 'Uma partida. Todos os <em>ângulos.</em>')}</h2></div>
{tp('Our post-match analysis of Kenya’s 2–1 defeat to South Africa: Kenya had 57% of the ball and two shots on target, South Africa had eight. Here is how each side found its final touch, and what a coaching staff takes from it.', 'Notre analyse d’après-match de la défaite 2–1 du Kenya face à l’Afrique du Sud : 57 % de possession et deux tirs cadrés pour le Kenya, huit pour l’Afrique du Sud. Voici comment chaque équipe a trouvé sa dernière touche, et ce qu’un staff en retient.', 'Uchambuzi wetu wa kipigo cha Kenya cha 2–1 dhidi ya Afrika Kusini: Kenya ilimiliki mpira 57% na mashuti mawili yaliyolenga lango, Afrika Kusini manane. Hivi ndivyo kila timu ilivyopata mguso wa mwisho, na kile benchi la ufundi linachojifunza.', 'Nossa análise pós-jogo da derrota do Quênia por 2–1 para a África do Sul: 57% de posse e duas finalizações no alvo para o Quênia, oito para a África do Sul. Veja como cada lado encontrou o toque final, e o que uma comissão técnica tira disso.')}</div>
<div class="va"><div class="vframe wide rv"><button class="sound" type="button" data-sound>{SND}</button><video data-auto controls playsinline muted preload="metadata" poster="assets/media/kenya-south-africa-analysis.jpg" aria-label="MatchIQ post-match analysis: Kenya 1, South Africa 2"><source src="assets/media/kenya-south-africa-analysis.mp4" type="video/mp4"></video><span class="lbl s"><i></i>MatchIQ · {t('Post-match analysis', 'Analyse d’après-match', 'Uchambuzi baada ya mechi', 'Análise pós-jogo')}</span></div>
<div class="va-side"><p class="va-h">{t('What we can do for clubs and federations', 'Ce que nous faisons pour les clubs et fédérations', 'Tunachoweza kufanya kwa klabu na mashirikisho', 'O que fazemos para clubes e federações')}</p><ol class="vt">{va_rows}</ol>
<button type="button" class="btn go1" data-pick="federation" data-topic='{topic("Video analysis","Analyse vidéo","Uchambuzi wa video","Análise de vídeo")}'>{t('Get your match analysed like this', 'Faites analyser votre match ainsi', 'Chambuliwa mechi yako hivi', 'Analise sua partida assim')} {arrow}</button></div></div>
</div></section>"""

main = '<main>' + hero + ticker + reality + nums + news + miq + work + services + video + moves + audiences + method + listen + founder + process + final + '</main>\n' + foot + '\n'
head = head.replace('<html lang="en">', '<html lang="en" class="no-js">', 1)
import re as _re
T_ = 'Afritech Sports | Football scouting, match analysis and player data for African football'
D_ = 'African football talent, backed by evidence. Afritech Sports in Nairobi delivers scouting dossiers, MatchIQ match analysis, video analysis, football CVs, GPS player tracking and FIFA training-reward guidance for clubs, academies, agents and federations, in English, French, Swahili and Portuguese.'
head = _re.sub(r'<title>.*?</title>', '<title>' + T_ + '</title>', head, count=1, flags=_re.S)
head = _re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="' + D_ + '">', head, count=1)
head = _re.sub(r'<meta property="og:title" content="[^"]*">', '<meta property="og:title" content="' + T_ + '">', head, count=1)
head = _re.sub(r'<meta property="og:description" content="[^"]*">', '<meta property="og:description" content="' + D_ + '">', head, count=1)
if 'theme-color' not in head:
    head = head.replace('<meta charset="utf-8">', '<meta charset="utf-8"><meta name="theme-color" content="#0B2A21">', 1)
if 'rel="preload"' not in head:
    head = head.replace('</head>', '<link rel="preload" href="assets/fonts/anton.woff2" as="font" type="font/woff2" crossorigin><link rel="preload" href="assets/fonts/archivo-400.woff2" as="font" type="font/woff2" crossorigin>\n</head>', 1)
out = head + header + main + tail
(R / 'index.html').write_text(out, encoding='utf-8')
print('index.html', len(out))
