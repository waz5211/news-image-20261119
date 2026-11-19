#!/usr/bin/env python3
"""Draw the front page for Thursday 19 November 2026.

Everything is drawn with Pillow primitives: a masthead, one lead story
about the first Trump-Xi-Putin trilateral summit in Shenzhen, and a
three-by-four grid of twelve shorter stories from the same day.
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (248, 244, 232)
INK = (20, 20, 20)
GREY = (90, 86, 76)
RED = (163, 22, 33)
BLUE = (29, 78, 137)
GOLD = (176, 141, 44)
RULE = (60, 56, 48)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap returning a list of lines that fit `width`."""
    lines, current = [], ""
    for word in text.split():
        trial = f"{current} {word}".strip()
        if draw.textlength(trial, font=fnt) <= width or not current:
            current = trial
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_text_block(draw, x, y, text, fnt, width, fill=INK, leading=None):
    """Draw wrapped text; return the y just below the last line."""
    if leading is None:
        leading = int(fnt.size * 1.28)
    for line in wrap(draw, text, fnt, width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


# (headline, summary, motif key) for the twelve short stories.
STORIES = [
    ("Kerch Bridge hit again",
     "Ukraine strikes the Crimea bridge for a third time in four days; rail traffic is halted.",
     "bridge"),
    ("Gulf crisis widens",
     "Iran hits Kuwait and Bahrain after US strikes on Qeshm Island; tankers are struck by mines.",
     "drop"),
    ("Rohingya ruling due",
     "The International Court of Justice rules in Gambia v. Myanmar over the Rohingya genocide case.",
     "scales"),
    ("Anthropic prices IPO",
     "Shares are priced at $83 ahead of the AI company's debut on the Nasdaq.",
     "chart"),
    ("COP31 talks stall",
     "Ministers in Antalya push to unblock the climate negotiations.",
     "globe"),
    ("Inflation at 4.7%",
     "IMF chief Georgieva warns that global inflation has reached 4.7%.",
     "percent"),
    ("Jeffries to lead House",
     "Hakeem Jeffries is set to become the first African-American Speaker of the US House.",
     "dome"),
    ("Measles returns",
     "Measles spreads again in the United States, ending 26 years of elimination.",
     "virus"),
    ("Van Gogh record",
     "A Van Gogh painting sells for $190.4 million, an artist record.",
     "frame"),
    ("Bangladesh unrest",
     "Protesters set fire to Yunus's ancestral home amid unrest.",
     "flame"),
    ("Korea enrichment grows",
     "The IAEA says North Korea has expanded uranium enrichment.",
     "atom"),
    ("Riyadh tower hit",
     "A Houthi missile damages a Saudi wealth fund tower in Riyadh.",
     "tower"),
]


def motif(draw, key, x, y, s=30):
    """Draw a tiny pictogram for one story inside a s-by-s box."""
    c = BLUE
    if key == "bridge":
        draw.line([(x, y + s * 0.7), (x + s, y + s * 0.7)], fill=c, width=3)
        draw.arc([x + 2, y + s * 0.15, x + s - 2, y + s * 0.85], 180, 360,
                 fill=c, width=3)
        draw.line([(x + s * 0.2, y + s * 0.3), (x + s * 0.2, y + s * 0.7)],
                  fill=c, width=3)
        draw.line([(x + s * 0.8, y + s * 0.3), (x + s * 0.8, y + s * 0.7)],
                  fill=c, width=3)
    elif key == "drop":
        draw.polygon([(x + s / 2, y + 2), (x + s - 3, y + s * 0.62),
                      (x + 3, y + s * 0.62)], fill=c)
        draw.ellipse([x + 3, y + s * 0.5, x + s - 3, y + s - 2], fill=c)
    elif key == "scales":
        draw.line([(x + s / 2, y + 2), (x + s / 2, y + s - 4)], fill=c, width=3)
        draw.line([(x + 3, y + s * 0.32), (x + s - 3, y + s * 0.32)],
                  fill=c, width=3)
        draw.arc([x + 2, y + s * 0.32, x + s * 0.38, y + s * 0.62], 0, 180,
                 fill=c, width=2)
        draw.arc([x + s * 0.62, y + s * 0.32, x + s - 2, y + s * 0.62], 0, 180,
                 fill=c, width=2)
        draw.line([(x + s * 0.28, y + s - 4), (x + s * 0.72, y + s - 4)],
                  fill=c, width=3)
    elif key == "chart":
        draw.line([(x + 3, y + s - 5), (x + 3, y + 4)], fill=c, width=2)
        draw.line([(x + 3, y + s - 5), (x + s - 3, y + s - 5)], fill=c, width=2)
        draw.line([(x + 5, y + s * 0.72), (x + s * 0.45, y + s * 0.5),
                   (x + s * 0.68, y + s * 0.6), (x + s - 4, y + 5)],
                  fill=c, width=3)
        draw.polygon([(x + s - 4, y + 5), (x + s - 11, y + 6),
                      (x + s - 5, y + 12)], fill=c)
    elif key == "globe":
        draw.ellipse([x + 2, y + 2, x + s - 2, y + s - 2], outline=c, width=3)
        draw.ellipse([x + s * 0.32, y + 2, x + s * 0.68, y + s - 2],
                     outline=c, width=2)
        draw.line([(x + 2, y + s / 2), (x + s - 2, y + s / 2)], fill=c, width=2)
        draw.arc([x + 2, y - s * 0.18, x + s - 2, y + s * 0.55], 300, 60,
                 fill=(34, 120, 60), width=3)
    elif key == "percent":
        f = font(SANS_B, s)
        draw.text((x + 2, y - 2), "%", font=f, fill=c)
    elif key == "dome":
        draw.arc([x + s * 0.22, y + 2, x + s * 0.78, y + s * 0.5], 180, 360,
                 fill=c, width=3)
        draw.rectangle([x + 4, y + s * 0.5, x + s - 4, y + s * 0.62], fill=c)
        draw.rectangle([x + 2, y + s * 0.62, x + s - 2, y + s - 4], fill=c)
        draw.line([(x + s / 2, y + 2), (x + s / 2, y - 2)], fill=c, width=2)
    elif key == "virus":
        cx, cy, r = x + s / 2, y + s / 2, s * 0.26
        for k in range(8):
            import math
            ang = math.pi * k / 4
            draw.line([(cx + math.cos(ang) * r, cy + math.sin(ang) * r),
                       (cx + math.cos(ang) * (r + 7),
                        cy + math.sin(ang) * (r + 7))], fill=c, width=2)
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=c)
    elif key == "frame":
        draw.rectangle([x + 2, y + 2, x + s - 2, y + s - 2], outline=GOLD,
                       width=3)
        draw.rectangle([x + 6, y + 6, x + s - 6, y + s - 6], fill=(250, 225, 140))
        draw.arc([x + 7, y + 8, x + s - 8, y + s - 8], 200, 340, fill=RED,
                 width=2)
        draw.ellipse([x + s * 0.55, y + s * 0.2, x + s * 0.72, y + s * 0.37],
                     fill=(240, 170, 40))
    elif key == "flame":
        draw.polygon([(x + s / 2, y + 1), (x + s - 4, y + s * 0.55),
                      (x + s * 0.68, y + s * 0.5), (x + s * 0.62, y + s - 3),
                      (x + s * 0.3, y + s - 3), (x + 4, y + s * 0.62)],
                     fill=(214, 90, 20))
        draw.polygon([(x + s / 2, y + s * 0.5), (x + s * 0.68, y + s * 0.8),
                      (x + s * 0.32, y + s * 0.8)], fill=(240, 190, 40))
    elif key == "atom":
        cx, cy = x + s / 2, y + s / 2
        draw.ellipse([cx - 12, cy - 5, cx + 12, cy + 5], outline=c, width=2)
        draw.ellipse([cx - 5, cy - 12, cx + 5, cy + 12], outline=c, width=2)
        draw.ellipse([cx - 3, cy - 3, cx + 3, cy + 3], fill=RED)
    elif key == "tower":
        draw.rectangle([x + s * 0.3, y + s * 0.25, x + s * 0.7, y + s - 3],
                       fill=c)
        draw.polygon([(x + s / 2, y + 1), (x + s * 0.3, y + s * 0.25),
                      (x + s * 0.7, y + s * 0.25)], fill=c)
        for row in range(3):
            yy = y + s * 0.38 + row * s * 0.18
            draw.rectangle([x + s * 0.4, yy, x + s * 0.6, yy + 3],
                           fill=PAPER)


