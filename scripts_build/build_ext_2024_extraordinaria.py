#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera el JSON del examen Extremadura EBAU 2024 (extraordinaria) para pau-dashboard."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import svg_open, box, summer, arrow, line, txt

# ---------------- FIGURAS DEL ENUNCIADO ----------------

def fig_neumatico():
    """Q1 · circuito neumatico: cilindro simple efecto, valvula estranguladora,
    valvula 3/2 con pulsador y unidad de mantenimiento."""
    s = ("<svg viewBox='0 0 560 640' width='100%' style='max-width:440px;height:auto' "
         "fill='none' font-family='Inter,system-ui,sans-serif' stroke='#e2e8f0' stroke-width='2'>")
    # ---- 1.0 cilindro simple efecto con muelle (arriba) ----
    cx, cy = 300, 70
    s += f"<rect x='{cx}' y='{cy}' width='170' height='60' fill='#1e293b' stroke='#e2e8f0' stroke-width='2'/>"
    s += f"<rect x='{cx+8}' y='{cy+4}' width='14' height='52' fill='#38bdf8' stroke='#38bdf8'/>"   # embolo
    s += f"<line x1='{cx+22}' y1='{cy+30}' x2='{cx+150}' y2='{cy+30}' stroke='#e2e8f0' stroke-width='4'/>"  # vastago
    s += f"<line x1='{cx+150}' y1='{cy+30}' x2='{cx+200}' y2='{cy+30}' stroke='#e2e8f0' stroke-width='4'/>"
    # muelle
    sp = f"M{cx+30} {cy+30}"
    for i in range(6):
        xx = cx + 30 + i * 18
        sp += f" L{xx+9} {cy+14} L{xx+18} {cy+46}"
    s += f"<path d='{sp}' fill='none' stroke='#f59e0b' stroke-width='1.8'/>"
    s += f"<text x='{cx+80}' y='{cy-10}' fill='#cbd5e1' font-size='15' text-anchor='middle'>1.0</text>"
    # linea de salida del cilindro hacia abajo
    s += f"<line x1='{cx+15}' y1='{cy+60}' x2='{cx+15}' y2='190' stroke='#e2e8f0' stroke-width='2'/>"
    # ---- 1.01 valvula estranguladora antirretorno ----
    bx, by = cx - 40, 190
    s += f"<rect x='{bx}' y='{by}' width='110' height='90' fill='none' stroke='#94a3b8' stroke-width='1.6' stroke-dasharray='5 4'/>"
    # antirretorno (bola + asiento) a la izquierda
    s += f"<circle cx='{bx+30}' cy='{by+45}' r='12' fill='none' stroke='#38bdf8' stroke-width='2'/>"
    s += f"<line x1='{bx+18}' y1='{by+30}' x2='{bx+18}' y2='{by+60}' stroke='#38bdf8' stroke-width='2'/>"
    # estrangulador (flecha oblicua) a la derecha
    s += f"<line x1='{bx+62}' y1='{by+30}' x2='{bx+82}' y2='{by+60}' stroke='#f59e0b' stroke-width='2'/>"
    s += f"<line x1='{bx+82}' y1='{by+30}' x2='{bx+62}' y2='{by+60}' stroke='#f59e0b' stroke-width='2'/>"
    s += f"<line x1='{bx+55}' y1='{by+68}' x2='{bx+80}' y2='{by+50}' stroke='#f59e0b' stroke-width='1.8' marker-end='url(#arn)'/>"
    s += f"<line x1='{bx+10}' y1='{by+45}' x2='{bx+18}' y2='{by+45}'/><line x1='{bx+42}' y1='{by+45}' x2='{bx+100}' y2='{by+45}'/>"
    s += f"<line x1='{cx+15}' y1='{by}' x2='{cx+15}' y2='{by+45}'/><line x1='{cx+15}' y1='{by+45}' x2='{bx+100}' y2='{by+45}'/>"
    s += ("<defs><marker id='arn' markerWidth='9' markerHeight='8' refX='6' refY='3' orient='auto'>"
          "<path d='M0,0 L7,3 L0,6 Z' fill='#f59e0b'/></marker>"
          "<marker id='ara' markerWidth='9' markerHeight='8' refX='6' refY='3' orient='auto'>"
          "<path d='M0,0 L7,3 L0,6 Z' fill='#e2e8f0'/></marker></defs>")
    s += f"<text x='{bx+125}' y='{by+50}' fill='#cbd5e1' font-size='15'>1.01</text>"
    s += f"<line x1='{bx+30}' y1='{by+90}' x2='{bx+30}' y2='360' stroke='#e2e8f0' stroke-width='2'/>"
    # ---- 1.1 valvula 3/2 con pulsador y muelle ----
    vx, vy = bx - 30, 360
    s += f"<rect x='{vx}' y='{vy}' width='120' height='60' fill='none' stroke='#e2e8f0' stroke-width='2'/>"
    s += f"<line x1='{vx+60}' y1='{vy}' x2='{vx+60}' y2='{vy+60}' stroke='#e2e8f0' stroke-width='2'/>"
    # casilla derecha (reposo): 1->cerrado, 2->3 escape ; flecha diagonal
    s += f"<line x1='{vx+70}' y1='{vy+48}' x2='{vx+100}' y2='{vy+14}' stroke='#38bdf8' stroke-width='2' marker-end='url(#arb)'/>"
    s += f"<line x1='{vx+82}' y1='{vy+12}' x2='{vx+82}' y2='{vy+20}' stroke='#e2e8f0'/>"   # tope
    # casilla izquierda (accionada): flecha vertical
    s += f"<line x1='{vx+30}' y1='{vy+48}' x2='{vx+30}' y2='{vy+14}' stroke='#38bdf8' stroke-width='2' marker-end='url(#arb)'/>"
    s += ("<defs><marker id='arb' markerWidth='9' markerHeight='8' refX='6' refY='3' orient='auto'>"
          "<path d='M0,0 L7,3 L0,6 Z' fill='#38bdf8'/></marker></defs>")
    # pulsador a la izquierda
    s += f"<line x1='{vx}' y1='{vy+30}' x2='{vx-24}' y2='{vy+30}'/>"
    s += f"<rect x='{vx-38}' y='{vy+22}' width='14' height='16' fill='none' stroke='#e2e8f0'/>"
    s += f"<line x1='{vx-31}' y1='{vy+22}' x2='{vx-31}' y2='{vy+10}'/>"
    # muelle a la derecha
    s += f"<line x1='{vx+120}' y1='{vy+30}' x2='{vx+134}' y2='{vy+30}'/>"
    sp2 = f"M{vx+134} {vy+30}"
    for i in range(3):
        xx = vx + 134 + i * 12
        sp2 += f" L{xx+6} {vy+22} L{xx+12} {vy+38}"
    s += f"<path d='{sp2}' fill='none' stroke='#f59e0b' stroke-width='1.6'/>"
    s += f"<text x='{vx+108}' y='{vy-8}' fill='#cbd5e1' font-size='15'>1.1</text>"
    # puertos: 2 (arriba, salida a 1.01), 1 (abajo, presion), 3 (escape)
    s += f"<text x='{vx+52}' y='{vy-8}' fill='#7dd3fc' font-size='13'>2</text>"
    s += f"<text x='{vx+52}' y='{vy+78}' fill='#7dd3fc' font-size='13'>1</text>"
    s += f"<text x='{vx+96}' y='{vy+78}' fill='#7dd3fc' font-size='13'>3</text>"
    # linea 2 -> arriba (ya viene de 1.01 a x=bx+30 = vx+60)
    s += f"<line x1='{vx+60}' y1='{vy}' x2='{vx+60}' y2='{vy}' stroke='#e2e8f0'/>"
    # escape 3
    s += f"<line x1='{vx+90}' y1='{vy+60}' x2='{vx+90}' y2='{vy+72}'/><polygon points='{vx+83},{vy+72} {vx+97},{vy+72} {vx+90},{vy+82}' fill='none' stroke='#e2e8f0'/>"
    # puerto 1 hacia abajo (alimentacion)
    s += f"<line x1='{vx+60}' y1='{vy+60}' x2='{vx+60}' y2='545'/>"
    s += f"<line x1='{vx+60}' y1='545' x2='250' y2='545'/>"
    # ---- 0.2 unidad de mantenimiento (filtro-regulador + manometro) ----
    ux, uy = 155, 520
    s += f"<rect x='{ux}' y='{uy}' width='95' height='50' fill='none' stroke='#e2e8f0' stroke-width='2' stroke-dasharray='5 4'/>"
    s += f"<line x1='{ux+30}' y1='{uy}' x2='{ux+30}' y2='{uy+50}'/>"
    s += f"<circle cx='{ux+62}' cy='{uy+25}' r='13' fill='none' stroke='#a78bfa' stroke-width='2'/>"
    s += f"<line x1='{ux+62}' y1='{uy+25}' x2='{ux+70}' y2='{uy+16}' stroke='#a78bfa' stroke-width='2'/>"
    s += f"<path d='M{ux+8} {uy+14} l14 22 M{ux+22} {uy+14} l-14 22' stroke='#38bdf8' stroke-width='1.6'/>"
    s += f"<text x='{ux+45}' y='{uy-8}' fill='#cbd5e1' font-size='15' text-anchor='middle'>0.2</text>"
    s += f"<line x1='{ux+95}' y1='{uy+25}' x2='250' y2='{uy+25}'/><line x1='250' y1='{uy+25}' x2='250' y2='545'/>"
    # ---- 0.1 valvula de corte (llave) ----
    kx, ky = 70, 520
    s += f"<circle cx='{kx}' cy='{ky+25}' r='6' fill='none' stroke='#e2e8f0'/>"
    s += f"<line x1='{kx+6}' y1='{ky+25}' x2='{kx+24}' y2='{ky+25}'/>"
    s += f"<polygon points='{kx+24},{ky+13} {kx+24},{ky+37} {kx+38},{ky+25}' fill='none' stroke='#e2e8f0' stroke-width='2'/>"
    s += f"<polygon points='{kx+52},{ky+13} {kx+52},{ky+37} {kx+38},{ky+25}' fill='none' stroke='#e2e8f0' stroke-width='2'/>"
    s += f"<line x1='{kx+38}' y1='{ky+25}' x2='{kx+38}' y2='{ky+15}'/><line x1='{kx+33}' y1='{ky+15}' x2='{kx+43}' y2='{ky+15}'/>"
    s += f"<line x1='{kx+52}' y1='{ky+25}' x2='{ux}' y2='{ky+25}'/>"
    s += f"<text x='{kx+28}' y='{ky-8}' fill='#cbd5e1' font-size='15' text-anchor='middle'>0.1</text>"
    s += "</svg>"
    return s

