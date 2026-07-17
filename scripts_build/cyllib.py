# -*- coding: utf-8 -*-
"""Generadores SVG reutilizables para los dashboards de Castilla y León (tema oscuro).

Cubre las figuras recurrentes de Tecnología e Ingeniería II:
 - diagrama tensión-deformación (ensayo de tracción)
 - diagrama de fases (isomorfo / eutéctico)
 - vigas con apoyos + diagramas de cortante y flector
 - circuitos de corriente alterna (serie y paralelo) y triángulo de potencias
 - puertas lógicas
Los diagramas de bloques y símbolos genéricos se construyen con svglib.
"""
import math
from svglib import svg_open, box, summer, arrow, line, txt, MARK

INK   = '#e7ecf7'
MUT   = '#94a3c0'
GRID  = '#31405f'
ACC   = '#38bdf8'
CURVE = '#22d3ee'
OK    = '#4ade80'
ROSE  = '#fb7185'
AMBER = '#f59e0b'
VIOL  = '#a78bfa'


def _hdr(vb, maxw):
    return (f"<svg viewBox='0 0 {vb}' width='100%' style='max-width:{maxw}px;height:auto' "
            "fill='none' font-family='Inter,system-ui,sans-serif' font-size='13'>" + MARK)


# ----------------------------------------------------------------------------
#  PLOT 2D genérico (ejes con flechas, rejilla, mapeo valor->px)
# ----------------------------------------------------------------------------
class Plot:
    def __init__(self, xr, yr, w=460, h=320, pl=58, pb=46, pt=20, pr=26,
                 xlabel='', ylabel='', maxw=None):
        self.x0, self.x1 = xr
        self.y0, self.y1 = yr
        self.W, self.H = w, h
        self.pl, self.pb, self.pt, self.pr = pl, pb, pt, pr
        self.gx0, self.gx1 = pl, w - pr           # zona de dibujo (px)
        self.gy0, self.gy1 = h - pb, pt
        self.s = _hdr(f'{w} {h}', maxw or w)
        self.xlabel, self.ylabel = xlabel, ylabel

    def mx(self, v):
        return self.gx0 + (v - self.x0) / (self.x1 - self.x0) * (self.gx1 - self.gx0)

    def my(self, v):
        return self.gy0 + (v - self.y0) / (self.y1 - self.y0) * (self.gy1 - self.gy0)

    def axes(self, xticks=None, yticks=None, xfmt=str, yfmt=str, grid=True):
        s = ''
        if grid:
            if xticks:
                for xv in xticks:
                    X = self.mx(xv)
                    s += f"<line x1='{X:.1f}' y1='{self.gy0}' x2='{X:.1f}' y2='{self.gy1}' stroke='{GRID}' stroke-width='1' stroke-dasharray='3 4'/>"
            if yticks:
                for yv in yticks:
                    Y = self.my(yv)
                    s += f"<line x1='{self.gx0}' y1='{Y:.1f}' x2='{self.gx1}' y2='{Y:.1f}' stroke='{GRID}' stroke-width='1' stroke-dasharray='3 4'/>"
        # ejes con flecha
        s += f"<line x1='{self.gx0}' y1='{self.gy0}' x2='{self.gx1+14}' y2='{self.gy0}' stroke='{INK}' stroke-width='2' marker-end='url(#ar)'/>"
        s += f"<line x1='{self.gx0}' y1='{self.gy0}' x2='{self.gx0}' y2='{self.gy1-14}' stroke='{INK}' stroke-width='2' marker-end='url(#ar)'/>"
        if xticks:
            for xv in xticks:
                X = self.mx(xv)
                s += f"<line x1='{X:.1f}' y1='{self.gy0}' x2='{X:.1f}' y2='{self.gy0+5}' stroke='{INK}' stroke-width='1.5'/>"
                s += f"<text x='{X:.1f}' y='{self.gy0+18}' fill='{MUT}' font-size='12' text-anchor='middle'>{xfmt(xv)}</text>"
        if yticks:
            for yv in yticks:
                Y = self.my(yv)
                s += f"<line x1='{self.gx0-5}' y1='{Y:.1f}' x2='{self.gx0}' y2='{Y:.1f}' stroke='{INK}' stroke-width='1.5'/>"
                s += f"<text x='{self.gx0-8}' y='{Y+4:.1f}' fill='{MUT}' font-size='12' text-anchor='end'>{yfmt(yv)}</text>"
        if self.xlabel:
            s += f"<text x='{self.gx1+8}' y='{self.gy0-10}' fill='{INK}' font-size='13' text-anchor='end'>{self.xlabel}</text>"
        if self.ylabel:
            s += f"<text x='{self.gx0+6}' y='{self.gy1-4}' fill='{INK}' font-size='13'>{self.ylabel}</text>"
        self.s += s
        return self

    def polyline(self, pts, color=CURVE, width=2.5, dash=None):
        d = ' '.join(f"{self.mx(x):.1f},{self.my(y):.1f}" for x, y in pts)
        da = f" stroke-dasharray='{dash}'" if dash else ''
        self.s += f"<polyline points='{d}' fill='none' stroke='{color}' stroke-width='{width}'{da}/>"
        return self

    def path(self, dstr, color=CURVE, width=2.5):
        self.s += f"<path d='{dstr}' fill='none' stroke='{color}' stroke-width='{width}'/>"
        return self

    def point(self, x, y, label='', color=ACC, dx=8, dy=-8, r=3.6, anchor='start'):
        X, Y = self.mx(x), self.my(y)
        self.s += f"<circle cx='{X:.1f}' cy='{Y:.1f}' r='{r}' fill='{color}' stroke='#0d1220' stroke-width='1'/>"
        if label:
            self.s += f"<text x='{X+dx:.1f}' y='{Y+dy:.1f}' fill='{INK}' font-size='12.5' text-anchor='{anchor}'>{label}</text>"
        return self

    def vline(self, xv, y_from, y_to, color=MUT, dash='4 4'):
        X = self.mx(xv)
        self.s += f"<line x1='{X:.1f}' y1='{self.my(y_from):.1f}' x2='{X:.1f}' y2='{self.my(y_to):.1f}' stroke='{color}' stroke-width='1.3' stroke-dasharray='{dash}'/>"
        return self

    def hline(self, yv, x_from, x_to, color=MUT, dash='4 4'):
        Y = self.my(yv)
        self.s += f"<line x1='{self.mx(x_from):.1f}' y1='{Y:.1f}' x2='{self.mx(x_to):.1f}' y2='{Y:.1f}' stroke='{color}' stroke-width='1.3' stroke-dasharray='{dash}'/>"
        return self

    def text(self, xv, yv, s, color=INK, fs=12.5, anchor='middle'):
        self.s += f"<text x='{self.mx(xv):.1f}' y='{self.my(yv):.1f}' fill='{color}' font-size='{fs}' text-anchor='{anchor}'>{s}</text>"
        return self

    def rawtext(self, X, Y, s, color=INK, fs=12.5, anchor='middle'):
        self.s += f"<text x='{X}' y='{Y}' fill='{color}' font-size='{fs}' text-anchor='{anchor}'>{s}</text>"
        return self

    def close(self):
        return self.s + "</svg>"


