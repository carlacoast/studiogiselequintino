import os
from PIL import Image, ImageDraw, ImageFont, ImageOps

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERO = os.path.join(SITE, "fotos", "perfil", "2.jpg")

W, H = 1200, 630
SPLIT = 760
SAFE_LEFT = 285
SAFE_RIGHT = 915

BG = (246, 241, 234)     # --porcelain
INK = (26, 23, 20)       # --ink
NUDE_DEEP = (169, 133, 95)  # --nude-deep

NAME_FONT = "/System/Library/Fonts/Supplemental/Didot.ttc"
ROLE_FONT = "/System/Library/Fonts/HelveticaNeue.ttc"


def fit_photo(path, w, h):
    img = Image.open(path)
    img = ImageOps.exif_transpose(img).convert("RGB")
    return ImageOps.fit(img, (w, h), method=Image.LANCZOS, centering=(0.5, 0.1))


def make_card(out_path, name, role, tag, name_font_index=0):
    canvas = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(canvas)

    photo = fit_photo(HERO, W - SPLIT, H)
    canvas.paste(photo, (SPLIT, 0))

    shadow = Image.new("RGBA", (30, H), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    for i in range(30):
        sd.line([(i, 0), (i, H)], fill=(0, 0, 0, int(90 * (1 - i / 30))))
    canvas.paste(shadow, (SPLIT, 0), shadow)

    try:
        name_font = ImageFont.truetype(NAME_FONT, 66, index=name_font_index)
    except Exception:
        name_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/BigCaslon.ttf", 64)
    role_font = ImageFont.truetype(ROLE_FONT, 16, index=1)
    tag_font = ImageFont.truetype(ROLE_FONT, 17, index=1)

    pad_left = SAFE_LEFT + 25
    y_role = 214
    draw.line([(pad_left, y_role - 22), (pad_left + 40, y_role - 22)], fill=NUDE_DEEP, width=2)
    x = pad_left
    for ch in role.upper():
        draw.text((x, y_role), ch, font=role_font, fill=NUDE_DEEP)
        x += draw.textlength(ch, font=role_font) + 2

    y_name = y_role + 46
    words = name.split(" ")
    if len(words) <= 1:
        line1, line2 = words[0], ""
    else:
        cut = (len(words) + 1) // 2
        line1 = " ".join(words[:cut])
        line2 = " ".join(words[cut:])
    draw.text((pad_left, y_name), line1, font=name_font, fill=INK)
    if line2:
        bbox = draw.textbbox((0, 0), line1, font=name_font)
        line_h = (bbox[3] - bbox[1]) + 16
        draw.text((pad_left, y_name + line_h), line2, font=name_font, fill=INK)
        name_bbox = draw.textbbox((pad_left, y_name + line_h), line2, font=name_font)
    else:
        name_bbox = draw.textbbox((pad_left, y_name), line1, font=name_font)

    draw.text((pad_left, name_bbox[3] + 24), tag, font=tag_font, fill=NUDE_DEEP)

    canvas.save(out_path, "JPEG", quality=90)
    crop = canvas.crop((SAFE_LEFT, 0, SAFE_RIGHT, H))
    crop.save(out_path.replace(".jpg", "-crop-preview.jpg"), "JPEG", quality=90)
    print("saved", out_path)


make_card(os.path.join(SITE, "og-image.jpg"),
          "Studio Gisele Quintino", "São José do Rio Preto",
          "CABELO · SOBRANCELHA · UNHA · BEM-ESTAR")
