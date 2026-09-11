import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from images_b64 import IMAGES
from common import (SITE, wa, CHECK_SVG, CTA_NOTADO_ESCURO, NOTADO_CREDIT, PALETTE, FONTS,
                    BASE_CSS, REVEAL_JS, CARROSSEL_JS, ENDERECO, ENDERECO_Q, INSTAGRAM, TRINKS, head)

WA_AGENDAR = wa("Olá! Vim pelo site do Studio Gisele Quintino e gostaria de agendar um horário.")

ICO_CORTE = '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="6" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><path d="M20 4 8.12 15.88M14.47 14.48 20 20M8.12 8.12 12 12"/></svg>'
ICO_COR = '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3c4 3 7 7.5 7 11a7 7 0 0 1-14 0c0-3.5 3-8 7-11Z"/></svg>'
ICO_TRAT = '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21s-7-4.5-9.5-9C1 8 2.5 4.5 6 4c2-.3 4 .7 6 3 2-2.3 4-3.3 6-3 3.5.5 5 4 3.5 8-2.5 4.5-9.5 9-9.5 9Z"/></svg>'
ICO_MEGA = '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M7 4c-1 3 0 6 2 8M12 4c-1 4 0 7 1 9M17 4c-1 5 1 8 3 10"/><path d="M4 21c3-2 13-2 16 0"/></svg>'
ICO_SOBRANC = '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 15C7 9 11 7.5 14 8s5 2.5 7 4.5"/></svg>'
ICO_DEPIL = '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3s6.5 7.2 6.5 12a6.5 6.5 0 0 1-13 0C5.5 10.2 12 3 12 3Z"/></svg>'
ICO_PENTEADO = '<svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor" aria-hidden="true"><path d="M12 2l2.1 6.1L20 10l-5.9 1.9L12 18l-2.1-6.1L4 10l5.9-1.9z"/><path d="M18.5 14l.9 2.6 2.6.9-2.6.9-.9 2.6-.9-2.6-2.6-.9 2.6-.9z"/></svg>'
ICO_UNHA = '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M7 20V9a5 5 0 0 1 10 0v11"/><path d="M7 14h10"/></svg>'

SERVICOS = [
    {"nome": "Mechas, Luzes & Coloração", "ico": ICO_COR,
     "desc": "Técnicas personalizadas de iluminação e coloração para valorizar sua beleza, respeitando o histórico e a saúde dos fios.",
     "itens": ["Mechas e luzes", "Coloração", "Retoque de raiz", "Matização e tonalização", "Teste de mechas"],
     "preco": "Sob consulta"},
    {"nome": "Cortes & Finalização", "ico": ICO_CORTE,
     "desc": "Cortes e finalizações pensados para valorizar o formato do rosto, o estilo e a identidade de cada cliente.",
     "itens": ["Cortes femininos", "Cortes masculinos", "Cortes infantis", "Escova e finalização", "Baby liss e cachos"],
     "preco": "A partir de R$ 80"},
    {"nome": "Tratamentos & Terapia Capilar", "ico": ICO_TRAT,
     "desc": "Cuidados direcionados às necessidades dos fios e do couro cabeludo, com avaliação e tratamentos específicos.",
     "itens": ["Consulta de terapia capilar", "Hidratação", "Reconstrução", "Detox capilar"],
     "preco": "A partir de R$ 100"},
    {"nome": "Mega Hair", "ico": ICO_MEGA,
     "desc": "Alongamento e harmonização capilar para conquistar mais comprimento e volume com resultado integrado ao cabelo natural.",
     "itens": ["Mega Hair com fita", "Harmonização capilar", "Manutenção", "Avaliação personalizada"],
     "preco": "A partir de R$ 500"},
    {"nome": "Sobrancelhas", "ico": ICO_SOBRANC,
     "desc": "Design pensado para valorizar os traços naturais do rosto e proporcionar sobrancelhas mais definidas e harmoniosas.",
     "itens": ["Design de sobrancelhas", "Design com henna", "Aplicação de henna"],
     "preco": "A partir de R$ 30"},
    {"nome": "Depilação", "ico": ICO_DEPIL,
     "desc": "Depilação com cera para diferentes regiões do rosto e do corpo, com opções de atendimento de acordo com cada necessidade.",
     "itens": ["Axilas", "Buço", "Pernas", "Virilha", "Rosto", "Costas"],
     "preco": "A partir de R$ 15"},
    {"nome": "Penteados & Maquiagem", "ico": ICO_PENTEADO,
     "desc": "Produção de beleza para ocasiões especiais, com penteados e maquiagem para complementar e valorizar cada detalhe.",
     "itens": ["Penteados", "Baby liss e cachos", "Maquiagem", "Produção para eventos"],
     "preco": "Sob consulta"},
    {"nome": "Unhas", "ico": ICO_UNHA,
     "desc": "Cuidados e serviços de beleza para manter as unhas bonitas e bem cuidadas, realizados pela equipe do Studio.",
     "itens": ["Cuidados com as unhas", "Serviços pela equipe do Studio"],
     "preco": "Sob consulta"},
]

