#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera el JSON del examen Extremadura EBAU 2024 (ordinaria) para pau-dashboard."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import svg_open, box, summer, arrow, line, txt

# ---------------- FIGURAS DEL ENUNCIADO ----------------

def fig_bloques():
    """Q6 · diagrama de bloques del sistema de control."""
    s = svg_open('900 330', 800)
    ym = 90
    # nodos principales
    s += arrow(55, ym, 95, ym)                 # R -> S1
    s += summer(110, ym)
    s += arrow(126, ym, 189, ym)               # S1 -> S2
    s += summer(205, ym)
    s += arrow(221, ym, 265, ym)               # S2 -> G1
    s += box(265, 68, 80, 44, 'G<tspan dy="4" font-size="11">1</tspan>', '#22d3ee')
    s += arrow(345, ym, 470, ym)               # G1 -> S3 (pasa por N1)
    s += summer(485, ym)
    s += arrow(501, ym, 545, ym)               # S3 -> G2
    s += box(545, 68, 80, 44, 'G<tspan dy="4" font-size="11">2</tspan>', '#22d3ee')
    s += arrow(625, ym, 800, ym)               # G2 -> salida
    # nodos
    for nx in (405, 700, 760):
        s += f"<circle cx='{nx}' cy='{ym}' r='3.2' fill='#cbd5e1' stroke='none'/>"
    # etiquetas
    s += txt(28, ym + 5, 'R(s)', '#e2e8f0', 15)
    s += txt(812, ym + 5, 'G(s)', '#e2e8f0', 15)
    # signos sumadores
    s += txt(92, 80, '+', '#4ade80', 15); s += txt(96, 122, '−', '#fb7185', 18)
    s += txt(186, 80, '+', '#4ade80', 15); s += txt(214, 124, '+', '#4ade80', 15)
    s += txt(466, 80, '+', '#4ade80', 15); s += txt(494, 124, '+', '#4ade80', 15)
    # --- H1: realimentacion positiva a S2 (desde N1) ---
    s += box(265, 175, 80, 40, 'H<tspan dy="4" font-size="11">1</tspan>', '#a78bfa')
    s += line(405, ym, 405, 195); s += line(405, 195, 345, 195)
    s += line(265, 195, 205, 195); s += arrow(205, 195, 205, 107)
    # --- H2: realimentacion positiva a S3 (desde N2) ---
    s += box(545, 175, 80, 40, 'H<tspan dy="4" font-size="11">2</tspan>', '#a78bfa')
    s += line(700, ym, 700, 195); s += line(700, 195, 625, 195)
    s += line(545, 195, 485, 195); s += arrow(485, 195, 485, 107)
    # --- H3: realimentacion negativa a S1 (desde la salida) ---
    s += box(410, 258, 92, 40, 'H<tspan dy="4" font-size="11">3</tspan>', '#fb7185')
    s += line(760, ym, 760, 278); s += line(760, 278, 502, 278)
    s += line(410, 278, 110, 278); s += arrow(110, 278, 110, 107)
    s += "</svg>"
    return s

def fig_viga():
    """Q7 · viga con carga distribuida en la mitad izquierda."""
    x0, x1, xm = 95, 585, 340          # A, B, fin de la carga (3 m)
    yb = 165                            # cara superior de la viga
    s = ("<svg viewBox='0 0 660 300' width='100%' style='max-width:560px;height:auto' "
         "fill='none' font-family='Inter,system-ui,sans-serif'>")
    s += f"<text x='{(x0+xm)//2}' y='40' fill='#e2e8f0' font-size='16' text-anchor='middle'>Q = 2500 kg/m</text>"
    s += f"<line x1='{x0}' y1='52' x2='{xm}' y2='52' stroke='#f59e0b' stroke-width='2'/>"
    n = 8
    for i in range(n + 1):
        xa = x0 + (xm - x0) * i / n
        s += f"<line x1='{xa:.0f}' y1='52' x2='{xa:.0f}' y2='{yb-2}' stroke='#f59e0b' stroke-width='1.6'/>"
        s += f"<polygon points='{xa-4:.0f},{yb-10} {xa+4:.0f},{yb-10} {xa:.0f},{yb-1}' fill='#f59e0b'/>"
    # viga
    s += f"<rect x='{x0}' y='{yb}' width='{x1-x0}' height='15' rx='2' fill='#1e293b' stroke='#e2e8f0' stroke-width='2'/>"
    # apoyo fijo A (triangulo)
    s += f"<polygon points='{x0},{yb+15} {x0-13},{yb+42} {x0+13},{yb+42}' fill='none' stroke='#38bdf8' stroke-width='2'/>"
    for i in range(4):
        hx = x0 - 13 + i * 8.7
        s += f"<line x1='{hx:.0f}' y1='{yb+42}' x2='{hx-8:.0f}' y2='{yb+52}' stroke='#94a3b8' stroke-width='1.4'/>"
    s += f"<text x='{x0}' y='{yb+40}' fill='#7dd3fc' font-size='15' font-weight='700' text-anchor='middle'>A</text>"
    # apoyo movil B (triangulo + rodillos)
    s += f"<polygon points='{x1},{yb+15} {x1-13},{yb+38} {x1+13},{yb+38}' fill='none' stroke='#38bdf8' stroke-width='2'/>"
    s += f"<circle cx='{x1-7}' cy='{yb+44}' r='5' fill='none' stroke='#38bdf8' stroke-width='1.8'/>"
    s += f"<circle cx='{x1+7}' cy='{yb+44}' r='5' fill='none' stroke='#38bdf8' stroke-width='1.8'/>"
    s += f"<line x1='{x1-15}' y1='{yb+50}' x2='{x1+15}' y2='{yb+50}' stroke='#94a3b8' stroke-width='1.6'/>"
    s += f"<text x='{x1}' y='{yb+40}' fill='#7dd3fc' font-size='15' font-weight='700' text-anchor='middle'>B</text>"
    # cotas
    yc = yb + 78
    for (xa, xbb, lab) in ((x0, xm, '3 m'), (xm, x1, '3 m')):
        s += f"<line x1='{xa}' y1='{yc}' x2='{xbb}' y2='{yc}' stroke='#94a3b8' stroke-width='1.4'/>"
        s += f"<polygon points='{xa},{yc} {xa+11},{yc-5} {xa+11},{yc+5}' fill='#94a3b8'/>"
        s += f"<polygon points='{xbb},{yc} {xbb-11},{yc-5} {xbb-11},{yc+5}' fill='#94a3b8'/>"
        s += f"<line x1='{xa}' y1='{yc-7}' x2='{xa}' y2='{yc+7}' stroke='#94a3b8' stroke-width='1.2'/>"
        s += f"<line x1='{xbb}' y1='{yc-7}' x2='{xbb}' y2='{yc+7}' stroke='#94a3b8' stroke-width='1.2'/>"
        s += f"<text x='{(xa+xbb)//2}' y='{yc-9}' fill='#cbd5e1' font-size='14' text-anchor='middle'>{lab}</text>"
    s += "</svg>"
    return s