def fig_bloques4():
    """Q4 · diagrama de bloques con H2 (realim. positiva) y lazo unitario negativo."""
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
    s += txt(40, ym+5, 'E(s)', '#e2e8f0', 15)
    s += txt(812, ym+5, 'C(s)', '#e2e8f0', 15)
    # H2 arriba (realimentacion positiva alrededor de G2)
    s += box(305, 62, 82, 40, 'H2', '#a78bfa')
    s += f"<circle cx='460' cy='{ym}' r='3.2' fill='#cbd5e1' stroke='none'/>"
    s += line(460, ym, 460, 82); s += line(460, 82, 387, 82)
    s += line(305, 82, 268, 82); s += arrow(268, 82, 268, ym-18)
    s += txt(285, 96, '+', '#4ade80', 15)          # entrada superior de sum1
    s += txt(250, ym+24, '+', '#4ade80', 15)       # entrada izquierda sum1
    s += txt(486, ym-16, '+', '#4ade80', 15)       # entrada superior sum2
    s += txt(512, ym+34, '−', '#fb7185', 17)       # entrada inferior sum2
    # lazo inferior: toma de la linea E(s) (unitario) a sum2 (-)
    s += f"<circle cx='88' cy='{ym}' r='3.2' fill='#cbd5e1' stroke='none'/>"
    s += line(88, ym, 88, 300); s += line(88, 300, 502, 300); s += arrow(502, 300, 502, ym+18)
    s += "</svg>"
    return s

def fig_viga5():
    """Q5 · viga biapoyada con carga puntual central."""
    x0, x1, xc = 90, 540, 315
    yb = 150
    s = ("<svg viewBox='0 0 620 290' width='100%' style='max-width:560px;height:auto' "
         "fill='none' font-family='Inter,system-ui,sans-serif'>")
    # carga puntual
    s += f"<line x1='{xc}' y1='55' x2='{xc}' y2='{yb-2}' stroke='#fb7185' stroke-width='3'/>"
    s += f"<polygon points='{xc-8},{yb-14} {xc+8},{yb-14} {xc},{yb-1}' fill='#fb7185'/>"
    s += f"<text x='{xc+16}' y='80' fill='#fda4af' font-size='16' font-weight='700'>P = 3000 N</text>"
    # viga
    s += f"<rect x='{x0}' y='{yb}' width='{x1-x0}' height='15' rx='2' fill='#1e293b' stroke='#e2e8f0' stroke-width='2'/>"
    # apoyo fijo A
    s += f"<polygon points='{x0},{yb+15} {x0-13},{yb+42} {x0+13},{yb+42}' fill='none' stroke='#38bdf8' stroke-width='2'/>"
    for i in range(4):
        hx = x0 - 13 + i * 8.7
        s += f"<line x1='{hx:.0f}' y1='{yb+42}' x2='{hx-8:.0f}' y2='{yb+52}' stroke='#94a3b8' stroke-width='1.4'/>"
    s += f"<text x='{x0}' y='{yb-6}' fill='#7dd3fc' font-size='15' font-weight='700' text-anchor='middle'>A</text>"
    # apoyo movil B
    s += f"<polygon points='{x1},{yb+15} {x1-13},{yb+38} {x1+13},{yb+38}' fill='none' stroke='#38bdf8' stroke-width='2'/>"
    s += f"<circle cx='{x1-7}' cy='{yb+44}' r='5' fill='none' stroke='#38bdf8' stroke-width='1.8'/>"
    s += f"<circle cx='{x1+7}' cy='{yb+44}' r='5' fill='none' stroke='#38bdf8' stroke-width='1.8'/>"
    s += f"<line x1='{x1-15}' y1='{yb+50}' x2='{x1+15}' y2='{yb+50}' stroke='#94a3b8' stroke-width='1.6'/>"
    s += f"<text x='{x1}' y='{yb-6}' fill='#7dd3fc' font-size='15' font-weight='700' text-anchor='middle'>B</text>"
    # cotas 2m + 2m
    yc = yb + 78
    for (xa, xbb, lab) in ((x0, xc, '2 m'), (xc, x1, '2 m')):
        s += f"<line x1='{xa}' y1='{yc}' x2='{xbb}' y2='{yc}' stroke='#94a3b8' stroke-width='1.4'/>"
        s += f"<polygon points='{xa},{yc} {xa+11},{yc-5} {xa+11},{yc+5}' fill='#94a3b8'/>"
        s += f"<polygon points='{xbb},{yc} {xbb-11},{yc-5} {xbb-11},{yc+5}' fill='#94a3b8'/>"
        s += f"<text x='{(xa+xbb)//2}' y='{yc-9}' fill='#cbd5e1' font-size='14' text-anchor='middle'>{lab}</text>"
    s += "</svg>"
    return s