CSS = """
.servicos{padding:88px 0; background:var(--white);}
.servicos .head{max-width:640px; margin-bottom:48px;}
.servicos .head h2{font-size:clamp(26px,3vw,36px);}
.servicos-grid{display:grid; grid-template-columns:1fr 1fr; gap:22px;}
.serv-card{
  background:var(--porcelain); border:1px solid var(--line); border-radius:20px; padding:30px;
  display:flex; flex-direction:column;
}
.serv-head{display:flex; align-items:center; gap:13px; margin-bottom:14px;}
.serv-head .ico{
  width:40px; height:40px; border-radius:12px; flex-shrink:0; background:var(--ink);
  display:flex; align-items:center; justify-content:center; color:var(--nude-2);
}
.serv-head h3{font-size:20px;}
.serv-card > p{font-size:14px; color:var(--ink-2); margin-bottom:16px;}
.serv-list{display:flex; flex-wrap:wrap; gap:8px; margin-bottom:20px;}
.serv-list span{
  font-size:12px; font-weight:600; color:var(--nude-deep);
  background:var(--white); border:1px solid var(--line);
  padding:6px 11px; border-radius:999px;
}
.serv-foot{display:flex; align-items:center; justify-content:space-between; gap:14px; margin-top:auto; padding-top:6px;}
.serv-price{font-family:'Fraunces',serif; font-size:15.5px; color:var(--ink);}
@media(max-width:860px){
  .servicos-grid{grid-template-columns:1fr;}
  .serv-foot{flex-direction:column; align-items:flex-start; gap:12px;}
}

.espaco{padding:88px 0; background:var(--porcelain);}
.espaco-inner{display:grid; grid-template-columns:1fr 1fr; gap:56px; align-items:center;}
.espaco-inner h2{font-size:clamp(26px,3.2vw,36px); margin:14px 0 16px;}
.espaco-inner p{max-width:440px; margin-bottom:18px;}
.espaco-address{font-size:14.5px; font-weight:600; color:var(--nude-deep); margin-bottom:26px; display:flex; align-items:center; gap:8px; width:fit-content;}
.espaco-address:hover{text-decoration:underline;}
.espaco-photo{border-radius:14px; aspect-ratio:4/3; overflow:hidden; border:1px solid var(--line); box-shadow:0 24px 50px rgba(26,23,20,0.18);}
.espaco-photo iframe{width:100%; height:100%; border:0; display:block; filter:grayscale(0.35) sepia(0.08) saturate(0.9);}
@media(max-width:860px){
  .espaco-inner{grid-template-columns:1fr;}
  .espaco-photo{order:-1;}
}

/* "Quem está à frente" com destaque — faixa escura entre duas seções claras. */
.sobre{background:linear-gradient(160deg, var(--ink-2), var(--ink));}
.sobre .eyebrow{color:var(--nude-2);}
.sobre .eyebrow::before{background:var(--gold);}
.sobre .sobre-story h2{color:var(--porcelain);}
.sobre .sobre-story p{color:rgba(246,241,234,0.8);}
.sobre .signature{color:var(--nude-2);}
.sobre .sobre-photo{border-color:rgba(246,241,234,0.16); box-shadow:0 30px 60px rgba(0,0,0,0.4);}
.sobre .stats-row{display:flex; gap:28px; margin-top:22px; flex-wrap:wrap;}
.sobre .stat b{display:block; font-family:'Fraunces',serif; font-size:24px; color:var(--nude-2);}
.sobre .stat span{font-size:12px; color:rgba(246,241,234,0.65); text-transform:uppercase; letter-spacing:0.6px;}

.resultados{padding:80px 0 88px; background:var(--white);}
.resultados .head{max-width:680px; margin:0 auto 40px; text-align:center;}
.resultados .head .eyebrow{justify-content:center;}
.resultados .head h2{font-size:clamp(26px,3.2vw,36px);}
.turmas-carousel-viewport{
  overflow:hidden; width:100%; margin-top:12px;
  -webkit-mask-image:linear-gradient(90deg, transparent 0, #000 6%, #000 94%, transparent 100%);
  mask-image:linear-gradient(90deg, transparent 0, #000 6%, #000 94%, transparent 100%);
}
.turmas-track{display:flex; gap:20px; width:max-content; animation:turmas-scroll 34s linear infinite; animation-play-state:paused;}
.turmas-track.ready{animation-play-state:running;}
.turmas-carousel-viewport:hover .turmas-track.ready{animation-play-state:paused;}
@keyframes turmas-scroll{from{transform:translateX(0);} to{transform:translateX(-50%);}}
.turmas-photo{
  position:relative; flex:0 0 270px; border-radius:16px; overflow:hidden;
  aspect-ratio:4/5; box-shadow:0 18px 36px -16px rgba(26,23,20,0.3); border:1px solid var(--line);
}
.turmas-photo img{width:100%; height:100%; object-fit:cover; display:block;}
@media (max-width:700px){.turmas-photo{flex:0 0 200px;}}
"""

