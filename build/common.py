import urllib.parse

SITE = "/Users/carlacosta/Documents/PROJETOS CLAUDE CODE/notado/colecao/gisele-quintino/studio-gisele-quintino"
SLUG = "studiogiselequintino"
TRACK_SLUG = "studiogiselequintino"  # linha nova, criada na entrega — sem afid

WA_NUM = "5517997594469"
INSTAGRAM = "https://www.instagram.com/studiogiselequintino/"
ENDERECO = "R. Jorge Tibiriçá, 2473 - Boa Vista, São José do Rio Preto - SP, 15025-060"
ENDERECO_Q = urllib.parse.quote(ENDERECO)
TRINKS = "https://www.trinks.com/espaco-gi-quintino"


def wa(msg):
    return f"https://wa.me/{WA_NUM}?text={urllib.parse.quote(msg)}"


CHECK_SVG = ('<svg viewBox="0 0 24 24" width="12" height="12" fill="none" stroke="currentColor" '
             'stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12.5L9.5 18L20 6"/></svg>')

CTA_NOTADO_ESCURO = (
    f'<a href="https://track.notado.site/l/{TRACK_SLUG}" target="_blank" class="cta-notado" '
    f'style="color:#F6F1EA; font-weight:700; font-size:12.5px; text-decoration:none;">'
    f'<svg width="15" height="15" viewBox="0 0 512 512" style="display:inline-block; vertical-align:-2px; margin-right:6px;" aria-hidden="true">'
    f'<rect width="512" height="512" rx="120" fill="#F0522B"/><circle cx="256" cy="256" r="86" fill="#FBF7F3"/></svg>'
    f'Quer um assim também? <br class="cta-quebra">Clique aqui e faça o seu! 🧡</a>'
)

CTA_NOTADO_CLARO = (
    f'<a href="https://track.notado.site/l/{TRACK_SLUG}" target="_blank" '
    f'style="color:#1A1714; font-weight:700; font-size:12.5px; text-decoration:none;">'
    f'Quer um assim também? <br>Clique aqui e faça o seu! 🧡</a>'
)

NOTADO_CREDIT = f'''<a href="https://track.notado.site/l/{TRACK_SLUG}" target="_blank" class="notado-credit" aria-label="Site criado pela notado.site">
          <span class="notado-credit-label">Site criado por</span>
          <span class="notado-lockup">
            <svg viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><rect width="512" height="512" rx="120" fill="#F0522B"/><circle cx="256" cy="256" r="86" fill="#FBF7F3"/></svg>
            <span class="notado-lockup-text">notado<span class="notado-dot"></span><span class="notado-ext">site</span></span>
          </span>
        </a>'''

# Paleta Studio Gisele Quintino: preto + nude + dourado sobre porcelana —
# salão de alto padrão (briefing pediu Preto/Nude; dourado é o acento
# editorial, presente na sinalização de madeira do próprio salão).
PALETTE = """
  --ink:#1A1714;
  --ink-2:#3A342E;
  --nude:#C7A98C;
  --nude-2:#E3D2BE;
  --nude-deep:#A9855F;
  --gold:#B08D57;
  --gold-light:#D3B786;
  --porcelain:#F6F1EA;
  --white:#FFFFFF;
  --slate:#8A8078;
  --line: rgba(26,23,20,0.13);
"""

FONTS = "@import url('https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;1,9..144,500&family=Inter:wght@400;500;600;700;800&family=Fredoka:wght@500&display=swap');"