# ----------------------------------------------------------------------------
#  VIGA (beam) con apoyos, cargas y cotas
# ----------------------------------------------------------------------------
def _support_pin(x, y):
    """Apoyo articulado fijo (triángulo) con base rayada."""
    s = f"<path d='M{x} {y} L{x-12} {y+20} L{x+12} {y+20} Z' fill='none' stroke='{INK}' stroke-width='2'/>"
    for i in range(-12, 13, 6):
        s += f"<line x1='{x+i}' y1='{y+20}' x2='{x+i-5}' y2='{y+26}' stroke='{MUT}' stroke-width='1.4'/>"
    s += f"<line x1='{x-16}' y1='{y+20}' x2='{x+16}' y2='{y+20}' stroke='{INK}' stroke-width='2'/>"
    return s


def _support_roller(x, y):
    """Apoyo móvil (triángulo con rueditas)."""
    s = f"<path d='M{x} {y} L{x-12} {y+17} L{x+12} {y+17} Z' fill='none' stroke='{INK}' stroke-width='2'/>"
    s += f"<circle cx='{x-6}' cy='{y+22}' r='4' fill='none' stroke='{INK}' stroke-width='1.6'/>"
    s += f"<circle cx='{x+6}' cy='{y+22}' r='4' fill='none' stroke='{INK}' stroke-width='1.6'/>"
    s += f"<line x1='{x-16}' y1='{y+27}' x2='{x+16}' y2='{y+27}' stroke='{INK}' stroke-width='2'/>"
    return s