def draw_masthead(draw):
    draw.line([(24, 18), (W - 24, 18)], fill=RULE, width=3)
    title = font(SERIF_B, 62)
    name = "THE WORLD TODAY"
    tw = draw.textlength(name, font=title)
    draw.text(((W - tw) / 2, 30), name, font=title, fill=INK)
    date_f = font(SANS_B, 21)
    date = "THURSDAY 19 NOVEMBER 2026"
    dw = draw.textlength(date, font=date_f)
    draw.text(((W - dw) / 2, 108), date, font=date_f, fill=RED)
    sub = font(SERIF, 15)
    tag = "The day's news, at a glance"
    sw = draw.textlength(tag, font=sub)
    draw.text(((W - sw) / 2, 140), tag, font=sub, fill=GREY)
    draw.line([(24, 168), (W - 24, 168)], fill=RULE, width=2)
    draw.line([(24, 173), (W - 24, 173)], fill=RULE, width=1)


def draw_lead(draw):
    y = 192
    kick = font(SANS_B, 16)
    draw.text((28, y), "SHENZHEN SUMMIT", font=kick, fill=RED)
    y += 26
    head = font(SERIF_B, 37)
    y = draw_text_block(draw, 28, y,
                        "Trump, Xi and Putin hold first trilateral summit",
                        head, 600, leading=44)
    y += 8
    body = font(SANS, 17)
    y = draw_text_block(
        draw, 28, y,
        "The three leaders met on the sidelines of APEC in Shenzhen, "
        "with Ukraine and nuclear arms control at the top of the agenda.",
        body, 600, leading=23)
    # Globe motif on the right of the lead block. Kept clear of the
    # masthead rules above it and the lead rule below it.
    gx, gy, gr = 790, 250, 72
    draw.ellipse([gx - gr, gy - gr, gx + gr, gy + gr], outline=BLUE, width=4)
    draw.ellipse([gx - gr * 0.45, gy - gr, gx + gr * 0.45, gy + gr],
                 outline=BLUE, width=2)
    draw.line([(gx - gr, gy), (gx + gr, gy)], fill=BLUE, width=2)
    draw.arc([gx - gr, gy - gr * 1.25, gx + gr, gy + gr * 0.25], 300, 60,
             fill=(34, 120, 60), width=3)
    draw.arc([gx - gr, gy - gr * 0.25, gx + gr, gy + gr * 1.25], 120, 240,
             fill=(34, 120, 60), width=3)
    # Three small flags under the globe: United States, China, Russia.
    fy, fw, fh = 332, 56, 32
    for i, (fx, colours) in enumerate([
            (688, [(200, 40, 40), (255, 255, 255), (30, 60, 140)]),
            (758, [(222, 41, 16)]),
            (828, [(255, 255, 255), (0, 57, 166), (213, 0, 50)])]):
        bx = fx
        if i == 0:  # stripes
            for s in range(7):
                draw.rectangle([bx, fy + s * fh / 7, bx + fw,
                                fy + (s + 1) * fh / 7],
                               fill=colours[s % 2])
            draw.rectangle([bx, fy, bx + fw * 0.45, fy + fh * 0.55],
                           fill=(30, 60, 140))
        elif i == 1:  # red field with one star dot
            draw.rectangle([bx, fy, bx + fw, fy + fh], fill=colours[0])
            draw.ellipse([bx + 8, fy + 7, bx + 18, fy + 17], fill=(255, 222, 0))
        else:  # horizontal tricolour
            for s, col in enumerate(colours):
                draw.rectangle([bx, fy + s * fh / 3, bx + fw,
                                fy + (s + 1) * fh / 3], fill=col)
        draw.rectangle([bx, fy, bx + fw, fy + fh], outline=INK, width=1)
    draw.line([(24, 372), (W - 24, 372)], fill=RULE, width=2)