BASE_CSS = """
*{box-sizing:border-box; margin:0; padding:0;}
html{scroll-behavior:smooth;}
body{
  font-family:'Inter', sans-serif;
  color:var(--ink);
  background:var(--porcelain);
  -webkit-font-smoothing:antialiased;
  overflow-x:hidden;
}
h1,h2,h3{font-family:'Fraunces', serif; font-weight:500; line-height:1.16; color:var(--ink);}
p{line-height:1.7; color:var(--ink-2);}
a{text-decoration:none; color:inherit;}
img{max-width:100%; display:block;}
.wrap{max-width:1120px; margin:0 auto; padding:0 24px;}

.eyebrow{
  display:flex; align-items:center; gap:10px;
  font-size:12.5px; font-weight:700; letter-spacing:2.5px; text-transform:uppercase;
  color:var(--nude-deep); margin-bottom:14px;
}
.eyebrow::before{content:""; width:26px; height:1px; background:var(--gold);}

.topbar{
  position:sticky; top:0; z-index:50;
  background:rgba(246,241,234,0.92); backdrop-filter:blur(10px);
  border-bottom:1px solid var(--line);
}
.topbar-inner{
  max-width:1120px; margin:0 auto; padding:16px 24px;
  display:flex; align-items:center; justify-content:space-between;
}
.logo{font-family:'Fraunces', serif; font-size:21px; letter-spacing:0.2px; font-weight:500; color:var(--ink);}
.logo span{color:var(--nude-deep); font-style:italic;}
.nav-pill{
  display:flex; align-items:center; gap:4px;
  background:rgba(26,23,20,0.05); border:1px solid var(--line); border-radius:999px; padding:6px;
}
.nav-pill a{
  padding:9px 16px; font-size:13.5px; font-weight:500; border-radius:999px; color:var(--ink);
  transition:background .2s, color .2s;
}
.nav-pill a:hover{background:var(--ink); color:var(--porcelain);}
.btn{
  display:inline-flex; align-items:center; justify-content:center; gap:8px;
  padding:13px 26px; border-radius:999px; font-weight:600; font-size:14px;
  cursor:pointer; border:1px solid transparent; transition:transform .2s, box-shadow .2s, background .2s;
}
.btn-ink{background:linear-gradient(135deg, var(--ink-2), var(--ink)); color:var(--porcelain);}
.btn-ink:hover{transform:translateY(-2px); box-shadow:0 10px 24px rgba(26,23,20,0.3);}
.btn-outline{background:transparent; border:1.5px solid var(--ink); color:var(--ink);}
.btn-outline:hover{background:var(--ink); color:var(--porcelain);}
.btn-sm{padding:10px 18px; font-size:13px;}

.hero{padding:74px 0 56px;}
.hero-inner{display:grid; grid-template-columns:1.05fr 0.95fr; gap:56px; align-items:center;}
.hero h1{font-size:clamp(30px,4vw,46px); margin-bottom:20px;}
.hero h1 em{font-style:italic; color:var(--nude-deep);}
.hero p.lead{font-size:16.5px; max-width:480px; margin-bottom:32px;}
.hero-ctas{display:flex; gap:14px; flex-wrap:wrap;}
.hero-photo-wrap{
  position:relative; border-radius:18px; overflow:hidden;
  aspect-ratio:4/5; box-shadow:0 30px 60px rgba(26,23,20,0.28); border:1px solid var(--line);
}
.hero-photo-wrap img{width:100%; height:100%; object-fit:cover;}
.hero-badge{
  position:absolute; left:20px; bottom:20px;
  background:rgba(26,23,20,0.82); backdrop-filter:blur(6px); border:1px solid rgba(246,241,234,0.15);
  border-radius:14px; padding:13px 17px; display:flex; align-items:center; gap:10px;
  box-shadow:0 12px 30px rgba(0,0,0,0.25);
}
.hero-badge .dot{width:9px; height:9px; border-radius:50%; background:var(--gold-light); flex-shrink:0;}
.hero-badge span{font-size:12.5px; font-weight:600; color:var(--porcelain);}

.ticker{background:var(--ink); overflow:hidden; padding:13px 0;}
.ticker-track{display:flex; gap:36px; align-items:center; width:max-content; animation:ticker-scroll 32s linear infinite;}
.ticker:hover .ticker-track{animation-play-state:paused;}
@keyframes ticker-scroll{from{transform:translateX(0);} to{transform:translateX(-50%);}}
.ticker-item{font-family:'Inter'; font-size:12.5px; font-weight:700; letter-spacing:2px; text-transform:uppercase; color:var(--nude-2); white-space:nowrap;}
.ticker-dot{width:5px; height:5px; border-radius:50%; background:rgba(246,241,234,0.3); flex-shrink:0;}

.galeria{padding:88px 0; background:var(--white);}
.galeria .head{max-width:640px; margin-bottom:40px;}
.galeria .head h2{font-size:clamp(26px,3.2vw,36px);}
.galeria-grid{display:grid; grid-template-columns:repeat(4,1fr); gap:16px;}
.galeria-photo{border-radius:14px; overflow:hidden; aspect-ratio:3/4; box-shadow:0 14px 30px rgba(26,23,20,0.13); border:1px solid var(--line);}
.galeria-photo img{width:100%; height:100%; object-fit:cover; display:block; transition:transform .4s ease;}
.galeria-photo:hover img{transform:scale(1.06);}
@media(max-width:860px){.galeria-grid{grid-template-columns:repeat(2,1fr);}}

.sobre{padding:88px 0;}
.sobre .wrap{display:grid; grid-template-columns:0.9fr 1.1fr; gap:56px; align-items:center;}
.sobre-photo{border-radius:18px; overflow:hidden; aspect-ratio:4/5; box-shadow:0 24px 50px rgba(26,23,20,0.22); border:1px solid var(--line);}
.sobre-photo img{width:100%; height:100%; object-fit:cover;}
.sobre-story h2{font-size:clamp(26px,3vw,34px); margin-bottom:20px;}
.sobre-story p{margin-bottom:14px; font-size:15px;}
.signature{font-family:'Fraunces', serif; font-style:italic; font-size:20px; margin-top:18px; color:var(--nude-deep);}

.faq{padding:88px 0; background:var(--white);}
.faq .head{max-width:640px; margin-bottom:40px;}
.faq .head h2{font-size:clamp(26px,3vw,34px);}
.faq-item{border-bottom:1px solid var(--line); padding:22px 0;}
.faq-item summary{
  cursor:pointer; list-style:none; display:flex; align-items:center; justify-content:space-between;
  font-weight:600; font-size:15.5px; font-family:'Inter'; color:var(--ink);
}
.faq-item summary::-webkit-details-marker{display:none;}
.faq-item summary .plus{font-size:20px; color:var(--nude-deep); transition:transform .2s;}
.faq-item[open] summary .plus{transform:rotate(45deg);}
.faq-item p{margin-top:12px; font-size:14.5px; max-width:640px;}

.cta-final{padding:96px 0; text-align:center; background:linear-gradient(135deg, var(--ink-2), var(--ink)); color:var(--porcelain);}
.cta-final h2{color:var(--porcelain); font-size:clamp(28px,3.6vw,44px); max-width:680px; margin:0 auto 18px;}
.cta-final p{color:rgba(246,241,234,0.8); max-width:520px; margin:0 auto 32px; font-size:16px;}
.cta-final .btn-ink{background:var(--nude); color:var(--ink);}
.cta-final .btn-ink:hover{background:var(--nude-2); box-shadow:0 10px 24px rgba(0,0,0,0.3);}

footer{background:var(--ink); color:rgba(246,241,234,0.7); padding:64px 0 28px;}
.footer-grid{
  display:grid; grid-template-columns:1.4fr 1fr 1fr; gap:40px;
  padding-bottom:40px; border-bottom:1px solid rgba(246,241,234,0.14);
}
.footer-brand .logo{color:var(--porcelain); font-size:19px; margin-bottom:12px;}
.footer-brand .logo span{color:var(--nude-light,var(--gold-light));}
.footer-brand p{color:rgba(246,241,234,0.55); font-size:13.5px; max-width:270px; line-height:1.6;}
.notado-credit{display:inline-flex; flex-direction:column; gap:7px; margin-top:22px; text-decoration:none; width:fit-content;}
.notado-credit-label{font-size:10.5px; font-weight:600; letter-spacing:0.8px; text-transform:uppercase; color:rgba(246,241,234,0.4);}
.notado-lockup{display:flex; align-items:center; font-family:'Fredoka', sans-serif; font-weight:500; font-size:15px;}
.notado-lockup svg{width:0.95em; height:0.95em; margin-right:0.4167em; flex-shrink:0; display:block;}
.notado-lockup-text{color:#F6F1EA;}
.notado-dot{display:inline-block; width:0.19em; height:0.19em; border-radius:50%; background:#F0522B; margin-left:0.03em;}
.notado-ext{color:#F0522B; margin-left:0.04em;}
.footer-col h4{
  color:var(--porcelain); font-size:12px; font-weight:700; text-transform:uppercase;
  letter-spacing:1px; margin-bottom:16px;
}
.footer-col a{display:block; font-size:14px; color:rgba(246,241,234,0.6); margin-bottom:12px;}
.footer-col a:hover{color:var(--nude-light,var(--gold-light));}
.foot{
  display:flex; flex-wrap:wrap; align-items:center; justify-content:space-between; gap:10px;
  font-size:12.5px; color:rgba(246,241,234,0.4); margin-top:24px;
}
.foot a{color:rgba(246,241,234,0.6); text-decoration:none;}
.foot a:hover{color:var(--gold-light);}
.cta-notado{white-space:nowrap;}
.cta-quebra{display:none;}
@media(max-width:860px){
  .footer-grid{grid-template-columns:1fr 1fr; gap:32px;}
  .footer-brand{grid-column:1 / -1;}
  .cta-notado{white-space:normal;}
  .cta-quebra{display:block;}
}
@media(max-width:560px){
  .footer-grid{grid-template-columns:1fr; gap:28px;}
  .foot{flex-direction:column; align-items:flex-start;}
}

.js .reveal{opacity:0; transform:translateY(24px); transition:opacity .7s ease, transform .7s ease;}
.js .reveal.in{opacity:1; transform:translateY(0);}

@media(max-width:860px){
  .hero-inner{grid-template-columns:1fr;}
  .hero-photo-wrap{order:-1; max-width:380px; margin:0 auto;}
  .sobre .wrap{grid-template-columns:1fr;}
  .sobre-photo{max-width:340px; margin:0 auto;}
  .nav-pill{display:none;}
}
"""

