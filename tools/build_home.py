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

head = src[:src.index('<header class="top">')]
header = src[src.index('<header class="top">'):src.index('<main>')]
tail = src[src.index('<div class="modal" id="picker"'):]
foot = re.search(r'<footer class="foot">.*?</footer>', src, re.S).group(0)

DESK = 'https://afritech-advisory.github.io/Afritech-Advisory-afritech-tournament-desk/'
MIQ = 'https://afritech-advisory.github.io/afritech-matchiq/matches/2026-11-07-japan-nigeria-u17w-final/'
CVD = 'https://afritech-advisory.github.io/afritech-sports-cv-desk/'

# live pill in header
live = f'<a class="live" href="{DESK}qatar-u17-2026/" target="_blank" rel="noopener"><i></i>' + t('Live: U-17 Tournament Desk', 'En direct : Desk U-17', 'Moja kwa moja: Dawati la U-17', 'Ao vivo: Mesa Sub-17') + '</a>'
if 'class="live"' not in header:
    header = header.replace('<div class="langs"', live + '<div class="langs"', 1)

arrow = '<span class="ar" aria-hidden="true">→</span>'
pitch_svg = '''<svg class="pitchlines" viewBox="0 0 1200 700" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><rect x="40" y="40" width="1120" height="620"/><path d="M600 40V660"/><circle cx="600" cy="350" r="92"/><rect x="40" y="200" width="150" height="300"/><rect x="1010" y="200" width="150" height="300"/><path d="M190 290a70 70 0 0 1 0 120M1010 290a70 70 0 0 0 0 120"/></svg>'''

hero = f'''<section class="h-hero">{pitch_svg}<div class="h-in"><div>
<p class="eyebrow">{t('Nairobi · Football intelligence for Africa', 'Nairobi · Intelligence football pour l’Afrique', 'Nairobi · Ujasusi wa soka kwa Afrika', 'Nairóbi · Inteligência de futebol para a África')}</p>
<h1>{t('<span class="ln"><span>Find the <em>talent.</em></span></span><span class="ln"><span>Read the <em>game.</em></span></span><span class="ln"><span>Run the <em>tech.</em></span></span>',
       '<span class="ln"><span>Trouver le <em>talent.</em></span></span><span class="ln"><span>Lire le <em>jeu.</em></span></span><span class="ln"><span>Faire tourner la <em>tech.</em></span></span>',
       '<span class="ln"><span>Pata <em>vipaji.</em></span></span><span class="ln"><span>Soma <em>mchezo.</em></span></span><span class="ln"><span>Endesha <em>teknolojia.</em></span></span>',
       '<span class="ln"><span>Encontre o <em>talento.</em></span></span><span class="ln"><span>Leia o <em>jogo.</em></span></span><span class="ln"><span>Faça a <em>tecnologia</em> funcionar.</span></span>')}</h1>
{'<div class="lead">' + tp('Match reports, scouting dossiers, football CVs and player tracking for clubs, academies, agents and federations across Africa. Built in Nairobi, made to open on any phone, even with no signal.', 'Rapports de match, dossiers de recrutement, CV football et suivi des joueurs pour les clubs, académies, agents et fédérations d’Afrique. Conçus à Nairobi, lisibles sur n’importe quel téléphone, même sans réseau.', 'Ripoti za mechi, ripoti za uskauti, CV za soka na ufuatiliaji wa wachezaji kwa klabu, akademia, mawakala na mashirikisho kote Afrika. Zimetengenezwa Nairobi, zinafunguka kwenye simu yoyote, hata bila mtandao.', 'Relatórios de partida, dossiês de scouting, currículos de futebol e monitoramento de jogadores para clubes, academias, agentes e federações da África. Feitos em Nairóbi, abrem em qualquer celular, mesmo sem sinal.') + '</div>'}
<div class="acts"><a class="btn go1" href="#first-move">{t('Pick your first move', 'Choisissez votre premier pas', 'Chagua hatua yako ya kwanza', 'Escolha seu primeiro passo')} {arrow}</a><a class="btn ghost" href="#work">{t('See the work', 'Voir le travail', 'Ona kazi yetu', 'Veja o trabalho')}</a></div>
<div class="h-meta"><span>{t('<b>EN · FR · SW · PT</b> four languages', '<b>EN · FR · SW · PT</b> quatre langues', '<b>EN · FR · SW · PT</b> lugha nne', '<b>EN · FR · SW · PT</b> quatro idiomas')}</span><span>{t('<b>Works offline</b> on any phone', '<b>Hors ligne</b> sur tout téléphone', '<b>Bila mtandao</b> kwenye simu yoyote', '<b>Funciona offline</b> em qualquer celular')}</span></div>
</div>
<div class="stage"><button class="pp" type="button" aria-label="Pause video" data-pp><svg viewBox="0 0 14 14"><rect x="2" y="1" width="3.5" height="12"/><rect x="8.5" y="1" width="3.5" height="12"/></svg></button>
<div class="phone"><div class="screen"><video data-src="assets/media/matchiq-final.mp4" poster="assets/media/matchiq-final.jpg" muted loop playsinline preload="none" aria-label="Scrolling through the MatchIQ report on the FIFA U-17 Women's World Cup final"></video></div></div>
<div class="chip c1"><b>16</b>{t('named sources', 'sources citées', 'vyanzo vilivyotajwa', 'fontes citadas')}</div>
<div class="chip c2"><b>2–1</b>{t('Nigeria · final read', 'Nigeria · la finale lue', 'Nigeria · fainali', 'Nigéria · a final')}</div>
<p class="cap">{t('MatchIQ · U-17 Women’s World Cup final', 'MatchIQ · finale Coupe du monde féminine U-17', 'MatchIQ · fainali ya Kombe la Dunia U-17', 'MatchIQ · final da Copa Feminina Sub-17')}</p></div>
</div></section>'''

