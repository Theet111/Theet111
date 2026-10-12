"""Regenerate the static System 7 inspired PNG artwork for the README."""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).parent
BLACK = "#202326"
WHITE = "#fffefa"
WALL = "#b8d4cc"
DOT = "#9dbeb7"
SHADOW = "#657772"
FONT_REGULAR = "C:/Windows/Fonts/arial.ttf"
FONT_BOLD = "C:/Windows/Fonts/arialbd.ttf"


def font(size, bold=False):
    return ImageFont.truetype(FONT_BOLD if bold else FONT_REGULAR, size)


def text_center(draw, x, y, value, size, bold=False, color=BLACK):
    f = font(size, bold)
    box = draw.textbbox((0, 0), value, font=f)
    draw.text((x - (box[2] - box[0]) / 2, y), value, font=f, fill=color)


def wallpaper(image):
    d = ImageDraw.Draw(image)
    d.rectangle((0, 0, image.width, image.height), fill=WALL)
    for y in range(0, image.height, 5):
        for x in range(0 if (y // 5) % 2 == 0 else 2, image.width, 5):
            d.point((x, y), fill=DOT)
    return d


def apple(draw):
    draw.ellipse((24, 13, 43, 40), fill=BLACK)
    draw.ellipse((38, 13, 57, 40), fill=BLACK)
    draw.polygon([(23, 26), (29, 44), (36, 47), (41, 43), (48, 47), (55, 43), (59, 26)], fill=BLACK)
    draw.ellipse((53, 18, 65, 30), fill=WHITE)
    draw.ellipse((41, 4, 53, 15), fill=BLACK)


def title_window(draw, box, title, close=True):
    x0, y0, x1, y1 = box
    draw.rectangle((x0 + 7, y0 + 7, x1 + 7, y1 + 7), fill=SHADOW)
    draw.rectangle(box, fill=WHITE, outline=BLACK, width=3)
    for yy in range(y0 + 9, y0 + 37, 4):
        draw.line((x0 + 8, yy, x1 - 8, yy), fill="#626a68", width=1)
    draw.rectangle((x0 + 8, y0 + 6, x0 + 43, y0 + 40), fill=WHITE)
    if close:
        draw.rectangle((x0 + 13, y0 + 12, x0 + 33, y0 + 32), fill=WHITE, outline=BLACK, width=3)
    label_width = int(draw.textlength(title, font=font(23, True))) + 34
    draw.rectangle((540 - label_width // 2, y0 + 4, 540 + label_width // 2, y0 + 42), fill=WHITE)
    text_center(draw, 540, y0 + 11, title, 23, True)
    draw.line((x0 + 2, y0 + 45, x1 - 2, y0 + 45), fill=BLACK, width=3)


header = Image.new("RGB", (1080, 330))
d = wallpaper(header)
d.rectangle((0, 0, 1079, 51), fill=WHITE)
d.line((0, 51, 1079, 51), fill=BLACK, width=3)
apple(d)
for label, x in [("File", 86), ("Edit", 153), ("View", 223), ("Label", 300), ("Special", 380)]:
    d.text((x, 13), label, font=font(23), fill=BLACK)
d.text((970, 14), "Finder", font=font(21, True), fill=BLACK)

title_window(d, (35, 70, 1045, 246), "About This Macintosh")
d.rectangle((74, 138, 139, 211), fill="#d9d9d7", outline=BLACK, width=4)
d.rectangle((82, 147, 131, 190), fill=WHITE, outline=BLACK, width=3)
d.point((96, 163), fill=BLACK)
d.point((117, 163), fill=BLACK)
d.arc((95, 167, 119, 182), 0, 180, fill=BLACK, width=3)
d.rectangle((98, 211, 116, 218), fill=BLACK)
d.line((85, 218, 129, 218), fill=BLACK, width=4)
d.text((172, 140), "Purv Mistry", font=font(31, True), fill=BLACK)
d.text((173, 182), "Full-Stack Developer", font=font(21), fill=BLACK)
d.text((173, 211), "Designer  ·  Open-Source Contributor", font=font(18), fill=BLACK)

title_window(d, (28, 264, 1052, 329), "Macintosh HD")
d.rectangle((31, 311, 1049, 326), fill=WHITE)
d.text((48, 310), "6 items", font=font(14), fill=BLACK)
d.text((802, 310), "Click an icon to open", font=font(14), fill=BLACK)
header.save(OUT / "header.png", optimize=True)


def icon_drawing(kind, color):
    """Small pixel-art symbol, enlarged with nearest-neighbor scaling."""
    im = Image.new("RGBA", (36, 36), (0, 0, 0, 0))
    p = ImageDraw.Draw(im)
    if kind == "about":
        p.rectangle((5, 2, 30, 33), fill="#f7f3e8", outline=BLACK, width=2)
        p.rectangle((9, 7, 26, 13), fill=color, outline=BLACK)
        p.ellipse((13, 16, 22, 24), fill="#f1c3a3", outline=BLACK)
        p.polygon([(9, 30), (11, 25), (18, 23), (25, 25), (27, 30)], fill=color, outline=BLACK)
    elif kind == "apps":
        p.rectangle((2, 11, 33, 31), fill="#bf8632", outline=BLACK, width=2)
        p.polygon([(2, 11), (2, 6), (14, 6), (18, 11)], fill="#ffd96f", outline=BLACK)
        p.rectangle((3, 13, 32, 29), fill=color, outline=BLACK, width=2)
        p.line((5, 16, 29, 16), fill="#fff3be", width=2)
    elif kind == "projects":
        p.polygon([(6, 7), (29, 7), (33, 18), (3, 18)], fill="#c6e9a0", outline=BLACK)
        p.rectangle((3, 18, 33, 31), fill=color, outline=BLACK, width=2)
        p.line((6, 21, 30, 21), fill="#e4f6c8", width=2)
        p.rectangle((8, 26, 10, 28), fill=BLACK)
        p.rectangle((14, 26, 16, 28), fill=BLACK)
    elif kind == "music":
        p.ellipse((3, 5, 31, 33), fill=color, outline=BLACK, width=2)
        p.ellipse((12, 14, 22, 24), fill=WHITE, outline=BLACK)
        p.line((25, 8, 25, 24), fill=BLACK, width=2)
        p.line((17, 11, 25, 8), fill=BLACK, width=2)
        p.ellipse((12, 22, 18, 28), fill=BLACK)
        p.line((17, 11, 17, 24), fill=BLACK, width=2)
    elif kind == "network":
        p.line((18, 8, 18, 20), fill=BLACK, width=3)
        p.line((18, 19, 6, 28), fill=BLACK, width=3)
        p.line((18, 19, 30, 28), fill=BLACK, width=3)
        for x, y in [(18, 7), (6, 29), (30, 29)]:
            p.ellipse((x - 5, y - 5, x + 5, y + 5), fill=color, outline=BLACK, width=2)
    elif kind == "quotes":
        p.polygon([(3, 5), (33, 5), (33, 26), (15, 26), (8, 33), (9, 26), (3, 26)], fill=color, outline=BLACK)
        p.rectangle((9, 11, 15, 17), fill=WHITE, outline=BLACK)
        p.rectangle((21, 11, 27, 17), fill=WHITE, outline=BLACK)
        p.line((12, 17, 9, 21), fill=BLACK, width=2)
        p.line((24, 17, 21, 21), fill=BLACK, width=2)
    return im.resize((90, 90), Image.Resampling.NEAREST)


def icon_image(label, kind, color, filename, column, bottom):
    image = Image.new("RGB", (360, 158), WHITE)
    d = ImageDraw.Draw(image)
    if column == 0:
        d.rectangle((0, 0, 27, 157), fill=WALL)
        for y in range(0, 158, 5):
            for x in range(0, 28, 5):
                d.point((x, y), fill=DOT)
        d.line((28, 0, 28, 157), fill=BLACK, width=3)
    if column == 2:
        d.rectangle((333, 0, 359, 157), fill=WALL)
        for y in range(0, 158, 5):
            for x in range(333, 360, 5):
                d.point((x, y), fill=DOT)
        d.line((332, 0, 332, 157), fill=BLACK, width=3)
    if bottom:
        d.line((28 if column == 0 else 0, 155, 332 if column == 2 else 359, 155), fill=BLACK, width=3)
    symbol = icon_drawing(kind, color)
    image.paste(symbol, (135, 15), symbol)
    text_center(d, 180, 111, label, 20, True)
    image.save(OUT / filename, optimize=True)


for i, spec in enumerate([
    ("About Me", "about", "#658cd0", "about-me.png"),
    ("Applications", "apps", "#f1bd43", "applications.png"),
    ("Projects", "projects", "#84bf68", "projects.png"),
    ("Music", "music", "#d46aa9", "music.png"),
    ("Network", "network", "#51bfc6", "network.png"),
    ("Quotes", "quotes", "#9d85d3", "quotes.png"),
]):
    icon_image(*spec, i % 3, i >= 3)


def trash_symbol():
    im = Image.new("RGBA", (36, 36), (0, 0, 0, 0))
    p = ImageDraw.Draw(im)
    p.rectangle((8, 5, 28, 9), fill="#eef4f2", outline=BLACK, width=2)
    p.rectangle((13, 2, 23, 5), fill="#eef4f2", outline=BLACK)
    p.polygon([(10, 10), (27, 10), (25, 32), (12, 32)], fill="#d7e0dc", outline=BLACK)
    for x in [15, 19, 23]:
        p.line((x, 14, x, 28), fill="#7c8e89", width=2)
    return im.resize((72, 72), Image.Resampling.NEAREST)


footer = Image.new("RGB", (900, 114))
wallpaper(footer)
footer.save(OUT / "footer.png", optimize=True)
trash = Image.new("RGB", (180, 114))
td = wallpaper(trash)
symbol = trash_symbol()
trash.paste(symbol, (54, 0), symbol)
text_center(td, 90, 76, "Trash", 18, True)
trash.save(OUT / "trash.png", optimize=True)


for name, title, subtitle, kind, color in [
    ("about", "About Me", "Purv Mistry", "about", "#658cd0"),
    ("applications", "Applications", "Deployed websites and tools", "apps", "#f1bd43"),
    ("music", "Music", "Hand-picked listening card", "music", "#d46aa9"),
    ("network", "Network", "Where to find me", "network", "#51bfc6"),
    ("quotes", "Quotes", "TV and game character lines", "quotes", "#9d85d3"),
    ("trash", "Trash", "A little Pawnee surprise", "trash", "#d7e0dc"),
]:
    page = Image.new("RGB", (960, 150))
    pd = wallpaper(page)
    pd.rectangle((24, 17, 948, 142), fill=SHADOW)
    pd.rectangle((17, 10, 941, 135), fill=WHITE, outline=BLACK, width=3)
    for yy in range(18, 48, 4):
        pd.line((25, yy, 933, yy), fill="#626a68")
    pd.rectangle((23, 15, 57, 51), fill=WHITE)
    pd.rectangle((29, 22, 48, 41), fill=WHITE, outline=BLACK, width=3)
    label_width = int(pd.textlength(title, font=font(23, True))) + 38
    pd.rectangle((480 - label_width // 2, 13, 480 + label_width // 2, 53), fill=WHITE)
    text_center(pd, 480, 19, title, 23, True)
    pd.line((19, 55, 939, 55), fill=BLACK, width=3)
    source_symbol = trash_symbol() if kind == "trash" else icon_drawing(kind, color)
    symbol = source_symbol.resize((65, 65), Image.Resampling.NEAREST)
    page.paste(symbol, (65, 64), symbol)
    pd.text((159, 70), title, font=font(25, True), fill=BLACK)
    pd.text((160, 103), subtitle, font=font(18), fill=BLACK)
    page.save(OUT / f"page-{name}.png", optimize=True)