def fig_barra():
    """Q9 · pieza cilindrica sometida a traccion."""
    xa, xb = 190, 440
    yc = 118
    s = ("<svg viewBox='0 0 620 220' width='100%' style='max-width:520px;height:auto' "
         "fill='none' font-family='Inter,system-ui,sans-serif'>")
    # barra
    s += f"<rect x='{xa}' y='{yc-30}' width='{xb-xa}' height='60' fill='#1e293b' stroke='#e2e8f0' stroke-width='2'/>"
    # fuerzas F (hacia afuera)
    s += f"<line x1='{xa-20}' y1='{yc}' x2='60' y2='{yc}' stroke='#fb7185' stroke-width='2.4' marker-end='url(#arF)'/>"
    s += f"<line x1='{xb+20}' y1='{yc}' x2='560' y2='{yc}' stroke='#fb7185' stroke-width='2.4' marker-end='url(#arF)'/>"
    s += ("<defs><marker id='arF' markerWidth='11' markerHeight='10' refX='8' refY='4' orient='auto'>"
          "<path d='M0,0 L9,4 L0,8 Z' fill='#fb7185'/></marker></defs>")
    s += f"<text x='95' y='{yc-12}' fill='#fda4af' font-size='16' font-weight='700'>F</text>"
    s += f"<text x='510' y='{yc-12}' fill='#fda4af' font-size='16' font-weight='700'>F</text>"
    # cota diametro
    s += f"<line x1='390' y1='{yc-30}' x2='390' y2='{yc+30}' stroke='#94a3b8' stroke-width='1.3'/>"
    s += f"<polygon points='390,{yc-30} 385,{yc-19} 395,{yc-19}' fill='#94a3b8'/>"
    s += f"<polygon points='390,{yc+30} 385,{yc+19} 395,{yc+19}' fill='#94a3b8'/>"
    s += f"<text x='405' y='{yc+5}' fill='#cbd5e1' font-size='14'>&#248; = 30</text>"
    # cota longitud
    yl = yc + 58
    s += f"<line x1='{xa}' y1='{yl}' x2='{xb}' y2='{yl}' stroke='#94a3b8' stroke-width='1.3'/>"
    s += f"<polygon points='{xa},{yl} {xa+11},{yl-5} {xa+11},{yl+5}' fill='#94a3b8'/>"
    s += f"<polygon points='{xb},{yl} {xb-11},{yl-5} {xb-11},{yl+5}' fill='#94a3b8'/>"
    s += f"<line x1='{xa}' y1='{yc+30}' x2='{xa}' y2='{yl+6}' stroke='#94a3b8' stroke-width='1'/>"
    s += f"<line x1='{xb}' y1='{yc+30}' x2='{xb}' y2='{yl+6}' stroke='#94a3b8' stroke-width='1'/>"
    s += f"<text x='{(xa+xb)//2}' y='{yl-9}' fill='#cbd5e1' font-size='14' text-anchor='middle'>Lo = 50</text>"
    s += f"<text x='310' y='210' fill='#94a3b8' font-size='12' text-anchor='middle'>Medidas en mm</text>"
    s += "</svg>"
    return s

def fig_rl():
    """Q10 · circuito RL serie con generador de alterna."""
    xl, xr, yt, yb = 70, 450, 80, 200
    s = ("<svg viewBox='0 0 520 250' width='100%' style='max-width:460px;height:auto' "
         "fill='none' font-family='Inter,system-ui,sans-serif' stroke='#e2e8f0' stroke-width='2.2'>")
    # marco
    s += f"<line x1='{xl}' y1='{yt}' x2='238' y2='{yt}'/><line x1='282' y1='{yt}' x2='{xr}' y2='{yt}'/>"
    s += f"<line x1='{xl}' y1='{yt}' x2='{xl}' y2='{yb}'/><line x1='{xr}' y1='{yt}' x2='{xr}' y2='{yb}'/>"
    s += f"<line x1='{xl}' y1='{yb}' x2='130' y2='{yb}'/><line x1='250' y1='{yb}' x2='330' y2='{yb}'/><line x1='420' y1='{yb}' x2='{xr}' y2='{yb}'/>"
    # generador
    s += f"<circle cx='260' cy='{yt}' r='22' fill='none' stroke='#a78bfa' stroke-width='2.2'/>"
    s += f"<path d='M246 {yt} q7 -12 14 0 t14 0' fill='none' stroke='#a78bfa' stroke-width='2'/>"
    s += f"<text x='260' y='34' fill='#c4b5fd' font-size='15' font-weight='700' text-anchor='middle'>125 V / 50 Hz</text>"
    # resistencia (zig-zag) entre 130 y 250
    s += ("<polyline points='130,200 138,192 154,208 170,192 186,208 202,192 218,208 234,192 242,200 250,200' "
          "fill='none' stroke='#38bdf8' stroke-width='2.2'/>")
    s += f"<text x='190' y='236' fill='#7dd3fc' font-size='14' text-anchor='middle'>R = 20 &#8486;</text>"
    # bobina entre 330 y 420
    s += ("<path d='M330 200 q8 -14 16 0 q8 -14 16 0 q8 -14 16 0 q8 -14 16 0 l6 0' "
          "fill='none' stroke='#f59e0b' stroke-width='2.2'/>")
    s += f"<text x='378' y='236' fill='#fbbf24' font-size='14' text-anchor='middle'>L = 50 mH</text>"
    s += "</svg>"
    return s

# ---------------- FIGURAS DE LA SOLUCION ----------------

def fig_kmap():
    """Q5 · mapa de Karnaugh de F(A,B,C)."""
    x0, y0, cw, ch = 120, 60, 60, 48
    cols = ['00', '01', '11', '10']
    vals = [[0, 0, 1, 1], [1, 1, 1, 1]]     # filas A=0, A=1
    s = ("<svg viewBox='0 0 420 220' width='100%' style='max-width:400px;height:auto' "
         "fill='none' font-family='Inter,system-ui,sans-serif'>")
    s += f"<text x='{x0-30}' y='{y0-14}' fill='#94a3b8' font-size='13'>A\\BC</text>"
    for j, c in enumerate(cols):
        s += f"<text x='{x0+cw*j+cw/2:.0f}' y='{y0-14}' fill='#7dd3fc' font-size='14' text-anchor='middle'>{c}</text>"
    for i in range(2):
        s += f"<text x='{x0-18}' y='{y0+ch*i+ch/2+5:.0f}' fill='#7dd3fc' font-size='14' text-anchor='middle'>{i}</text>"
        for j in range(4):
            xx, yy = x0 + cw * j, y0 + ch * i
            s += f"<rect x='{xx}' y='{yy}' width='{cw}' height='{ch}' fill='none' stroke='#334155' stroke-width='1.4'/>"
            col = '#4ade80' if vals[i][j] else '#64748b'
            s += f"<text x='{xx+cw/2:.0f}' y='{yy+ch/2+6:.0f}' fill='{col}' font-size='18' font-weight='700' text-anchor='middle'>{vals[i][j]}</text>"
    # grupo A (fila inferior completa)
    s += f"<rect x='{x0-5}' y='{y0+ch-5}' width='{cw*4+10}' height='{ch+10}' rx='10' fill='none' stroke='#f59e0b' stroke-width='2.4'/>"
    s += f"<text x='{x0+cw*4+14}' y='{y0+ch+ch/2+5:.0f}' fill='#fbbf24' font-size='14'>A</text>"
    # grupo B (columnas 11 y 10, ambas filas)
    s += f"<rect x='{x0+cw*2-5}' y='{y0-5}' width='{cw*2+10}' height='{ch*2+10}' rx='10' fill='none' stroke='#a78bfa' stroke-width='2.4'/>"
    s += f"<text x='{x0+cw*3+2:.0f}' y='{y0-24}' fill='#c4b5fd' font-size='14' text-anchor='middle'>B</text>"
    s += "</svg>"
    return s