galeria = "\n".join(
    f'      <div class="galeria-photo reveal"><img src="{IMAGES[f"trab_{i}"]}" alt="Trabalho do Studio Gisele Quintino"></div>'
    for i in range(1, 9)
)

resultado_keys = sorted((k for k in IMAGES if k.startswith("resultado_")), key=lambda k: int(k.split("_")[1]))
resultados_html = "\n".join(
    f'      <div class="turmas-photo"><img src="{IMAGES[k]}" alt="Resultado de cliente do Studio Gisele Quintino"></div>'
    for k in resultado_keys
)

serv_cards = ""
for s in SERVICOS:
    pills = "".join(f"<span>{it}</span>" for it in s["itens"])
    serv_cards += f"""
      <div class="serv-card reveal">
        <div class="serv-head"><span class="ico">{s['ico']}</span><h3>{s['nome']}</h3></div>
        <p>{s['desc']}</p>
        <div class="serv-list">{pills}</div>
        <div class="serv-foot">
          <span class="serv-price">{s['preco']}</span>
          <a class="btn btn-ink btn-sm" href="{TRINKS}" target="_blank" rel="noopener">Ver horários e agendar</a>
        </div>
      </div>"""

HTML = f"""{head("Studio Gisele Quintino | Cabelo, Beleza e Bem-Estar em São José do Rio Preto",
              "Mechas, coloração, cortes, tratamentos capilares, mega hair, sobrancelhas e mais no Studio Gisele Quintino, em São José do Rio Preto. Agende seu horário.",
              path="")}
<style>
{FONTS}

:root{{{PALETTE}}}
{BASE_CSS}
{CSS}
</style>
</head>
<body>

<div class="topbar">
  <div class="topbar-inner">
    <a class="logo" href="/">Studio <span>Gisele Quintino</span></a>
    <nav class="nav-pill">
      <a href="#servicos">Serviços</a>
      <a href="#galeria">Trabalhos</a>
      <a href="#sobre">Equipe</a>
      <a href="#espaco">Espaço</a>
      <a href="#faq">Dúvidas</a>
    </nav>
    <a class="btn btn-ink btn-sm" href="{TRINKS}" target="_blank" rel="noopener">Agendar horário</a>
  </div>
</div>

<section class="hero">
  <div class="wrap hero-inner">
    <div>
      <div class="eyebrow">Studio Gisele Quintino</div>
      <h1>Beleza e <em>bem-estar</em> em um só lugar</h1>
      <p class="lead">Cabelo, sobrancelha, unha e cuidados especiais num espaço pensado pra sua experiência do início ao fim. Em São José do Rio Preto.</p>
      <div class="hero-ctas">
        <a class="btn btn-ink" href="{TRINKS}" target="_blank" rel="noopener">Ver horários e agendar</a>
        <a class="btn btn-outline" href="{WA_AGENDAR}" target="_blank">Chamar no WhatsApp</a>
      </div>
    </div>
    <div class="hero-photo-wrap reveal">
      <img src="{IMAGES['perfil_hero']}" alt="Gisele Quintino">
      <div class="hero-badge"><div class="dot"></div><span>+8 mil seguidores no Instagram</span></div>
    </div>
  </div>
</section>

<section class="ticker">
  <div class="ticker-track">
    <span class="ticker-item">STUDIO GISELE QUINTINO</span><span class="ticker-dot"></span>
    <span class="ticker-item">CABELO &middot; SOBRANCELHA &middot; UNHA</span><span class="ticker-dot"></span>
    <span class="ticker-item">MECHAS &amp; COLORAÇÃO</span><span class="ticker-dot"></span>
    <span class="ticker-item">SÃO JOSÉ DO RIO PRETO</span><span class="ticker-dot"></span>
    <span class="ticker-item">STUDIO GISELE QUINTINO</span><span class="ticker-dot"></span>
    <span class="ticker-item">CABELO &middot; SOBRANCELHA &middot; UNHA</span><span class="ticker-dot"></span>
    <span class="ticker-item">MECHAS &amp; COLORAÇÃO</span><span class="ticker-dot"></span>
    <span class="ticker-item">SÃO JOSÉ DO RIO PRETO</span><span class="ticker-dot"></span>
  </div>
</section>

<section class="galeria" id="galeria">
  <div class="wrap">
    <div class="head reveal">
      <div class="eyebrow">Trabalhos</div>
      <h2>Resultados com técnica e acabamento impecável</h2>
    </div>
    <div class="galeria-grid">
{galeria}
    </div>
  </div>
</section>

<section class="servicos" id="servicos">
  <div class="wrap">
    <div class="head reveal">
      <div class="eyebrow">Serviços</div>
      <h2>Tudo o que a gente cuida por aqui</h2>
      <p style="margin-top:14px;">Confira os horários disponíveis e agende direto pelo nosso sistema — ou chame no WhatsApp.</p>
    </div>
    <div class="servicos-grid">{serv_cards}
    </div>
  </div>
</section>

<section class="sobre" id="sobre">
  <div class="wrap">
    <div class="sobre-photo reveal">
      <img src="{IMAGES['perfil_sobre']}" alt="Equipe do Studio Gisele Quintino">
    </div>
    <div class="sobre-story reveal">
      <div class="eyebrow">Quem está à frente</div>
      <h2>Mais de 20 anos de beleza e bem-estar</h2>
      <p>O Studio Gisele Quintino é um espaço de beleza e bem-estar em São José do Rio Preto, criado para oferecer diferentes cuidados em um só lugar.</p>
      <p>Com atuação especialmente reconhecida no universo dos cabelos, o Studio reúne serviços como cortes, luzes, coloração, hidratação e terapia capilar, além de cuidados com sobrancelhas, pele, unhas e maquiagem.</p>
      <p>À frente do Studio está Gisele Quintino, profissional com mais de 20 anos de experiência no mercado da beleza e uma trajetória construída também na educação de cabeleireiros no Brasil e no exterior.</p>
      <div class="stats-row">
        <div class="stat"><b>20+</b><span>Anos de experiência</span></div>
        <div class="stat"><b>8 mil+</b><span>Seguidores no Instagram</span></div>
      </div>
      <div class="signature">Gisele Quintino</div>
    </div>
  </div>
</section>

<section class="resultados">
  <div class="wrap">
    <div class="head reveal">
      <div class="eyebrow">Mais resultados</div>
      <h2>Clientes que já viveram essa experiência</h2>
    </div>
  </div>
  <div class="turmas-carousel-viewport">
    <div class="turmas-track">
{resultados_html}
    </div>
  </div>
</section>

<section class="espaco" id="espaco">
  <div class="wrap espaco-inner">
    <div class="reveal">
      <div class="eyebrow">Onde ficamos</div>
      <h2>Venha viver essa experiência</h2>
      <p>Atendimento em São José do Rio Preto, num espaço pensado pra proporcionar cuidado, técnica e valorização da sua beleza.</p>
      <a class="espaco-address" href="https://www.google.com/maps/search/?api=1&query={ENDERECO_Q}" target="_blank">{ENDERECO}</a>
      <a class="btn btn-ink" href="{TRINKS}" target="_blank" rel="noopener">Ver horários e agendar</a>
    </div>
    <div class="espaco-photo reveal">
      <iframe src="https://www.google.com/maps?q={ENDERECO_Q}&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
    </div>
  </div>
</section>

<section class="faq" id="faq">
  <div class="wrap">
    <div class="head reveal">
      <div class="eyebrow">Dúvidas frequentes</div>
      <h2>Antes de você agendar</h2>
    </div>
    <details class="faq-item reveal">
      <summary>Como faço pra agendar um horário? <span class="plus">+</span></summary>
      <p>Direto pelo nosso sistema de agendamento online ou chamando no WhatsApp — você escolhe o serviço, o dia e o horário que funcionam melhor pra você.</p>
    </details>
    <details class="faq-item reveal">
      <summary>Quais serviços o Studio oferece? <span class="plus">+</span></summary>
      <p>Cabelo (cortes, mechas, coloração, tratamentos, mega hair), sobrancelhas, depilação, unhas e produção de penteados e maquiagem.</p>
    </details>
    <details class="faq-item reveal">
      <summary>Os valores estão atualizados? <span class="plus">+</span></summary>
      <p>Os valores de partida estão listados em cada serviço. Alguns procedimentos variam de acordo com comprimento, técnica e produto — confirme o valor exato no agendamento.</p>
    </details>
    <details class="faq-item reveal">
      <summary>A Gisele também dá cursos para cabeleireiros? <span class="plus">+</span></summary>
      <p>Sim! Gisele Quintino é educadora internacional, especialista em mechas e colorimetria. Fale com a equipe do Studio pra saber mais.</p>
    </details>
    <details class="faq-item reveal">
      <summary>Onde fica o Studio? <span class="plus">+</span></summary>
      <p>Na {ENDERECO}.</p>
    </details>
  </div>
</section>

<section class="cta-final">
  <div class="wrap">
    <h2 class="reveal">Pronta pra cuidar de você no Studio Gisele Quintino?</h2>
    <p class="reveal">Confira os horários disponíveis e agende seu horário agora mesmo.</p>
    <a class="btn btn-ink reveal" href="{TRINKS}" target="_blank" rel="noopener">Ver horários e agendar</a>
  </div>
</section>

<footer>
  <div class="wrap">
    <div class="footer-grid">
      <div class="footer-brand">
        <div class="logo">Studio Gisele Quintino</div>
        <p>Cabelo, sobrancelha, unha e bem-estar em São José do Rio Preto. Atendimento técnico, acolhedor e de alto padrão.</p>
        {NOTADO_CREDIT}
      </div>
      <div class="footer-col">
        <h4>Studio</h4>
        <a href="{TRINKS}" target="_blank" rel="noopener">Ver horários e agendar</a>
        <a href="{WA_AGENDAR}" target="_blank">Chamar no WhatsApp</a>
        <a href="/bio">Link da bio</a>
      </div>
      <div class="footer-col">
        <h4>Redes</h4>
        <a href="{INSTAGRAM}" target="_blank">Instagram</a>
      </div>
    </div>
    <div class="foot">
      <span>© 2026 Studio Gisele Quintino. Todos os direitos reservados.</span>
      <span>{CTA_NOTADO_ESCURO}</span>
    </div>
  </div>
</footer>

<script>{REVEAL_JS}
{CARROSSEL_JS}</script>

</body>
</html>
"""

out = os.path.join(SITE, "index.html")
with open(out, "w", encoding="utf-8") as f:
    f.write(HTML)
print("index.html gerado:", len(HTML), "chars")