def draw_grid(draw):
    x0, y0 = 24, 392
    cw, chh, gap = 320, 132, 8
    num_f = font(SANS_B, 15)
    head_f = font(SANS_B, 15)
    body_f = font(SANS, 13)
    for idx, (headline, summary, key) in enumerate(STORIES):
        row, col = divmod(idx, 3)
        x = x0 + col * (cw + gap)
        y = y0 + row * (chh + gap)
        draw.rectangle([x, y, x + cw, y + chh], outline=(200, 194, 178),
                       width=1)
        # Number badge and motif share the cell's header row.
        draw.ellipse([x + 8, y + 8, x + 30, y + 30], fill=RED)
        label = str(idx + 1)
        lw = draw.textlength(label, font=num_f)
        draw.text((x + 19 - lw / 2, y + 10), label, font=num_f,
                  fill=(255, 255, 255))
        motif(draw, key, x + cw - 38, y + 6, 28)
        hy = draw_text_block(draw, x + 8, y + 36, headline, head_f,
                             cw - 16, leading=19)
        draw_text_block(draw, x + 8, hy + 2, summary, body_f, cw - 16,
                        fill=(50, 48, 42), leading=16)


def draw_footer(draw):
    y = 972
    draw.line([(24, y), (W - 24, y)], fill=RULE, width=2)
    f = font(SERIF_B, 16)
    text = "Thursday 19 November 2026  ·  The World Today"
    tw = draw.textlength(text, font=f)
    draw.text(((W - tw) / 2, y + 10), text, font=f, fill=INK)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)
    draw_masthead(draw)
    draw_lead(draw)
    draw_grid(draw)
    draw_footer(draw)
    img.save("entry.png", optimize=True)
    print("wrote entry.png")


if __name__ == "__main__":
    main()