def fig_rc():
    """Q8 · circuito RC serie."""
    xl, xr, yt, yb = 70, 470, 70, 200
    s = ("<svg viewBox='0 0 540 250' width='100%' style='max-width:470px;height:auto' "
         "fill='none' font-family='Inter,system-ui,sans-serif' stroke='#e2e8f0' stroke-width='2.2'>")
    # fase F (arriba), neutro N (medio)
    s += f"<text x='40' y='{yt+5}' fill='#e2e8f0' font-size='15' text-anchor='end'>F</text>"
    s += f"<text x='40' y='125' fill='#e2e8f0' font-size='15' text-anchor='end'>N</text>"
    s += f"<line x1='55' y1='{yt}' x2='{xr}' y2='{yt}'/>"
    s += f"<line x1='55' y1='120' x2='{xr}' y2='120'/>"
    s += f"<text x='260' y='40' fill='#c4b5fd' font-size='15' font-weight='700' text-anchor='middle'>220 V / 50 Hz</text>"
    s += f"<circle cx='150' cy='{yt}' r='3.4' fill='#e2e8f0'/><circle cx='{xr}' cy='{yt}' r='3.4' fill='#e2e8f0'/>"
    s += f"<circle cx='150' cy='120' r='3.4' fill='#e2e8f0'/><circle cx='400' cy='120' r='3.4' fill='#e2e8f0'/>"
    # rama serie: de F (x=150) baja a C, luego R, sube a N (x=400)
    s += f"<line x1='150' y1='{yt}' x2='150' y2='{yb-45}'/>"
    # condensador
    s += f"<line x1='130' y1='{yb-45}' x2='170' y2='{yb-45}'/>"
    s += f"<line x1='130' y1='{yb-30}' x2='170' y2='{yb-30}'/>"
    s += f"<line x1='150' y1='{yb-30}' x2='150' y2='{yb}'/>"
    s += f"<line x1='150' y1='{yb-45}' x2='150' y2='{yb-60}'/>"
    s += f"<text x='150' y='{yb+28}' fill='#7dd3fc' font-size='14' text-anchor='middle'>C = 120 &micro;F</text>"
    # tramo inferior a R
    s += f"<line x1='150' y1='{yb}' x2='300' y2='{yb}'/>"
    s += f"<rect x='300' y='{yb-13}' width='70' height='26' fill='none' stroke='#f59e0b' stroke-width='2.2'/>"
    s += f"<line x1='370' y1='{yb}' x2='400' y2='{yb}'/><line x1='400' y1='{yb}' x2='400' y2='120'/>"
    s += f"<text x='335' y='{yb+30}' fill='#fbbf24' font-size='14' text-anchor='middle'>R = 150 &ohm;</text>"
    s += "</svg>"
    return s

# ---------------- FIGURAS DE SOLUCION ----------------

def fig_kmap3(vals, rot_note=''):
    """Mapa de Karnaugh generico de 3 variables (A filas, BC columnas)."""
    x0, y0, cw, ch = 130, 60, 60, 46
    cols = ['00', '01', '11', '10']
    s = ("<svg viewBox='0 0 440 200' width='100%' style='max-width:410px;height:auto' "
         "fill='none' font-family='Inter,system-ui,sans-serif'>")
    s += f"<text x='{x0-34}' y='{y0-14}' fill='#94a3b8' font-size='13'>{rot_note}</text>"
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
    return s, x0, y0, cw, ch

def fig_kmap_q3():
    vals = [[0, 0, 1, 0], [0, 1, 1, 1]]   # A filas; BC 00,01,11,10 ; m3,m5,m6,m7
    s, x0, y0, cw, ch = fig_kmap3(vals, 'A\\BC')
    # grupo AB (a=1,b=1 -> col 11 y 10 fila1): cols 11(idx2),10(idx3) fila i=1
    s += f"<rect x='{x0+cw*2-4}' y='{y0+ch-4}' width='{cw*2+8}' height='{ch+8}' rx='9' fill='none' stroke='#f59e0b' stroke-width='2.2'/>"
    # grupo AC (a=1,c=1 -> col 01,11 fila1)
    s += f"<rect x='{x0+cw-6}' y='{y0+ch-8}' width='{cw*2+12}' height='{ch+16}' rx='12' fill='none' stroke='#38bdf8' stroke-width='2.2'/>"
    # grupo BC (b=1,c=1 -> col 11 ambas filas)
    s += f"<rect x='{x0+cw*2-8}' y='{y0-6}' width='{cw+16}' height='{ch*2+12}' rx='11' fill='none' stroke='#a78bfa' stroke-width='2.2'/>"
    s += "</svg>"
    return s

def fig_kmap_q10():
    vals = [[0, 1, 0, 0], [1, 1, 0, 0]]   # a filas; bc 00,01,11,10 ; m1,m4,m5
    s, x0, y0, cw, ch = fig_kmap3(vals, 'a\\bc')
    # grupo a·b' (a=1,b=0 -> col 00,01 fila1)
    s += f"<rect x='{x0-5}' y='{y0+ch-4}' width='{cw*2+10}' height='{ch+8}' rx='10' fill='none' stroke='#f59e0b' stroke-width='2.2'/>"
    # grupo b'·c (b=0,c=1 -> col 01 ambas filas)
    s += f"<rect x='{x0+cw-6}' y='{y0-6}' width='{cw+12}' height='{ch*2+12}' rx='11' fill='none' stroke='#38bdf8' stroke-width='2.2'/>"
    s += "</svg>"
    return s

def fig_nand():
    """Q3 · implementacion con puertas NAND (mayoria)."""
    s = ("<svg viewBox='0 0 470 260' width='100%' style='max-width:440px;height:auto' "
         "fill='none' font-family='Inter,system-ui,sans-serif' stroke='#e2e8f0' stroke-width='1.8'>")
    def nand(x, y, w=44, h=44, col='#38bdf8'):
        r = ("<path d='M{x} {y} L{a} {y} A{rr} {rr} 0 0 1 {a} {yb} L{x} {yb} Z' fill='none' stroke='{c}' stroke-width='2'/>"
             "<circle cx='{cc}' cy='{cy}' r='4.5' fill='none' stroke='{c}' stroke-width='2'/>").format(
            x=x, y=y, a=x + w - h / 2, yb=y + h, rr=h / 2, c=col, cc=x + w - h / 2 + h / 2 + 5, cy=y + h / 2)
        return r
    # 3 NAND de 2 entradas (AB, AC, BC) + 1 NAND de 3 entradas
    s += nand(120, 20); s += nand(120, 95); s += nand(120, 170)
    s += "<text x='95' y='30' fill='#e2e8f0' font-size='13'>A</text><text x='95' y='52' fill='#e2e8f0' font-size='13'>B</text>"
    s += "<text x='95' y='105' fill='#e2e8f0' font-size='13'>A</text><text x='95' y='127' fill='#e2e8f0' font-size='13'>C</text>"
    s += "<text x='95' y='180' fill='#e2e8f0' font-size='13'>B</text><text x='95' y='202' fill='#e2e8f0' font-size='13'>C</text>"
    for yy in (30, 50, 105, 125, 180, 200):
        s += f"<line x1='108' y1='{yy}' x2='120' y2='{yy}'/>"
    # salidas de las 3 NAND (x~175) a la NAND final
    s += nand(320, 95, 50, 70, '#f59e0b')
    for (yout, yin) in ((42, 108), (117, 125), (192, 142)):
        s += f"<line x1='178' y1='{yout}' x2='250' y2='{yout}'/><line x1='250' y1='{yout}' x2='250' y2='{yin}'/><line x1='250' y1='{yin}' x2='320' y2='{yin}'/>"
    s += "<line x1='383' y1='130' x2='450' y2='130'/><text x='456' y='135' fill='#e2e8f0' font-size='15'>F</text>"
    s += "</svg>"
    return s