def fig_or():
    """Q5 · puerta OR de dos entradas."""
    s = ("<svg viewBox='0 0 320 150' width='100%' style='max-width:300px;height:auto' "
         "fill='none' font-family='Inter,system-ui,sans-serif' stroke='#e2e8f0' stroke-width='2'>")
    s += "<text x='18' y='55' fill='#e2e8f0' font-size='16'>A</text>"
    s += "<text x='18' y='110' fill='#e2e8f0' font-size='16'>B</text>"
    s += "<line x1='34' y1='50' x2='120' y2='50'/><line x1='34' y1='105' x2='120' y2='105'/>"
    s += ("<path d='M110 30 Q150 30 200 77 Q150 125 110 125 Q132 77 110 30 Z' "
          "fill='none' stroke='#34d399' stroke-width='2.4'/>")
    s += "<line x1='200' y1='77' x2='285' y2='77'/>"
    s += "<text x='292' y='82' fill='#e2e8f0' font-size='16'>F</text>"
    s += "</svg>"
    return s

def fig_esfuerzos():
    """Q7 · diagramas de cortante y flector."""
    x0, x1, xm = 70, 520, 295      # A, B, fin carga (mapea 6 m)
    s = ("<svg viewBox='0 0 600 320' width='100%' style='max-width:560px;height:auto' "
         "fill='none' font-family='Inter,system-ui,sans-serif'>")
    # --- cortante ---
    yc = 70
    s += f"<line x1='{x0-5}' y1='{yc}' x2='{x1+15}' y2='{yc}' stroke='#94a3b8' stroke-width='1.4'/>"
    s += f"<text x='{x0-5}' y='{yc-56}' fill='#e2e8f0' font-size='13'>V (kgf)</text>"
    # V: +5625 en A -> -1875 en xm -> constante hasta B
    yA = yc - 45; yM = yc + 15
    s += (f"<polygon points='{x0},{yc} {x0},{yA} {xm},{yM} {xm},{yc}' fill='rgba(56,189,248,.20)' stroke='none'/>")
    s += (f"<polygon points='{xm},{yc} {xm},{yM} {x1},{yM} {x1},{yc}' fill='rgba(251,113,133,.18)' stroke='none'/>")
    s += f"<polyline points='{x0},{yA} {xm},{yM} {x1},{yM} {x1},{yc}' fill='none' stroke='#38bdf8' stroke-width='2.4'/>"
    s += f"<line x1='{x0}' y1='{yc}' x2='{x0}' y2='{yA}' stroke='#38bdf8' stroke-width='2.4'/>"
    s += f"<text x='{x0+8}' y='{yA-4}' fill='#7dd3fc' font-size='12' text-anchor='start'>+5625</text>"
    s += f"<text x='{x1-8}' y='{yM+16}' fill='#fda4af' font-size='12' text-anchor='end'>-1875</text>"
    s += f"<text x='{x0-6}' y='{yc+22}' fill='#94a3b8' font-size='12' text-anchor='middle'>A</text>"
    s += f"<text x='{x1+6}' y='{yc+22}' fill='#94a3b8' font-size='12' text-anchor='middle'>B</text>"
    # --- flector ---
    yf = 230
    s += f"<line x1='{x0-5}' y1='{yf}' x2='{x1+15}' y2='{yf}' stroke='#94a3b8' stroke-width='1.4'/>"
    s += f"<text x='{x0-8}' y='{yf-92}' fill='#e2e8f0' font-size='13'>M (kgf&#183;m)</text>"
    # parabola 0..2.25 pico, luego baja; xpico = x0 + (2.25/6)*(x1-x0)
    xpk = x0 + (2.25 / 6) * (x1 - x0)
    ypk = yf - 80
    # muestreo parabola en [0,3]
    pts = []
    import math
    for k in range(0, 61):
        xx = k / 10.0
        if xx <= 3:
            M = 5625 * xx - 1250 * xx * xx
        else:
            M = 1875 * (6 - xx)
        px = x0 + (xx / 6) * (x1 - x0)
        py = yf - (M / 6328.125) * 80
        pts.append(f"{px:.1f},{py:.1f}")
    s += f"<polygon points='{x0},{yf} " + " ".join(pts) + f" {x1},{yf}' fill='rgba(74,222,128,.18)' stroke='none'/>"
    s += f"<polyline points='" + " ".join(pts) + f"' fill='none' stroke='#4ade80' stroke-width='2.4'/>"
    s += f"<line x1='{xpk:.0f}' y1='{yf}' x2='{xpk:.0f}' y2='{ypk}' stroke='#4ade80' stroke-width='1' stroke-dasharray='4 3'/>"
    s += f"<text x='{xpk:.0f}' y='{ypk-6}' fill='#86efac' font-size='12' text-anchor='middle'>6328</text>"
    s += f"<text x='{xpk:.0f}' y='{yf+18}' fill='#94a3b8' font-size='11' text-anchor='middle'>x=2,25 m</text>"
    s += f"<text x='{x0}' y='{yf+18}' fill='#94a3b8' font-size='12' text-anchor='middle'>A</text>"
    s += f"<text x='{x1}' y='{yf+18}' fill='#94a3b8' font-size='12' text-anchor='middle'>B</text>"
    s += "</svg>"
    return s


# ---------------- CONTENIDO ----------------