tick_items = [('Match analysis','Analyse de match','Uchambuzi wa mechi','Análise de partidas'),('Scouting dossiers','Dossiers de recrutement','Ripoti za uskauti','Dossiês de scouting'),('Football CVs','CV football','CV za soka','Currículos de futebol'),('INSAIT JOY','INSAIT JOY','INSAIT JOY','INSAIT JOY'),('Soccerbee GPS','Soccerbee GPS','Soccerbee GPS','Soccerbee GPS'),('Contracts & transfers','Contrats & transferts','Mikataba na uhamisho','Contratos e transferências'),('Workshops','Ateliers','Warsha','Workshops'),('Tournament Desk','Desk Tournoi','Dawati la Mashindano','Mesa do Torneio')]
tk = ''.join('<span>' + t(*i) + '</span>' for i in tick_items)
ticker = f'<div class="tick" aria-hidden="true"><div class="tick-in">{tk}{tk}</div></div>'

nums = f'''<section class="sx"><div class="in">
<p class="kick">{t('The scoreboard', 'Le tableau d’affichage', 'Ubao wa matokeo', 'O placar')}</p>
<div class="nums rv">
<div class="num"><b>120</b><span>{t('countries where our podcast is heard', 'pays où notre podcast est écouté', 'nchi ambako podikasti yetu inasikilizwa', 'países onde nosso podcast é ouvido')}</span></div>
<div class="num"><b>5K<small>+</small></b><span>{t('streams and downloads, March 2026', 'écoutes et téléchargements, mars 2026', 'usikilizaji na upakuaji, Machi 2026', 'reproduções e downloads, março de 2026')}</span></div>
<div class="num"><b>10</b><span>{t('African nations followed at the U-17 World Cup', 'nations africaines suivies à la Coupe du monde U-17', 'mataifa ya Afrika tunayofuatilia Kombe la Dunia U-17', 'seleções africanas acompanhadas na Copa Sub-17')}</span></div>
<div class="num"><b>4</b><span>{t('languages on every page and every form', 'langues sur chaque page et chaque formulaire', 'lugha kwenye kila ukurasa na kila fomu', 'idiomas em cada página e cada formulário')}</span></div>
<div class="num"><b>3</b><span>{t('live desks you can open today', 'desks en ligne à ouvrir aujourd’hui', 'madawati yaliyo hewani unayoweza kufungua leo', 'mesas no ar para abrir hoje')}</span></div>
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
work = f'''<section class="sx" id="work"><div class="in">
<div class="shead"><div><p class="kick">{t('Selected work', 'Travaux choisis', 'Kazi teule', 'Trabalhos selecionados')}</p><h2>{t('Work you can <em>open</em> today.', 'Du travail à <em>ouvrir</em> aujourd’hui.', 'Kazi unayoweza <em>kufungua</em> leo.', 'Trabalho para <em>abrir</em> hoje.')}</h2></div>
{tp('Every piece below is live and public. No mock-ups, no stock photos: the same reports, desks and CVs our clients receive.', 'Tout ce qui suit est en ligne et public. Pas de maquettes, pas de photos de banque d’images : les mêmes rapports, desks et CV que reçoivent nos clients.', 'Kila kazi hapa chini iko hewani na wazi kwa umma. Hakuna picha za kuigiza: ni ripoti, madawati na CV zile zile wanazopokea wateja wetu.', 'Tudo abaixo está no ar e é público. Sem maquetes, sem fotos de banco: os mesmos relatórios, mesas e currículos que nossos clientes recebem.')}</div>
<div class="work">
{wk('w7', MIQ, ('wide', '<img class="cover" src="assets/img/final.jpg" alt="MatchIQ report: Japan 1, Nigeria 2" loading="lazy">'), LIVE, True,
    t('MatchIQ · U-17 final', 'MatchIQ · finale U-17', 'MatchIQ · fainali U-17', 'MatchIQ · final Sub-17'),
    t('Nigeria 2–1 Japan, read goal by goal: player radars, where each game broke down, five dated next steps.', 'Nigeria 2–1 Japon, but par but : radars des joueuses, où chaque jeu a cédé, cinq prochaines étapes datées.', 'Nigeria 2–1 Japan, bao kwa bao: rada za wachezaji, mchezo ulipovunjika, hatua tano zenye tarehe.', 'Nigéria 2–1 Japão, gol a gol: radares das jogadoras, onde cada jogo falhou, cinco próximos passos com data.'))}
{wk('w5', DESK + 'qatar-u17-2026/', ('pitchbg tall', mini('assets/media/tournament-desk.mp4', 'assets/media/tournament-desk.jpg', 'Scrolling the Tournament Desk on a phone')), LIVE, True,
    t('Tournament Desk', 'Desk Tournoi', 'Dawati la Mashindano', 'Mesa do Torneio'),
    t('Africa’s ten nations at the FIFA U-17 World Cup, match by match, until 13 December.', 'Les dix nations africaines à la Coupe du monde U-17, match après match, jusqu’au 13 décembre.', 'Mataifa kumi ya Afrika Kombe la Dunia U-17, mechi kwa mechi, hadi 13 Desemba.', 'As dez seleções africanas na Copa Sub-17, jogo a jogo, até 13 de dezembro.'))}
{wk('w4', CVD, ('inkbg tall', mini('assets/media/cv-desk.mp4', 'assets/media/cv-desk.jpg', 'Scrolling the CV Desk on a phone')), LIVE, True,
    t('CV Desk', 'Bureau CV', 'Dawati la CV', 'Mesa de Currículos'),
    t('Football CVs for players, coaches, scouts and analysts, built to our standard.', 'CV football pour joueurs, entraîneurs, recruteurs et analystes, à notre standard.', 'CV za soka kwa wachezaji, makocha, maskauti na wachambuzi, kwa kiwango chetu.', 'Currículos de futebol para jogadores, treinadores, olheiros e analistas, no nosso padrão.'))}
{wk('w4', 'advisory/#education', ('sq', '<img class="cover" src="assets/img/webinar.jpg" alt="From Footage to Insight workshop poster" loading="lazy">'), t('Free workshop', 'Atelier gratuit', 'Warsha ya bure', 'Workshop gratuito'), False,
    t('From Footage to Insight', 'From Footage to Insight', 'From Footage to Insight', 'From Footage to Insight'),
    t('Live tagging of a real Kenyan match, with FootLab (Morocco).', 'Annotation en direct d’un vrai match kényan, avec FootLab (Maroc).', 'Kuwekea alama mechi halisi ya Kenya moja kwa moja, pamoja na FootLab (Morocco).', 'Marcação ao vivo de uma partida real do Quênia, com a FootLab (Marrocos).'))}
{wk('w4', 'technology/', ('sq', '<img class="cover" src="assets/img/insait.jpg" alt="INSAIT JOY smart shin guards kit" loading="lazy">'), t('Hardware', 'Matériel', 'Vifaa', 'Equipamento'), False,
    t('INSAIT JOY', 'INSAIT JOY', 'INSAIT JOY', 'INSAIT JOY'),
    t('Smart shin guards: every run, touch and kick, on the coach’s phone after the session.', 'Protège-tibias connectés : chaque course, touche et frappe, sur le téléphone du coach.', 'Vilinda-muundi janja: kila mbio, mguso na teke, kwenye simu ya kocha baada ya mazoezi.', 'Caneleiras inteligentes: cada corrida, toque e chute, no celular do treinador.'))}
