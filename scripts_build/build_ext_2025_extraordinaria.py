#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera el JSON del examen Extremadura PAU 2025 (extraordinaria) para pau-dashboard."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import svg_open, box, summer, arrow, line, txt

# ---------------- FIGURAS ENUNCIADO ----------------

def _valv32(x, y, num, w=110, h=62):
    """Valvula 3/2 con rodillo (izq) y muelle (der). Puertos A(arriba) P(abajo) R(escape)."""
    s = f"<rect x='{x}' y='{y}' width='{w}' height='{h}' fill='none' stroke='#e2e8f0' stroke-width='2'/>"
    s += f"<line x1='{x+w/2}' y1='{y}' x2='{x+w/2}' y2='{y+h}' stroke='#e2e8f0' stroke-width='2'/>"
    # casilla izquierda (accionada): flecha vertical
    s += f"<line x1='{x+w*0.25:.0f}' y1='{y+h-12}' x2='{x+w*0.25:.0f}' y2='{y+14}' stroke='#38bdf8' stroke-width='2' marker-end='url(#arp)'/>"
    # casilla derecha (reposo): P cerrado, A->R
    s += f"<line x1='{x+w*0.58:.0f}' y1='{y+h-14}' x2='{x+w*0.80:.0f}' y2='{y+16}' stroke='#38bdf8' stroke-width='2' marker-end='url(#arp)'/>"
    s += f"<line x1='{x+w*0.66:.0f}' y1='{y+14}' x2='{x+w*0.66:.0f}' y2='{y+22}' stroke='#e2e8f0'/>"
    # rodillo (izquierda)
    s += f"<line x1='{x}' y1='{y+h/2}' x2='{x-22}' y2='{y+h/2}' stroke='#e2e8f0' stroke-width='2'/>"
    s += f"<circle cx='{x-28}' cy='{y+h/2-6}' r='6' fill='none' stroke='#e2e8f0' stroke-width='1.8'/>"
    # muelle (derecha)
    s += f"<line x1='{x+w}' y1='{y+h/2}' x2='{x+w+12}' y2='{y+h/2}' stroke='#e2e8f0' stroke-width='2'/>"
    sp = f"M{x+w+12} {y+h/2}"
    for i in range(3):
        xx = x + w + 12 + i * 11
        sp += f" L{xx+5.5} {y+h/2-8} L{xx+11} {y+h/2+8}"
    s += f"<path d='{sp}' fill='none' stroke='#f59e0b' stroke-width='1.6'/>"
    # etiquetas de puertos
    s += f"<text x='{x+w*0.30:.0f}' y='{y-6}' fill='#7dd3fc' font-size='13'>A</text>"
    s += f"<text x='{x+w*0.25:.0f}' y='{y+h+16}' fill='#7dd3fc' font-size='13'>P</text>"
    s += f"<text x='{x+w*0.70:.0f}' y='{y+h+16}' fill='#7dd3fc' font-size='13'>R</text>"
    s += f"<text x='{x+w+8}' y='{y-6}' fill='#cbd5e1' font-size='14'>{num}</text>"
    # escape R (triangulo)
    s += f"<line x1='{x+w*0.70:.0f}' y1='{y+h}' x2='{x+w*0.70:.0f}' y2='{y+h+8}' stroke='#e2e8f0'/>"
    s += f"<polygon points='{x+w*0.70-6:.0f},{y+h+8} {x+w*0.70+6:.0f},{y+h+8} {x+w*0.70:.0f},{y+h+16:.0f}' fill='none' stroke='#e2e8f0'/>"
    return s

