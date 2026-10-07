"""Compact PNG previews; regenerate print PNGs with the plotting scripts first."""
from pathlib import Path
from PIL import Image
root = Path(__file__).resolve().parents[1]
for source in (root / 'figures').rglob('*.png'):
    with Image.open(source) as image:
        image.thumbnail((1100, 800))
        preview = image.convert('RGB').quantize(colors=32)
    preview.save(source, optimize=True)
