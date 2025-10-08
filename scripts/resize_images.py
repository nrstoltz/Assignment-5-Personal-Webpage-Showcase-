from PIL import Image
import os

IMAGES = [
    'images/parking-wizard-1.png',
    'images/parking-wizard-2.png',
    'images/bathroom-problem-1.png',
    'images/bathroom-problem-2.png',
]

OUT_WIDTH = 900

os.makedirs('images', exist_ok=True)

for src in IMAGES:
    if not os.path.exists(src):
        print('missing', src)
        continue
    try:
        im = Image.open(src)
    except Exception as e:
        print('error opening', src, e)
        continue
    w, h = im.size
    if w <= OUT_WIDTH:
        print('skip (already small):', src)
        continue
    new_h = int(h * OUT_WIDTH / w)
    im2 = im.resize((OUT_WIDTH, new_h), Image.LANCZOS)
    base, ext = os.path.splitext(src)
    out = f"{base}-sm.jpg"
    try:
        im2.convert('RGB').save(out, quality=85)
        print('wrote', out)
    except Exception as e:
        print('error saving', out, e)