def fig_neumatico2():
    s = ("<svg viewBox='0 0 620 540' width='100%' style='max-width:490px;height:auto' "
         "fill='none' font-family='Inter,system-ui,sans-serif' stroke='#e2e8f0' stroke-width='2'>")
    s += ("<defs><marker id='arp' markerWidth='9' markerHeight='8' refX='6' refY='3' orient='auto'>"
          "<path d='M0,0 L7,3 L0,6 Z' fill='#38bdf8'/></marker></defs>")
    # cilindro 1.0
    cx, cy = 350, 50
    s += f"<rect x='{cx}' y='{cy}' width='170' height='58' fill='#1e293b' stroke='#e2e8f0' stroke-width='2'/>"
    s += f"<rect x='{cx+8}' y='{cy+4}' width='13' height='50' fill='#38bdf8' stroke='#38bdf8'/>"
    s += f"<line x1='{cx+21}' y1='{cy+29}' x2='{cx+200}' y2='{cy+29}' stroke='#e2e8f0' stroke-width='4'/>"
    sp = f"M{cx+30} {cy+29}"
    for i in range(6):
        xx = cx + 30 + i * 18
        sp += f" L{xx+9} {cy+13} L{xx+18} {cy+45}"
    s += f"<path d='{sp}' fill='none' stroke='#f59e0b' stroke-width='1.7'/>"
    s += f"<text x='{cx+80}' y='{cy-10}' fill='#cbd5e1' font-size='15' text-anchor='middle'>1.0</text>"
    s += f"<line x1='{cx+14}' y1='{cy+58}' x2='{cx+14}' y2='170' stroke='#e2e8f0' stroke-width='2'/>"
    # valvula principal 1.01 (pilotada X / Y, salida A)
    vx, vy = 300, 170
    s += f"<rect x='{vx}' y='{vy}' width='110' height='58' fill='none' stroke='#e2e8f0' stroke-width='2'/>"
    s += f"<line x1='{vx+55}' y1='{vy}' x2='{vx+55}' y2='{vy+58}' stroke='#e2e8f0' stroke-width='2'/>"
    s += f"<line x1='{vx+18}' y1='{vy+42}' x2='{vx+38}' y2='{vy+16}' stroke='#38bdf8' stroke-width='2'/>"
    s += f"<line x1='{vx+72}' y1='{vy+16}' x2='{vx+92}' y2='{vy+42}' stroke='#38bdf8' stroke-width='2'/>"
    s += f"<text x='{vx+52}' y='{vy-6}' fill='#7dd3fc' font-size='13'>A</text>"
    s += f"<text x='{vx+118}' y='{vy+34}' fill='#cbd5e1' font-size='14'>1.01</text>"
    # pilotos X (izq) e Y (der)
    s += f"<rect x='{vx-16}' y='{vy+18}' width='16' height='22' fill='none' stroke='#e2e8f0'/>"
    s += f"<rect x='{vx+110}' y='{vy+18}' width='16' height='22' fill='none' stroke='#e2e8f0'/>"
    s += f"<text x='{vx-20}' y='{vy+14}' fill='#7dd3fc' font-size='13' text-anchor='middle'>X</text>"
    s += f"<text x='{vx+118}' y='{vy+14}' fill='#7dd3fc' font-size='13' text-anchor='middle'>Y</text>"
    # A -> cilindro
    s += f"<line x1='{vx+55}' y1='{vy}' x2='{vx+55}' y2='108' stroke='#e2e8f0'/>"
    # P y R de 1.01
    s += f"<line x1='{vx+40}' y1='{vy+58}' x2='{vx+40}' y2='470' stroke='#e2e8f0'/>"
    # valvulas 1.2 (izq) y 1.4 (der)
    s += _valv32(140, 330, '1.2')
    s += _valv32(400, 330, '1.4')
    # A de 1.2 (x=140+110*0.30=173) sube a piloto X (vx-8=292)
    s += f"<line x1='173' y1='330' x2='173' y2='196' stroke='#38bdf8' stroke-width='1.8'/>"
    s += f"<line x1='173' y1='196' x2='{vx-16}' y2='196' stroke='#38bdf8' stroke-width='1.8'/>"
    # A de 1.4 (x=400+33=433) sube a piloto Y (vx+126=426)
    s += f"<line x1='433' y1='330' x2='433' y2='210' stroke='#38bdf8' stroke-width='1.8'/>"
    s += f"<line x1='433' y1='210' x2='{vx+126}' y2='210' stroke='#38bdf8' stroke-width='1.8'/>"
    # P de 1.2 (x=140+27=167) y de 1.4 (x=400+27=427) a la linea de alimentacion
    s += f"<line x1='167' y1='392' x2='167' y2='470' stroke='#e2e8f0'/>"
    s += f"<line x1='427' y1='392' x2='427' y2='470' stroke='#e2e8f0'/>"
    s += f"<line x1='167' y1='470' x2='427' y2='470' stroke='#e2e8f0'/>"
    # unidad de mantenimiento 0.2 y valvula de corte 0.1
    ux, uy = 175, 445
    s += f"<rect x='{ux}' y='{uy}' width='80' height='44' fill='none' stroke='#e2e8f0' stroke-width='2' stroke-dasharray='5 4'/>"
    s += f"<line x1='{ux+26}' y1='{uy}' x2='{ux+26}' y2='{uy+44}'/>"
    s += f"<circle cx='{ux+54}' cy='{uy+22}' r='12' fill='none' stroke='#a78bfa' stroke-width='2'/>"
    s += f"<line x1='{ux+54}' y1='{uy+22}' x2='{ux+61}' y2='{uy+14}' stroke='#a78bfa' stroke-width='2'/>"
    s += f"<path d='M{ux+7} {uy+12} l12 20 M{ux+19} {uy+12} l-12 20' stroke='#38bdf8' stroke-width='1.5'/>"
    s += f"<text x='{ux+40}' y='{uy-6}' fill='#cbd5e1' font-size='14' text-anchor='middle'>0.2</text>"
    s += f"<line x1='{ux+80}' y1='{uy+22}' x2='167' y2='{uy+22}'/><line x1='167' y1='{uy+22}' x2='167' y2='470'/>"
    kx, ky = 70, 445
    s += f"<circle cx='{kx}' cy='{ky+22}' r='6' fill='none' stroke='#e2e8f0'/>"
    s += f"<polygon points='{kx+8},{ky+11} {kx+8},{ky+33} {kx+22},{ky+22}' fill='none' stroke='#e2e8f0' stroke-width='2'/>"
    s += f"<polygon points='{kx+36},{ky+11} {kx+36},{ky+33} {kx+22},{ky+22}' fill='none' stroke='#e2e8f0' stroke-width='2'/>"
    s += f"<line x1='{kx+22}' y1='{ky+22}' x2='{kx+22}' y2='{ky+12}'/>"
    s += f"<line x1='{kx+6}' y1='{ky+22}' x2='{kx}' y2='{ky+22}'/><line x1='{kx+36}' y1='{ky+22}' x2='{ux}' y2='{ky+22}'/>"
    s += f"<text x='{kx+18}' y='{ky-6}' fill='#cbd5e1' font-size='14' text-anchor='middle'>0.1</text>"
    s += "</svg>"
    return s