def fig_or_ac():
    """Q10 · circuito de S = b'(a+c)."""
    s = ("<svg viewBox='0 0 420 190' width='100%' style='max-width:400px;height:auto' "
         "fill='none' font-family='Inter,system-ui,sans-serif' stroke='#e2e8f0' stroke-width='2'>")
    # NOT b
    s += "<text x='16' y='128' fill='#e2e8f0' font-size='15'>b</text>"
    s += "<line x1='30' y1='123' x2='60' y2='123'/>"
    s += "<polygon points='60,108 60,138 88,123' fill='none' stroke='#a78bfa' stroke-width='2'/>"
    s += "<circle cx='93' cy='123' r='4.5' fill='none' stroke='#a78bfa' stroke-width='2'/>"
    # OR (a,c)
    s += "<text x='16' y='45' fill='#e2e8f0' font-size='15'>a</text><text x='16' y='80' fill='#e2e8f0' font-size='15'>c</text>"
    s += "<line x1='30' y1='40' x2='120' y2='40'/><line x1='30' y1='75' x2='120' y2='75'/>"
    s += "<path d='M112 24 Q150 24 190 57 Q150 90 112 90 Q132 57 112 24 Z' fill='none' stroke='#34d399' stroke-width='2.2'/>"
    s += "<line x1='190' y1='57' x2='240' y2='57'/>"
    # AND final
    s += "<line x1='98' y1='123' x2='240' y2='123'/>"
    s += "<line x1='240' y1='57' x2='240' y2='75'/><line x1='240' y1='123' x2='240' y2='105'/>"
    s += "<path d='M250 62 L282 62 A28 28 0 0 1 282 118 L250 118 Z' fill='none' stroke='#38bdf8' stroke-width='2.2'/>"
    s += "<line x1='240' y1='75' x2='250' y2='75'/><line x1='240' y1='105' x2='250' y2='105'/>"
    s += "<line x1='310' y1='90' x2='360' y2='90'/><text x='366' y='95' fill='#e2e8f0' font-size='15'>S</text>"
    s += "</svg>"
    return s

# ---------------- CONTENIDO ----------------

TV3 = ("<table class='dat'><tr><th>A</th><th>B</th><th>C</th><th>F</th></tr>"
       "<tr><td>0</td><td>0</td><td>0</td><td>0</td></tr>"
       "<tr><td>0</td><td>0</td><td>1</td><td>0</td></tr>"
       "<tr><td>0</td><td>1</td><td>0</td><td>0</td></tr>"
       "<tr style='background:rgba(74,222,128,.14)'><td>0</td><td>1</td><td>1</td><td>1</td></tr>"
       "<tr><td>1</td><td>0</td><td>0</td><td>0</td></tr>"
       "<tr style='background:rgba(74,222,128,.14)'><td>1</td><td>0</td><td>1</td><td>1</td></tr>"
       "<tr style='background:rgba(74,222,128,.14)'><td>1</td><td>1</td><td>0</td><td>1</td></tr>"
       "<tr style='background:rgba(74,222,128,.14)'><td>1</td><td>1</td><td>1</td><td>1</td></tr></table>")