REVEAL_JS = """
(function(){
  var els = document.querySelectorAll('.reveal');
  if(!('IntersectionObserver' in window)){ els.forEach(function(el){ el.classList.add('in'); }); return; }
  var io = new IntersectionObserver(function(entries){
    entries.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target); } });
  }, {threshold:0.12, rootMargin:'0px 0px -5% 0px'});
  els.forEach(function(el){ io.observe(el); });
  setTimeout(function(){ els.forEach(function(el){ el.classList.add('in'); }); }, 2500);
})();
"""

CARROSSEL_JS = """
(function(){
  var track = document.querySelector('.turmas-track');
  if(!track) return;
  Array.prototype.slice.call(track.children).forEach(function(el){
    var c = el.cloneNode(true);
    c.setAttribute('aria-hidden', 'true');
    c.querySelectorAll('img').forEach(function(i){ i.alt = ''; });
    track.appendChild(c);
  });
  var imgs = Array.prototype.slice.call(track.querySelectorAll('img'));
  var pending = imgs.length;
  function ready(){ pending--; if(pending <= 0){ track.classList.add('ready'); } }
  imgs.forEach(function(img){
    if(img.complete){ ready(); }
    else { img.addEventListener('load', ready); img.addEventListener('error', ready); }
  });
})();
"""


def head(title, description, path=""):
    url = f"https://{SLUG}.pages.dev/{path}"
    og = f"https://{SLUG}.pages.dev/{path}og-image.jpg"
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:image" content="{og}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="{og}">
<script>document.documentElement.className = 'js';</script>"""