def fig_viga_2cargas():
    """Q2.1 viga 12 m con P1 a 5 m de A y P2 a 5 m de B."""
    x0, x1 = 80, 560
    xp1 = x0 + (5 / 12) * (x1 - x0)
    xp2 = x0 + (7 / 12) * (x1 - x0)
    yb = 160
    s = ("<svg viewBox='0 0 640 300' width='100%' style='max-width:580px;height:auto' "
         "fill='none' font-family='Inter,system-ui,sans-serif'>")
    for (xp, lab) in ((xp1, 'P1'), (xp2, 'P2')):
        s += f"<line x1='{xp:.0f}' y1='60' x2='{xp:.0f}' y2='{yb-2}' stroke='#fb7185' stroke-width='3'/>"
        s += f"<polygon points='{xp-8:.0f},{yb-14} {xp+8:.0f},{yb-14} {xp:.0f},{yb-1}' fill='#fb7185'/>"
        s += f"<text x='{xp:.0f}' y='50' fill='#fda4af' font-size='15' font-weight='700' text-anchor='middle'>{lab}</text>"
    s += f"<rect x='{x0}' y='{yb}' width='{x1-x0}' height='15' rx='2' fill='#1e293b' stroke='#e2e8f0' stroke-width='2'/>"
    s += f"<polygon points='{x0},{yb+15} {x0-13},{yb+42} {x0+13},{yb+42}' fill='none' stroke='#38bdf8' stroke-width='2'/>"
    for i in range(4):
        hx = x0 - 13 + i * 8.7
        s += f"<line x1='{hx:.0f}' y1='{yb+42}' x2='{hx-8:.0f}' y2='{yb+52}' stroke='#94a3b8' stroke-width='1.4'/>"
    s += f"<text x='{x0}' y='{yb-6}' fill='#7dd3fc' font-size='15' font-weight='700' text-anchor='middle'>A</text>"
    s += f"<polygon points='{x1},{yb+15} {x1-13},{yb+38} {x1+13},{yb+38}' fill='none' stroke='#38bdf8' stroke-width='2'/>"
    s += f"<circle cx='{x1-7}' cy='{yb+44}' r='5' fill='none' stroke='#38bdf8' stroke-width='1.8'/>"
    s += f"<circle cx='{x1+7}' cy='{yb+44}' r='5' fill='none' stroke='#38bdf8' stroke-width='1.8'/>"
    s += f"<line x1='{x1-15}' y1='{yb+50}' x2='{x1+15}' y2='{yb+50}' stroke='#94a3b8' stroke-width='1.6'/>"
    s += f"<text x='{x1}' y='{yb-6}' fill='#7dd3fc' font-size='15' font-weight='700' text-anchor='middle'>B</text>"
    yc = yb + 76
    for (xa, xbb, lab) in ((x0, xp1, 'a = 5 m'), (xp2, x1, 'a = 5 m')):
        s += f"<line x1='{xa:.0f}' y1='{yc}' x2='{xbb:.0f}' y2='{yc}' stroke='#94a3b8' stroke-width='1.4'/>"
        s += f"<polygon points='{xa:.0f},{yc} {xa+11:.0f},{yc-5} {xa+11:.0f},{yc+5}' fill='#94a3b8'/>"
        s += f"<polygon points='{xbb:.0f},{yc} {xbb-11:.0f},{yc-5} {xbb-11:.0f},{yc+5}' fill='#94a3b8'/>"
        s += f"<text x='{(xa+xbb)/2:.0f}' y='{yc-9}' fill='#cbd5e1' font-size='13' text-anchor='middle'>{lab}</text>"
    # cota total L
    yl = yc + 30
    s += f"<line x1='{x0}' y1='{yl}' x2='{x1}' y2='{yl}' stroke='#94a3b8' stroke-width='1.4'/>"
    s += f"<polygon points='{x0},{yl} {x0+11},{yl-5} {x0+11},{yl+5}' fill='#94a3b8'/>"
    s += f"<polygon points='{x1},{yl} {x1-11},{yl-5} {x1-11},{yl+5}' fill='#94a3b8'/>"
    s += f"<text x='{(x0+x1)//2}' y='{yl-9}' fill='#cbd5e1' font-size='13' text-anchor='middle'>L = 12 m</text>"
    s += "</svg>"
    return s

def fig_rl():
    xl, xr, yt, yb = 70, 450, 80, 200
    s = ("<svg viewBox='0 0 520 250' width='100%' style='max-width:460px;height:auto' "
         "fill='none' font-family='Inter,system-ui,sans-serif' stroke='#e2e8f0' stroke-width='2.2'>")
    s += f"<line x1='{xl}' y1='{yt}' x2='238' y2='{yt}'/><line x1='282' y1='{yt}' x2='{xr}' y2='{yt}'/>"
    s += f"<line x1='{xl}' y1='{yt}' x2='{xl}' y2='{yb}'/><line x1='{xr}' y1='{yt}' x2='{xr}' y2='{yb}'/>"
    s += f"<line x1='{xl}' y1='{yb}' x2='130' y2='{yb}'/><line x1='250' y1='{yb}' x2='330' y2='{yb}'/><line x1='420' y1='{yb}' x2='{xr}' y2='{yb}'/>"
    s += f"<circle cx='260' cy='{yt}' r='22' fill='none' stroke='#a78bfa' stroke-width='2.2'/>"
    s += f"<path d='M246 {yt} q7 -12 14 0 t14 0' fill='none' stroke='#a78bfa' stroke-width='2'/>"
    s += f"<text x='260' y='34' fill='#c4b5fd' font-size='15' font-weight='700' text-anchor='middle'>125 V / 50 Hz</text>"
    s += ("<polyline points='130,200 138,192 154,208 170,192 186,208 202,192 218,208 234,192 242,200 250,200' "
          "fill='none' stroke='#38bdf8' stroke-width='2.2'/>")
    s += f"<text x='190' y='236' fill='#7dd3fc' font-size='14' text-anchor='middle'>R = 25 &#8486;</text>"
    s += ("<path d='M330 200 q8 -14 16 0 q8 -14 16 0 q8 -14 16 0 q8 -14 16 0 l6 0' "
          "fill='none' stroke='#f59e0b' stroke-width='2.2'/>")
    s += f"<text x='378' y='236' fill='#fbbf24' font-size='14' text-anchor='middle'>L = 45 mH</text>"
    s += "</svg>"
    return s

def fig_bloq41():
    """Q4.1 · Z=f(X): lazo interno P1 con realim. P2·P3 y feedforward de X a la salida."""
    s = svg_open('880 340', 800)
    ym = 150
    s += arrow(60, ym, 118, ym)
    s += summer(134, ym)
    s += arrow(150, ym, 300, ym)
    s += box(300, ym-22, 82, 44, 'P1', '#22d3ee')
    s += arrow(382, ym, 560, ym)
    s += summer(576, ym)
    s += arrow(592, ym, 760, ym)
    s += txt(34, ym+5, 'X', '#e2e8f0', 16); s += txt(772, ym+5, 'Z', '#e2e8f0', 16)
    s += f"<circle cx='95' cy='{ym}' r='3.2' fill='#cbd5e1' stroke='none'/>"
    s += f"<circle cx='470' cy='{ym}' r='3.2' fill='#cbd5e1' stroke='none'/>"
    s += txt(116, ym-14, '+', '#4ade80', 14); s += txt(120, ym+26, '−', '#fb7185', 16)
    s += txt(560, ym-14, '+', '#4ade80', 14); s += txt(564, ym+26, '+', '#4ade80', 14)
    # realim P2 P3 (de N1 a sum1, negativa)
    s += box(480, 250, 82, 40, 'P3', '#a78bfa')
    s += box(300, 250, 82, 40, 'P2', '#a78bfa')
    s += line(470, ym, 470, 270); s += arrow(470, 270, 562, 270)
    s += arrow(480, 270, 382, 270)
    s += line(300, 270, 134, 270); s += arrow(134, 270, 134, ym+18)
    # feedforward de X a sum2 (+)
    s += line(95, ym, 95, 315); s += line(95, 315, 576, 315); s += arrow(576, 315, 576, ym+18)
    s += "</svg>"
    return s