data = {
 "meta": {
  "titulo": "Tecnología e Ingeniería II",
  "subtitulo": "Prueba de Acceso a la Universidad (EBAU) · Universidad de Extremadura · Curso 2023-2024 · Examen resuelto y comentado",
  "cabecera_titulo": "EBAU 2024 · <span>Tecnología e Ingeniería II</span> · Extremadura · Ordinaria",
  "pill": "90 min · se eligen 5 de 10 · 2 pt/pregunta",
  "enunciado_pdf": "../../examens/Extremadura/Tecnologia_Extremadura_2024_ordinaria.pdf",
  "pdf_dir": "pdf_ext_2024_ordinaria",
  "footer": "Dpto. Tecnología · Solucionario EBAU 2024 · Extremadura · Tecnología e Ingeniería II (Ordinaria)",
  "intro_inicio": "El examen consta de <b>10 preguntas</b> de 2 puntos; el estudiante debe responder <b>5</b>, elegidas libremente. Aquí se resuelven <b>todas</b> para repasar. Selecciona un bloque o una pregunta en la barra lateral. Cada una incluye el enunciado oficial, una introducción con los conceptos que se aplican y la solución paso a paso.",
  "indice_nombre": "Exámenes de Extremadura",
  "indice_url": "index.html"
 },
 "bloques": [
  {
   "id": "b1", "titulo": "Preguntas 1-3 · Termodinámica, neumática y materiales", "color": "#f59e0b",
   "descripcion_tarjeta": "Bomba de calor de Carnot, cilindro neumático de doble efecto y ensayo de dureza Brinell.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#f59e0b' stroke-width='3'><path d='M12 46 Q28 8 46 30 T78 20'/><circle cx='12' cy='46' r='3' fill='#f59e0b'/></svg>",
   "cuestiones": [
    {
     "id": "q1", "titulo": "Pregunta 1 · Bomba de calor (ciclo de Carnot)", "etiqueta": "TERMODINÁMICA",
     "menu": "P1 · Bomba de calor", "titulo_corto": "P1",
     "meta": "Pregunta de 2 puntos (a: 0,5 · b: 0,75 · c: 0,75)",
     "enunciado_html": "<p>Se desea climatizar una nave a 25 &deg;C mediante una <b>bomba de calor</b> de 2,5 kW de potencia. Si la temperatura exterior es de 5 &deg;C y la bomba funciona según un <b>ciclo de Carnot reversible</b>, determina:</p><ol type='a'><li>Eficiencia de la bomba de calor. <span class='pts'>(0,5 puntos)</span></li><li>Calor cedido al foco caliente durante una hora, en kJ. <span class='pts'>(0,75 puntos)</span></li><li>Calor absorbido del foco frío durante una hora, en kJ. <span class='pts'>(0,75 puntos)</span></li></ol>",
     "figura_enunciado_svg": "",
     "aplica_html": "<p>Una bomba de calor en modo <b>calefacción</b> toma calor del foco frío (\\(T_f\\)) y lo cede al caliente (\\(T_c\\)) consumiendo un trabajo \\(W\\). Su eficiencia es el <b>COP de calefacción</b>:</p><div class='formula'>$$\\mathrm{COP}=\\frac{Q_c}{W}=\\frac{T_c}{T_c-T_f}$$</div><p>Las temperaturas se toman en <b>kelvin</b>. Balance de energía: \\(Q_c=Q_f+W\\).</p>",
     "solucion_html": "<p>Datos: \\(T_c=25\\,\\mathrm{^\\circ C}=298\\,\\mathrm{K}\\), \\(T_f=5\\,\\mathrm{^\\circ C}=278\\,\\mathrm{K}\\), \\(P=2{,}5\\,\\mathrm{kW}\\).</p><h5>a) Eficiencia (COP)</h5><div class='formula'>$$\\mathrm{COP}=\\frac{T_c}{T_c-T_f}=\\frac{298}{298-278}=\\frac{298}{20}=14{,}9$$</div><div class='res'><b>COP = 14,9</b></div><h5>b) Calor cedido al foco caliente en 1 hora</h5><p>Trabajo consumido en una hora: \\(W=P\\cdot t=2{,}5\\,\\mathrm{kW}\\cdot 3600\\,\\mathrm{s}=9000\\,\\mathrm{kJ}\\).</p><div class='formula'>$$Q_c=\\mathrm{COP}\\cdot W=14{,}9\\cdot 9000=134\\,100\\,\\mathrm{kJ}$$</div><div class='res'><b>Q<sub>c</sub> = 134 100 kJ &asymp; 134,1 MJ</b></div><h5>c) Calor absorbido del foco frío en 1 hora</h5><div class='formula'>$$Q_f=Q_c-W=134\\,100-9000=125\\,100\\,\\mathrm{kJ}$$</div><div class='res'><b>Q<sub>f</sub> = 125 100 kJ &asymp; 125,1 MJ</b></div>"
    },
    {
     "id": "q2", "titulo": "Pregunta 2 · Cilindro neumático de doble efecto", "etiqueta": "NEUMÁTICA",
     "menu": "P2 · Cilindro de doble efecto", "titulo_corto": "P2",
     "meta": "Pregunta de 2 puntos (a: 1,0 · b: 1,0)",
     "enunciado_html": "<p>Un dispositivo neumático dispone de un <b>cilindro de doble efecto</b> con: diámetro del émbolo 90 mm; fuerza teórica de retroceso 3393 N; presión de trabajo 6&middot;10<sup>5</sup> Pa; pérdidas por rozamiento 10 % de la fuerza teórica. Calcula:</p><ol type='a'><li>La fuerza real de empuje en el avance. <span class='pts'>(1 punto)</span></li><li>El diámetro del vástago, en mm. <span class='pts'>(1 punto)</span></li></ol>",
     "figura_enunciado_svg": "",
     "aplica_html": "<p>En el <b>avance</b> la presión actúa sobre toda la sección del émbolo; en el <b>retroceso</b>, sobre la sección del émbolo menos la del vástago:</p><div class='formula'>$$F_{av}=p\\cdot\\frac{\\pi D^2}{4}\\qquad F_{ret}=p\\cdot\\frac{\\pi (D^2-d^2)}{4}$$</div><p>La fuerza <b>real</b> descuenta las pérdidas por rozamiento.</p>",
     "solucion_html": "<p>Datos: \\(D=90\\,\\mathrm{mm}=0{,}09\\,\\mathrm{m}\\), \\(p=6\\cdot10^5\\,\\mathrm{Pa}\\), \\(F_{ret,teo}=3393\\,\\mathrm{N}\\), pérdidas 10 %.</p><h5>a) Fuerza real de empuje (avance)</h5><p>Sección del émbolo:</p><div class='formula'>$$A=\\frac{\\pi D^2}{4}=\\frac{\\pi (0{,}09)^2}{4}=6{,}362\\cdot10^{-3}\\,\\mathrm{m^2}$$</div><div class='formula'>$$F_{av,teo}=p\\cdot A=6\\cdot10^5\\cdot 6{,}362\\cdot10^{-3}=3817\\,\\mathrm{N}$$</div><p>Descontando el 10 % de rozamiento:</p><div class='formula'>$$F_{av,real}=0{,}9\\cdot 3817=3435\\,\\mathrm{N}$$</div><div class='res'><b>F<sub>avance</sub> &asymp; 3435 N</b></div><h5>b) Diámetro del vástago</h5><p>De la fuerza teórica de retroceso:</p><div class='formula'>$$A_{emb}-A_{vas}=\\frac{F_{ret,teo}}{p}=\\frac{3393}{6\\cdot10^5}=5{,}655\\cdot10^{-3}\\,\\mathrm{m^2}$$</div><div class='formula'>$$A_{vas}=6{,}362\\cdot10^{-3}-5{,}655\\cdot10^{-3}=7{,}07\\cdot10^{-4}\\,\\mathrm{m^2}$$</div><div class='formula'>$$d=\\sqrt{\\frac{4A_{vas}}{\\pi}}=\\sqrt{\\frac{4\\cdot 7{,}07\\cdot10^{-4}}{\\pi}}=0{,}030\\,\\mathrm{m}$$</div><div class='res'><b>d = 30 mm</b></div>"
    },
    {
     "id": "q3", "titulo": "Pregunta 3 · Ensayo de dureza Brinell", "etiqueta": "MATERIALES",
     "menu": "P3 · Dureza Brinell", "titulo_corto": "P3",
     "meta": "Pregunta de 2 puntos (a: 1,0 · b: 1,0)",
     "enunciado_html": "<p>Para determinar la <b>dureza Brinell</b> de un material se utiliza una bola de 5 mm de diámetro y se elige una constante K = 30, obteniéndose una huella de 1,80 mm de diámetro. Calcula:</p><ol type='a'><li>Dureza Brinell del material. <span class='pts'>(1 punto)</span></li><li>Profundidad de la huella. <span class='pts'>(1 punto)</span></li></ol>",
     "figura_enunciado_svg": "",
     "aplica_html": "<p>En el ensayo Brinell la carga se fija con \\(F=K\\,D^2\\) (en kgf) y la dureza es la carga entre el área del casquete esférico de la huella:</p><div class='formula'>$$\\mathrm{HB}=\\frac{2F}{\\pi D\\left(D-\\sqrt{D^2-d^2}\\right)}$$</div><p>La profundidad de la huella es \\(h=\\dfrac{D-\\sqrt{D^2-d^2}}{2}\\).</p>",
     "solucion_html": "<p>Datos: \\(D=5\\,\\mathrm{mm}\\), \\(K=30\\), \\(d=1{,}80\\,\\mathrm{mm}\\).</p><h5>a) Dureza Brinell</h5><p>Carga aplicada:</p><div class='formula'>$$F=K\\,D^2=30\\cdot 5^2=750\\,\\mathrm{kgf}$$</div><div class='formula'>$$\\sqrt{D^2-d^2}=\\sqrt{25-3{,}24}=4{,}665\\,\\mathrm{mm}$$</div><div class='formula'>$$\\mathrm{HB}=\\frac{2\\cdot 750}{\\pi\\cdot 5\\,(5-4{,}665)}=\\frac{1500}{5{,}265}=284{,}9$$</div><div class='res'><b>HB &asymp; 285 kgf/mm²</b></div><h5>b) Profundidad de la huella</h5><div class='formula'>$$h=\\frac{D-\\sqrt{D^2-d^2}}{2}=\\frac{5-4{,}665}{2}=0{,}168\\,\\mathrm{mm}$$</div><div class='res'><b>h &asymp; 0,168 mm</b></div>"
    }
   ]
  },
  {
   "id": "b2", "titulo": "Preguntas 4-6 · Motores, electrónica digital y control", "color": "#22d3ee",
   "descripcion_tarjeta": "Motor de combustión de cuatro cilindros, función lógica por Karnaugh y reducción de un sistema de control.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#22d3ee' stroke-width='3'><circle cx='30' cy='30' r='16'/><path d='M30 8v-5M30 57v-5M8 30H3M57 30h-5'/><circle cx='30' cy='30' r='5'/></svg>",
   "cuestiones": [
    {
     "id": "q4", "titulo": "Pregunta 4 · Motor de combustión de 4 cilindros", "etiqueta": "MOTORES",
     "menu": "P4 · Motor de 4 cilindros", "titulo_corto": "P4",
     "meta": "Pregunta de 2 puntos (a-d: 0,5 c/u)",
     "enunciado_html": "<p>Un motor de 4 cilindros desarrolla una <b>potencia efectiva</b> de 60 CV a 3500 rpm. El diámetro de cada pistón es 70 mm, la carrera 90 mm y \\(R_c=9/1\\). Determina:</p><ol type='a'><li>La cilindrada del motor. <span class='pts'>(0,5 puntos)</span></li><li>El volumen de la cámara de combustión. <span class='pts'>(0,5 puntos)</span></li><li>El par motor. <span class='pts'>(0,5 puntos)</span></li><li>Si consume 8 kg/h de combustible con \\(P_c=48000\\,\\mathrm{kJ/kg}\\), la potencia absorbida y el rendimiento efectivo (en CV). <span class='pts'>(0,5 puntos)</span></li></ol>",
     "figura_enunciado_svg": "",
     "aplica_html": "<p>Cilindrada unitaria \\(V_u=\\frac{\\pi D^2}{4}\\,S\\); total \\(V_T=n\\,V_u\\). La relación de compresión relaciona el volumen desplazado con el de la cámara: \\(R_c=\\frac{V_u+V_c}{V_c}\\). El par se obtiene de \\(P=M\\,\\omega\\) y el rendimiento de \\(\\eta=\\frac{P_{efectiva}}{P_{absorbida}}\\).</p>",
     "solucion_html": "<p>Datos: \\(n=4\\), \\(D=7\\,\\mathrm{cm}\\), \\(S=9\\,\\mathrm{cm}\\), \\(R_c=9\\), \\(N=3500\\,\\mathrm{rpm}\\), \\(P_e=60\\,\\mathrm{CV}\\).</p><h5>a) Cilindrada</h5><div class='formula'>$$V_u=\\frac{\\pi\\cdot 7^2}{4}\\cdot 9=346{,}4\\,\\mathrm{cm^3}\\;\\Rightarrow\\; V_T=4\\cdot 346{,}4=1385\\,\\mathrm{cm^3}$$</div><div class='res'><b>V<sub>T</sub> &asymp; 1385 cm³ (1,385 L)</b></div><h5>b) Volumen de la cámara de combustión</h5><div class='formula'>$$R_c=\\frac{V_u+V_c}{V_c}\\Rightarrow V_c=\\frac{V_u}{R_c-1}=\\frac{346{,}4}{8}=43{,}3\\,\\mathrm{cm^3}$$</div><div class='res'><b>V<sub>c</sub> &asymp; 43,3 cm³ por cilindro</b></div><h5>c) Par motor</h5><p>\\(P_e=60\\,\\mathrm{CV}=44\\,130\\,\\mathrm{W}\\); \\(\\omega=3500\\cdot\\frac{2\\pi}{60}=366{,}5\\,\\mathrm{rad/s}\\).</p><div class='formula'>$$M=\\frac{P_e}{\\omega}=\\frac{44\\,130}{366{,}5}=120{,}4\\,\\mathrm{N\\cdot m}$$</div><div class='res'><b>M &asymp; 120,4 N&middot;m</b></div><h5>d) Potencia absorbida y rendimiento</h5><div class='formula'>$$P_{abs}=\\dot m\\cdot P_c=8\\cdot 48000=384\\,000\\,\\mathrm{kJ/h}=106{,}7\\,\\mathrm{kW}=145{,}0\\,\\mathrm{CV}$$</div><div class='formula'>$$\\eta_e=\\frac{P_e}{P_{abs}}=\\frac{60}{145}=0{,}414$$</div><div class='res'><b>P<sub>abs</sub> &asymp; 145 CV &nbsp;·&nbsp; &eta;<sub>e</sub> &asymp; 41,4 %</b></div>"
    },
    {
     "id": "q5", "titulo": "Pregunta 5 · Función lógica y método de Karnaugh", "etiqueta": "ELECTRÓNICA DIGITAL",
     "menu": "P5 · Karnaugh", "titulo_corto": "P5",
     "meta": "Pregunta de 2 puntos (a: 0,75 · b: 0,75 · c: 0,5)",
     "enunciado_html": "<p>A partir de la siguiente tabla de verdad:</p><table class='dat'><tr><th>A</th><th>B</th><th>C</th><th>F</th></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>1</td><td>0</td></tr><tr style='background:rgba(74,222,128,.14)'><td>0</td><td>1</td><td>0</td><td>1</td></tr><tr style='background:rgba(74,222,128,.14)'><td>0</td><td>1</td><td>1</td><td>1</td></tr><tr style='background:rgba(74,222,128,.14)'><td>1</td><td>0</td><td>0</td><td>1</td></tr><tr style='background:rgba(74,222,128,.14)'><td>1</td><td>0</td><td>1</td><td>1</td></tr><tr style='background:rgba(74,222,128,.14)'><td>1</td><td>1</td><td>0</td><td>1</td></tr><tr style='background:rgba(74,222,128,.14)'><td>1</td><td>1</td><td>1</td><td>1</td></tr></table><ol type='a'><li>Obtener la primera forma canónica de la función. <span class='pts'>(0,75 puntos)</span></li><li>Simplificar por el método de Karnaugh. <span class='pts'>(0,75 puntos)</span></li><li>Implementar el circuito combinacional correspondiente. <span class='pts'>(0,5 puntos)</span></li></ol>",
     "figura_enunciado_svg": "",
     "aplica_html": "<p>La <b>primera forma canónica</b> es la suma de los <b>minterms</b> (productos) donde \\(F=1\\). El <b>mapa de Karnaugh</b> agrupa unos adyacentes en potencias de 2 para eliminar las variables que cambian dentro de cada grupo.</p>",
     "solucion_html": "<h5>a) Primera forma canónica (suma de minterms)</h5><p>\\(F=1\\) en los minterms 2, 3, 4, 5, 6 y 7:</p><div class='formula'>$$F=\\bar A B\\bar C+\\bar A BC+A\\bar B\\bar C+A\\bar BC+AB\\bar C+ABC$$</div><h5>b) Simplificación por Karnaugh</h5><p>Solo hay dos ceros (A=0, B=0). Se forman dos grupos de cuatro: la fila \\(A=1\\) completa (&rarr; A) y las columnas con \\(B=1\\) (&rarr; B).</p><figure class='fig'>" + fig_kmap() + "<figcaption>Mapa de Karnaugh de F(A,B,C): grupo A (naranja) y grupo B (violeta).</figcaption></figure><div class='formula'>$$F=A+B$$</div><div class='res'><b>F = A + B</b></div><h5>c) Circuito combinacional</h5><p>Se implementa con una única <b>puerta OR</b> de dos entradas:</p><figure class='fig'>" + fig_or() + "<figcaption>Implementación de F = A + B con una puerta OR.</figcaption></figure>"
    },
    {
     "id": "q6", "titulo": "Pregunta 6 · Reducción de un sistema de control", "etiqueta": "CONTROL",
     "menu": "P6 · Sistema de control", "titulo_corto": "P6",
     "meta": "Pregunta de 2 puntos",
     "enunciado_html": "<p>Simplifica el siguiente sistema de control hasta conseguir la <b>función de transferencia</b> del sistema. <span class='pts'>(2 puntos)</span></p>",
     "figura_enunciado_svg": "<figure class='fig'>" + fig_bloques() + "<figcaption>Diagrama de bloques: dos lazos internos de realimentación positiva (H<sub>1</sub>, H<sub>2</sub>) y un lazo externo de realimentación negativa (H<sub>3</sub>).</figcaption></figure>",
     "aplica_html": "<p>Se reduce por lazos. Un lazo de realimentación <b>positiva</b> equivale a \\(\\frac{G}{1-GH}\\); uno <b>negativo</b>, a \\(\\frac{G}{1+GH}\\). Los bloques en serie se multiplican.</p>",
     "solucion_html": "<h5>Lazos internos (realimentación positiva)</h5><p>El primer sumador interno es positivo, así que el lazo de \\(G_1\\) con \\(H_1\\):</p><div class='formula'>$$M_1=\\frac{G_1}{1-G_1H_1}$$</div><p>Análogamente, el lazo de \\(G_2\\) con \\(H_2\\):</p><div class='formula'>$$M_2=\\frac{G_2}{1-G_2H_2}$$</div><h5>Serie y lazo externo (realimentación negativa con H<sub>3</sub>)</h5><p>En cascada \\(M_1M_2\\), realimentado negativamente por \\(H_3\\):</p><div class='formula'>$$\\frac{G(s)}{R(s)}=\\frac{M_1M_2}{1+M_1M_2H_3}$$</div><p>Sustituyendo \\(M_1\\) y \\(M_2\\) y operando:</p><div class='formula'>$$\\boxed{\\dfrac{G(s)}{R(s)}=\\dfrac{G_1G_2}{(1-G_1H_1)(1-G_2H_2)+G_1G_2H_3}}$$</div><div class='res'><b>FT = G<sub>1</sub>G<sub>2</sub> / [ (1&minus;G<sub>1</sub>H<sub>1</sub>)(1&minus;G<sub>2</sub>H<sub>2</sub>) + G<sub>1</sub>G<sub>2</sub>H<sub>3</sub> ]</b></div>"
    }
   ]
  },
  {
   "id": "b3", "titulo": "Preguntas 7-8 · Estructuras y máquinas térmicas", "color": "#a78bfa",
   "descripcion_tarjeta": "Viga biapoyada con carga distribuida parcial y máquina frigorífica de Carnot.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#a78bfa' stroke-width='3'><path d='M10 30h70'/><path d='M20 30v-12M32 30v-12M44 30v-12M56 30v-12'/><path d='M10 30l-6 12h12zM80 42a6 6 0 100-1'/></svg>",
   "cuestiones": [
    {
     "id": "q7", "titulo": "Pregunta 7 · Viga con carga distribuida parcial", "etiqueta": "ESTRUCTURAS",
     "menu": "P7 · Viga biapoyada", "titulo_corto": "P7",
     "meta": "Pregunta de 2 puntos",
     "enunciado_html": "<p>Para la viga mostrada, calcula las <b>reacciones</b> en los apoyos y el valor <b>máximo</b> del esfuerzo cortante y del momento flector. <span class='pts'>(2 puntos)</span></p>",
     "figura_enunciado_svg": "<figure class='fig'>" + fig_viga() + "<figcaption>Viga biapoyada de 6 m con carga uniforme Q = 2500 kg/m sobre la mitad izquierda (3 m).</figcaption></figure>",
     "aplica_html": "<p>La carga distribuida \\(Q\\) sobre una longitud \\(L_1\\) equivale a una resultante \\(R=Q\\,L_1\\) aplicada en su centro de gravedad. Se plantean \\(\\sum M=0\\) y \\(\\sum F_y=0\\). El <b>momento flector</b> es máximo donde el <b>cortante</b> se anula.</p>",
     "solucion_html": "<p>Carga total: \\(R=Q\\cdot L_1=2500\\cdot 3=7500\\,\\mathrm{kgf}\\), aplicada a 1,5 m de A. Luz total 6 m.</p><h5>Reacciones</h5><div class='formula'>$$\\sum M_A=0:\\; R_B\\cdot 6-7500\\cdot 1{,}5=0\\Rightarrow R_B=1875\\,\\mathrm{kgf}$$</div><div class='formula'>$$R_A=7500-1875=5625\\,\\mathrm{kgf}$$</div><div class='res'><b>R<sub>A</sub> = 5625 kgf &nbsp;·&nbsp; R<sub>B</sub> = 1875 kgf</b></div><h5>Cortante máximo</h5><p>El cortante vale \\(+R_A\\) justo a la derecha de A y decrece con la carga: \\(V(x)=5625-2500x\\). Su valor máximo (en A) es:</p><div class='res'><b>V<sub>máx</sub> = 5625 kgf (en A)</b></div><h5>Momento flector máximo</h5><p>Se anula el cortante en \\(x=\\frac{5625}{2500}=2{,}25\\,\\mathrm{m}\\):</p><div class='formula'>$$M_{max}=5625\\cdot 2{,}25-2500\\cdot\\frac{2{,}25^2}{2}=6328\\,\\mathrm{kgf\\cdot m}$$</div><div class='res'><b>M<sub>máx</sub> &asymp; 6328 kgf&middot;m (en x = 2,25 m)</b></div><figure class='fig'>" + fig_esfuerzos() + "<figcaption>Diagramas de esfuerzo cortante (arriba) y momento flector (abajo).</figcaption></figure>"
    },
    {
     "id": "q8", "titulo": "Pregunta 8 · Máquina frigorífica de Carnot", "etiqueta": "TERMODINÁMICA",
     "menu": "P8 · Congelador de Carnot", "titulo_corto": "P8",
     "meta": "Pregunta de 2 puntos (a: 0,75 · b: 0,5 · c: 0,75)",
     "enunciado_html": "<p>Un pequeño congelador funciona según un <b>ciclo frigorífico de Carnot</b> y enfría a una velocidad de 700 kJ/h. La temperatura de la nevera debe ser de aprox. &minus;10 &deg;C y la temperatura ambiente del recinto es de 28 &deg;C. Determina:</p><ol type='a'><li>La eficiencia de la máquina y la potencia que debe tener el motor. <span class='pts'>(0,75 puntos)</span></li><li>El calor cedido a la atmósfera. <span class='pts'>(0,5 puntos)</span></li><li>La potencia del motor si la eficiencia real fuese un 60 % de la del ciclo de Carnot. <span class='pts'>(0,75 puntos)</span></li></ol>",
     "figura_enunciado_svg": "",
     "aplica_html": "<p>En una máquina frigorífica la eficiencia es el <b>COP de refrigeración</b>: \\(\\mathrm{COP}=\\frac{Q_f}{W}=\\frac{T_f}{T_c-T_f}\\) (temperaturas en K). La potencia del motor es \\(W=\\frac{\\dot Q_f}{\\mathrm{COP}}\\) y el calor cedido \\(\\dot Q_c=\\dot Q_f+W\\).</p>",
     "solucion_html": "<p>Datos: \\(T_f=-10\\,\\mathrm{^\\circ C}=263\\,\\mathrm{K}\\), \\(T_c=28\\,\\mathrm{^\\circ C}=301\\,\\mathrm{K}\\), \\(\\dot Q_f=700\\,\\mathrm{kJ/h}\\).</p><h5>a) Eficiencia y potencia del motor</h5><div class='formula'>$$\\mathrm{COP}=\\frac{T_f}{T_c-T_f}=\\frac{263}{301-263}=\\frac{263}{38}=6{,}92$$</div><div class='formula'>$$\\dot W=\\frac{\\dot Q_f}{\\mathrm{COP}}=\\frac{700}{6{,}92}=101{,}1\\,\\mathrm{kJ/h}=28{,}1\\,\\mathrm{W}$$</div><div class='res'><b>COP = 6,92 &nbsp;·&nbsp; P<sub>motor</sub> &asymp; 28,1 W</b></div><h5>b) Calor cedido a la atmósfera</h5><div class='formula'>$$\\dot Q_c=\\dot Q_f+\\dot W=700+101{,}1=801{,}1\\,\\mathrm{kJ/h}$$</div><div class='res'><b>Q<sub>c</sub> &asymp; 801 kJ/h</b></div><h5>c) Potencia con eficiencia real (60 % de la de Carnot)</h5><div class='formula'>$$\\mathrm{COP}_{real}=0{,}6\\cdot 6{,}92=4{,}15$$</div><div class='formula'>$$\\dot W=\\frac{700}{4{,}15}=168{,}6\\,\\mathrm{kJ/h}=46{,}8\\,\\mathrm{W}$$</div><div class='res'><b>P<sub>motor,real</sub> &asymp; 46,8 W</b></div>"
    }
   ]
  },
  {
   "id": "b4", "titulo": "Preguntas 9-10 · Resistencia de materiales y corriente alterna", "color": "#34d399",
   "descripcion_tarjeta": "Barra de acero a tracción (tensión, seguridad y alargamiento) y circuito RL serie en alterna.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#34d399' stroke-width='3'><path d='M8 30h74'/><path d='M8 30l8-6M8 30l8 6M82 30l-8-6M82 30l-8 6'/><rect x='30' y='22' width='30' height='16'/></svg>",
   "cuestiones": [
    {
     "id": "q9", "titulo": "Pregunta 9 · Barra de acero a tracción", "etiqueta": "RESISTENCIA DE MATERIALES",
     "menu": "P9 · Tracción de una barra", "titulo_corto": "P9",
     "meta": "Pregunta de 2 puntos (a: 0,75 · b: 0,5 · c: 0,75)",
     "enunciado_html": "<p>La pieza de la figura es de acero, con límite elástico de 3900 kgf/cm². Se somete a una fuerza F de 6000 kgf. Calcula:</p><ol type='a'><li>Tensión de trabajo (&sigma;<sub>t</sub>). <span class='pts'>(0,75 puntos)</span></li><li>Coeficiente de seguridad (n) respecto al límite elástico. <span class='pts'>(0,5 puntos)</span></li><li>Alargamiento de la barra. <span class='pts'>(0,75 puntos)</span></li></ol><p>Dato: \\(E=2{,}1\\cdot10^6\\,\\mathrm{kgf/cm^2}\\). Medidas en mm.</p>",
     "figura_enunciado_svg": "<figure class='fig'>" + fig_barra() + "<figcaption>Barra cilíndrica de &oslash; 30 mm y longitud L<sub>o</sub> = 50 mm sometida a tracción.</figcaption></figure>",
     "aplica_html": "<p>La tensión de trabajo es \\(\\sigma_t=\\frac{F}{A}\\), con \\(A=\\frac{\\pi D^2}{4}\\). El coeficiente de seguridad respecto al límite elástico es \\(n=\\frac{\\sigma_e}{\\sigma_t}\\). En régimen elástico (ley de Hooke) el alargamiento es \\(\\Delta L=\\frac{\\sigma_t\\,L_0}{E}\\).</p>",
     "solucion_html": "<p>Datos: \\(D=30\\,\\mathrm{mm}=3\\,\\mathrm{cm}\\), \\(L_0=50\\,\\mathrm{mm}=5\\,\\mathrm{cm}\\), \\(F=6000\\,\\mathrm{kgf}\\), \\(\\sigma_e=3900\\,\\mathrm{kgf/cm^2}\\).</p><h5>a) Tensión de trabajo</h5><div class='formula'>$$A=\\frac{\\pi D^2}{4}=\\frac{\\pi\\cdot 3^2}{4}=7{,}069\\,\\mathrm{cm^2}$$</div><div class='formula'>$$\\sigma_t=\\frac{F}{A}=\\frac{6000}{7{,}069}=848{,}8\\,\\mathrm{kgf/cm^2}$$</div><div class='res'><b>&sigma;<sub>t</sub> &asymp; 848,8 kgf/cm²</b></div><h5>b) Coeficiente de seguridad</h5><div class='formula'>$$n=\\frac{\\sigma_e}{\\sigma_t}=\\frac{3900}{848{,}8}=4{,}59$$</div><div class='res'><b>n &asymp; 4,6</b></div><h5>c) Alargamiento</h5><div class='formula'>$$\\Delta L=\\frac{\\sigma_t\\,L_0}{E}=\\frac{848{,}8\\cdot 5}{2{,}1\\cdot10^6}=2{,}02\\cdot10^{-3}\\,\\mathrm{cm}$$</div><div class='res'><b>&Delta;L &asymp; 0,0202 mm</b></div>"
    },
    {
     "id": "q10", "titulo": "Pregunta 10 · Circuito RL serie en corriente alterna", "etiqueta": "CORRIENTE ALTERNA",
     "menu": "P10 · Circuito RL serie", "titulo_corto": "P10",
     "meta": "Pregunta de 2 puntos (a-d: 0,5 c/u)",
     "enunciado_html": "<p>El circuito equivalente de la bobina de un contactor consta de una resistencia de 20 &ohm; y de una bobina pura con coeficiente de autoinducción de 50 mH, alimentado a 125 V / 50 Hz. Calcula:</p><ol type='a'><li>Impedancia total. <span class='pts'>(0,5 puntos)</span></li><li>Intensidad total. <span class='pts'>(0,5 puntos)</span></li><li>Ángulo de desfase. <span class='pts'>(0,5 puntos)</span></li><li>Caída de tensión en la resistencia y en la bobina. <span class='pts'>(0,5 puntos)</span></li></ol>",
     "figura_enunciado_svg": "<figure class='fig'>" + fig_rl() + "<figcaption>Circuito RL serie: R = 20 &ohm; y L = 50 mH alimentados a 125 V / 50 Hz.</figcaption></figure>",
     "aplica_html": "<p>La reactancia inductiva es \\(X_L=2\\pi f L\\). En serie, la impedancia es \\(Z=\\sqrt{R^2+X_L^2}\\), la intensidad \\(I=\\frac{V}{Z}\\), el desfase \\(\\varphi=\\arctan\\frac{X_L}{R}\\), y las caídas \\(V_R=I\\,R\\), \\(V_L=I\\,X_L\\).</p>",
     "solucion_html": "<p>Datos: \\(R=20\\,\\Omega\\), \\(L=50\\,\\mathrm{mH}=0{,}05\\,\\mathrm{H}\\), \\(V=125\\,\\mathrm{V}\\), \\(f=50\\,\\mathrm{Hz}\\).</p><h5>a) Impedancia total</h5><div class='formula'>$$X_L=2\\pi f L=2\\pi\\cdot 50\\cdot 0{,}05=15{,}71\\,\\Omega$$</div><div class='formula'>$$Z=\\sqrt{20^2+15{,}71^2}=\\sqrt{646{,}7}=25{,}43\\,\\Omega$$</div><div class='res'><b>Z &asymp; 25,43 &ohm;</b></div><h5>b) Intensidad total</h5><div class='formula'>$$I=\\frac{V}{Z}=\\frac{125}{25{,}43}=4{,}92\\,\\mathrm{A}$$</div><div class='res'><b>I &asymp; 4,92 A</b></div><h5>c) Ángulo de desfase</h5><div class='formula'>$$\\varphi=\\arctan\\frac{X_L}{R}=\\arctan\\frac{15{,}71}{20}=38{,}1^\\circ$$</div><div class='res'><b>&phi; &asymp; 38,1° (la corriente atrasa respecto a la tensión)</b></div><h5>d) Caídas de tensión</h5><div class='formula'>$$V_R=I\\,R=4{,}92\\cdot 20=98{,}3\\,\\mathrm{V}$$</div><div class='formula'>$$V_L=I\\,X_L=4{,}92\\cdot 15{,}71=77{,}3\\,\\mathrm{V}$$</div><div class='res'><b>V<sub>R</sub> &asymp; 98,3 V &nbsp;·&nbsp; V<sub>L</sub> &asymp; 77,3 V</b></div><p style='color:#94a3b8;font-size:.85rem'>Comprobación: \\(\\sqrt{98{,}3^2+77{,}3^2}\\approx125\\,\\mathrm{V}\\). ✓</p>"
    }
   ]
  }
 ]
}

out = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ext_2024_ordinaria.json"))
with open(out, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print("JSON escrito:", out)