data = {
 "meta": {
  "titulo": "Tecnología e Ingeniería II",
  "subtitulo": "Prueba de Acceso a la Universidad (EBAU) · Universidad de Extremadura · Curso 2023-2024 · Examen resuelto y comentado",
  "cabecera_titulo": "EBAU 2024 · <span>Tecnología e Ingeniería II</span> · Extremadura · Extraordinaria",
  "pill": "90 min · se eligen 5 de 10 · 2 pt/pregunta",
  "enunciado_pdf": "../../examens/Extremadura/Tecnologia_Extremadura_2024_extraordinaria.pdf",
  "pdf_dir": "pdf_ext_2024_extraordinaria",
  "footer": "Dpto. Tecnología · Solucionario EBAU 2024 · Extremadura · Tecnología e Ingeniería II (Extraordinaria)",
  "intro_inicio": "El examen consta de <b>10 preguntas</b> de 2 puntos; el estudiante debe responder <b>5</b>, elegidas libremente. Aquí se resuelven <b>todas</b> para repasar. Selecciona un bloque o una pregunta en la barra lateral. Cada una incluye el enunciado oficial, una introducción con los conceptos que se aplican y la solución paso a paso.",
  "indice_nombre": "Exámenes de Extremadura",
  "indice_url": "index.html"
 },
 "bloques": [
  {
   "id": "b1", "titulo": "Preguntas 1-3 · Neumática, materiales y lógica", "color": "#f59e0b",
   "descripcion_tarjeta": "Circuito neumático con válvula 3/2, dimensionado de una barra a tracción y control lógico de un motor.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#f59e0b' stroke-width='3'><rect x='12' y='22' width='40' height='18'/><path d='M52 31h22'/><path d='M20 22v-6M30 22v-6'/></svg>",
   "cuestiones": [
    {
     "id": "q1", "titulo": "Pregunta 1 · Circuito neumático (válvula 3/2)", "etiqueta": "NEUMÁTICA",
     "menu": "P1 · Circuito neumático", "titulo_corto": "P1",
     "meta": "Pregunta de 2 puntos (a: 0,75 · b: 0,75 · c: 0,5)",
     "enunciado_html": "<p>Para el circuito neumático representado en la figura, se pide:</p><ol type='a'><li>Identificar los componentes, indicando el significado de los números sobre los orificios del elemento 1.1. <span class='pts'>(0,75 puntos)</span></li><li>Explicar el funcionamiento. <span class='pts'>(0,75 puntos)</span></li><li>Dibujar el diagrama espacio-fase. <span class='pts'>(0,5 puntos)</span></li></ol>",
     "figura_enunciado_svg": "<figure class='fig'>" + fig_neumatico() + "<figcaption>Circuito neumático: cilindro simple efecto (1.0), regulador de caudal unidireccional (1.01), válvula 3/2 con pulsador y retorno por muelle (1.1) y grupo de acondicionamiento (0.1, 0.2).</figcaption></figure>",
     "aplica_html": "<p>Reconoceremos la simbología neumática normalizada (cilindro, válvula distribuidora, reguladora de caudal, unidad de mantenimiento) y el significado de la numeración de orificios de una válvula distribuidora según norma.</p>",
     "solucion_html": "<h5>a) Componentes y numeración</h5><ul><li><b>1.0</b> — Cilindro de <b>simple efecto</b> con retorno por muelle.</li><li><b>1.01</b> — <b>Regulador de caudal unidireccional</b> (estrangulador + antirretorno en paralelo): regula la velocidad de salida del vástago.</li><li><b>1.1</b> — <b>Válvula distribuidora 3/2</b> (3 vías, 2 posiciones), accionada por <b>pulsador</b> y retorno por <b>muelle</b>, normalmente cerrada.</li><li><b>0.2</b> — <b>Unidad de mantenimiento</b> (filtro + regulador con manómetro).</li><li><b>0.1</b> — <b>Válvula de corte</b> general.</li></ul><p>Significado de los orificios de la 1.1: <b>1</b> = alimentación (presión); <b>2</b> = utilización (salida al cilindro); <b>3</b> = escape (a la atmósfera).</p><h5>b) Funcionamiento</h5><p>En reposo, la 3/2 conecta <b>2&rarr;3</b> (el cilindro está sin presión y el muelle mantiene el vástago dentro). Al <b>pulsar</b> la válvula, se conecta <b>1&rarr;2</b>: el aire llega al cilindro y el vástago <b>avanza</b> (la velocidad la limita el regulador 1.01). Al <b>soltar</b> el pulsador, el muelle devuelve la válvula a reposo, el aire del cilindro escapa por <b>2&rarr;3</b> y el muelle del cilindro hace <b>retroceder</b> el vástago.</p><h5>c) Diagrama espacio-fase</h5><p>Con una sola fase de mando, el vástago describe un ciclo <b>avance&ndash;retroceso</b>:</p><figure class='fig'><svg viewBox='0 0 420 170' width='100%' style='max-width:400px;height:auto' fill='none' font-family='Inter,system-ui,sans-serif'><line x1='60' y1='30' x2='60' y2='130' stroke='#94a3b8' stroke-width='1.4'/><line x1='60' y1='130' x2='380' y2='130' stroke='#94a3b8' stroke-width='1.4'/><text x='30' y='42' fill='#cbd5e1' font-size='12'>1 (fuera)</text><text x='30' y='128' fill='#cbd5e1' font-size='12'>0 (dentro)</text><polyline points='60,130 140,40 240,40 320,130' fill='none' stroke='#38bdf8' stroke-width='2.4'/><text x='100' y='150' fill='#94a3b8' font-size='12'>pulsar</text><text x='185' y='150' fill='#94a3b8' font-size='12'>mantenido</text><text x='285' y='150' fill='#94a3b8' font-size='12'>soltar</text></svg><figcaption>Diagrama espacio-fase del cilindro 1.0.</figcaption></figure>"
    },
    {
     "id": "q2", "titulo": "Pregunta 2 · Dimensionado de una barra a tracción", "etiqueta": "MATERIALES",
     "menu": "P2 · Barra a tracción", "titulo_corto": "P2",
     "meta": "Pregunta de 2 puntos",
     "enunciado_html": "<p>Una barra cilíndrica de acero con límite elástico &sigma;<sub>E</sub> = 310 MPa va a ser sometida a una carga de 12500 N. Si la longitud inicial es 350 mm, ¿cuál debe ser el diámetro para que <b>no se alargue más de 0,50 mm</b>? <span class='pts'>(2 puntos)</span></p><p>Dato: \\(E=22\\cdot10^4\\,\\mathrm{MPa}\\).</p>",
     "figura_enunciado_svg": "",
     "aplica_html": "<p>Por la <b>ley de Hooke</b>, \\(\\Delta L=\\frac{F\\,L_0}{A\\,E}\\). Despejamos el área mínima para no superar el alargamiento admisible y obtenemos el diámetro. Conviene además <b>comprobar</b> que la tensión de trabajo no supere el límite elástico.</p>",
     "solucion_html": "<p>Datos: \\(F=12500\\,\\mathrm{N}\\), \\(L_0=350\\,\\mathrm{mm}\\), \\(\\Delta L_{max}=0{,}50\\,\\mathrm{mm}\\), \\(E=220000\\,\\mathrm{MPa}=220000\\,\\mathrm{N/mm^2}\\).</p><h5>Criterio de rigidez (alargamiento)</h5><div class='formula'>$$A\\ge\\frac{F\\,L_0}{\\Delta L\\,E}=\\frac{12500\\cdot 350}{0{,}50\\cdot 220000}=39{,}77\\,\\mathrm{mm^2}$$</div><div class='formula'>$$d=\\sqrt{\\frac{4A}{\\pi}}=\\sqrt{\\frac{4\\cdot 39{,}77}{\\pi}}=7{,}12\\,\\mathrm{mm}$$</div><h5>Comprobación de resistencia</h5><p>Con ese diámetro \\(\\sigma=\\frac{F}{A}=\\frac{12500}{39{,}77}=314\\,\\mathrm{MPa}>\\sigma_E\\). Debe ampliarse hasta cumplir también \\(A\\ge\\frac{F}{\\sigma_E}=\\frac{12500}{310}=40{,}32\\,\\mathrm{mm^2}\\Rightarrow d=7{,}16\\,\\mathrm{mm}\\).</p><div class='res'><b>d &ge; 7,2 mm</b> (rige la resistencia; el alargamiento exigía 7,12 mm)</div>"
    },
    {
     "id": "q3", "titulo": "Pregunta 3 · Control lógico de un motor (NAND)", "etiqueta": "ELECTRÓNICA DIGITAL",
     "menu": "P3 · Función mayoría (NAND)", "titulo_corto": "P3",
     "meta": "Pregunta de 2 puntos (a-d: 0,5 c/u)",
     "enunciado_html": "<p>Un motor se controla con tres pulsadores A, B y C; se activa <b>solo cuando se pulsan dos cualesquiera o los tres</b>. Se pide:</p><ol type='a'><li>Tabla de verdad. <span class='pts'>(0,5 puntos)</span></li><li>Función lógica en primera forma canónica. <span class='pts'>(0,5 puntos)</span></li><li>Expresión simplificada por Karnaugh. <span class='pts'>(0,5 puntos)</span></li><li>Implementación con el menor número de puertas NAND de dos y tres entradas. <span class='pts'>(0,5 puntos)</span></li></ol>",
     "figura_enunciado_svg": "",
     "aplica_html": "<p>Es la <b>función mayoría</b> de tres variables. La primera forma canónica es la suma de minterms; el mapa de Karnaugh la reduce, y por el teorema de De Morgan una suma de productos se implementa con puertas NAND.</p>",
     "solucion_html": "<h5>a) Tabla de verdad</h5>" + TV3 + "<h5>b) Primera forma canónica</h5><div class='formula'>$$F=\\bar A BC+A\\bar BC+AB\\bar C+ABC$$</div><h5>c) Simplificación por Karnaugh</h5><figure class='fig'>" + fig_kmap_q3() + "<figcaption>Grupos AB (naranja), AC (azul) y BC (violeta).</figcaption></figure><div class='formula'>$$F=AB+AC+BC$$</div><div class='res'><b>F = AB + AC + BC</b> (función mayoría)</div><h5>d) Implementación con puertas NAND</h5><p>Por De Morgan: \\(F=\\overline{\\overline{AB}\\cdot\\overline{AC}\\cdot\\overline{BC}}\\). Se necesitan <b>tres NAND de 2 entradas</b> y <b>una NAND de 3 entradas</b> (4 puertas):</p><figure class='fig'>" + fig_nand() + "<figcaption>Implementación con 3 NAND de 2 entradas y 1 NAND de 3 entradas.</figcaption></figure>"
    }
   ]
  },
  {
   "id": "b2", "titulo": "Preguntas 4-6 · Control, estructuras y motores", "color": "#22d3ee",
   "descripcion_tarjeta": "Reducción de un diagrama de bloques, viga con carga puntual y motor Otto de cuatro cilindros.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#22d3ee' stroke-width='3'><rect x='10' y='22' width='22' height='16'/><rect x='52' y='22' width='22' height='16'/><path d='M32 30h20'/></svg>",
   "cuestiones": [
    {
     "id": "q4", "titulo": "Pregunta 4 · Reducción de un sistema de control", "etiqueta": "CONTROL",
     "menu": "P4 · Sistema de control", "titulo_corto": "P4",
     "meta": "Pregunta de 2 puntos",
     "enunciado_html": "<p>Simplifica el siguiente sistema de control hasta conseguir la <b>función de transferencia</b> del sistema. <span class='pts'>(2 puntos)</span></p>",
     "figura_enunciado_svg": "<figure class='fig'>" + fig_bloques4() + "<figcaption>Diagrama de bloques: lazo interno de realimentación positiva de G<sub>2</sub> con H<sub>2</sub> y lazo externo unitario negativo tomado de la línea de entrada.</figcaption></figure>",
     "aplica_html": "<p>Se reduce por lazos. El lazo positivo de \\(G_2\\) con \\(H_2\\) equivale a \\(\\frac{G_2}{1-G_2H_2}\\). Los bloques en serie se multiplican; el comparador final resta la señal realimentada.</p>",
     "solucion_html": "<h5>Lazo interno (H<sub>2</sub>, realimentación positiva sobre G<sub>2</sub>)</h5><div class='formula'>$$G_2'=\\frac{G_2}{1-G_2H_2}$$</div><h5>Camino directo hasta el segundo comparador</h5><p>La señal que llega al segundo comparador por la rama superior es \\(G_1G_2'\\,E\\); por la rama inferior se resta la propia entrada \\(E\\) (realimentación unitaria). Tras \\(G_3\\):</p><div class='formula'>$$C=G_3\\left(G_1G_2'-1\\right)E$$</div><div class='formula'>$$\\boxed{\\dfrac{C(s)}{E(s)}=G_3\\left(\\dfrac{G_1G_2}{1-G_2H_2}-1\\right)=\\dfrac{G_3\\,(G_1G_2-1+G_2H_2)}{1-G_2H_2}}$$</div><div class='res'><b>C/E = G<sub>3</sub>(G<sub>1</sub>G<sub>2</sub> − 1 + G<sub>2</sub>H<sub>2</sub>) / (1 − G<sub>2</sub>H<sub>2</sub>)</b></div>"
    },
    {
     "id": "q5", "titulo": "Pregunta 5 · Viga con carga puntual central", "etiqueta": "ESTRUCTURAS",
     "menu": "P5 · Viga (carga puntual)", "titulo_corto": "P5",
     "meta": "Pregunta de 2 puntos",
     "enunciado_html": "<p>Dada la viga simplemente apoyada sometida a una carga aislada de 3000 N, calcula las <b>reacciones</b>, escribe las ecuaciones del <b>esfuerzo cortante</b> y del <b>momento flector</b> en cualquier punto y traza los diagramas. <span class='pts'>(2 puntos)</span></p>",
     "figura_enunciado_svg": "<figure class='fig'>" + fig_viga5() + "<figcaption>Viga biapoyada de 4 m con carga puntual P = 3000 N en el centro.</figcaption></figure>",
     "aplica_html": "<p>Con la carga en el centro la viga es simétrica: \\(R_A=R_B=P/2\\). El cortante es constante a tramos y el momento flector es máximo bajo la carga.</p>",
     "solucion_html": "<h5>Reacciones</h5><p>Por simetría (carga centrada, luz 4 m):</p><div class='formula'>$$R_A=R_B=\\frac{P}{2}=\\frac{3000}{2}=1500\\,\\mathrm{N}$$</div><div class='res'><b>R<sub>A</sub> = R<sub>B</sub> = 1500 N</b></div><h5>Ecuaciones (origen en A)</h5><p>Tramo AC \\((0\\le x\\le 2)\\): \\(V=+1500\\,\\mathrm{N}\\), \\(M=1500\\,x\\).</p><p>Tramo CB \\((2\\le x\\le 4)\\): \\(V=-1500\\,\\mathrm{N}\\), \\(M=1500\\,x-3000(x-2)=-1500\\,x+6000\\).</p><h5>Valores máximos</h5><div class='formula'>$$V_{max}=1500\\,\\mathrm{N}\\qquad M_{max}=1500\\cdot 2=3000\\,\\mathrm{N\\cdot m}$$</div><div class='res'><b>V<sub>máx</sub> = 1500 N &nbsp;·&nbsp; M<sub>máx</sub> = 3000 N&middot;m (en el centro)</b></div><figure class='fig'><svg viewBox='0 0 560 300' width='100%' style='max-width:520px;height:auto' fill='none' font-family='Inter,system-ui,sans-serif'><line x1='60' y1='70' x2='500' y2='70' stroke='#94a3b8' stroke-width='1.4'/><text x='58' y='24' fill='#e2e8f0' font-size='13'>V (N)</text><polygon points='60,70 60,40 280,40 280,100 500,100 500,70' fill='rgba(56,189,248,.16)' stroke='none'/><polyline points='60,40 280,40 280,100 500,100' fill='none' stroke='#38bdf8' stroke-width='2.4'/><line x1='60' y1='70' x2='60' y2='40' stroke='#38bdf8' stroke-width='2.4'/><line x1='500' y1='100' x2='500' y2='70' stroke='#38bdf8' stroke-width='2.4'/><text x='72' y='34' fill='#7dd3fc' font-size='12'>+1500</text><text x='488' y='114' fill='#7dd3fc' font-size='12' text-anchor='end'>-1500</text><line x1='60' y1='250' x2='500' y2='250' stroke='#94a3b8' stroke-width='1.4'/><text x='58' y='170' fill='#e2e8f0' font-size='13'>M (N·m)</text><polygon points='60,250 280,180 500,250' fill='rgba(74,222,128,.18)' stroke='none'/><polyline points='60,250 280,180 500,250' fill='none' stroke='#4ade80' stroke-width='2.4'/><text x='280' y='172' fill='#86efac' font-size='12' text-anchor='middle'>3000</text><text x='60' y='268' fill='#94a3b8' font-size='12' text-anchor='middle'>A</text><text x='280' y='268' fill='#94a3b8' font-size='12' text-anchor='middle'>C</text><text x='500' y='268' fill='#94a3b8' font-size='12' text-anchor='middle'>B</text></svg><figcaption>Diagramas de esfuerzo cortante y momento flector.</figcaption></figure>"
    },
    {
     "id": "q6", "titulo": "Pregunta 6 · Motor Otto de cuatro cilindros", "etiqueta": "MOTORES",
     "menu": "P6 · Motor Otto", "titulo_corto": "P6",
     "meta": "Pregunta de 2 puntos (a-d: 0,5 c/u)",
     "enunciado_html": "<p>Un motor <b>Otto</b> de 4 cilindros desarrolla 65 CV a 3500 rpm. El diámetro de cada pistón es 72 mm, la carrera 94 mm y \\(R_c=9/1\\). Determina:</p><ol type='a'><li>Cilindrada del motor. <span class='pts'>(0,5 puntos)</span></li><li>Volumen de la cámara de combustión. <span class='pts'>(0,5 puntos)</span></li><li>Rendimiento térmico (tomar &alpha; = 1,33). <span class='pts'>(0,5 puntos)</span></li><li>Par motor. <span class='pts'>(0,5 puntos)</span></li></ol>",
     "figura_enunciado_svg": "",
     "aplica_html": "<p>Cilindrada \\(V_T=n\\frac{\\pi D^2}{4}S\\); cámara \\(V_c=\\frac{V_u}{R_c-1}\\). El rendimiento del ciclo Otto es \\(\\eta=1-\\frac{1}{R_c^{\\,\\alpha-1}}\\) y el par \\(M=\\frac{P}{\\omega}\\).</p>",
     "solucion_html": "<p>Datos: \\(n=4\\), \\(D=7{,}2\\,\\mathrm{cm}\\), \\(S=9{,}4\\,\\mathrm{cm}\\), \\(R_c=9\\), \\(\\alpha=1{,}33\\), \\(N=3500\\,\\mathrm{rpm}\\), \\(P_e=65\\,\\mathrm{CV}\\).</p><h5>a) Cilindrada</h5><div class='formula'>$$V_u=\\frac{\\pi\\cdot 7{,}2^2}{4}\\cdot 9{,}4=382{,}7\\,\\mathrm{cm^3}\\;\\Rightarrow\\; V_T=4\\cdot 382{,}7=1531\\,\\mathrm{cm^3}$$</div><div class='res'><b>V<sub>T</sub> &asymp; 1531 cm³ (1,53 L)</b></div><h5>b) Volumen de la cámara</h5><div class='formula'>$$V_c=\\frac{V_u}{R_c-1}=\\frac{382{,}7}{8}=47{,}8\\,\\mathrm{cm^3}$$</div><div class='res'><b>V<sub>c</sub> &asymp; 47,8 cm³</b></div><h5>c) Rendimiento térmico</h5><div class='formula'>$$\\eta=1-\\frac{1}{R_c^{\\,\\alpha-1}}=1-\\frac{1}{9^{0{,}33}}=1-\\frac{1}{2{,}065}=0{,}516$$</div><div class='res'><b>&eta; &asymp; 51,6 %</b></div><h5>d) Par motor</h5><p>\\(P_e=65\\,\\mathrm{CV}=47\\,808\\,\\mathrm{W}\\); \\(\\omega=3500\\cdot\\frac{2\\pi}{60}=366{,}5\\,\\mathrm{rad/s}\\).</p><div class='formula'>$$M=\\frac{P_e}{\\omega}=\\frac{47\\,808}{366{,}5}=130{,}4\\,\\mathrm{N\\cdot m}$$</div><div class='res'><b>M &asymp; 130,4 N&middot;m</b></div>"
    }
   ]
  },
  {
   "id": "b3", "titulo": "Preguntas 7-8 · Máquinas térmicas y corriente alterna", "color": "#a78bfa",
   "descripcion_tarjeta": "Máquina frigorífica con eficiencia real y circuito RC serie en corriente alterna.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#a78bfa' stroke-width='3'><rect x='20' y='12' width='50' height='36'/><path d='M30 12v36M30 24h40M30 36h40'/></svg>",
   "cuestiones": [
    {
     "id": "q7", "titulo": "Pregunta 7 · Máquina frigorífica (eficiencia real)", "etiqueta": "TERMODINÁMICA",
     "menu": "P7 · Máquina frigorífica", "titulo_corto": "P7",
     "meta": "Pregunta de 2 puntos (a: 0,75 · b: 0,75 · c: 0,5)",
     "enunciado_html": "<p>Una máquina frigorífica absorbe 15000 J/min del foco frío, que está a &minus;23 &deg;C. El foco caliente está a 27 &deg;C. Calcula:</p><ol type='a'><li>El calor cedido al foco caliente, sabiendo que su eficiencia es la <b>mitad</b> de la del ciclo de Carnot. <span class='pts'>(0,75 puntos)</span></li><li>La potencia del motor necesaria. <span class='pts'>(0,75 puntos)</span></li><li>La eficiencia si la máquina actuara como <b>bomba de calor</b>. <span class='pts'>(0,5 puntos)</span></li></ol>",
     "figura_enunciado_svg": "",
     "aplica_html": "<p>COP de Carnot (refrigeración): \\(\\mathrm{COP}_C=\\frac{T_f}{T_c-T_f}\\). El real es la mitad. Con \\(\\mathrm{COP}=\\frac{Q_f}{W}\\) se obtiene el trabajo y \\(Q_c=Q_f+W\\). Como bomba de calor, \\(\\mathrm{COP}_{BC}=\\mathrm{COP}_R+1\\).</p>",
     "solucion_html": "<p>Datos: \\(\\dot Q_f=15000\\,\\mathrm{J/min}\\), \\(T_f=250\\,\\mathrm{K}\\), \\(T_c=300\\,\\mathrm{K}\\).</p><h5>a) Calor cedido al foco caliente</h5><div class='formula'>$$\\mathrm{COP}_C=\\frac{T_f}{T_c-T_f}=\\frac{250}{50}=5\\;\\Rightarrow\\;\\mathrm{COP}=\\frac{5}{2}=2{,}5$$</div><div class='formula'>$$\\dot W=\\frac{\\dot Q_f}{\\mathrm{COP}}=\\frac{15000}{2{,}5}=6000\\,\\mathrm{J/min}$$</div><div class='formula'>$$\\dot Q_c=\\dot Q_f+\\dot W=15000+6000=21000\\,\\mathrm{J/min}$$</div><div class='res'><b>Q<sub>c</sub> = 21000 J/min = 350 W</b></div><h5>b) Potencia del motor</h5><div class='formula'>$$P=\\dot W=6000\\,\\mathrm{J/min}=\\frac{6000}{60}=100\\,\\mathrm{W}$$</div><div class='res'><b>P = 100 W</b></div><h5>c) Eficiencia como bomba de calor</h5><div class='formula'>$$\\mathrm{COP}_{BC}=\\mathrm{COP}_R+1=2{,}5+1=3{,}5$$</div><div class='res'><b>COP<sub>bomba</sub> = 3,5</b></div>"
    },
    {
     "id": "q8", "titulo": "Pregunta 8 · Circuito RC serie en corriente alterna", "etiqueta": "CORRIENTE ALTERNA",
     "menu": "P8 · Circuito RC serie", "titulo_corto": "P8",
     "meta": "Pregunta de 2 puntos (a-d: 0,5 c/u)",
     "enunciado_html": "<p>En el circuito de la figura (220 V / 50 Hz, C = 120 &micro;F y R = 150 &ohm; en serie), determina:</p><ol type='a'><li>La intensidad que circula. <span class='pts'>(0,5 puntos)</span></li><li>La caída de tensión en cada elemento. <span class='pts'>(0,5 puntos)</span></li><li>El factor de potencia. <span class='pts'>(0,5 puntos)</span></li><li>Las potencias activa, reactiva y aparente. <span class='pts'>(0,5 puntos)</span></li></ol>",
     "figura_enunciado_svg": "<figure class='fig'>" + fig_rc() + "<figcaption>Circuito RC serie: C = 120 &micro;F y R = 150 &ohm; a 220 V / 50 Hz.</figcaption></figure>",
     "aplica_html": "<p>Reactancia capacitiva \\(X_C=\\frac{1}{2\\pi f C}\\); impedancia \\(Z=\\sqrt{R^2+X_C^2}\\); intensidad \\(I=\\frac{V}{Z}\\); factor de potencia \\(\\cos\\varphi=\\frac{R}{Z}\\). Potencias: \\(S=VI\\), \\(P=I^2R\\), \\(Q=I^2X_C\\).</p>",
     "solucion_html": "<p>Datos: \\(V=220\\,\\mathrm{V}\\), \\(f=50\\,\\mathrm{Hz}\\), \\(C=120\\,\\mu\\mathrm{F}\\), \\(R=150\\,\\Omega\\).</p><h5>a) Intensidad</h5><div class='formula'>$$X_C=\\frac{1}{2\\pi f C}=\\frac{1}{2\\pi\\cdot 50\\cdot 120\\cdot10^{-6}}=26{,}53\\,\\Omega$$</div><div class='formula'>$$Z=\\sqrt{150^2+26{,}53^2}=152{,}3\\,\\Omega\\;\\Rightarrow\\; I=\\frac{220}{152{,}3}=1{,}44\\,\\mathrm{A}$$</div><div class='res'><b>I &asymp; 1,44 A</b></div><h5>b) Caídas de tensión</h5><div class='formula'>$$V_R=I\\,R=1{,}44\\cdot 150=216{,}6\\,\\mathrm{V}\\qquad V_C=I\\,X_C=1{,}44\\cdot 26{,}53=38{,}3\\,\\mathrm{V}$$</div><div class='res'><b>V<sub>R</sub> &asymp; 216,6 V &nbsp;·&nbsp; V<sub>C</sub> &asymp; 38,3 V</b></div><h5>c) Factor de potencia</h5><div class='formula'>$$\\cos\\varphi=\\frac{R}{Z}=\\frac{150}{152{,}3}=0{,}985\\;(\\varphi=10^\\circ,\\text{ capacitivo})$$</div><div class='res'><b>cos&phi; &asymp; 0,985 (capacitivo)</b></div><h5>d) Potencias</h5><div class='formula'>$$S=VI=220\\cdot 1{,}44=317{,}7\\,\\mathrm{VA}$$</div><div class='formula'>$$P=I^2R=1{,}44^2\\cdot 150=312{,}9\\,\\mathrm{W}\\qquad Q=I^2X_C=1{,}44^2\\cdot 26{,}53=55{,}3\\,\\mathrm{VAr}$$</div><div class='res'><b>S &asymp; 318 VA &nbsp;·&nbsp; P &asymp; 313 W &nbsp;·&nbsp; Q &asymp; 55 VAr</b></div>"
    }
   ]
  },
  {
   "id": "b4", "titulo": "Preguntas 9-10 · Neumática y electrónica digital", "color": "#34d399",
   "descripcion_tarjeta": "Cilindro de doble efecto (fuerzas y consumo de aire) y simplificación de una función lógica.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#34d399' stroke-width='3'><rect x='12' y='20' width='42' height='20'/><path d='M54 30h24'/><path d='M20 20v20'/></svg>",
   "cuestiones": [
    {
     "id": "q9", "titulo": "Pregunta 9 · Cilindro de doble efecto (consumo de aire)", "etiqueta": "NEUMÁTICA",
     "menu": "P9 · Cilindro doble efecto", "titulo_corto": "P9",
     "meta": "Pregunta de 2 puntos (a-d: 0,5 c/u)",
     "enunciado_html": "<p>Un cilindro de doble efecto tiene émbolo de 70 mm de diámetro, vástago de 25 mm, carrera 400 mm y presión de trabajo 6 kp/cm². Determina:</p><ol type='a'><li>Fuerza teórica en el avance. <span class='pts'>(0,5 puntos)</span></li><li>Fuerza teórica en el retroceso. <span class='pts'>(0,5 puntos)</span></li><li>Consumo de aire en avance y retroceso referido a condiciones normales (en litros). <span class='pts'>(0,5 puntos)</span></li><li>Volumen total de aire (en litros). <span class='pts'>(0,5 puntos)</span></li></ol>",
     "figura_enunciado_svg": "",
     "aplica_html": "<p>Avance: \\(F=p\\,\\frac{\\pi D^2}{4}\\). Retroceso: \\(F=p\\,\\frac{\\pi (D^2-d^2)}{4}\\). El consumo en condiciones normales multiplica el volumen geométrico por la <b>relación de compresión</b> \\(n=\\frac{p_{abs}}{p_{atm}}\\).</p>",
     "solucion_html": "<p>Datos: \\(D=7\\,\\mathrm{cm}\\), \\(d=2{,}5\\,\\mathrm{cm}\\), carrera \\(=40\\,\\mathrm{cm}\\), \\(p=6\\,\\mathrm{kp/cm^2}\\).</p><h5>a) Fuerza de avance</h5><div class='formula'>$$A_{emb}=\\frac{\\pi\\cdot 7^2}{4}=38{,}48\\,\\mathrm{cm^2}\\;\\Rightarrow\\; F_{av}=6\\cdot 38{,}48=230{,}9\\,\\mathrm{kp}$$</div><div class='res'><b>F<sub>avance</sub> &asymp; 231 kp (&asymp; 2265 N)</b></div><h5>b) Fuerza de retroceso</h5><div class='formula'>$$A_{ret}=\\frac{\\pi(7^2-2{,}5^2)}{4}=33{,}57\\,\\mathrm{cm^2}\\;\\Rightarrow\\; F_{ret}=6\\cdot 33{,}57=201{,}4\\,\\mathrm{kp}$$</div><div class='res'><b>F<sub>retroceso</sub> &asymp; 201 kp (&asymp; 1976 N)</b></div><h5>c) Consumo de aire (condiciones normales)</h5><p>Volúmenes geométricos: \\(V_{av}=38{,}48\\cdot 40=1539\\,\\mathrm{cm^3}=1{,}54\\,\\mathrm{L}\\); \\(V_{ret}=33{,}57\\cdot 40=1343\\,\\mathrm{cm^3}=1{,}34\\,\\mathrm{L}\\).</p><p>Relación de compresión (tomando \\(p_{atm}\\approx1\\,\\mathrm{kp/cm^2}\\)): \\(n=\\frac{6+1}{1}=7\\).</p><div class='formula'>$$V_{normal}=n\\,(V_{av}+V_{ret})=7\\cdot(1{,}54+1{,}34)=20{,}2\\,\\mathrm{L}$$</div><div class='res'><b>Consumo &asymp; 20,2 L (normales) por ciclo</b></div><h5>d) Volumen total (a presión de trabajo)</h5><div class='formula'>$$V_{total}=V_{av}+V_{ret}=1{,}54+1{,}34=2{,}88\\,\\mathrm{L}$$</div><div class='res'><b>V<sub>total</sub> &asymp; 2,88 L</b></div>"
    },
    {
     "id": "q10", "titulo": "Pregunta 10 · Simplificación por Karnaugh", "etiqueta": "ELECTRÓNICA DIGITAL",
     "menu": "P10 · Karnaugh", "titulo_corto": "P10",
     "meta": "Pregunta de 2 puntos (a: 1,0 · b: 1,0)",
     "enunciado_html": "<p>Sea la función lógica \\(S=\\bar a\\bar b c+a\\bar b\\bar c+a\\bar b c\\).</p><ol type='a'><li>Simplificar por Karnaugh. <span class='pts'>(1 punto)</span></li><li>Dibujar el circuito lógico de la función simplificada. <span class='pts'>(1 punto)</span></li></ol>",
     "figura_enunciado_svg": "",
     "aplica_html": "<p>Colocamos los tres minterms en un mapa de Karnaugh de tres variables y agrupamos los unos adyacentes para obtener la mínima suma de productos.</p>",
     "solucion_html": "<h5>a) Simplificación</h5><p>Los minterms son \\(\\bar a\\bar b c\\,(m_1)\\), \\(a\\bar b\\bar c\\,(m_4)\\) y \\(a\\bar b c\\,(m_5)\\):</p><figure class='fig'>" + fig_kmap_q10() + "<figcaption>Grupos a&middot;b&#773; (naranja) y b&#773;&middot;c (azul).</figcaption></figure><div class='formula'>$$S=a\\bar b+\\bar b c=\\bar b\\,(a+c)$$</div><div class='res'><b>S = b&#773;·(a + c)</b></div><h5>b) Circuito lógico</h5><p>Un inversor para \\(\\bar b\\), una OR \\((a+c)\\) y una AND final:</p><figure class='fig'>" + fig_or_ac() + "<figcaption>Implementación de S = b&#773;(a + c).</figcaption></figure>"
    }
   ]
  }
 ]
}

out = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ext_2024_extraordinaria.json"))
with open(out, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print("JSON escrito:", out)