def fig_bloques4():
    """Q4.2 · (idéntico al de la extraordinaria 2024)."""
    s = svg_open('880 340', 800)
    ym = 160
    s += arrow(70, ym, 108, ym)
    s += box(110, ym-22, 82, 44, 'G1', '#22d3ee')
    s += arrow(192, ym, 252, ym)
    s += summer(268, ym)
    s += arrow(284, ym, 340, ym)
    s += box(342, ym-22, 82, 44, 'G2', '#22d3ee')
    s += arrow(424, ym, 486, ym)
    s += summer(502, ym)
    s += arrow(518, ym, 574, ym)
    s += box(576, ym-22, 82, 44, 'G3', '#22d3ee')
    s += arrow(658, ym, 800, ym)
    s += txt(40, ym+5, 'E(s)', '#e2e8f0', 15); s += txt(812, ym+5, 'C(s)', '#e2e8f0', 15)
    s += box(305, 62, 82, 40, 'H2', '#a78bfa')
    s += f"<circle cx='460' cy='{ym}' r='3.2' fill='#cbd5e1' stroke='none'/>"
    s += line(460, ym, 460, 82); s += line(460, 82, 387, 82)
    s += line(305, 82, 268, 82); s += arrow(268, 82, 268, ym-18)
    s += txt(285, 96, '+', '#4ade80', 15); s += txt(250, ym+24, '+', '#4ade80', 15)
    s += txt(486, ym-16, '+', '#4ade80', 15); s += txt(512, ym+34, '−', '#fb7185', 17)
    s += f"<circle cx='88' cy='{ym}' r='3.2' fill='#cbd5e1' stroke='none'/>"
    s += line(88, ym, 88, 300); s += line(88, 300, 502, 300); s += arrow(502, 300, 502, ym+18)
    s += "</svg>"
    return s

# ---------------- FIGURAS SOLUCION ----------------

def fig_esfuerzos_2cargas():
    x0, x1 = 70, 520
    xp1 = x0 + (5 / 12) * (x1 - x0)
    xp2 = x0 + (7 / 12) * (x1 - x0)
    s = ("<svg viewBox='0 0 560 300' width='100%' style='max-width:520px;height:auto' "
         "fill='none' font-family='Inter,system-ui,sans-serif'>")
    yc = 70
    s += f"<line x1='{x0-5}' y1='{yc}' x2='{x1+10}' y2='{yc}' stroke='#94a3b8' stroke-width='1.4'/>"
    s += f"<text x='{x0-5}' y='{yc-42}' fill='#e2e8f0' font-size='13'>V (kg)</text>"
    yp, yn = yc - 34, yc + 34
    s += (f"<polygon points='{x0},{yc} {x0},{yp} {xp1:.0f},{yp} {xp1:.0f},{yc}' fill='rgba(56,189,248,.18)' stroke='none'/>")
    s += (f"<polygon points='{xp2:.0f},{yc} {xp2:.0f},{yn} {x1},{yn} {x1},{yc}' fill='rgba(251,113,133,.16)' stroke='none'/>")
    s += (f"<polyline points='{x0},{yp} {xp1:.0f},{yp} {xp1:.0f},{yc} {xp2:.0f},{yc} {xp2:.0f},{yn} {x1},{yn}' fill='none' stroke='#38bdf8' stroke-width='2.4'/>")
    s += f"<line x1='{x0}' y1='{yc}' x2='{x0}' y2='{yp}' stroke='#38bdf8' stroke-width='2.4'/>"
    s += f"<line x1='{x1}' y1='{yn}' x2='{x1}' y2='{yc}' stroke='#38bdf8' stroke-width='2.4'/>"
    s += f"<text x='{x0+8}' y='{yp-6}' fill='#7dd3fc' font-size='12'>+800</text>"
    s += f"<text x='{x1-8}' y='{yn+16}' fill='#7dd3fc' font-size='12' text-anchor='end'>-800</text>"
    yf = 240
    s += f"<line x1='{x0-5}' y1='{yf}' x2='{x1+10}' y2='{yf}' stroke='#94a3b8' stroke-width='1.4'/>"
    s += f"<text x='{x0-5}' y='{yf-92}' fill='#e2e8f0' font-size='13'>M (kg·m)</text>"
    ypk = yf - 80
    s += (f"<polygon points='{x0},{yf} {xp1:.0f},{ypk} {xp2:.0f},{ypk} {x1},{yf}' fill='rgba(74,222,128,.18)' stroke='none'/>")
    s += (f"<polyline points='{x0},{yf} {xp1:.0f},{ypk} {xp2:.0f},{ypk} {x1},{yf}' fill='none' stroke='#4ade80' stroke-width='2.4'/>")
    s += f"<text x='{(xp1+xp2)/2:.0f}' y='{ypk-6}' fill='#86efac' font-size='12' text-anchor='middle'>4000</text>"
    s += f"<text x='{x0}' y='{yf+18}' fill='#94a3b8' font-size='12' text-anchor='middle'>A</text>"
    s += f"<text x='{x1}' y='{yf+18}' fill='#94a3b8' font-size='12' text-anchor='middle'>B</text>"
    s += "</svg>"
    return s

