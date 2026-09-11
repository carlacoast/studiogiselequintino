import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from images_b64 import IMAGES
from common import SITE, wa, INSTAGRAM, NOTADO_CREDIT, CTA_NOTADO_CLARO, PALETTE, FONTS, TRINKS, head

WA_BIO = wa("Olá! Vim pelo link da bio do Instagram e gostaria de agendar um horário.")

chip_keys = sorted((k for k in IMAGES if k.startswith("chip_")), key=lambda k: int(k.split("_")[1]))
chips_vis = "".join(f'<div class="nail-chip"><img src="{IMAGES[k]}" alt="Trabalho"></div>\n' for k in chip_keys)
chips_dup = "".join(f'<div class="nail-chip" aria-hidden="true"><img src="{IMAGES[k]}" alt=""></div>\n' for k in chip_keys)

CHEV = ('<svg class="chev" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        'stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M9 6l6 6-6 6"/></svg>')
ICON_STUDIO = ('<svg width="19" height="19" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
               '<path d="M12 2l2.1 6.1L20 10l-5.9 1.9L12 18l-2.1-6.1L4 10l5.9-1.9z"/>'
               '<path d="M18.5 14l.9 2.6 2.6.9-2.6.9-.9 2.6-.9-2.6-2.6-.9 2.6-.9z"/></svg>')
ICON_AGENDA = ('<svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
               'stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M16 3v4M8 3v4M3 10h18"/></svg>')
ICON_WA = ('<svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
           'stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.4 8.4 0 0 1-12.3 7.4L3 20.5l1.7-5.6A8.4 8.4 0 1 1 21 11.5Z"/></svg>')
ICON_IG = ('<svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
           'stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1"/></svg>')

HTML = f"""{head("Studio Gisele Quintino | Cabelo, Beleza e Bem-Estar",
              "Studio Gisele Quintino, em São José do Rio Preto: cabelo, sobrancelha, unha e bem-estar num só lugar.")}
<style>
{FONTS}
:root{{{PALETTE}}}
*{{box-sizing:border-box; margin:0; padding:0;}}
a{{text-decoration:none; color:inherit;}}
body{{
  font-family:'Inter', sans-serif;
  background:linear-gradient(180deg, #E7DCCB, var(--porcelain));
  min-height:100vh;
  display:flex; align-items:center; justify-content:center;
  padding:32px 16px;
  color:var(--ink);
}}
.card{{
  width:100%; max-width:420px;
  background:var(--white);
  border-radius:26px;
  overflow:hidden;
  border:1px solid var(--line);
  box-shadow:0 30px 70px rgba(26,23,20,0.25);
}}
.hero-photo{{position:relative; aspect-ratio:4/5; width:100%;}}
.hero-photo img{{width:100%; height:100%; object-fit:cover; display:block;}}
.nail-strip{{
  position:absolute; left:16px; right:16px; bottom:16px;
  background:rgba(26,23,20,0.36); backdrop-filter:blur(10px); -webkit-backdrop-filter:blur(10px);
  border:1px solid rgba(246,241,234,0.35);
  border-radius:16px; padding:7px; overflow:hidden;
  box-shadow:0 10px 24px rgba(0,0,0,0.3);
  -webkit-mask-image:linear-gradient(90deg, transparent 0, #000 8%, #000 92%, transparent 100%);
  mask-image:linear-gradient(90deg, transparent 0, #000 8%, #000 92%, transparent 100%);
}}
.nail-strip-track{{display:flex; gap:7px; width:max-content; animation:nail-scroll 55s linear infinite; animation-play-state:paused;}}
.nail-strip-track.ready{{animation-play-state:running;}}
.nail-strip:hover .nail-strip-track.ready{{animation-play-state:paused;}}
@keyframes nail-scroll{{from{{transform:translateX(0);}} to{{transform:translateX(-50%);}}}}
.nail-chip{{flex:0 0 50px; height:50px; border-radius:10px; overflow:hidden;}}
.nail-chip img{{width:100%; height:100%; object-fit:cover; display:block;}}

.name-block{{padding:24px 26px 0; text-align:center;}}
.name-block h1{{font-family:'Fraunces', serif; font-weight:500; font-size:25px; line-height:1.18; color:var(--ink);}}
.name-block .role{{margin-top:8px; font-size:11.5px; font-weight:700; letter-spacing:1.6px; text-transform:uppercase; color:var(--nude-deep);}}
.info{{padding:14px 26px 6px; text-align:center;}}
.info .stats{{font-size:15px; color:var(--slate); font-weight:500;}}

.links{{display:flex; flex-direction:column; gap:12px; padding:18px 22px 6px;}}
.link-card{{
  display:flex; align-items:center; gap:14px;
  background:var(--porcelain); border:1px solid var(--line); border-radius:16px; padding:14px 16px;
  transition:transform .15s ease, box-shadow .15s ease;
}}
.link-card:hover{{transform:translateY(-2px); box-shadow:0 12px 24px rgba(26,23,20,0.15);}}
.link-card .icon{{
  flex-shrink:0; width:42px; height:42px; border-radius:50%;
  background:linear-gradient(135deg, var(--nude), var(--nude-deep));
  display:flex; align-items:center; justify-content:center; color:var(--white);
}}
.link-card.alt .icon{{background:linear-gradient(135deg, var(--ink-2), var(--ink));}}
.link-card .txt{{flex:1; min-width:0;}}
.link-card .txt .t{{display:block; font-size:16px; font-weight:700; color:var(--ink);}}
.link-card .txt .s{{display:block; font-size:13px; color:var(--slate); margin-top:3px;}}
.link-card .chev{{flex-shrink:0; color:var(--nude-deep);}}

.social-row{{display:flex; align-items:center; justify-content:center; gap:14px; padding:20px 0 8px;}}
.social-row a{{
  width:40px; height:40px; border-radius:50%; border:1px solid var(--line);
  display:flex; align-items:center; justify-content:center; color:var(--ink);
  transition:border-color .15s ease, color .15s ease;
}}
.social-row a:hover{{border-color:var(--gold); color:var(--nude-deep);}}

.foot{{
  text-align:center; font-size:13px; color:rgba(26,23,20,0.5);
  padding:16px 20px 24px; border-top:1px solid var(--line); margin-top:8px;
  display:flex; flex-direction:column; align-items:center; gap:14px;
}}
.foot a{{color:var(--ink);}}
.notado-credit{{display:inline-flex; flex-direction:column; align-items:center; gap:7px; text-decoration:none;}}
.notado-credit-label{{font-size:10.5px; font-weight:600; letter-spacing:0.8px; text-transform:uppercase; color:rgba(26,23,20,0.4);}}
.notado-lockup{{display:flex; align-items:center; font-family:'Fredoka', sans-serif; font-weight:500; font-size:15px;}}
.notado-lockup svg{{width:0.95em; height:0.95em; margin-right:0.4167em; flex-shrink:0; display:block;}}
.notado-lockup-text{{color:#1A1714;}}
.notado-dot{{display:inline-block; width:0.19em; height:0.19em; border-radius:50%; background:#F0522B; margin-left:0.03em;}}
.notado-ext{{color:#F0522B; margin-left:0.04em;}}
</style>
</head>
<body>

<div class="card">
  <div class="hero-photo">
    <img src="{IMAGES['perfil_hero']}" alt="Studio Gisele Quintino">
    <div class="nail-strip">
      <div class="nail-strip-track">
{chips_vis}{chips_dup}      </div>
    </div>
  </div>

  <div class="name-block">
    <h1>Studio Gisele Quintino</h1>
    <div class="role">Cabelo &middot; Sobrancelha &middot; Unha &middot; Bem-Estar</div>
  </div>

  <div class="info">
    <div class="stats">São José do Rio Preto &middot; SP</div>
  </div>

  <div class="links">
    <a class="link-card alt" href="/">
      <span class="icon">{ICON_STUDIO}</span>
      <span class="txt">
        <span class="t">Conheça o Studio</span>
        <span class="s">Serviços, equipe e localização</span>
      </span>
      {CHEV}
    </a>

    <a class="link-card" href="{TRINKS}" target="_blank" rel="noopener">
      <span class="icon">{ICON_AGENDA}</span>
      <span class="txt">
        <span class="t">Ver horários e agendar</span>
        <span class="s">Agendamento online</span>
      </span>
      {CHEV}
    </a>

    <a class="link-card" href="{WA_BIO}" target="_blank">
      <span class="icon">{ICON_WA}</span>
      <span class="txt">
        <span class="t">Falar no WhatsApp</span>
        <span class="s">Tire dúvidas com a equipe</span>
      </span>
      {CHEV}
    </a>
  </div>

  <div class="social-row">
    <a href="{INSTAGRAM}" target="_blank" aria-label="Instagram">{ICON_IG}</a>
  </div>

  <div class="foot">
    {NOTADO_CREDIT}
    {CTA_NOTADO_CLARO}
  </div>
</div>

<script>
(function(){{
  var track = document.querySelector('.nail-strip-track');
  if(!track) return;
  var imgs = Array.prototype.slice.call(track.querySelectorAll('img'));
  var pending = imgs.length;
  function ready(){{ pending--; if(pending <= 0){{ track.classList.add('ready'); }} }}
  imgs.forEach(function(img){{
    if(img.complete){{ ready(); }}
    else {{ img.addEventListener('load', ready); img.addEventListener('error', ready); }}
  }});
}})();
</script>

</body>
</html>
"""

out = os.path.join(SITE, "bio.html")
with open(out, "w", encoding="utf-8") as f:
    f.write(HTML)
print("bio.html gerado:", len(HTML), "chars")
