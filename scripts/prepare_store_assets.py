"""Prepare Chrome Web Store assets from the repository's existing artwork.

Requires Pillow. Run after npm run zip; store assets are not included in GSVR.zip.
"""
from pathlib import Path
import shutil

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "release" / "store-assets"
OUT.mkdir(parents=True, exist_ok=True)

SCALE = 3
image = Image.new("RGB", (440 * SCALE, 280 * SCALE), "#10243a")
draw = ImageDraw.Draw(image)


def font(size):
    for candidate in (
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    ):
        if Path(candidate).exists():
            return ImageFont.truetype(candidate, size * SCALE)
    return ImageFont.load_default(size=size * SCALE)


def text(x, y, value, size, color):
    draw.text((x * SCALE, y * SCALE), value, font=font(size), fill=color)


# A simple brand panel with the extension's existing icon and venue rank chips.
draw.ellipse((285 * SCALE, -95 * SCALE, 580 * SCALE, 210 * SCALE), fill="#193853")
icon = Image.open(ROOT / "GSVR" / "icons" / "icon128.png").convert("RGBA")
icon = icon.resize((66 * SCALE, 66 * SCALE), Image.Resampling.LANCZOS)
image.paste(icon, (30 * SCALE, 25 * SCALE), icon)
text(30, 111, "Scholar with Ranks", 29, "#ffffff")
text(32, 158, "Venue rankings on Google Scholar", 17, "#c9dce8")

for x, label, color in ((32, "A*", "#fbd957"), (104, "A", "#86d866"), (176, "Q1", "#fbd957"), (248, "Q2", "#86d866")):
    draw.rounded_rectangle((x * SCALE, 207 * SCALE, (x + 58) * SCALE, 244 * SCALE), radius=12 * SCALE, fill=color)
    bounds = draw.textbbox((0, 0), label, font=font(18))
    width = bounds[2] - bounds[0]
    draw.text(((x + 29) * SCALE - width / 2, 214 * SCALE), label, font=font(18), fill="#183125")

image.resize((440, 280), Image.Resampling.LANCZOS).save(OUT / "promo-440x280.png")
shutil.copy2(ROOT / "GSVR" / "icons" / "icon128.png", OUT / "icon128.png")
shutil.copy2(ROOT / "docs" / "images" / "screenshot-candidate.png", OUT / "screenshot-candidate.png")
shutil.copy2(ROOT / "docs" / "privacy.html", OUT / "privacy.html")
shutil.copy2(ROOT / "docs" / "chrome-web-store-listing.md", OUT / "listing.md")
shutil.copy2(ROOT / "docs" / "publishing-checklist.md", OUT / "publishing-checklist.md")
print(f"Store assets prepared in {OUT}")