def fig_kmap_maj():
    x0, y0, cw, ch = 130, 60, 60, 46
    cols = ['00', '01', '11', '10']
    vals = [[0, 0, 1, 0], [0, 1, 1, 1]]
    s = ("<svg viewBox='0 0 440 200' width='100%' style='max-width:410px;height:auto' "
         "fill='none' font-family='Inter,system-ui,sans-serif'>")
    s += f"<text x='{x0-34}' y='{y0-14}' fill='#94a3b8' font-size='13'>A\\BC</text>"
    for j, c in enumerate(cols):
        s += f"<text x='{x0+cw*j+cw/2:.0f}' y='{y0-14}' fill='#7dd3fc' font-size='14' text-anchor='middle'>{c}</text>"
    for i in range(2):
        s += f"<text x='{x0-18}' y='{y0+ch*i+ch/2+5:.0f}' fill='#7dd3fc' font-size='14' text-anchor='middle'>{i}</text>"
        for j in range(4):
            xx, yy = x0 + cw * j, y0 + ch * i
            s += f"<rect x='{xx}' y='{yy}' width='{cw}' height='{ch}' fill='none' stroke='#334155' stroke-width='1.4'/>"
            v = vals[i][j]
            col = '#4ade80' if v else '#64748b'
            s += f"<text x='{xx+cw/2:.0f}' y='{yy+ch/2+6:.0f}' fill='{col}' font-size='18' font-weight='700' text-anchor='middle'>{v}</text>"
    s += f"<rect x='{x0+cw*2-4}' y='{y0+ch-4}' width='{cw*2+8}' height='{ch+8}' rx='9' fill='none' stroke='#f59e0b' stroke-width='2.2'/>"
    s += f"<rect x='{x0+cw-6}' y='{y0+ch-8}' width='{cw*2+12}' height='{ch+16}' rx='12' fill='none' stroke='#38bdf8' stroke-width='2.2'/>"
    s += f"<rect x='{x0+cw*2-8}' y='{y0-6}' width='{cw+16}' height='{ch*2+12}' rx='11' fill='none' stroke='#a78bfa' stroke-width='2.2'/>"
    s += "</svg>"
    return s

def fig_nand_maj():
    s = ("<svg viewBox='0 0 470 260' width='100%' style='max-width:440px;height:auto' "
         "fill='none' font-family='Inter,system-ui,sans-serif' stroke='#e2e8f0' stroke-width='1.8'>")
    def nand(x, y, col, w=44, h=44):
        r = f"<path d='M{x} {y} L{x+w-h/2} {y} A{h/2} {h/2} 0 0 1 {x+w-h/2} {y+h} L{x} {y+h} Z' fill='none' stroke='{col}' stroke-width='2'/>"
        r += f"<circle cx='{x+w-h/2+h/2+5}' cy='{y+h/2}' r='4.5' fill='none' stroke='{col}' stroke-width='2'/>"
        return r
    s += nand(120, 20, '#38bdf8'); s += nand(120, 95, '#34d399'); s += nand(120, 170, '#a78bfa')
    s += "<text x='95' y='30' fill='#e2e8f0' font-size='13'>A</text><text x='95' y='52' fill='#e2e8f0' font-size='13'>B</text>"
    s += "<text x='95' y='105' fill='#e2e8f0' font-size='13'>A</text><text x='95' y='127' fill='#e2e8f0' font-size='13'>C</text>"
    s += "<text x='95' y='180' fill='#e2e8f0' font-size='13'>B</text><text x='95' y='202' fill='#e2e8f0' font-size='13'>C</text>"
    for yy in (30, 50, 105, 125, 180, 200):
        s += f"<line x1='108' y1='{yy}' x2='120' y2='{yy}'/>"
    s += nand(320, 95, '#f59e0b', 50, 70)
    for (yout, yin) in ((42, 108), (117, 125), (192, 142)):
        s += f"<line x1='177' y1='{yout}' x2='250' y2='{yout}'/><line x1='250' y1='{yout}' x2='250' y2='{yin}'/><line x1='250' y1='{yin}' x2='320' y2='{yin}'/>"
    s += "<line x1='383' y1='130' x2='450' y2='130'/><text x='456' y='135' fill='#e2e8f0' font-size='15'>F</text>"
    s += "</svg>"
    return s

TV_MAJ = ("<table class='dat'><tr><th>A</th><th>B</th><th>C</th><th>F</th></tr>"
          "<tr><td>0</td><td>0</td><td>0</td><td>0</td></tr>"
          "<tr><td>0</td><td>0</td><td>1</td><td>0</td></tr>"
          "<tr><td>0</td><td>1</td><td>0</td><td>0</td></tr>"
          "<tr style='background:rgba(74,222,128,.14)'><td>0</td><td>1</td><td>1</td><td>1</td></tr>"
          "<tr><td>1</td><td>0</td><td>0</td><td>0</td></tr>"
          "<tr style='background:rgba(74,222,128,.14)'><td>1</td><td>0</td><td>1</td><td>1</td></tr>"
          "<tr style='background:rgba(74,222,128,.14)'><td>1</td><td>1</td><td>0</td><td>1</td></tr>"
          "<tr style='background:rgba(74,222,128,.14)'><td>1</td><td>1</td><td>1</td><td>1</td></tr></table>")

# ---------------- CONTENIDO ----------------

