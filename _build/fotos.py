# Di Trani: SUS fotos de Instagram con un mismo tratamiento (Receta Corrado), sin matar las etiquetas.
# Mezcla la foto con un duotono cálido de la marca (negro del logo + pino de las cajas).
# Uso: python -I _build/fotos.py [#oscuro] [#claro] [mezcla 0-1]
import sys
from pathlib import Path
from PIL import Image, ImageOps, ImageEnhance
R = Path(__file__).resolve().parent.parent
DARK = sys.argv[1] if len(sys.argv) > 1 else '#1a1412'
LIGHT = sys.argv[2] if len(sys.argv) > 2 else '#f3e7d2'
MIX = float(sys.argv[3]) if len(sys.argv) > 3 else .32
MID = '#8a5a3a'
IG = lambda i: f'ig/ig_{i}.jpg'
# destino: (origen, ancho, alto, foco x, foco y)
MAPA = {
 'barricas':  (IG('DVRgZQ8EkDB'), 1200, 1500, .5, .5),   # pared de botellas
 'estante':   (IG('DW1hFhhgBJY'), 1200, 1500, .5, .5),   # cajas sobre la barrica
 'copa':      (IG('DQCiapqDL1h'), 1200, 1500, .5, .5),
 'corchos':   (IG('DXZt_UjlXC5'), 1200, 1500, .5, .5),   # Privado sobre la barrica
 'semana':    (IG('DTiuJG4laiK'), 1100, 1100, .5, .0),
 'regalo':    (IG('DecTCDtAeBv'), 1400, 1050, .5, .55),  # caja Felino + chocolate + copa
 'envio':     (IG('DOW412_kZD-'), 1000, 1250, .5, .6),
 'calle':     (IG('DTtOm8VkmOY'), 1000, 1250, .5, .12),   # la vidriera
 'maridaje':  (IG('DNgf4B_yhk8'), 1400, 1050, .5, .6),
 'caja':      (IG('DVjK65UgNCi'), 1400, 1050, .5, .6),
 'uco':       (IG('DOg_xtsEu6V'), 900, 900, .5, .45),
 'lujan':     (IG('DYSchkJApd_'), 900, 900, .5, .6),
 'maipu':     (IG('DNyNwrWwPKQ'), 900, 900, .5, .6),
 'andes':     (IG('DXHuvfbgGa0'), 900, 900, .5, .55),
 'espumante': (IG('DSfW7lKDNXE'), 900, 900, .5, .5),
 'cafayate':  (IG('DPCbT99kmZG'), 900, 900, .5, .5),     # gines Restinga
 'colome':    (IG('DQup09-jE4i'), 900, 900, .5, .55),    # aceites D.V. Catena
 'barrica-sq':(IG('DdR0oJaAQ6p'), 900, 900, .5, .6),
 'faq':       (IG('DXpg4YSgdom'), 1050, 1400, .5, .5),
 'faq-sq':    (IG('DRA8Nj4DIoM'), 700, 700, .5, .7),
 'cata':      (IG('DfIGk2HxKqk'), 1000, 1400, .5, .5),
 'cj-felino': (IG('DecTCDtAeBv'), 800, 1000, .5, .5),
 'cj-nina':   (IG('DRA8Nj4DIoM'), 800, 1000, .5, .6),
 'cj-chandon':(IG('DOW412_kZD-'), 800, 1000, .5, .6),
 'cj-catena': (IG('DOypmQZEZmF'), 800, 1000, .5, .6),
 'cj-zuccardi':(IG('DPrNi-9gEcj'), 800, 1000, .5, .5),
 'cj-estirpe':(IG('DfkuZamgJJY'), 800, 1000, .5, .5),
}
out = R / 'assets' / 'img'
for f in out.glob('*.jpg'): f.unlink()
for dst, (src, w, h, fx, fy) in MAPA.items():
    im = Image.open(R / 'assets' / 'raw' / src).convert('RGB')
    im = ImageOps.fit(im, (w, h), Image.LANCZOS, centering=(fx, fy))
    g = ImageOps.autocontrast(im.convert('L'), cutoff=1)
    duo = ImageOps.colorize(g, black=DARK, mid=MID, white=LIGHT, midpoint=120)
    im = ImageEnhance.Color(im).enhance(.88)
    col = Image.blend(im, duo, MIX)
    col.save(out / f'{dst}.jpg', quality=80, optimize=True, progressive=True)
# logo: el de la foto de perfil (trazos blancos sobre negro) → tinta oscura con transparencia
p = Image.open(R / 'assets' / 'raw' / 'ig' / 'ig_perfil.jpg').convert('L')
a = ImageOps.autocontrast(p, cutoff=1).point(lambda v: 0 if v < 60 else min(255, int((v - 60) * 1.4)))
for name, ink in (('logo-osc', DARK), ('logo-clr', LIGHT)):
    L = Image.new('RGBA', p.size, ink); L.putalpha(a)
    L.resize((600, 600), Image.LANCZOS).save(out.parent / f'{name}.png', optimize=True)
print('ok', len(MAPA))
