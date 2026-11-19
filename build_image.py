#!/usr/bin/env python3
"""Build entry.png for make.fun competition news-image-20261119.

Draws a newspaper-front-page infographic summing up Thursday
19 November 2026 world news: a masthead naming the day, a lead
story on the first Trump-Xi-Putin summit in Shenzhen, and twelve
more stories from every region and beat, each with a small drawn
motif. Everything is drawn with Pillow; no AI-generated imagery
or text in the image. Run:  python3 build_image.py
(writes entry.png next to this file)
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "entry.png")

W, H = 1024, 1024
PAPER = (247, 244, 236)
INK = (24, 24, 22)
RED = (163, 24, 44)
BLUE = (30, 58, 96)
GRAY = (98, 94, 86)
RULE = (186, 180, 166)
CARD = (255, 255, 255)
EDGE = (212, 205, 190)
LEAD_BG = (240, 236, 226)
SKY = (214, 228, 238)
SEA = (158, 190, 212)

FD = "/usr/share/fonts/truetype/noto"
SERIF = os.path.join(FD, "NotoSerif-Bold.ttf")
SANS = os.path.join(FD, "NotoSans-Regular.ttf")
SANS_B = os.path.join(FD, "NotoSans-Bold.ttf")
SANS_X = os.path.join(FD, "NotoSans-Black.ttf")


def fnt(path, size):
    return ImageFont.truetype(path, size)


def wrap(d, text, font, max_w):
    lines, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_wrapped(d, x, y, text, font, max_w, fill, leading=None):
    if leading is None:
        leading = int(font.size * 1.3)
    for line in wrap(d, text, font, max_w):
        d.text((x, y), line, font=font, fill=fill)
        y += leading
    return y


def spaced(d, cx, y, text, font, fill, gap=6):
    widths = [d.textlength(ch, font=font) for ch in text]
    total = sum(widths) + gap * (len(text) - 1)
    x = cx - total / 2
    for ch, w in zip(text, widths):
        d.text((x, y), ch, font=font, fill=fill)
        x += w + gap
    return y + font.size


def num_badge(d, x, y, n, dia=26):
    d.ellipse([x, y, x + dia, y + dia], fill=RED)
    f = fnt(SANS_B, 15)
    t = str(n)
    tw = d.textlength(t, font=f)
    d.text((x + (dia - tw) / 2, y + (dia - f.size) / 2 - 1), t,
           font=f, fill=(255, 255, 255))


# ---- small motifs, each drawn inside an s x s box at (x, y) ----
def motif_bridge(d, x, y, s):
    d.rectangle([x, y, x + s, y + s], fill=SKY)
    wy = y + int(s * 0.66)
    d.rectangle([x, wy, x + s, y + s], fill=SEA)
    dy = wy - int(s * 0.30)
    d.line([(x + 3, dy), (x + int(s * 0.34), dy)], fill=INK, width=5)
    d.line([(x + int(s * 0.66), dy), (x + s - 3, dy)], fill=INK, width=5)
    d.line([(x + 8, dy), (x + 8, wy)], fill=INK, width=4)
    d.line([(x + s - 9, dy), (x + s - 9, wy)], fill=INK, width=4)
    # red burst marking the strike in the gap
    import math
    bx, by = x + s // 2, dy - 2
    for ang in range(0, 360, 45):
        a = math.radians(ang)
        d.line([(bx, by), (bx + int(8 * math.cos(a)), by + int(8 * math.sin(a)))],
               fill=RED, width=2)
    d.ellipse([bx - 3, by - 3, bx + 3, by + 3], fill=RED)


def motif_mine(d, x, y, s):
    d.rectangle([x, y, x + s, y + s], fill=SKY)
    d.rectangle([x, y + int(s * 0.62), x + s, y + s], fill=SEA)
    # tanker hull
    d.rectangle([x + 3, y + int(s * 0.42), x + s - 3, y + int(s * 0.62)],
                fill=(120, 40, 40))
    d.rectangle([x + 8, y + int(s * 0.30), x + int(s * 0.55),
                 y + int(s * 0.42)], fill=(120, 40, 40))
    # spiked mine
    cx, cy, r = x + int(s * 0.74), y + int(s * 0.30), 7
    for ang in range(0, 360, 45):
        import math
        a = math.radians(ang)
        d.line([(cx + int((r - 1) * math.cos(a)), cy + int((r - 1) * math.sin(a))),
                (cx + int((r + 5) * math.cos(a)), cy + int((r + 5) * math.sin(a)))],
               fill=INK, width=2)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=INK)


def motif_scales(d, x, y, s):
    d.rectangle([x, y, x + s, y + s], fill=(232, 228, 216))
    cx = x + s // 2
    d.line([(cx, y + 5), (cx, y + s - 8)], fill=INK, width=3)
    d.line([(x + 6, y + 10), (x + s - 6, y + 10)], fill=INK, width=3)
    for sx in (x + 9, x + s - 9):
        d.line([(sx, y + 10), (sx - 5, y + 10)], fill=INK, width=1)
        d.line([(sx, y + 10), (sx, y + 26)], fill=INK, width=2)
        d.arc([sx - 8, y + 24, sx + 8, y + 38], 0, 180, fill=INK, width=3)
    d.line([(x + 8, y + s - 8), (x + s - 8, y + s - 8)], fill=INK, width=3)


def motif_chart(d, x, y, s):
    d.rectangle([x, y, x + s, y + s], fill=(232, 228, 216))
    d.line([(x + 6, y + s - 8), (x + s - 6, y + s - 8)], fill=GRAY, width=2)
    d.line([(x + 6, y + s - 8), (x + 6, y + 6)], fill=GRAY, width=2)
    pts = [(x + 9, y + s - 16), (x + 17, y + s - 22), (x + 25, y + s - 18),
           (x + 33, y + 14), (x + s - 8, y + 8)]
    d.line(pts, fill=RED, width=3)
    d.polygon([(x + s - 8, y + 8), (x + s - 16, y + 8), (x + s - 8, y + 16)],
              fill=RED)


def motif_globe(d, x, y, s):
    d.rectangle([x, y, x + s, y + s], fill=SKY)
    cx, cy, r = x + s // 2, y + s // 2, s // 2 - 3
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(90, 150, 90),
              outline=BLUE, width=2)
    d.arc([cx - r, cy - r, cx + r, cy + r], 90, 270, fill=BLUE, width=2)
    d.line([(cx, cy - r), (cx, cy + r)], fill=BLUE, width=2)
    d.line([(cx - r, cy), (cx + r, cy)], fill=BLUE, width=2)
    # leaf
    d.pieslice([cx + 2, cy - 2, cx + 16, cy + 12], 270, 90, fill=(40, 110, 50))


def motif_gauge(d, x, y, s):
    d.rectangle([x, y, x + s, y + s], fill=(232, 228, 216))
    cx, cy = x + s // 2, y + s - 8
    d.arc([x + 4, y + 6, x + s - 4, y + s + 6], 180, 360, fill=GRAY, width=4)
    import math
    a = math.radians(225)
    d.line([(cx, cy), (cx + int(16 * math.cos(a)), cy + int(16 * math.sin(a)))],
           fill=RED, width=3)
    d.ellipse([cx - 4, cy - 4, cx + 4, cy + 4], fill=INK)
    f = fnt(SANS_B, 13)
    t = "4.7%"
    d.text((x + (s - d.textlength(t, font=f)) / 2, y + s - 16), t,
           font=f, fill=INK)


def motif_dome(d, x, y, s):
    d.rectangle([x, y, x + s, y + s], fill=SKY)
    cx = x + s // 2
    d.rectangle([cx - 16, y + s - 16, cx + 16, y + s - 6], fill=(255, 255, 255),
                outline=INK, width=2)
    d.pieslice([cx - 12, y + 6, cx + 12, y + s - 14], 180, 360,
               fill=(255, 255, 255), outline=INK, width=2)
    d.rectangle([cx - 2, y + 2, cx + 2, y + 8], fill=INK)
    for px in (cx - 11, cx - 4, cx + 3, cx + 10):
        d.line([(px, y + s - 16), (px, y + s - 8)], fill=INK, width=2)


def motif_virus(d, x, y, s):
    d.rectangle([x, y, x + s, y + s], fill=(232, 228, 216))
    import math
    cx, cy, r = x + s // 2, y + s // 2, 11
    for ang in range(0, 360, 30):
        a = math.radians(ang)
        d.line([(cx + int(r * math.cos(a)), cy + int(r * math.sin(a))),
                (cx + int((r + 7) * math.cos(a)), cy + int((r + 7) * math.sin(a)))],
               fill=RED, width=2)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=RED)
    d.ellipse([cx - 4, cy - 5, cx + 1, cy], fill=(255, 255, 255))


def motif_frame(d, x, y, s):
    d.rectangle([x, y, x + s, y + s], fill=(232, 228, 216))
    d.rectangle([x + 6, y + 6, x + s - 6, y + s - 6], fill=(70, 110, 170),
                outline=(150, 110, 40), width=3)
    # sunflower: yellow petals around a brown centre
    import math
    cx, cy = x + s // 2, y + s // 2 + 2
    for ang in range(0, 360, 30):
        a = math.radians(ang)
        d.ellipse([cx + int(13 * math.cos(a)) - 4, cy + int(13 * math.sin(a)) - 4,
                   cx + int(13 * math.cos(a)) + 4, cy + int(13 * math.sin(a)) + 4],
                  fill=(240, 200, 40))
    d.ellipse([cx - 7, cy - 7, cx + 7, cy + 7], fill=(110, 70, 30))
    d.line([(cx, cy + 7), (cx, y + s - 8)], fill=(40, 110, 50), width=3)


def motif_flame(d, x, y, s):
    d.rectangle([x, y, x + s, y + s], fill=(232, 228, 216))
    cx = x + s // 2
    d.polygon([(cx, y + 4), (cx + 12, y + 22), (cx + 8, y + 30),
               (cx + 12, y + s - 8), (cx - 12, y + s - 8), (cx - 8, y + 30),
               (cx - 12, y + 22)], fill=(220, 90, 20))
    d.polygon([(cx, y + 18), (cx + 6, y + 28), (cx + 4, y + s - 10),
               (cx - 4, y + s - 10), (cx - 6, y + 28)], fill=(250, 200, 40))


def motif_atom(d, x, y, s):
    d.rectangle([x, y, x + s, y + s], fill=(232, 228, 216))
    import math
    cx, cy = x + s // 2, y + s // 2
    for rot in (0, 60, 120):
        th = math.radians(rot)
        pts = []
        for k in range(37):
            t = 2 * math.pi * k / 36
            px = 17 * math.cos(t)
            py = 7 * math.sin(t)
            rx = px * math.cos(th) - py * math.sin(th)
            ry = px * math.sin(th) + py * math.cos(th)
            pts.append((cx + rx, cy + ry))
        d.line(pts, fill=BLUE, width=2)
    d.ellipse([cx - 4, cy - 4, cx + 4, cy + 4], fill=RED)


def motif_tower(d, x, y, s):
    d.rectangle([x, y, x + s, y + s], fill=SKY)
    cx = x + s // 2
    d.rectangle([cx - 9, y + 12, cx + 9, y + s - 6], fill=(120, 120, 130),
                outline=INK, width=2)
    for yy in range(y + 16, y + s - 10, 7):
        d.line([(cx - 6, yy), (cx + 6, yy)], fill=INK, width=1)
    # impact burst at the top
    import math
    bx, by = cx, y + 10
    for ang in range(0, 360, 45):
        a = math.radians(ang)
        d.line([(bx, by), (bx + int(11 * math.cos(a)), by + int(11 * math.sin(a)))],
               fill=RED, width=2)
    d.ellipse([bx - 4, by - 4, bx + 4, by + 4], fill=RED)


def motif_flags(d, x, y, w, h):
    """Three flag panels (US, China, Russia) for the lead story."""
    pw = (w - 20) // 3
    labels = ["USA", "CHINA", "RUSSIA"]
    for i in range(3):
        fx = x + i * (pw + 10)
        if i == 0:  # United States: stripes + blue canton
            for s in range(7):
                d.rectangle([fx, y + s * (h // 7), fx + pw,
                             y + (s + 1) * (h // 7)],
                            fill=(178, 34, 52) if s % 2 == 0 else (255, 255, 255))
            d.rectangle([fx, y, fx + int(pw * 0.45), y + int(h * 0.55)],
                        fill=BLUE)
            for r in range(3):
                for c in range(3):
                    d.ellipse([fx + 4 + c * 11, y + 5 + r * 11,
                               fx + 8 + c * 11, y + 9 + r * 11],
                              fill=(255, 255, 255))
        elif i == 1:  # China: red field, yellow stars
            d.rectangle([fx, y, fx + pw, y + h], fill=(222, 41, 16))
            d.polygon([(fx + 12, y + 8), (fx + 16, y + 18), (fx + 26, y + 18),
                       (fx + 18, y + 24), (fx + 21, y + 34), (fx + 12, y + 28),
                       (fx + 3, y + 34), (fx + 6, y + 24), (fx - 2, y + 18),
                       (fx + 8, y + 18)], fill=(255, 222, 0))
            for sx, sy in ((fx + pw - 12, y + 8), (fx + pw - 10, y + 22)):
                d.ellipse([sx - 3, sy - 3, sx + 3, sy + 3], fill=(255, 222, 0))
        else:  # Russia: white, blue, red horizontal bands
            d.rectangle([fx, y, fx + pw, y + h // 3], fill=(255, 255, 255))
            d.rectangle([fx, y + h // 3, fx + pw, y + 2 * h // 3], fill=(0, 57, 166))
            d.rectangle([fx, y + 2 * h // 3, fx + pw, y + h], fill=(213, 0, 50))
        d.rectangle([fx, y, fx + pw, y + h], outline=INK, width=2)
        f = fnt(SANS_B, 14)
        t = labels[i]
        d.text((fx + (pw - d.textlength(t, font=f)) / 2, y + h + 5),
               t, font=f, fill=INK)


LEAD = ("Trump, Xi and Putin meet",
        "The first-ever trilateral summit opens in Shenzhen, on the "
        "APEC sidelines, with Ukraine and nuclear arms on the table.")

STORIES = [
    ("Kerch Bridge hit again",
     "Ukraine strikes the bridge a third time in four days; rail "
     "traffic halts.", motif_bridge),
    ("Iran widens the war",
     "Tehran hits Kuwait and Bahrain after US strikes on Qeshm "
     "Island; mines hit tankers off Hormuz.",
     motif_mine),
    ("Rohingya case decided",
     "The World Court rules on Gambia's genocide case against "
     "Myanmar.", motif_scales),
    ("Anthropic prices its IPO",
     "The AI firm prices shares at $83 ahead of its Nasdaq debut.",
     motif_chart),
    ("COP31 talks stall",
     "Ministers in Antalya push to unblock climate negotiations.",
     motif_globe),
    ("Inflation hits 4.7%",
     "The IMF chief warns global inflation has reached 4.7%.",
     motif_gauge),
    ("Jeffries to lead House",
     "Hakeem Jeffries is set to become the first African-American "
     "Speaker.", motif_dome),
    ("Measles returns in US",
     "Measles spreads again, ending 26 years of elimination in "
     "the US.", motif_virus),
    ("Van Gogh sets record",
     "A Van Gogh sells for $190.4 million, an artist record.",
     motif_frame),
    ("Unrest in Bangladesh",
     "Protests spread as Yunus's ancestral home is set on fire.",
     motif_flame),
    ("North Korea enriches more",
     "The IAEA says North Korea expanded uranium enrichment.",
     motif_atom),
    ("Missile hits Riyadh tower",
     "A Houthi missile damages a Saudi wealth fund tower in "
     "Riyadh.", motif_tower),
]


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    M = 36
    CW = W - 2 * M

    # ---- masthead ----
    y = 16
    spaced(d, W // 2, y, "THE WORLD IN ONE IMAGE", fnt(SANS_B, 19), GRAY, gap=6)
    y += 28
    f_mast = fnt(SERIF, 58)
    mast = "THE WORLD TODAY"
    d.text(((W - d.textlength(mast, font=f_mast)) / 2, y), mast,
           font=f_mast, fill=INK)
    y += 72
    d.line([(M, y), (W - M, y)], fill=INK, width=4)
    y += 5
    d.line([(M, y), (W - M, y)], fill=INK, width=1)
    y += 10
    f_date = fnt(SANS_X, 38)
    date = "Thursday 19 November 2026"
    d.text(((W - d.textlength(date, font=f_date)) / 2, y), date,
           font=f_date, fill=RED)
    y += 52
    d.line([(M, y), (W - M, y)], fill=INK, width=1)
    y += 10

    # ---- lead story ----
    lead_h = 168
    d.rectangle([M, y, W - M, y + lead_h], fill=LEAD_BG, outline=EDGE, width=1)
    d.rectangle([M, y, W - M, y + 5], fill=RED)
    lx, ly = M + 20, y + 16
    num_badge(d, lx, ly + 2, 1, dia=30)
    tx = lx + 44
    f_lh = fnt(SERIF, 34)
    hl = wrap(d, LEAD[0], f_lh, CW - 44 - 20 - 300)
    assert len(hl) == 1, f"lead headline wraps: {hl}"
    y2 = draw_wrapped(d, tx, ly, LEAD[0], f_lh, CW - 44 - 20 - 300, INK,
                      leading=40)
    f_lb = fnt(SANS, 22)
    bl = wrap(d, LEAD[1], f_lb, CW - 44 - 20 - 300)
    assert len(bl) <= 4, f"lead body too long: {bl}"
    draw_wrapped(d, tx, y2 + 6, LEAD[1], f_lb, CW - 44 - 20 - 300, INK,
                 leading=28)
    motif_flags(d, W - M - 20 - 292, y + 22, 292, 104)
    y += lead_h + 10

    # ---- grid: 12 stories, 3 columns x 4 rows ----
    gap = 10
    cols = 3
    cell_w = (CW - (cols - 1) * gap) // cols
    cell_h = 140
    grid_top = y
    f_head = fnt(SERIF, 20)
    f_body = fnt(SANS, 17)
    for idx, (head, body, motif) in enumerate(STORIES):
        r, c = divmod(idx, cols)
        cx = M + c * (cell_w + gap)
        cy = grid_top + r * (cell_h + gap)
        d.rectangle([cx, cy, cx + cell_w, cy + cell_h], fill=CARD,
                    outline=EDGE, width=1)
        num_badge(d, cx + 10, cy + 10, idx + 2, dia=26)
        motif(d, cx + cell_w - 56, cy + 10, 46)
        hw = cell_w - 46 - 66
        hl = wrap(d, head, f_head, hw)
        assert len(hl) <= 2, f"headline wraps too much: {hl}"
        yy = draw_wrapped(d, cx + 44, cy + 11, head, f_head, hw, INK,
                          leading=23)
        bl = wrap(d, body, f_body, cell_w - 20)
        assert len(bl) <= 3, f"body too long: {bl}"
        draw_wrapped(d, cx + 10, cy + 62, body, f_body, cell_w - 20,
                     (52, 50, 46), leading=21)
    y = grid_top + 4 * cell_h + 3 * gap + 10

    # ---- footer ----
    d.line([(M, y), (W - M, y)], fill=RULE, width=1)
    y += 8
    f_foot = fnt(SANS_B, 16)
    foot = "Thursday 19 November 2026  \u00b7  THE WORLD TODAY"
    d.text(((W - d.textlength(foot, font=f_foot)) / 2, y), foot,
           font=f_foot, fill=GRAY)

    assert y + 22 <= H, "content overflowed the page"
    img.save(OUT, format="PNG", optimize=True)
    print(f"wrote {OUT}  {W}x{H}  {os.path.getsize(OUT)} bytes")


if __name__ == "__main__":
    main()