data = {
 "meta": {
  "titulo": "Tecnología e Ingeniería II",
  "subtitulo": "Prueba de Acceso a la Universidad (PAU) · Universidad de Extremadura · Curso 2024-2025 · Examen resuelto y comentado",
  "cabecera_titulo": "PAU 2025 · <span>Tecnología e Ingeniería II</span> · Extremadura · Extraordinaria",
  "pill": "90 min · 4 preguntas · 2,5 pt/pregunta",
  "enunciado_pdf": "../../examens/Extremadura/Tecnologia_Extremadura_2025_extraordinaria.pdf",
  "pdf_dir": "pdf_ext_2025_extraordinaria",
  "footer": "Dpto. Tecnología · Solucionario PAU 2025 · Extremadura · Tecnología e Ingeniería II (Extraordinaria)",
  "intro_inicio": "El examen consta de <b>4 preguntas obligatorias</b> de 2,5 puntos. La primera es de opción única; en las otras tres se elige <b>una de las dos</b> cuestiones. Aquí se resuelven <b>todas</b> para repasar. Selecciona un apartado o una pregunta en la barra lateral.",
  "indice_nombre": "Exámenes de Extremadura",
  "indice_url": "index.html"
 },
 "bloques": [
  {
   "id": "b1", "titulo": "Pregunta 1 · Materiales y fabricación", "color": "#f59e0b",
   "descripcion_tarjeta": "Ensayo de dureza Brinell para comparar dos aceros inoxidables (AISI 304 y 316).",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#f59e0b' stroke-width='3'><circle cx='45' cy='26' r='11'/><path d='M45 4v11'/></svg>",
   "cuestiones": [
    {
     "id": "q1", "titulo": "Pregunta 1 · Dureza Brinell (AISI 304 vs 316)", "etiqueta": "MATERIALES",
     "menu": "P1 · Dureza Brinell", "titulo_corto": "P1",
     "meta": "Pregunta única y obligatoria · 2,5 puntos (a: 1,0 · b: 0,5 · c: 1,0)",
     "enunciado_html": "<p>Una empresa usa acero AISI 304 (170 HB) y estudia cambiar al AISI 316. Para conocer su resistencia al rayado, se somete el AISI 316 a un ensayo Brinell aplicando 750 kp con una bola de 5 mm; la huella resultante mide 2 mm. Contesta:</p><ol type='a'><li>¿Cuál es la dureza del acero? ¿Sería conveniente el cambio? <span class='pts'>(1 punto)</span></li><li>¿Se obtendría la misma dureza con bola de 10 mm y carga de 3000 kp? <span class='pts'>(0,5 puntos)</span></li><li>¿Cuál sería el diámetro de la huella en ese caso? <span class='pts'>(1 punto)</span></li></ol>",
     "figura_enunciado_svg": "",
     "aplica_html": "<p>\\(\\mathrm{HB}=\\frac{2F}{\\pi D(D-\\sqrt{D^2-d^2})}\\). Dos ensayos son comparables si conservan la constante \\(K=\\frac{F}{D^2}\\); en tal caso la dureza coincide y las huellas son semejantes.</p>",
     "solucion_html": "<h5>a) Dureza del AISI 316</h5><div class='formula'>$$\\sqrt{D^2-d^2}=\\sqrt{25-4}=4{,}583\\,\\mathrm{mm}$$</div><div class='formula'>$$\\mathrm{HB}=\\frac{2\\cdot 750}{\\pi\\cdot 5\\,(5-4{,}583)}=\\frac{1500}{6{,}556}=228{,}8$$</div><p>El AISI 316 (&asymp;229 HB) es <b>más duro</b> que el AISI 304 (170 HB), por lo que ofrece mayor resistencia al rayado: <b>sí sería conveniente</b> el cambio desde ese punto de vista.</p><div class='res'><b>HB &asymp; 229 kp/mm² &gt; 170 HB &rArr; conviene el cambio</b></div><h5>b) ¿Misma dureza con D=10 mm y F=3000 kp?</h5><p>Constante de ensayo: \\(K=\\frac{750}{25}=30\\) y \\(\\frac{3000}{100}=30\\). Coinciden, así que <b>sí</b>.</p><div class='res'><b>Sí: K = 30 en ambos casos</b></div><h5>c) Diámetro de la huella (D=10 mm)</h5><p>Por semejanza \\(d=2\\cdot\\frac{10}{5}=4\\,\\mathrm{mm}\\) (se comprueba con la fórmula de HB).</p><div class='res'><b>d = 4 mm</b></div>"
    }
   ]
  },
  {
   "id": "b2", "titulo": "Pregunta 2 · Sistemas mecánicos", "color": "#22d3ee",
   "descripcion_tarjeta": "Opción A: viga con dos cargas puntuales. Opción B: circuito neumático con válvula pilotada.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#22d3ee' stroke-width='3'><path d='M10 34h70'/><path d='M32 34v-16M58 34v-16'/><path d='M10 34l-6 12h12z'/></svg>",
   "cuestiones": [
    {
     "id": "q2a", "titulo": "Pregunta 2.1 (Opción A) · Viga con dos cargas puntuales", "etiqueta": "OPCIÓN A",
     "menu": "P2.1 (A) · Viga (2 cargas)", "titulo_corto": "P2.1",
     "meta": "2,5 puntos (a: 1,25 · b: 1,25)",
     "enunciado_html": "<p>Para la viga mostrada (P1 = P2 = 800 kg, a = 5 m, L = 12 m):</p><ol type='a'><li>Encuentra las ecuaciones de la fuerza cortante y el momento flector. <span class='pts'>(1,25 puntos)</span></li><li>Dibuja los diagramas correspondientes. <span class='pts'>(1,25 puntos)</span></li></ol>",
     "figura_enunciado_svg": "<figure class='fig'>" + fig_viga_2cargas() + "<figcaption>Viga biapoyada de 12 m con dos cargas iguales P1 y P2 situadas a 5 m de cada apoyo.</figcaption></figure>",
     "aplica_html": "<p>Por simetría (cargas iguales situadas simétricamente) \\(R_A=R_B=\\frac{P_1+P_2}{2}\\). El cortante es constante a tramos y el momento flector es máximo (y constante) en el tramo central entre las cargas.</p>",
     "solucion_html": "<h5>Reacciones</h5><div class='formula'>$$R_A=R_B=\\frac{800+800}{2}=800\\,\\mathrm{kg}$$</div><h5>a) Ecuaciones (origen en A)</h5><p>Tramo 0&ndash;5 m: \\(V=800\\,\\mathrm{kg}\\), \\(M=800\\,x\\).</p><p>Tramo 5&ndash;7 m: \\(V=0\\), \\(M=4000\\,\\mathrm{kg\\cdot m}\\) (constante).</p><p>Tramo 7&ndash;12 m: \\(V=-800\\,\\mathrm{kg}\\), \\(M=-800\\,x+9600\\).</p><h5>Valores máximos</h5><div class='formula'>$$V_{max}=800\\,\\mathrm{kg}\\qquad M_{max}=800\\cdot 5=4000\\,\\mathrm{kg\\cdot m}$$</div><div class='res'><b>V<sub>máx</sub> = 800 kg &nbsp;·&nbsp; M<sub>máx</sub> = 4000 kg&middot;m (tramo central)</b></div><h5>b) Diagramas</h5><figure class='fig'>" + fig_esfuerzos_2cargas() + "<figcaption>Cortante escalonado (+800 / 0 / &minus;800 kg) y momento flector trapezoidal (máx. 4000 kg&middot;m).</figcaption></figure>"
    },
    {
     "id": "q2b", "titulo": "Pregunta 2.2 (Opción B) · Circuito neumático con válvula pilotada", "etiqueta": "OPCIÓN B",
     "menu": "P2.2 (B) · Circuito neumático", "titulo_corto": "P2.2",
     "meta": "2,5 puntos (a: 1,25 · b: 1,25)",
     "enunciado_html": "<p>Para el circuito neumático representado, se pide:</p><ol type='a'><li>Identificar los componentes, indicando el significado de las letras sobre los orificios del elemento 1.2. <span class='pts'>(1,25 puntos)</span></li><li>Explicar el funcionamiento. <span class='pts'>(1,25 puntos)</span></li></ol>",
     "figura_enunciado_svg": "<figure class='fig'>" + fig_neumatico2() + "<figcaption>Cilindro (1.0), válvula distribuidora pilotada 4/2 (1.01) con pilotajes X e Y, válvulas 3/2 con rodillo (1.2 y 1.4) y grupo de acondicionamiento (0.1, 0.2).</figcaption></figure>",
     "aplica_html": "<p>Reconoceremos la simbología neumática: cilindro, válvula distribuidora pilotada (biestable), válvulas 3/2 de rodillo como emisoras de señal y unidad de mantenimiento. Las letras P, A y R son la <b>notación antigua</b> de los orificios de una válvula distribuidora.</p>",
     "solucion_html": "<h5>a) Componentes y significado de las letras de 1.2</h5><ul><li><b>1.0</b> — Cilindro con retorno por muelle.</li><li><b>1.01</b> — Válvula distribuidora <b>4/2 pilotada</b> (biestable) con pilotajes neumáticos <b>X</b> e <b>Y</b>; A es la salida hacia el cilindro.</li><li><b>1.2</b> y <b>1.4</b> — Válvulas <b>3/2 accionadas por rodillo</b> y retorno por muelle: emiten las señales de pilotaje X e Y.</li><li><b>0.2</b> — Unidad de mantenimiento (filtro-regulador con manómetro); <b>0.1</b> — válvula de corte general.</li></ul><p>Letras de los orificios de 1.2 (notación antigua): <b>P</b> = alimentación (presión); <b>A</b> = utilización (salida de señal); <b>R</b> = escape a la atmósfera.</p><h5>b) Funcionamiento</h5><p>El aire tratado en 0.2 alimenta el orificio <b>P</b> de las válvulas 1.2 y 1.4. Cuando se acciona el <b>rodillo de 1.2</b>, ésta conecta <b>P&rarr;A</b> y envía una señal de pilotaje a <b>X</b>, que conmuta la válvula 1.01 y hace que el cilindro <b>avance</b>. Al accionar el <b>rodillo de 1.4</b>, se envía señal a <b>Y</b>, la 1.01 conmuta a la otra posición y el cilindro <b>retrocede</b>. Como 1.01 es biestable, mantiene la posición aunque cese la señal, hasta recibir la señal contraria.</p>"
    }
   ]
  },
  {
   "id": "b3", "titulo": "Pregunta 3 · Sistemas eléctricos y electrónicos", "color": "#a78bfa",
   "descripcion_tarjeta": "Opción A: circuito RL serie (bobina de un contactor). Opción B: función mayoría con puertas NAND.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#a78bfa' stroke-width='3'><path d='M8 30q10-16 20 0t20 0 20 0'/></svg>",
   "cuestiones": [
    {
     "id": "q3a", "titulo": "Pregunta 3.1 (Opción A) · Circuito RL serie", "etiqueta": "OPCIÓN A",
     "menu": "P3.1 (A) · Circuito RL serie", "titulo_corto": "P3.1",
     "meta": "2,5 puntos (a: 0,75 · b: 0,5 · c: 0,5 · d: 0,75)",
     "enunciado_html": "<p>El circuito equivalente de la bobina de un contactor consta de R = 25 &ohm; y una bobina pura de 45 mH, alimentado a 125 V / 50 Hz. Calcula:</p><ol type='a'><li>Impedancia total. <span class='pts'>(0,75 puntos)</span></li><li>Intensidad total. <span class='pts'>(0,5 puntos)</span></li><li>Ángulo de desfase. <span class='pts'>(0,5 puntos)</span></li><li>Caída de tensión en la resistencia y en la bobina. <span class='pts'>(0,75 puntos)</span></li></ol>",
     "figura_enunciado_svg": "<figure class='fig'>" + fig_rl() + "<figcaption>Circuito RL serie: R = 25 &ohm; y L = 45 mH a 125 V / 50 Hz.</figcaption></figure>",
     "aplica_html": "<p>\\(X_L=2\\pi f L\\); \\(Z=\\sqrt{R^2+X_L^2}\\); \\(I=\\frac{V}{Z}\\); \\(\\varphi=\\arctan\\frac{X_L}{R}\\); \\(V_R=IR\\), \\(V_L=IX_L\\).</p>",
     "solucion_html": "<h5>a) Impedancia total</h5><div class='formula'>$$X_L=2\\pi\\cdot 50\\cdot 0{,}045=14{,}14\\,\\Omega$$</div><div class='formula'>$$Z=\\sqrt{25^2+14{,}14^2}=\\sqrt{824{,}9}=28{,}72\\,\\Omega$$</div><div class='res'><b>Z &asymp; 28,72 &ohm;</b></div><h5>b) Intensidad total</h5><div class='formula'>$$I=\\frac{125}{28{,}72}=4{,}35\\,\\mathrm{A}$$</div><div class='res'><b>I &asymp; 4,35 A</b></div><h5>c) Ángulo de desfase</h5><div class='formula'>$$\\varphi=\\arctan\\frac{14{,}14}{25}=29{,}5^\\circ$$</div><div class='res'><b>&phi; &asymp; 29,5° (inductivo)</b></div><h5>d) Caídas de tensión</h5><div class='formula'>$$V_R=IR=4{,}35\\cdot 25=108{,}8\\,\\mathrm{V}\\qquad V_L=IX_L=4{,}35\\cdot 14{,}14=61{,}5\\,\\mathrm{V}$$</div><div class='res'><b>V<sub>R</sub> &asymp; 108,8 V &nbsp;·&nbsp; V<sub>L</sub> &asymp; 61,5 V</b></div>"
    },
    {
     "id": "q3b", "titulo": "Pregunta 3.2 (Opción B) · Función mayoría con NAND", "etiqueta": "OPCIÓN B",
     "menu": "P3.2 (B) · Función mayoría", "titulo_corto": "P3.2",
     "meta": "2,5 puntos (a: 0,5 · b: 0,5 · c: 0,5 · d: 1,0)",
     "enunciado_html": "<p>Un motor se controla con tres pulsadores A, B, C y se activa cuando se pulsan <b>al menos dos</b> cualesquiera. Se pide:</p><ol type='a'><li>Tabla de verdad. <span class='pts'>(0,5 puntos)</span></li><li>Función lógica en primera forma canónica. <span class='pts'>(0,5 puntos)</span></li><li>Simplificar por Karnaugh. <span class='pts'>(0,5 puntos)</span></li><li>Implementar con puertas NAND. <span class='pts'>(1 punto)</span></li></ol>",
     "figura_enunciado_svg": "",
     "aplica_html": "<p>Es la <b>función mayoría</b> de tres variables. La primera forma canónica es la suma de minterms; Karnaugh la reduce y, por De Morgan, la suma de productos se implementa con NAND.</p>",
     "solucion_html": "<h5>a) Tabla de verdad</h5>" + TV_MAJ + "<h5>b) Primera forma canónica</h5><div class='formula'>$$F=\\bar ABC+A\\bar BC+AB\\bar C+ABC$$</div><h5>c) Simplificación por Karnaugh</h5><figure class='fig'>" + fig_kmap_maj() + "<figcaption>Grupos AB (naranja), AC (azul) y BC (violeta).</figcaption></figure><div class='formula'>$$F=AB+AC+BC$$</div><div class='res'><b>F = AB + AC + BC</b></div><h5>d) Implementación con NAND</h5><p>\\(F=\\overline{\\overline{AB}\\cdot\\overline{AC}\\cdot\\overline{BC}}\\): tres NAND de 2 entradas y una NAND de 3 entradas.</p><figure class='fig'>" + fig_nand_maj() + "<figcaption>Implementación de la función mayoría con puertas NAND.</figcaption></figure>"
    }
   ]
  },
  {
   "id": "b4", "titulo": "Pregunta 4 · Sistemas automáticos", "color": "#34d399",
   "descripcion_tarjeta": "Opción A y B: reducción de diagramas de bloques hasta la función de transferencia.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#34d399' stroke-width='3'><rect x='12' y='22' width='20' height='16'/><rect x='52' y='22' width='20' height='16'/><path d='M32 30h20'/></svg>",
   "cuestiones": [
    {
     "id": "q4a", "titulo": "Pregunta 4.1 (Opción A) · Función de transferencia Z = f(X)", "etiqueta": "OPCIÓN A",
     "menu": "P4.1 (A) · Diagrama de bloques", "titulo_corto": "P4.1",
     "meta": "2,5 puntos",
     "enunciado_html": "<p>Dado el diagrama de bloques de la figura, obtén la función de transferencia \\(Z=f(X)\\). <span class='pts'>(2,5 puntos)</span></p>",
     "figura_enunciado_svg": "<figure class='fig'>" + fig_bloq41() + "<figcaption>Lazo interno de G<sub>1</sub>... con realimentación P<sub>2</sub>·P<sub>3</sub> (negativa) y una rama directa de X que se suma a la salida.</figcaption></figure>",
     "aplica_html": "<p>El lazo de \\(P_1\\) realimentado por \\(P_2P_3\\) (negativo) da \\(\\frac{P_1}{1+P_1P_2P_3}\\). Además, la entrada \\(X\\) se suma directamente a la salida en el segundo comparador.</p>",
     "solucion_html": "<h5>Lazo interno</h5><p>Sea \\(Y\\) la señal tras \\(P_1\\). El primer comparador da \\(X-P_2P_3\\,Y\\), luego \\(Y=P_1(X-P_2P_3Y)\\):</p><div class='formula'>$$Y=\\frac{P_1}{1+P_1P_2P_3}\\,X$$</div><h5>Salida (segundo comparador: Y + X)</h5><div class='formula'>$$Z=Y+X=\\left(\\frac{P_1}{1+P_1P_2P_3}+1\\right)X$$</div><div class='formula'>$$\\boxed{\\dfrac{Z}{X}=\\dfrac{1+P_1+P_1P_2P_3}{1+P_1P_2P_3}}$$</div><div class='res'><b>Z/X = (1 + P<sub>1</sub> + P<sub>1</sub>P<sub>2</sub>P<sub>3</sub>) / (1 + P<sub>1</sub>P<sub>2</sub>P<sub>3</sub>)</b></div>"
    },
    {
     "id": "q4b", "titulo": "Pregunta 4.2 (Opción B) · Reducción de un sistema de control", "etiqueta": "OPCIÓN B",
     "menu": "P4.2 (B) · Sistema de control", "titulo_corto": "P4.2",
     "meta": "2,5 puntos",
     "enunciado_html": "<p>Simplifica el siguiente sistema de control hasta conseguir la función de transferencia. <span class='pts'>(2,5 puntos)</span></p>",
     "figura_enunciado_svg": "<figure class='fig'>" + fig_bloques4() + "<figcaption>Lazo interno de G<sub>2</sub> con H<sub>2</sub> (positivo) y lazo externo unitario negativo tomado de la línea de entrada.</figcaption></figure>",
     "aplica_html": "<p>El lazo positivo de \\(G_2\\) con \\(H_2\\) da \\(\\frac{G_2}{1-G_2H_2}\\). La rama inferior resta la propia entrada \\(E\\) en el segundo comparador.</p>",
     "solucion_html": "<h5>Lazo interno (H<sub>2</sub>, positivo)</h5><div class='formula'>$$G_2'=\\frac{G_2}{1-G_2H_2}$$</div><h5>Camino directo y comparador final</h5><p>Al segundo comparador llega \\(G_1G_2'\\,E\\) por arriba y se resta \\(E\\) por abajo; tras \\(G_3\\):</p><div class='formula'>$$\\boxed{\\dfrac{C(s)}{E(s)}=G_3\\left(\\dfrac{G_1G_2}{1-G_2H_2}-1\\right)=\\dfrac{G_3\\,(G_1G_2-1+G_2H_2)}{1-G_2H_2}}$$</div><div class='res'><b>C/E = G<sub>3</sub>(G<sub>1</sub>G<sub>2</sub> − 1 + G<sub>2</sub>H<sub>2</sub>) / (1 − G<sub>2</sub>H<sub>2</sub>)</b></div>"
    }
   ]
  }
 ]
}

out = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ext_2025_extraordinaria.json"))
with open(out, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print("JSON escrito:", out)