</div></div></section>'''

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
det = ''
for i, s in enumerate(svc_items, 1):
    lis = ''.join('<li>' + t(*b) + '</li>' for b in s[6])
    det += f'''<details{" open" if i == 1 else ""}><summary><span class="n">0{i}</span><span class="sn">{t(*s[:4])}</span><span class="pl" aria-hidden="true"></span></summary><div class="body"><div>{tp(*s[5])}<a class="lk" href="{s[4]}">{t('Open', 'Ouvrir', 'Fungua', 'Abrir')} {arrow}</a></div><ul>{lis}</ul></div></details>'''
services = f'''<section class="sx dark" id="services"><div class="in">
<div class="shead"><div><p class="kick">{t('What we do', 'Ce que nous faisons', 'Tunachofanya', 'O que fazemos')}</p><h2>{t('Seven ways we <em>help</em> you win.', 'Sept façons de vous <em>aider</em> à gagner.', 'Njia saba za <em>kukusaidia</em> kushinda.', 'Sete formas de <em>ajudar</em> você a vencer.')}</h2></div>
{tp('Evidence for every football decision, from the first scouting trip to the transfer paperwork.', 'Des preuves pour chaque décision football, du premier déplacement de recrutement aux papiers du transfert.', 'Ushahidi kwa kila uamuzi wa soka, kuanzia safari ya kwanza ya uskauti hadi nyaraka za uhamisho.', 'Evidências para cada decisão no futebol, da primeira viagem de scouting à papelada da transferência.')}</div>
<div class="svc">{det}</div></div></section>'''

def mv(no, tag, price, h, items, btn, fine, feat=False, pick=None, href=None):
    lis = ''.join('<li>' + t(*x) + '</li>' for x in items)
    b = f'<button type="button" class="btn {"go1" if feat else "ghost"}" data-pick="{pick or ""}" data-topic=\'{btn[1]}\'>{t(*btn[0])} {arrow}</button>' if href is None else f'<a class="btn {"go1" if feat else "ghost"}" href="{href}">{t(*btn[0])} {arrow}</a>'
    return f'<div class="mv rv{" feat" if feat else ""}"><div class="no"><span>{no}</span><span>{t(*tag)}</span></div><div class="price">{t(*price)}</div><h3>{t(*h)}</h3><ul>{lis}</ul>{b}<p class="fine">{t(*fine)}</p></div>'

import json
topic = lambda *a: H.escape(json.dumps(dict(zip(L, a)), ensure_ascii=False), quote=True)
moves = f'''<section class="sx" id="first-move"><div class="in">
<div class="shead"><div><p class="kick">{t('Three ways to start', 'Trois façons de commencer', 'Njia tatu za kuanza', 'Três formas de começar')}</p><h2>{t('Pick your first <em>move.</em>', 'Votre premier <em>pas.</em>', 'Chagua hatua ya <em>kwanza.</em>', 'Escolha o primeiro <em>passo.</em>')}</h2></div>
{tp('All three are low risk. See our work on your own match first, learn with us for free, or put one player under the microscope.', 'Les trois sont sans risque. Voyez notre travail sur votre propre match, apprenez gratuitement avec nous, ou passez un joueur au microscope.', 'Zote tatu hazina hatari. Ona kazi yetu kwenye mechi yako kwanza, jifunze nasi bure, au mchunguze mchezaji mmoja kwa kina.', 'As três têm baixo risco. Veja nosso trabalho na sua própria partida, aprenda com a gente de graça ou coloque um jogador no microscópio.')}</div>
<div class="moves">
{mv('01', ('Clubs · academies','Clubs · académies','Klabu · akademia','Clubes · academias'), ('Free','Gratuit','Bure','Grátis'), ('A free match read','Une lecture de match gratuite','Uchambuzi wa mechi bure','Uma leitura de partida grátis'),
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
rows = ''
for i, a in enumerate(aud, 1):
    ext = ' target="_blank" rel="noopener"' if a[8].startswith('http') else ''
    rows += f'''<div class="au rv"><span class="n">0{i}</span><h3>{t(*[f'<span class="hl">{x}</span>' for x in a[:4]])}</h3>{tp(*a[4:8])}<div class="row"><a class="btn ghost sm" href="{a[8]}"{ext}>{t('What we offer','Notre offre','Tunachotoa','O que oferecemos')}</a><button type="button" class="btn go1 sm" data-pick="{a[9]}">{t('Message us','Écrivez-nous','Tutumie ujumbe','Fale com a gente')}</button></div></div>'''
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
</div></div></div></section>'''

listen = f'''<section class="sx" id="listen"><div class="in"><div class="listen">
<div class="cover rv"><img src="assets/img/podcast.jpg" alt="Deep Dive Into Soccer podcast: 5,000 streams and downloads" loading="lazy"><div class="eq" aria-hidden="true"><i></i><i></i><i></i><i></i></div></div>
<div><p class="kick">{t('Listen', 'Écouter', 'Sikiliza', 'Ouça')}</p>
<h2>{t('Deep Dive Into <em>Soccer.</em>', 'Deep Dive Into <em>Soccer.</em>', 'Deep Dive Into <em>Soccer.</em>', 'Deep Dive Into <em>Soccer.</em>')}</h2>
{tp('Our podcast takes African football apart, in your language: a separate episode in English, French, Swahili and Portuguese.', 'Notre podcast décortique le football africain dans votre langue : un épisode distinct en anglais, français, swahili et portugais.', 'Podikasti yetu inachambua soka la Afrika kwa lugha yako: kipindi tofauti kwa Kiingereza, Kifaransa, Kiswahili na Kireno.', 'Nosso podcast destrincha o futebol africano no seu idioma: um episódio próprio em inglês, francês, suaíli e português.')}
<div class="player" data-player><div class="pb"><button class="playb" type="button" aria-label="Play the latest episode"><svg viewBox="0 0 14 16"><path d="M0 0l14 8-14 8z"/></svg></button><div class="ep"><small>{t('Latest episode', 'Dernier épisode', 'Kipindi kipya', 'Último episódio')}</small><span data-ep></span></div></div></div>
<div class="pods"><a href="innovation/#podcast">{t('All episodes', 'Tous les épisodes', 'Vipindi vyote', 'Todos os episódios')} →</a></div>
</div></div></div></section>'''

founder = f'''<section class="sx" id="about" style="padding-top:0"><div class="in"><div class="half" style="margin:0 0 clamp(64px,9vw,120px)"></div><div class="fd">
<div class="emb rv"><img src="assets/media/afritech-logo.jpg" alt="Afritech Sports Technology and Innovation Group Limited logo" width="900" height="900" loading="lazy"></div>
<div><p class="kick">{t('Why Afritech', 'Pourquoi Afritech', 'Kwa nini Afritech', 'Por que a Afritech')}</p>
<blockquote>{t('African football has the talent. What it is missing is the evidence. That is the gap we close, one match, one player and one club at a time.', 'Le football africain a le talent. Ce qui lui manque, ce sont les preuves. C’est ce vide que nous comblons, un match, un joueur et un club à la fois.', 'Soka la Afrika lina vipaji. Kinachokosekana ni ushahidi. Hilo ndilo pengo tunaloziba, mechi moja, mchezaji mmoja na klabu moja kwa wakati.', 'O futebol africano tem o talento. O que falta são as evidências. É essa lacuna que fechamos, uma partida, um jogador e um clube de cada vez.')}</blockquote>
<div class="sig"><img src="assets/media/andrew.jpg" alt="Andrew Rukidi" width="60" height="60" loading="lazy"><div><b>Andrew Rukidi</b><span>{t('Founder · Football intelligence & sports technology', 'Fondateur · Intelligence football & technologie sportive', 'Mwanzilishi · Ujasusi wa soka na teknolojia ya michezo', 'Fundador · Inteligência de futebol e tecnologia esportiva')}</span></div></div>
<div class="facts"><div><b>NBO</b><span>{t('Based in Nairobi, on the ground in Kenya', 'Basés à Nairobi, sur le terrain au Kenya', 'Tuko Nairobi, uwanjani Kenya', 'Em Nairóbi, presentes no Quênia')}</span></div><div><b>4</b><span>{t('Lawyer, coaches, finance, sports tech', 'Avocat, entraîneurs, finance, tech sportive', 'Mwanasheria, makocha, fedha, teknolojia', 'Advogado, treinadores, finanças, tecnologia')}</span></div><div><b>4</b><span>{t('Languages: English, French, Swahili, Portuguese', 'Langues : anglais, français, swahili, portugais', 'Lugha: Kiingereza, Kifaransa, Kiswahili, Kireno', 'Idiomas: inglês, francês, suaíli, português')}</span></div></div>
</div></div></div></section>'''

steps = [('Tell us','Dites-nous','Tuambie','Conte pra gente','Who you are and what you need, on WhatsApp or email.','Qui vous êtes et ce dont vous avez besoin, sur WhatsApp ou par e-mail.','Wewe ni nani na unahitaji nini, kwa WhatsApp au barua pepe.','Quem você é e o que precisa, no WhatsApp ou por e-mail.'),
 ('We scope it','Nous cadrons','Tunapanga','A gente define','A clear plan, a price and a date before any work starts.','Un plan clair, un prix et une date avant tout travail.','Mpango wa wazi, bei na tarehe kabla ya kazi kuanza.','Um plano claro, um preço e uma data antes de começar.'),
 ('We deliver','Nous livrons','Tunawasilisha','A gente entrega','Reports, dossiers, CVs or kit, on your phone, in your language.','Rapports, dossiers, CV ou matériel, sur votre téléphone, dans votre langue.','Ripoti, CV au vifaa, kwenye simu yako, kwa lugha yako.','Relatórios, dossiês, currículos ou equipamento, no seu celular, no seu idioma.'),
 ('We stay','Nous restons','Tunabaki nawe','A gente fica','Support through the season, not just the handover.','Un suivi toute la saison, pas seulement à la livraison.','Msaada msimu mzima, si siku ya kukabidhi tu.','Suporte durante a temporada, não só na entrega.')]
proc = ''.join(f'<div class="st rv"><b>{t(*s[:4])}</b>{t(*s[4:])}</div>' for s in steps)
process = f'''<section class="sx" style="padding-top:0"><div class="in"><p class="kick">{t('How we work', 'Notre façon de travailler', 'Jinsi tunavyofanya kazi', 'Como trabalhamos')}</p><h2>{t('Four steps. <em>No surprises.</em>', 'Quatre étapes. <em>Aucune surprise.</em>', 'Hatua nne. <em>Hakuna mshangao.</em>', 'Quatro passos. <em>Sem surpresas.</em>')}</h2><div class="steps" style="margin-top:34px">{proc}</div></div></section>'''

final = f'''<section class="sx dark final" id="contact"><div class="in">
<p class="kick">{t('Kick-off', 'Coup d’envoi', 'Mwanzo wa mchezo', 'Pontapé inicial')}</p>
<h2>{t('Your next decision deserves <em>evidence.</em>', 'Votre prochaine décision mérite des <em>preuves.</em>', 'Uamuzi wako ujao unastahili <em>ushahidi.</em>', 'Sua próxima decisão merece <em>evidências.</em>')}</h2>
<div class="acts"><button type="button" class="btn wa" data-pick="">{t('Message us on WhatsApp', 'Écrivez-nous sur WhatsApp', 'Tutumie ujumbe WhatsApp', 'Fale com a gente no WhatsApp')} {arrow}</button><a class="btn ghost" href="mailto:Advisory@afritechsports.com">{t('Email us', 'Envoyez-nous un e-mail', 'Tutumie barua pepe', 'Mande um e-mail')}</a></div>
<div class="ftr"><div><b>{t('Office', 'Bureau', 'Ofisi', 'Escritório')}</b>Afritech Sports Technology and Innovation Group Limited<br>{t('Advisory Services, Nairobi, Kenya', 'Services de conseil, Nairobi, Kenya', 'Huduma za Ushauri, Nairobi, Kenya', 'Consultoria, Nairóbi, Quênia')}</div>
<div><b>{t('Talk to us', 'Contact', 'Wasiliana nasi', 'Fale com a gente')}</b><a href="mailto:Advisory@afritechsports.com">Advisory@afritechsports.com</a><br><a href="tel:+254715551506">+254 715 551 506</a></div>
<div><b>{t('Follow', 'Suivre', 'Fuatilia', 'Siga')}</b><a href="https://www.linkedin.com/company/afritech-sports-technology-and-innovation-group-limited/" target="_blank" rel="noopener">Afritech Sports · LinkedIn</a><br><a href="https://www.linkedin.com/in/andrew-r-b1b514" target="_blank" rel="noopener">Andrew Rukidi · LinkedIn</a><br><a href="innovation/#podcast">{t('Podcast', 'Podcast', 'Podikasti', 'Podcast')}</a></div></div>
</div></section>'''

miq = f"""<section class="sx" id="matchiq"><div class="in"><div class="miq">
<div class="vframe portrait rv"><video data-lv controls playsinline preload="none" poster="assets/media/matchiq-promo-en.jpg" aria-label="Afritech MatchIQ: from football footage to insight">
<source src="assets/media/matchiq-promo-en.mp4" type="video/mp4"></video></div>
<div><p class="kick">MatchIQ</p>
<h2>{t('We don’t just watch the game. We <em>decode</em> it.', 'Nous ne regardons pas seulement le match. Nous le <em>décodons.</em>', 'Hatutazami mchezo tu. Tunau<em>chambua.</em>', 'Não só assistimos ao jogo. Nós o <em>decodificamos.</em>')}</h2>
{tp('Every match we analyse becomes a MatchIQ dashboard: the replay, the tactical reconstruction, the runs that open space and the moments that change a game. One file that opens on any phone, even with no signal.', 'Chaque match analysé devient un tableau de bord MatchIQ : le replay, la reconstruction tactique, les courses qui ouvrent l’espace et les moments qui font basculer un match. Un seul fichier, lisible sur n’importe quel téléphone, même sans réseau.', 'Kila mechi tunayochambua inakuwa dashibodi ya MatchIQ: marudio, uundaji upya wa mbinu, mbio zinazofungua nafasi na matukio yanayobadilisha mchezo. Faili moja linalofunguka kwenye simu yoyote, hata bila mtandao.', 'Cada partida que analisamos vira um painel MatchIQ: o replay, a reconstrução tática, as corridas que abrem espaço e os lances que mudam o jogo. Um arquivo que abre em qualquer celular, mesmo sem sinal.')}
<div class="miq-f"><div><b>{t('Replay', 'Replay', 'Marudio', 'Replay')}</b>{t('real speed and freeze-frame', 'vitesse réelle et arrêt sur image', 'kasi halisi na picha iliyosimamishwa', 'velocidade real e quadro congelado')}</div><div><b>{t('Reconstruction', 'Reconstruction', 'Uundaji upya', 'Reconstrução')}</b>{t('heat, runs and expected threat (xT)', 'chaleur, courses et menace attendue (xT)', 'joto, mbio na tishio linalotarajiwa (xT)', 'calor, corridas e ameaça esperada (xT)')}</div><div><b>{t('Your language', 'Votre langue', 'Lugha yako', 'Seu idioma')}</b>{t('English, French, Swahili', 'anglais, français, swahili', 'Kiingereza, Kifaransa, Kiswahili', 'inglês, francês, suaíli')}</div></div>
<div class="acts"><a class="btn go1" href="https://afritech-advisory.github.io/afritech-matchiq/" target="_blank" rel="noopener">{t('Open the MatchIQ library', 'Ouvrir la bibliothèque MatchIQ', 'Fungua maktaba ya MatchIQ', 'Abrir a biblioteca MatchIQ')} {arrow}</a><button type="button" class="btn ghost" data-pick="club" data-topic='{topic("MatchIQ","MatchIQ","MatchIQ","MatchIQ")}'>{t('Bring us your footage', 'Envoyez-nous vos images', 'Tuletee video zako', 'Traga suas imagens')}</button></div>
</div></div></div></section>"""

va_types = [('Post-match coaching review','Revue d’après-match pour le staff','Mapitio ya kocha baada ya mechi','Revisão pós-jogo para a comissão',"Possession, shots and the moments that decided it, cut for Monday's session.","Possession, tirs et moments décisifs, montés pour la séance du lundi.","Umiliki wa mpira, mashuti na matukio yaliyoamua mechi, kwa mazoezi ya Jumatatu.","Posse, finalizações e os lances decisivos, editados para o treino de segunda."),
 ('Goal and key-moment breakdown','Analyse des buts et moments clés','Uchambuzi wa mabao na matukio muhimu','Análise de gols e lances-chave','Every goal traced back: the run, the pass, the space, the mistake.','Chaque but décortiqué : la course, la passe, l’espace, l’erreur.','Kila bao linafuatiliwa: mbio, pasi, nafasi, kosa.','Cada gol rastreado: a corrida, o passe, o espaço, o erro.'),
 ('Tactical reconstruction','Reconstruction tactique','Uundaji upya wa mbinu','Reconstrução tática','Clips rebuilt on a 3D pitch with heat maps and expected threat (xT).','Séquences reconstruites sur un terrain 3D avec cartes de chaleur et menace attendue (xT).','Vipande vinajengwa upya kwenye uwanja wa 3D na ramani za joto na xT.','Lances reconstruídos em campo 3D com mapas de calor e ameaça esperada (xT).'),
 ('Full-match tagging','Annotation du match complet','Kuwekea alama mechi nzima','Marcação da partida completa','Every pass, shot, carry, duel and press logged by our Nairobi analysts.','Chaque passe, tir, conduite, duel et pressing relevé par nos analystes de Nairobi.','Kila pasi, shuti, ubebaji, pambano na kubana, Nairobi.','Cada passe, finalização, condução, duelo e pressão, registrado em Nairóbi.'),
 ('Opposition scouting','Analyse de l’adversaire','Kuchunguza mpinzani','Análise do adversário','How the next opponent builds, presses and defends set pieces.','Comment le prochain adversaire construit, presse et défend les coups de pied arrêtés.','Jinsi mpinzani ajaye anavyojenga, anavyobana na kulinda mipira ya adhabu.','Como o próximo adversário constrói, pressiona e defende bolas paradas.'),
 ('Player clip reels','Montages vidéo de joueurs','Video fupi za mchezaji','Vídeos de jogadores','Each player’s actions in one reel, for coaching, scouting dossiers and CVs.','Les actions d’un joueur dans un montage, pour le coaching, les dossiers et les CV.','Matendo ya mchezaji katika video moja, kwa ukocha, ripoti za uskauti na CV.','As ações de cada jogador num vídeo, para treino, dossiês e currículos.'),
 ('Tournament and squad packages','Forfaits tournoi et sélection','Vifurushi vya mashindano na timu za taifa','Pacotes de torneio e seleção','For federations: every match of a squad or competition, in four languages.','Pour les fédérations : chaque match d’une sélection ou d’une compétition, en quatre langues.','Kwa mashirikisho: kila mechi ya timu au mashindano, kwa lugha nne.','Para federações: cada jogo de uma seleção ou competição, em quatro idiomas.')]
va_rows = ''.join(f'<li><span class="n">{i:02d}</span><div><b>{t(*v[:4])}</b>{t(*v[4:])}</div></li>' for i, v in enumerate(va_types, 1))
video = f"""<section class="sx" id="video-analysis" style="padding-top:0"><div class="in">
<div class="shead"><div><p class="kick">{t('Video analysis · Kenya 1–2 South Africa', 'Analyse vidéo · Kenya 1–2 Afrique du Sud', 'Uchambuzi wa video · Kenya 1–2 Afrika Kusini', 'Análise de vídeo · Quênia 1–2 África do Sul')}</p><h2>{t('One match. Every <em>angle.</em>', 'Un match. Tous les <em>angles.</em>', 'Mechi moja. Kila <em>pembe.</em>', 'Uma partida. Todos os <em>ângulos.</em>')}</h2></div>
{tp('Our post-match analysis of Kenya’s 2–1 defeat to South Africa: Kenya had 57% of the ball and two shots on target, South Africa had eight. Here is how each side found its final touch, and what a coaching staff takes from it.', 'Notre analyse d’après-match de la défaite 2–1 du Kenya face à l’Afrique du Sud : 57 % de possession et deux tirs cadrés pour le Kenya, huit pour l’Afrique du Sud. Voici comment chaque équipe a trouvé sa dernière touche, et ce qu’un staff en retient.', 'Uchambuzi wetu wa kipigo cha Kenya cha 2–1 dhidi ya Afrika Kusini: Kenya ilimiliki mpira 57% na mashuti mawili yaliyolenga lango, Afrika Kusini manane. Hivi ndivyo kila timu ilivyopata mguso wa mwisho, na kile benchi la ufundi linachojifunza.', 'Nossa análise pós-jogo da derrota do Quênia por 2–1 para a África do Sul: 57% de posse e duas finalizações no alvo para o Quênia, oito para a África do Sul. Veja como cada lado encontrou o toque final, e o que uma comissão técnica tira disso.')}</div>
<div class="va"><div class="vframe wide rv"><video controls playsinline preload="none" poster="assets/media/kenya-south-africa-analysis.jpg" aria-label="MatchIQ post-match analysis: Kenya 1, South Africa 2"><source src="assets/media/kenya-south-africa-analysis.mp4" type="video/mp4"></video><span class="lbl s"><i></i>MatchIQ · {t('Post-match analysis', 'Analyse d’après-match', 'Uchambuzi baada ya mechi', 'Análise pós-jogo')}</span></div>
<div class="va-side"><p class="va-h">{t('What we can do for clubs and federations', 'Ce que nous faisons pour les clubs et fédérations', 'Tunachoweza kufanya kwa klabu na mashirikisho', 'O que fazemos para clubes e federações')}</p><ol class="vt">{va_rows}</ol>
<button type="button" class="btn go1" data-pick="federation" data-topic='{topic("Video analysis","Analyse vidéo","Uchambuzi wa video","Análise de vídeo")}'>{t('Get your match analysed', 'Faire analyser votre match', 'Chambuliwa mechi yako', 'Analise sua partida')} {arrow}</button></div></div>
</div></section>"""

main = '<main>' + hero + ticker + nums + news + miq + work + services + video + moves + audiences + method + listen + founder + process + final + '</main>\n' + foot + '\n'
head = head.replace('<html lang="en">', '<html lang="en" class="no-js">', 1)
if 'theme-color' not in head:
    head = head.replace('<meta charset="utf-8">', '<meta charset="utf-8"><meta name="theme-color" content="#0B2A21">', 1)
if 'rel="preload"' not in head:
    head = head.replace('</head>', '<link rel="preload" href="assets/fonts/bsd-800.woff2" as="font" type="font/woff2" crossorigin><link rel="preload" href="assets/fonts/plex-400.woff2" as="font" type="font/woff2" crossorigin>\n</head>', 1)
out = head + header + main + tail
(R / 'index.html').write_text(out, encoding='utf-8')
print('index.html', len(out))
