import os, io, base64
from PIL import Image, ImageOps

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FOTOS = os.path.join(SITE, "fotos")


def to_b64(path, max_side, quality, crop_ratio=None, top_bias=0.5):
    img = Image.open(path)
    img = ImageOps.exif_transpose(img)
    img = img.convert("RGB")

    if crop_ratio:
        w, h = img.size
        cur_ratio = w / h
        if cur_ratio > crop_ratio:
            new_w = int(h * crop_ratio)
            offset = int((w - new_w) * top_bias)
            img = img.crop((offset, 0, offset + new_w, h))
        else:
            new_h = int(w / crop_ratio)
            offset = int((h - new_h) * top_bias)
            img = img.crop((0, offset, w, offset + new_h))

    w, h = img.size
    side = max(w, h)
    if side > max_side:
        scale = max_side / side
        img = img.resize((int(w * scale), int(h * scale)), Image.LANCZOS)

    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=quality, optimize=True)
    return f"data:image/jpeg;base64,{base64.b64encode(buf.getvalue()).decode('ascii')}"


IMAGES = {}

# Perfil 571...: retrato de evento, terno azul-serenity, editorial — pro hero.
# Perfil 607...: foto de equipe no Studio (parede com logo em madeira) — pro "sobre".
PERFIL_HERO = os.path.join(FOTOS, "perfil", "saveclip.app-571749694-18364854922153933-1884547118609498220-n.jpg")
PERFIL_SOBRE = os.path.join(FOTOS, "perfil", "saveclip.app-607649641-18423654595114826-8053701832904481713-n.jpg")
IMAGES["perfil_hero"] = to_b64(PERFIL_HERO, 820, 80, crop_ratio=4 / 5, top_bias=0.08)
IMAGES["perfil_sobre"] = to_b64(PERFIL_SOBRE, 860, 80, crop_ratio=4 / 5, top_bias=0.02)

# Galeria: 8 resultados reais (mechas, corte, sobrancelha, unha)
TRABALHOS = os.path.join(FOTOS, "trabalhos")
GALERIA = [
    "saveclip.app-581699234-18417816337114826-5373332472238673508-n.jpg",  # volume/mechas loiro
    "saveclip.app-505895582-1550493289257162-4671523773056259197-n.jpg",   # sobrancelha macro
    "saveclip.app-506360571-23961073813559336-4883518365276499158-n.jpg",  # corte tesoura
    "saveclip.app-543654494-18405845746114826-3988309232258306272-n.jpg",  # mechas loiro volumoso
    "saveclip.app-659117184-18442570681114826-8268694881529733594-n.jpg",  # mechas castanho volumoso
    "saveclip.app-504516566-18394238038114826-931896548609875215-n.jpg",   # unha desenho azul
    "saveclip.app-588090206-18496827796075041-102490480819838689-n.jpg",   # unha nude
    "saveclip.app-654029771-18517057147075041-240919256819682125-n.jpg",   # mechas platinado
]
for i, nome in enumerate(GALERIA, start=1):
    IMAGES[f"trab_{i}"] = to_b64(os.path.join(TRABALHOS, nome), 520, 71, crop_ratio=3 / 4, top_bias=0.18)
for i, nome in enumerate(GALERIA, start=1):
    IMAGES[f"chip_{i}"] = to_b64(os.path.join(TRABALHOS, nome), 150, 70, crop_ratio=1, top_bias=0.15)

# "Resultados" (turma, mas aqui são clientes glam — não certificados): usados
# como segunda leva da galeria/ticker de prova social, 8, 4:5
RESULT = os.path.join(FOTOS, "turma")
resultados = sorted(n for n in os.listdir(RESULT) if not n.startswith("."))
for i, nome in enumerate(resultados, start=1):
    IMAGES[f"resultado_{i}"] = to_b64(os.path.join(RESULT, nome), 420, 68, crop_ratio=4 / 5, top_bias=0.12)

with open(os.path.join(os.path.dirname(__file__), "images_b64.py"), "w", encoding="utf-8") as f:
    f.write("IMAGES = {\n")
    for k, v in IMAGES.items():
        f.write(f"  {k!r}: {v!r},\n")
    f.write("}\n")

total_kb = sum(len(v) for v in IMAGES.values()) / 1024
print(f"Gerado images_b64.py com {len(IMAGES)} imagens, ~{total_kb:.0f}KB de base64 total")