def _support_fixed(x, y, side='left'):
    """Empotramiento (pared rayada)."""
    d = -1 if side == 'left' else 1
    s = f"<line x1='{x}' y1='{y-26}' x2='{x}' y2='{y+26}' stroke='{INK}' stroke-width='2.5'/>"
    for yy in range(-26, 27, 8):
        s += f"<line x1='{x}' y1='{y+yy}' x2='{x+d*10}' y2='{y+yy+8}' stroke='{MUT}' stroke-width='1.4'/>"
    return s


def beam(loads, supports, span_m, dims=None, w=560, h=210, y_beam=118, x0=90, x1=500,
         title='', maxw=560):
    """Dibuja una viga horizontal.
    loads: lista de dicts. Punto: {'type':'P','xm':1.5,'val':'P=16 kN'}
                            Distribuida: {'type':'q','x0':0,'x1':6,'val':'q=...'}
                            Momento: {'type':'M',...} (no usado por ahora)
    supports: lista {'xm':0,'kind':'pin'|'roller'|'fixed', 'label':'A'}
    span_m: longitud total (m) para mapear xm->px.
    dims: lista de tuplas (xa_m, xb_m, texto) para cotas bajo la viga.
    """
    s = _hdr(f'{w} {h}', maxw)
    def X(xm):
        return x0 + xm / span_m * (x1 - x0)
    if title:
        s += f"<text x='{w/2}' y='18' fill='{INK}' font-size='13' text-anchor='middle'>{title}</text>"
    # viga
    s += f"<rect x='{x0}' y='{y_beam-7}' width='{x1-x0}' height='14' rx='2' fill='#1b2640' stroke='{INK}' stroke-width='2'/>"
    # apoyos
    for sup in supports:
        xx = X(sup['xm'])
        k = sup['kind']
        if k == 'pin':
            s += _support_pin(xx, y_beam+7)
        elif k == 'roller':
            s += _support_roller(xx, y_beam+7)
        elif k == 'fixed':
            s += _support_fixed(xx, y_beam, sup.get('side', 'left'))
        if sup.get('label'):
            lx = xx - 20 if k == 'fixed' and sup.get('side','left')=='left' else xx
            s += f"<text x='{xx}' y='{y_beam+52}' fill='{ACC}' font-size='13' font-weight='700' text-anchor='middle'>{sup['label']}</text>"
    # cargas
    for ld in loads:
        if ld['type'] == 'P':
            xx = X(ld['xm'])
            s += arrow(xx, y_beam-52, xx, y_beam-9, ROSE)
            s += f"<text x='{xx}' y='{y_beam-58}' fill='{ROSE}' font-size='13' font-weight='700' text-anchor='middle'>{ld['val']}</text>"
        elif ld['type'] == 'q':
            xa, xb = X(ld['x0']), X(ld['x1'])
            s += f"<line x1='{xa}' y1='{y_beam-44}' x2='{xb}' y2='{y_beam-44}' stroke='{AMBER}' stroke-width='2'/>"
            n = max(2, int((xb-xa)//26))
            for i in range(n+1):
                ax = xa + i*(xb-xa)/n
                s += arrow(ax, y_beam-44, ax, y_beam-9, AMBER)
            s += f"<text x='{(xa+xb)/2}' y='{y_beam-50}' fill='{AMBER}' font-size='13' font-weight='700' text-anchor='middle'>{ld['val']}</text>"
    # cotas
    if dims:
        yd = y_beam + 66
        for (xa_m, xb_m, tx) in dims:
            xa, xb = X(xa_m), X(xb_m)
            s += f"<line x1='{xa}' y1='{yd}' x2='{xb}' y2='{yd}' stroke='{MUT}' stroke-width='1.3'/>"
            s += f"<line x1='{xa}' y1='{yd-5}' x2='{xa}' y2='{yd+5}' stroke='{MUT}' stroke-width='1.3'/>"
            s += f"<line x1='{xb}' y1='{yd-5}' x2='{xb}' y2='{yd+5}' stroke='{MUT}' stroke-width='1.3'/>"
            s += f"<text x='{(xa+xb)/2}' y='{yd-6}' fill='{MUT}' font-size='12' text-anchor='middle'>{tx}</text>"
    return s + "</svg>"


def diagram_VM(points, span_m, kind='V', unit='kN', w=560, h=190, x0=90, x1=500,
               color=None, title='', maxw=560):
    """Diagrama de esfuerzo cortante o momento flector.
    points: lista de (xm, valor) que definen la poligonal (o parábola por tramos si 3+ pts).
    Se dibuja una línea base y el área rellena.
    """
    color = color or (OK if kind == 'V' else VIOL)
    s = _hdr(f'{w} {h}', maxw)
    ybase = h/2 + 8
    vals = [v for _, v in points]
    vmax = max(abs(min(vals)), abs(max(vals)), 1e-9)
    scale = (h/2 - 30) / vmax
    def X(xm):
        return x0 + xm / span_m * (x1 - x0)
    def Y(v):
        return ybase - v * scale
    if title:
        s += f"<text x='{w/2}' y='16' fill='{INK}' font-size='13' text-anchor='middle'>{title}</text>"
    # área
    d = f"M{X(points[0][0]):.1f},{ybase:.1f} "
    d += ' '.join(f"L{X(x):.1f},{Y(v):.1f}" for x, v in points)
    d += f" L{X(points[-1][0]):.1f},{ybase:.1f} Z"
    s += f"<path d='{d}' fill='{color}22' stroke='none'/>"
    # línea del diagrama
    dl = 'M' + ' L'.join(f"{X(x):.1f},{Y(v):.1f}" for x, v in points)
    s += f"<path d='{dl}' fill='none' stroke='{color}' stroke-width='2.5'/>"
    # eje base
    s += f"<line x1='{x0-10}' y1='{ybase}' x2='{x1+16}' y2='{ybase}' stroke='{INK}' stroke-width='1.6' marker-end='url(#ar)'/>"
    # etiquetas de valores en vértices
    seen = set()
    for x, v in points:
        key = (round(X(x)), round(v, 2))
        if key in seen:
            continue
        seen.add(key)
        if abs(v) < 1e-6:
            continue
        dyy = -6 if v > 0 else 14
        s += f"<circle cx='{X(x):.1f}' cy='{Y(v):.1f}' r='2.6' fill='{color}'/>"
        s += f"<text x='{X(x):.1f}' y='{Y(v)+dyy:.1f}' fill='{INK}' font-size='11.5' text-anchor='middle'>{v:g} {unit}</text>"
    return s + "</svg>"


# ----------------------------------------------------------------------------
#  Símbolos de componentes de circuito
# ----------------------------------------------------------------------------
def _res_h(x, y, w=44, label='', color=AMBER):
    """Resistencia horizontal (zig-zag)."""
    zx = x + (w-30)/2
    pts = f"M{x},{y} L{zx},{y} l4,-7 l6,14 l6,-14 l6,14 l6,-14 l4,7 L{x+w},{y}"
    s = f"<path d='{pts}' stroke='{color}' stroke-width='2' fill='none'/>"
    if label:
        s += f"<text x='{x+w/2}' y='{y-12}' fill='{INK}' font-size='12.5' text-anchor='middle'>{label}</text>"
    return s


def _res_v(x, y, h=44, label='', color=AMBER):
    zy = y + (h-30)/2
    pts = f"M{x},{y} L{x},{zy} l-7,4 l14,6 l-14,6 l14,6 l-14,6 l7,4 L{x},{y+h}"
    s = f"<path d='{pts}' stroke='{color}' stroke-width='2' fill='none'/>"
    if label:
        s += f"<text x='{x+14}' y='{y+h/2+4}' fill='{INK}' font-size='12.5' text-anchor='start'>{label}</text>"
    return s


def _ind_v(x, y, h=44, label='', color=VIOL):
    """Bobina vertical (3 arcos)."""
    n = 3
    step = h/n
    d = f"M{x},{y} "
    for i in range(n):
        cy = y + i*step + step/2
        d += f"A6 {step/2} 0 0 1 {x},{y+(i+1)*step} "
    s = f"<path d='{d}' stroke='{color}' stroke-width='2' fill='none'/>"
    if label:
        s += f"<text x='{x+14}' y='{y+h/2+4}' fill='{INK}' font-size='12.5' text-anchor='start'>{label}</text>"
    return s


def _cap_v(x, y, h=44, label='', color=ACC):
    """Condensador vertical."""
    m = y + h/2
    s = (f"<line x1='{x}' y1='{y}' x2='{x}' y2='{m-6}' stroke='{color}' stroke-width='2'/>"
         f"<line x1='{x-11}' y1='{m-6}' x2='{x+11}' y2='{m-6}' stroke='{color}' stroke-width='2'/>"
         f"<line x1='{x-11}' y1='{m+6}' x2='{x+11}' y2='{m+6}' stroke='{color}' stroke-width='2'/>"
         f"<line x1='{x}' y1='{m+6}' x2='{x}' y2='{y+h}' stroke='{color}' stroke-width='2'/>")
    if label:
        s += f"<text x='{x+15}' y='{m+4}' fill='{INK}' font-size='12.5' text-anchor='start'>{label}</text>"
    return s


def _ac_source(x, y, r=17, label=''):
    s = (f"<circle cx='{x}' cy='{y}' r='{r}' fill='none' stroke='{INK}' stroke-width='2'/>"
         f"<path d='M{x-9},{y} q4.5,-9 9,0 q4.5,9 9,0' stroke='{INK}' stroke-width='1.6' fill='none'/>")
    if label:
        s += f"<text x='{x-r-6}' y='{y+4}' fill='{INK}' font-size='12.5' text-anchor='end'>{label}</text>"
    return s


def ac_series(items, V='230 V', f='50 Hz', w=470, h=170, maxw=470):
    """Circuito serie: fuente + componentes en lazo.
    items: lista de (tipo, etiqueta) con tipo in {'R','L','C'} colocados en la rama superior."""
    s = _hdr(f'{w} {h}', maxw)
    left, right, top, bot = 60, w-40, 40, h-34
    # fuente a la izquierda (vertical)
    s += _ac_source(left, (top+bot)/2)
    s += f"<text x='{left-8}' y='{(top+bot)/2-22}' fill='{INK}' font-size='12' text-anchor='end'>{V}</text>"
    s += f"<text x='{left-8}' y='{(top+bot)/2+30}' fill='{MUT}' font-size='12' text-anchor='end'>{f}</text>"
    s += line(left, top, left, (top+bot)/2-17, INK)
    s += line(left, (top+bot)/2+17, left, bot, INK)
    # rama superior con componentes
    n = len(items)
    seg = (right-left)/(n+1)
    s += line(left, top, left+seg*0.5, top, INK)
    xcur = left+seg*0.5
    for i, (typ, lab) in enumerate(items):
        cw = 44
        if typ == 'R':
            s += _res_h(xcur, top, cw, lab)
        elif typ == 'L':
            # bobina horizontal
            d = f"M{xcur},{top} "
            for k in range(3):
                d += f"a6 6 0 0 1 12 0 "
            s += f"<path d='{d}' stroke='{VIOL}' stroke-width='2' fill='none'/>"
            s += f"<text x='{xcur+18}' y='{top-12}' fill='{INK}' font-size='12.5' text-anchor='middle'>{lab}</text>"
            cw = 36
        elif typ == 'C':
            m = xcur+cw/2
            s += (f"<line x1='{xcur}' y1='{top}' x2='{m-6}' y2='{top}' stroke='{ACC}' stroke-width='2'/>"
                  f"<line x1='{m-6}' y1='{top-11}' x2='{m-6}' y2='{top+11}' stroke='{ACC}' stroke-width='2'/>"
                  f"<line x1='{m+6}' y1='{top-11}' x2='{m+6}' y2='{top+11}' stroke='{ACC}' stroke-width='2'/>"
                  f"<line x1='{m+6}' y1='{top}' x2='{xcur+cw}' y2='{top}' stroke='{ACC}' stroke-width='2'/>")
            s += f"<text x='{m}' y='{top-14}' fill='{INK}' font-size='12.5' text-anchor='middle'>{lab}</text>"
        xnext = xcur + seg
        s += line(xcur+cw, top, xnext, top, INK)
        xcur = xnext
    s += line(xcur, top, right, top, INK)
    # lados derecho e inferior
    s += line(right, top, right, bot, INK)
    s += line(left, bot, right, bot, INK)
    return s + "</svg>"


# ----------------------------------------------------------------------------
#  Triángulo de potencias
# ----------------------------------------------------------------------------
def power_triangle(P, Q, S, phi_deg, w=430, h=250, inductive=True, maxw=430,
                   punit='W', labels=None):
    """P (horizontal), Q (vertical), S (hipotenusa)."""
    s = _hdr(f'{w} {h}', maxw)
    ox, oy = 70, h-50
    L = min(w-150, 300)
    scale = L / max(P, 1e-9)
    px = ox + P*scale
    qy = oy - (Q*scale if inductive else -Q*scale)  # Q positiva hacia arriba (inductivo)
    # cateto P
    s += f"<line x1='{ox}' y1='{oy}' x2='{px:.1f}' y2='{oy}' stroke='{OK}' stroke-width='2.5'/>"
    # cateto Q (vertical en el extremo)
    s += f"<line x1='{px:.1f}' y1='{oy}' x2='{px:.1f}' y2='{qy:.1f}' stroke='{ROSE}' stroke-width='2.5'/>"
    # hipotenusa S
    s += f"<line x1='{ox}' y1='{oy}' x2='{px:.1f}' y2='{qy:.1f}' stroke='{ACC}' stroke-width='2.5'/>"
    # arco del ángulo
    r = 34
    ang = math.radians(phi_deg)
    ax = ox + r
    ay = oy - (r*math.tan(ang) if False else 0)
    ex = ox + r*math.cos(ang)
    ey = oy - r*math.sin(ang) if inductive else oy + r*math.sin(ang)
    sweep = 0 if inductive else 1
    s += f"<path d='M{ax},{oy} A{r},{r} 0 0 {sweep} {ex:.1f},{ey:.1f}' stroke='{MUT}' stroke-width='1.5' fill='none'/>"
    lbl = labels or {}
    s += f"<text x='{(ox+px)/2:.1f}' y='{oy+20}' fill='{OK}' font-size='12.5' text-anchor='middle'>{lbl.get('P','P')}</text>"
    s += f"<text x='{px+8:.1f}' y='{(oy+qy)/2:.1f}' fill='{ROSE}' font-size='12.5' text-anchor='start'>{lbl.get('Q','Q')}</text>"
    s += f"<text x='{(ox+px)/2-10:.1f}' y='{(oy+qy)/2-6:.1f}' fill='{ACC}' font-size='12.5' text-anchor='end'>{lbl.get('S','S')}</text>"
    s += f"<text x='{ox+r+6:.1f}' y='{oy-6 if inductive else oy+16}' fill='{MUT}' font-size='12'>&phi;</text>"
    return s + "</svg>"


# ----------------------------------------------------------------------------
#  Puertas lógicas (para circuitos simplificados)
# ----------------------------------------------------------------------------
def gate(x, y, kind, w=46, h=34):
    """kind: AND, OR, NAND, NOR, NOT, XOR. Devuelve (svg, (out_x,out_y))."""
    cy = y + h/2
    inv = kind in ('NAND', 'NOR', 'NOT')
    body = ''
    if kind in ('AND', 'NAND'):
        body = (f"<path d='M{x},{y} L{x+w*0.5},{y} A{h/2},{h/2} 0 0 1 {x+w*0.5},{y+h} "
                f"L{x},{y+h} Z' fill='#1b2640' stroke='{INK}' stroke-width='1.8'/>")
    elif kind in ('OR', 'NOR', 'XOR'):
        body = (f"<path d='M{x},{y} Q{x+w*0.55},{y} {x+w},{cy} Q{x+w*0.55},{y+h} {x},{y+h} "
                f"Q{x+w*0.28},{cy} {x},{y} Z' fill='#1b2640' stroke='{INK}' stroke-width='1.8'/>")
        if kind == 'XOR':
            body += f"<path d='M{x-6},{y} Q{x+w*0.22},{cy} {x-6},{y+h}' stroke='{INK}' stroke-width='1.8' fill='none'/>"
    elif kind == 'NOT':
        body = f"<path d='M{x},{y} L{x},{y+h} L{x+w*0.8},{cy} Z' fill='#1b2640' stroke='{INK}' stroke-width='1.8'/>"
    outx = x + w
    if inv:
        body += f"<circle cx='{x+w+5}' cy='{cy}' r='4.5' fill='#1b2640' stroke='{INK}' stroke-width='1.6'/>"
        outx = x + w + 10
    body += f"<text x='{x+w*0.42}' y='{cy+4}' fill='{MUT}' font-size='10' text-anchor='middle'>{kind}</text>"
    return body, (outx, cy)
