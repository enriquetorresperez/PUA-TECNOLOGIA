#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera el JSON del examen Extremadura PAU 2026 (ordinaria) para pau-dashboard."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import svg_open, box, summer, arrow, line, txt

# ---------------- FIGURAS ENUNCIADO ----------------

def fig_bloq71():
    s = svg_open('900 380', 820)
    ym = 175
    s += arrow(66, ym, 118, ym)
    s += summer(134, ym)
    s += arrow(150, ym, 190, ym)
    s += box(190, ym-22, 78, 44, 'P1', '#22d3ee')
    s += arrow(268, ym, 350, ym)
    s += box(350, ym-22, 78, 44, 'P2', '#22d3ee')
    s += arrow(428, ym, 486, ym)
    s += summer(502, ym)
    s += arrow(518, ym, 560, ym)
    s += box(560, ym-22, 78, 44, 'P5', '#22d3ee')
    s += arrow(638, ym, 800, ym)
    s += txt(40, ym+5, 'X', '#e2e8f0', 16); s += txt(812, ym+5, 'Z', '#e2e8f0', 16)
    s += f"<circle cx='300' cy='{ym}' r='3.2' fill='#cbd5e1' stroke='none'/>"
    s += f"<circle cx='680' cy='{ym}' r='3.2' fill='#cbd5e1' stroke='none'/>"
    s += txt(116, ym-14, '+', '#4ade80', 14); s += txt(120, ym+26, '−', '#fb7185', 16)
    s += txt(486, ym-14, '+', '#4ade80', 14); s += txt(490, ym+26, '+', '#4ade80', 14)
    # feedforward N1 -> sum2 (+)
    s += line(300, ym, 300, 95); s += line(300, 95, 502, 95); s += arrow(502, 95, 502, ym-18)
    # realim P4, P3 (de N2 a sum1, negativa)
    s += box(430, 300, 78, 40, 'P4', '#a78bfa')
    s += box(250, 300, 78, 40, 'P3', '#a78bfa')
    s += line(680, ym, 680, 320); s += arrow(680, 320, 508, 320)
    s += arrow(430, 320, 328, 320)
    s += line(250, 320, 134, 320); s += arrow(134, 320, 134, ym+18)
    s += "</svg>"
    return s

def fig_bloq72():
    s = svg_open('900 420', 820)
    ym = 175
    s += arrow(66, ym, 118, ym)
    s += summer(134, ym)
    s += line(150, ym, 190, ym)
    s += f"<circle cx='190' cy='{ym}' r='3.2' fill='#cbd5e1' stroke='none'/>"
    # rama superior P1
    s += box(240, 90, 80, 42, 'P1', '#22d3ee')
    s += line(190, ym, 190, 111); s += arrow(190, 111, 240, 111)
    s += line(320, 111, 545, 111); s += arrow(545, 111, 561, ym-18)
    # rama inferior P2 -> P3
    s += box(240, 240, 80, 42, 'P2', '#22d3ee')
    s += box(370, 240, 80, 42, 'P3', '#22d3ee')
    s += line(190, ym, 190, 261); s += arrow(190, 261, 240, 261)
    s += arrow(320, 261, 370, 261)
    s += line(450, 261, 545, 261); s += arrow(545, 261, 561, ym+18)
    # sum2 y P4
    s += summer(577, ym)
    s += arrow(593, ym, 660, ym)
    s += f"<circle cx='628' cy='{ym}' r='3.2' fill='#cbd5e1' stroke='none'/>"
    s += box(660, ym-22, 80, 44, 'P4', '#22d3ee')
    s += arrow(740, ym, 800, ym)
    s += txt(40, ym+5, 'X', '#e2e8f0', 16); s += txt(812, ym+5, 'Z', '#e2e8f0', 16)
    s += txt(116, ym-14, '+', '#4ade80', 14); s += txt(120, ym+26, '−', '#fb7185', 16)
    s += txt(561, ym-14, '+', '#4ade80', 14); s += txt(565, ym+26, '−', '#fb7185', 16)
    # realim P5 (de N a sum1, negativa)
    s += box(370, 350, 80, 42, 'P5', '#a78bfa')
    s += line(628, ym, 628, 371); s += arrow(628, 371, 450, 371)
    s += line(370, 371, 134, 371); s += arrow(134, 371, 134, ym+18)
    s += "</svg>"
    return s

def fig_viga7():
    """Q3.1 viga 6 m con carga puntual a 1,5 m de A."""
    x0, x1 = 90, 545
    xc = x0 + (1.5 / 6) * (x1 - x0)
    yb = 155
    s = ("<svg viewBox='0 0 620 290' width='100%' style='max-width:560px;height:auto' "
         "fill='none' font-family='Inter,system-ui,sans-serif'>")
    s += f"<line x1='{xc:.0f}' y1='58' x2='{xc:.0f}' y2='{yb-2}' stroke='#fb7185' stroke-width='3'/>"
    s += f"<polygon points='{xc-8:.0f},{yb-14} {xc+8:.0f},{yb-14} {xc:.0f},{yb-1}' fill='#fb7185'/>"
    s += f"<text x='{xc+14:.0f}' y='78' fill='#fda4af' font-size='15' font-weight='700'>P = 12000 N</text>"
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
    yc2 = yb + 76
    for (xa, xbb, lab) in ((x0, xc, '1,5 m'), (xc, x1, '4,5 m')):
        s += f"<line x1='{xa:.0f}' y1='{yc2}' x2='{xbb:.0f}' y2='{yc2}' stroke='#94a3b8' stroke-width='1.4'/>"
        s += f"<polygon points='{xa:.0f},{yc2} {xa+11:.0f},{yc2-5} {xa+11:.0f},{yc2+5}' fill='#94a3b8'/>"
        s += f"<polygon points='{xbb:.0f},{yc2} {xbb-11:.0f},{yc2-5} {xbb-11:.0f},{yc2+5}' fill='#94a3b8'/>"
        s += f"<text x='{(xa+xbb)/2:.0f}' y='{yc2-9}' fill='#cbd5e1' font-size='13' text-anchor='middle'>{lab}</text>"
    s += "</svg>"
    return s

# ---------------- FIGURAS SOLUCION ----------------

def fig_esfuerzos7():
    x0, x1 = 70, 520
    xc = x0 + (1.5 / 6) * (x1 - x0)
    s = ("<svg viewBox='0 0 560 300' width='100%' style='max-width:520px;height:auto' "
         "fill='none' font-family='Inter,system-ui,sans-serif'>")
    yc = 70
    s += f"<line x1='{x0-5}' y1='{yc}' x2='{x1+10}' y2='{yc}' stroke='#94a3b8' stroke-width='1.4'/>"
    s += f"<text x='{x0-5}' y='{yc-46}' fill='#e2e8f0' font-size='13'>V (N)</text>"
    yp, yn = yc - 42, yc + 18
    s += (f"<polygon points='{x0},{yc} {x0},{yp} {xc:.0f},{yp} {xc:.0f},{yc}' fill='rgba(56,189,248,.18)' stroke='none'/>")
    s += (f"<polygon points='{xc:.0f},{yc} {xc:.0f},{yn} {x1},{yn} {x1},{yc}' fill='rgba(251,113,133,.16)' stroke='none'/>")
    s += (f"<polyline points='{x0},{yp} {xc:.0f},{yp} {xc:.0f},{yn} {x1},{yn}' fill='none' stroke='#38bdf8' stroke-width='2.4'/>")
    s += f"<line x1='{x0}' y1='{yc}' x2='{x0}' y2='{yp}' stroke='#38bdf8' stroke-width='2.4'/>"
    s += f"<line x1='{x1}' y1='{yn}' x2='{x1}' y2='{yc}' stroke='#38bdf8' stroke-width='2.4'/>"
    s += f"<text x='{x0+8}' y='{yp-6}' fill='#7dd3fc' font-size='12'>+9000</text>"
    s += f"<text x='{x1-8}' y='{yn+16}' fill='#7dd3fc' font-size='12' text-anchor='end'>-3000</text>"
    yf = 240
    s += f"<line x1='{x0-5}' y1='{yf}' x2='{x1+10}' y2='{yf}' stroke='#94a3b8' stroke-width='1.4'/>"
    s += f"<text x='{x0-5}' y='{yf-92}' fill='#e2e8f0' font-size='13'>M (N·m)</text>"
    ypk = yf - 80
    s += (f"<polygon points='{x0},{yf} {xc:.0f},{ypk} {x1},{yf}' fill='rgba(74,222,128,.18)' stroke='none'/>")
    s += (f"<polyline points='{x0},{yf} {xc:.0f},{ypk} {x1},{yf}' fill='none' stroke='#4ade80' stroke-width='2.4'/>")
    s += f"<line x1='{xc:.0f}' y1='{yf}' x2='{xc:.0f}' y2='{ypk}' stroke='#4ade80' stroke-width='1' stroke-dasharray='4 3'/>"
    s += f"<text x='{xc:.0f}' y='{ypk-6}' fill='#86efac' font-size='12' text-anchor='middle'>13500</text>"
    s += f"<text x='{xc:.0f}' y='{yf+18}' fill='#94a3b8' font-size='11' text-anchor='middle'>x=1,5 m</text>"
    s += f"<text x='{x0}' y='{yf+18}' fill='#94a3b8' font-size='12' text-anchor='middle'>A</text>"
    s += f"<text x='{x1}' y='{yf+18}' fill='#94a3b8' font-size='12' text-anchor='middle'>B</text>"
    s += "</svg>"
    return s

def fig_kmap4_q1():
    x0, y0, cw, ch = 150, 72, 58, 44
    rows = ['00', '01', '11', '10']
    cols = ['00', '01', '11', '10']
    vals = [[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 1]]
    s = ("<svg viewBox='0 0 470 320' width='100%' style='max-width:430px;height:auto' "
         "fill='none' font-family='Inter,system-ui,sans-serif'>")
    s += f"<text x='{x0-40}' y='{y0-14}' fill='#94a3b8' font-size='12'>AB\\CD</text>"
    for j, c in enumerate(cols):
        s += f"<text x='{x0+cw*j+cw/2:.0f}' y='{y0-14}' fill='#7dd3fc' font-size='13' text-anchor='middle'>{c}</text>"
    for i, r in enumerate(rows):
        s += f"<text x='{x0-22}' y='{y0+ch*i+ch/2+5:.0f}' fill='#7dd3fc' font-size='13' text-anchor='middle'>{r}</text>"
        for j in range(4):
            xx, yy = x0 + cw * j, y0 + ch * i
            s += f"<rect x='{xx}' y='{yy}' width='{cw}' height='{ch}' fill='none' stroke='#334155' stroke-width='1.3'/>"
            v = vals[i][j]
            col = '#4ade80' if v else '#64748b'
            s += f"<text x='{xx+cw/2:.0f}' y='{yy+ch/2+6:.0f}' fill='{col}' font-size='17' font-weight='700' text-anchor='middle'>{v}</text>"
    # grupo B·C·D' : filas 01,11 (idx1,2) col 10 (idx3)
    s += f"<rect x='{x0+cw*3-5}' y='{y0+ch-4}' width='{cw+10}' height='{2*ch+8}' rx='9' fill='none' stroke='#a78bfa' stroke-width='2.2'/>"
    s += f"<text x='{x0+cw*3+cw+2}' y='{y0+ch+ch/2+5:.0f}' fill='#c4b5fd' font-size='12'>B·C·D&#773;</text>"
    # grupo A·C·D' : filas 11,10 (idx2,3) col 10 (idx3)
    s += f"<rect x='{x0+cw*3-9}' y='{y0+2*ch-8}' width='{cw+18}' height='{2*ch+16}' rx='12' fill='none' stroke='#f59e0b' stroke-width='2.2' stroke-dasharray='5 3'/>"
    s += f"<text x='{x0+cw*3+cw+2}' y='{y0+3*ch+ch/2+5:.0f}' fill='#fbbf24' font-size='12'>A·C·D&#773;</text>"
    s += "</svg>"
    return s

def fig_circ_q1():
    """Q1.4 · S = (A+B)·C·D'."""
    s = ("<svg viewBox='0 0 500 260' width='100%' style='max-width:470px;height:auto' "
         "fill='none' font-family='Inter,system-ui,sans-serif' stroke='#e2e8f0' stroke-width='1.8'>")
    s += "<text x='16' y='55' fill='#e2e8f0' font-size='14'>A</text><text x='16' y='95' fill='#e2e8f0' font-size='14'>B</text>"
    s += "<text x='16' y='150' fill='#e2e8f0' font-size='14'>C</text><text x='16' y='215' fill='#e2e8f0' font-size='14'>D</text>"
    # OR(A,B)
    s += "<line x1='30' y1='50' x2='120' y2='50'/><line x1='30' y1='90' x2='120' y2='90'/>"
    s += "<path d='M112 34 Q150 34 190 70 Q150 106 112 106 Q132 70 112 34 Z' fill='none' stroke='#34d399' stroke-width='2.2'/>"
    s += "<line x1='190' y1='70' x2='300' y2='70'/><line x1='300' y1='70' x2='300' y2='96'/>"
    # NOT D -> D'
    s += "<line x1='30' y1='210' x2='90' y2='210'/>"
    s += "<polygon points='90,196 90,224 118,210' fill='none' stroke='#a78bfa' stroke-width='2'/><circle cx='123' cy='210' r='4' fill='none' stroke='#a78bfa' stroke-width='2'/>"
    s += "<text x='130' y='202' fill='#c4b5fd' font-size='12'>D&#773;</text>"
    # AND de 3 entradas: (A+B), C, D'
    s += "<line x1='30' y1='150' x2='300' y2='150'/>"
    s += "<line x1='128' y1='210' x2='300' y2='210'/><line x1='300' y1='210' x2='300' y2='204'/>"
    s += "<path d='M300 60 L340 60 A50 50 0 0 1 340 200 L300 200 Z' fill='none' stroke='#38bdf8' stroke-width='2.4'/>"
    s += "<line x1='300' y1='96' x2='300' y2='96'/>"
    s += "<line x1='390' y1='130' x2='460' y2='130'/><text x='466' y='135' fill='#e2e8f0' font-size='15'>S</text>"
    s += "</svg>"
    return s

TV_Q1 = "<table class='dat'><tr><th>A</th><th>B</th><th>C</th><th>D</th><th>S</th></tr>"
_S = {6, 10, 14}
for i in range(16):
    A, B, C, D = (i >> 3) & 1, (i >> 2) & 1, (i >> 1) & 1, i & 1
    v = 1 if i in _S else 0
    bg = " style='background:rgba(74,222,128,.14)'" if v else ""
    TV_Q1 += f"<tr{bg}><td>{A}</td><td>{B}</td><td>{C}</td><td>{D}</td><td>{v}</td></tr>"
TV_Q1 += "</table>"

# ---------------- CONTENIDO ----------------

data = {
 "meta": {
  "titulo": "Tecnología e Ingeniería II",
  "subtitulo": "Prueba de Acceso a la Universidad (PAU) · Universidad de Extremadura · Curso 2025-2026 · Examen resuelto y comentado",
  "cabecera_titulo": "PAU 2026 · <span>Tecnología e Ingeniería II</span> · Extremadura · Ordinaria",
  "pill": "90 min · 4 preguntas · 2,5 pt/pregunta",
  "enunciado_pdf": "../../examens/Extremadura/Tecnologia_Extremadura_2026_ordinaria.pdf",
  "pdf_dir": "pdf_ext_2026_ordinaria",
  "footer": "Dpto. Tecnología · Solucionario PAU 2026 · Extremadura · Tecnología e Ingeniería II (Ordinaria)",
  "intro_inicio": "El examen consta de <b>4 preguntas obligatorias</b> de 2,5 puntos. La primera es de opción única; en las otras tres se elige <b>una de las dos</b> cuestiones. Aquí se resuelven <b>todas</b> para repasar. Selecciona un apartado o una pregunta en la barra lateral.",
  "indice_nombre": "Exámenes de Extremadura",
  "indice_url": "index.html"
 },
 "bloques": [
  {
   "id": "b1", "titulo": "Pregunta 1 · Sistemas eléctricos y electrónicos", "color": "#f59e0b",
   "descripcion_tarjeta": "Control lógico del mecanismo de apertura de una máquina dispensadora de libros.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#f59e0b' stroke-width='3'><rect x='20' y='12' width='50' height='40'/><path d='M30 12v40M30 22h40'/></svg>",
   "cuestiones": [
    {
     "id": "q1", "titulo": "Pregunta 1 · Dispensadora de libros (lógica)", "etiqueta": "SISTEMAS ELÉCTRICOS",
     "menu": "P1 · Dispensadora (lógica)", "titulo_corto": "P1",
     "meta": "Pregunta única y obligatoria · 2,5 puntos (a: 1,0 · b: 0,5 · c: 0,5 · d: 0,5)",
     "enunciado_html": "<p>Una máquina dispensadora entrega un libro según las opciones A (novela) y B (ciencia); con ambas pulsadas entrega historia. Además hay dos sensores: C (acceso validado) y D (no hay libros disponibles). El mecanismo abre la compuerta si se cumplen las condiciones de suministro. Se pide:</p><ol type='a'><li>Elaborar la tabla de verdad. <span class='pts'>(1 punto)</span></li><li>Función lógica en primera forma canónica. <span class='pts'>(0,5 puntos)</span></li><li>Simplificar por Karnaugh. <span class='pts'>(0,5 puntos)</span></li><li>Representar el circuito lógico. <span class='pts'>(0,5 puntos)</span></li></ol>",
     "figura_enunciado_svg": "",
     "aplica_html": "<p>La compuerta debe abrirse (S=1) si se solicita algún libro (<b>A o B</b> pulsados), el acceso está validado (<b>C=1</b>) y <b>hay</b> libros disponibles (D=0, es decir \\(\\bar D\\)). Traducimos a lógica, obtenemos la canónica y simplificamos con Karnaugh.</p>",
     "solucion_html": "<h5>a) Tabla de verdad</h5><p>S=1 cuando (A+B)=1, C=1 y D=0; es decir en los minterms 6, 10 y 14:</p>" + TV_Q1 + "<h5>b) Primera forma canónica</h5><div class='formula'>$$S=\\bar A B C\\bar D+A\\bar B C\\bar D+ABC\\bar D$$</div><h5>c) Simplificación por Karnaugh</h5><figure class='fig'>" + fig_kmap4_q1() + "<figcaption>Grupos B&#183;C&#183;D&#773; (violeta) y A&#183;C&#183;D&#773; (naranja).</figcaption></figure><div class='formula'>$$S=BC\\bar D+AC\\bar D=(A+B)\\,C\\,\\bar D$$</div><div class='res'><b>S = (A + B) · C · D&#773;</b></div><h5>d) Circuito lógico</h5><figure class='fig'>" + fig_circ_q1() + "<figcaption>Una OR (A+B), un inversor para D&#773; y una AND de tres entradas.</figcaption></figure>"
    }
   ]
  },
  {
   "id": "b2", "titulo": "Pregunta 2 · Materiales y fabricación", "color": "#22d3ee",
   "descripcion_tarjeta": "Opción A: ensayo Brinell (cálculo inverso de la carga). Opción B: ensayo Charpy (energías).",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#22d3ee' stroke-width='3'><circle cx='45' cy='26' r='11'/><path d='M45 4v11'/></svg>",
   "cuestiones": [
    {
     "id": "q2a", "titulo": "Pregunta 2.1 (Opción A) · Ensayo de dureza Brinell", "etiqueta": "OPCIÓN A",
     "menu": "P2.1 (A) · Dureza Brinell", "titulo_corto": "P2.1",
     "meta": "2,5 puntos (a: 1,25 · b: 1,25)",
     "enunciado_html": "<p>Un material presenta 50 HB. Se pide:</p><ol type='a'><li>La carga aplicada si el penetrador es una bola de 5 mm y la huella tiene 1,2 mm de diámetro. <span class='pts'>(1,25 puntos)</span></li><li>La constante del ensayo del material. <span class='pts'>(1,25 puntos)</span></li></ol>",
     "figura_enunciado_svg": "",
     "aplica_html": "<p>De \\(\\mathrm{HB}=\\frac{2F}{\\pi D(D-\\sqrt{D^2-d^2})}\\) despejamos la carga \\(F\\). La constante del ensayo es \\(K=\\frac{F}{D^2}\\).</p>",
     "solucion_html": "<h5>a) Carga aplicada</h5><div class='formula'>$$\\sqrt{D^2-d^2}=\\sqrt{25-1{,}44}=4{,}854\\,\\mathrm{mm}$$</div><div class='formula'>$$F=\\frac{\\mathrm{HB}\\cdot\\pi D(D-\\sqrt{D^2-d^2})}{2}=\\frac{50\\cdot\\pi\\cdot 5\\,(5-4{,}854)}{2}=57{,}3\\,\\mathrm{kp}$$</div><div class='res'><b>F &asymp; 57,3 kp</b></div><h5>b) Constante del ensayo</h5><div class='formula'>$$K=\\frac{F}{D^2}=\\frac{57{,}3}{25}=2{,}29\\approx 2{,}5$$</div><p>Corresponde a la constante normalizada \\(K=2{,}5\\), propia de materiales blandos.</p><div class='res'><b>K &asymp; 2,3 (constante normalizada 2,5)</b></div>"
    },
    {
     "id": "q2b", "titulo": "Pregunta 2.2 (Opción B) · Ensayo Charpy", "etiqueta": "OPCIÓN B",
     "menu": "P2.2 (B) · Ensayo Charpy", "titulo_corto": "P2.2",
     "meta": "2,5 puntos (a: 1,25 · b: 1,25)",
     "enunciado_html": "<p>En un ensayo Charpy (probeta cuadrada de 10 mm de lado, entalla en V de 2 mm) la energía absorbida en la rotura fue 180 J, con un martillo de 30 kg que cae desde 102 cm. Se pide:</p><ol type='a'><li>La energía almacenada por el martillo antes de la caída. <span class='pts'>(1,25 puntos)</span></li><li>La altura a la que se elevará el martillo tras romper la probeta. <span class='pts'>(1,25 puntos)</span></li></ol>",
     "figura_enunciado_svg": "",
     "aplica_html": "<p>La energía potencial del martillo es \\(E=m\\,g\\,h\\). La energía tras el golpe es la inicial menos la absorbida por la probeta; de ahí se obtiene la altura de elevación \\(h'=\\frac{E'}{m\\,g}\\).</p>",
     "solucion_html": "<p>Datos: \\(m=30\\,\\mathrm{kg}\\), \\(h_1=1{,}02\\,\\mathrm{m}\\), \\(E_{abs}=180\\,\\mathrm{J}\\).</p><h5>a) Energía antes de la caída</h5><div class='formula'>$$E_1=m\\,g\\,h_1=30\\cdot 9{,}81\\cdot 1{,}02=300{,}2\\,\\mathrm{J}$$</div><div class='res'><b>E<sub>1</sub> &asymp; 300,2 J</b></div><h5>b) Altura de elevación tras la rotura</h5><div class='formula'>$$E_2=E_1-E_{abs}=300{,}2-180=120{,}2\\,\\mathrm{J}$$</div><div class='formula'>$$h_2=\\frac{E_2}{m\\,g}=\\frac{120{,}2}{30\\cdot 9{,}81}=0{,}408\\,\\mathrm{m}$$</div><div class='res'><b>h<sub>2</sub> &asymp; 0,41 m (40,8 cm)</b></div>"
    }
   ]
  },
  {
   "id": "b3", "titulo": "Pregunta 3 · Sistemas mecánicos", "color": "#a78bfa",
   "descripcion_tarjeta": "Opción A: viga con carga puntual descentrada. Opción B: bomba de calor de Carnot.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#a78bfa' stroke-width='3'><path d='M10 34h70'/><path d='M34 34v-16'/><path d='M10 34l-6 12h12z'/></svg>",
   "cuestiones": [
    {
     "id": "q3a", "titulo": "Pregunta 3.1 (Opción A) · Viga con carga puntual descentrada", "etiqueta": "OPCIÓN A",
     "menu": "P3.1 (A) · Viga (carga descentrada)", "titulo_corto": "P3.1",
     "meta": "2,5 puntos (a: 1,25 · b: 1,25)",
     "enunciado_html": "<p>La viga simplemente apoyada de la figura soporta una carga puntual descentrada de 12000 N (a 1,5 m de A, luz total 6 m). Se pide:</p><ol type='a'><li>Ecuaciones de esfuerzos cortantes y momentos flectores. <span class='pts'>(1,25 puntos)</span></li><li>Dibujar los diagramas correspondientes. <span class='pts'>(1,25 puntos)</span></li></ol>",
     "figura_enunciado_svg": "<figure class='fig'>" + fig_viga7() + "<figcaption>Viga biapoyada de 6 m con carga puntual de 12000 N situada a 1,5 m del apoyo A.</figcaption></figure>",
     "aplica_html": "<p>Se calculan las reacciones con \\(\\sum M=0\\) y \\(\\sum F_y=0\\). El cortante es constante a tramos y el momento flector es máximo bajo la carga.</p>",
     "solucion_html": "<h5>Reacciones</h5><div class='formula'>$$\\sum M_A=0:\\;R_B\\cdot 6=12000\\cdot 1{,}5\\Rightarrow R_B=3000\\,\\mathrm{N}$$</div><div class='formula'>$$R_A=12000-3000=9000\\,\\mathrm{N}$$</div><div class='res'><b>R<sub>A</sub> = 9000 N &nbsp;·&nbsp; R<sub>B</sub> = 3000 N</b></div><h5>a) Ecuaciones (origen en A)</h5><p>Tramo AC \\((0\\le x\\le 1{,}5)\\): \\(V=9000\\,\\mathrm{N}\\), \\(M=9000\\,x\\).</p><p>Tramo CB \\((1{,}5\\le x\\le 6)\\): \\(V=-3000\\,\\mathrm{N}\\), \\(M=-3000\\,x+18000\\).</p><h5>Valores máximos</h5><div class='formula'>$$V_{max}=9000\\,\\mathrm{N}\\qquad M_{max}=9000\\cdot 1{,}5=13500\\,\\mathrm{N\\cdot m}$$</div><div class='res'><b>V<sub>máx</sub> = 9000 N &nbsp;·&nbsp; M<sub>máx</sub> = 13500 N&middot;m (bajo la carga)</b></div><h5>b) Diagramas</h5><figure class='fig'>" + fig_esfuerzos7() + "<figcaption>Cortante escalonado (+9000 / &minus;3000 N) y momento flector triangular (máx. 13500 N&middot;m).</figcaption></figure>"
    },
    {
     "id": "q3b", "titulo": "Pregunta 3.2 (Opción B) · Bomba de calor de Carnot", "etiqueta": "OPCIÓN B",
     "menu": "P3.2 (B) · Bomba de calor", "titulo_corto": "P3.2",
     "meta": "2,5 puntos (a: 1,0 · b: 0,75 · c: 0,75)",
     "enunciado_html": "<p>Una bomba de calor funciona según el ciclo de Carnot entre 22 &deg;C y 5 &deg;C. La energía suministrada a la máquina es de 0,8 kWh. Calcula:</p><ol type='a'><li>Eficacia del ciclo. <span class='pts'>(1 punto)</span></li><li>Calorías aportadas al foco caliente. <span class='pts'>(0,75 puntos)</span></li><li>Calorías aportadas por el foco frío. <span class='pts'>(0,75 puntos)</span></li></ol>",
     "figura_enunciado_svg": "",
     "aplica_html": "<p>Eficacia (COP calefacción) \\(=\\frac{T_c}{T_c-T_f}\\) (K). El calor cedido al foco caliente es \\(Q_c=\\mathrm{COP}\\cdot W\\) y el aportado por el foco frío \\(Q_f=Q_c-W\\). Se convierte a calorías con \\(1\\,\\mathrm{cal}=4{,}186\\,\\mathrm{J}\\).</p>",
     "solucion_html": "<p>Datos: \\(T_c=295\\,\\mathrm{K}\\), \\(T_f=278\\,\\mathrm{K}\\), \\(W=0{,}8\\,\\mathrm{kWh}=2{,}88\\cdot10^6\\,\\mathrm{J}\\).</p><h5>a) Eficacia del ciclo</h5><div class='formula'>$$\\mathrm{COP}=\\frac{T_c}{T_c-T_f}=\\frac{295}{295-278}=\\frac{295}{17}=17{,}35$$</div><div class='res'><b>COP &asymp; 17,35</b></div><h5>b) Calor aportado al foco caliente</h5><div class='formula'>$$Q_c=\\mathrm{COP}\\cdot W=17{,}35\\cdot 2{,}88\\cdot10^6=5{,}00\\cdot10^7\\,\\mathrm{J}$$</div><div class='formula'>$$Q_c=\\frac{5{,}00\\cdot10^7}{4{,}186}=1{,}19\\cdot10^7\\,\\mathrm{cal}\\approx11\\,940\\,\\mathrm{kcal}$$</div><div class='res'><b>Q<sub>c</sub> &asymp; 1,19·10<sup>7</sup> cal (&asymp; 11 940 kcal)</b></div><h5>c) Calor aportado por el foco frío</h5><div class='formula'>$$Q_f=Q_c-W=5{,}00\\cdot10^7-2{,}88\\cdot10^6=4{,}71\\cdot10^7\\,\\mathrm{J}$$</div><div class='formula'>$$Q_f=\\frac{4{,}71\\cdot10^7}{4{,}186}=1{,}13\\cdot10^7\\,\\mathrm{cal}\\approx11\\,250\\,\\mathrm{kcal}$$</div><div class='res'><b>Q<sub>f</sub> &asymp; 1,13·10<sup>7</sup> cal (&asymp; 11 250 kcal)</b></div>"
    }
   ]
  },
  {
   "id": "b4", "titulo": "Pregunta 4 · Sistemas automáticos", "color": "#34d399",
   "descripcion_tarjeta": "Opción A y B: reducción de diagramas de bloques hasta la función de transferencia.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#34d399' stroke-width='3'><rect x='12' y='22' width='20' height='16'/><rect x='52' y='22' width='20' height='16'/><path d='M32 30h20'/></svg>",
   "cuestiones": [
    {
     "id": "q4a", "titulo": "Pregunta 4.1 (Opción A) · Función de transferencia", "etiqueta": "OPCIÓN A",
     "menu": "P4.1 (A) · Diagrama de bloques", "titulo_corto": "P4.1",
     "meta": "2,5 puntos",
     "enunciado_html": "<p>Dado el diagrama de bloques de la figura, obtén la función de transferencia. <span class='pts'>(2,5 puntos)</span></p>",
     "figura_enunciado_svg": "<figure class='fig'>" + fig_bloq71() + "<figcaption>Camino directo con una rama que puentea P<sub>2</sub> (paralelo 1 + P<sub>2</sub>) y realimentación P<sub>3</sub>·P<sub>4</sub> negativa.</figcaption></figure>",
     "aplica_html": "<p>La señal tras P<sub>1</sub> llega a la salida por dos caminos que se suman: uno directo y otro a través de P<sub>2</sub> (equivalen a \\(1+P_2\\)). El lazo se cierra negativamente por P<sub>3</sub>·P<sub>4</sub>.</p>",
     "solucion_html": "<h5>Rama en paralelo (bypass de P<sub>2</sub>)</h5><p>La señal a la salida de P<sub>1</sub> se suma consigo misma a través de P<sub>2</sub>: equivale a \\((1+P_2)\\). El camino directo es \\(P_1(1+P_2)P_5\\).</p><h5>Lazo de realimentación</h5><p>Realimentación negativa \\(P_3P_4\\) sobre todo el camino directo:</p><div class='formula'>$$\\boxed{\\dfrac{Z}{X}=\\dfrac{P_1P_5(1+P_2)}{1+P_1P_3P_4P_5(1+P_2)}}$$</div><div class='res'><b>Z/X = P<sub>1</sub>P<sub>5</sub>(1 + P<sub>2</sub>) / [1 + P<sub>1</sub>P<sub>3</sub>P<sub>4</sub>P<sub>5</sub>(1 + P<sub>2</sub>)]</b></div>"
    },
    {
     "id": "q4b", "titulo": "Pregunta 4.2 (Opción B) · Reducción de un sistema de control", "etiqueta": "OPCIÓN B",
     "menu": "P4.2 (B) · Sistema de control", "titulo_corto": "P4.2",
     "meta": "2,5 puntos",
     "enunciado_html": "<p>Simplifica el siguiente sistema de control hasta conseguir la función de transferencia. <span class='pts'>(2,5 puntos)</span></p>",
     "figura_enunciado_svg": "<figure class='fig'>" + fig_bloq72() + "<figcaption>Dos ramas en paralelo (P<sub>1</sub> y P<sub>2</sub>·P<sub>3</sub>) que se restan, seguidas de P<sub>4</sub>, con realimentación P<sub>5</sub> negativa.</figcaption></figure>",
     "aplica_html": "<p>Las ramas P<sub>1</sub> y P<sub>2</sub>P<sub>3</sub> parten del mismo punto y se combinan en el comparador (una con signo +, otra con &minus;): equivalen a \\((P_1-P_2P_3)\\). Después va P<sub>4</sub> y el lazo se cierra con P<sub>5</sub> negativo.</p>",
     "solucion_html": "<h5>Ramas en paralelo</h5><p>La señal tras el primer comparador se bifurca por P<sub>1</sub> (+) y por P<sub>2</sub>P<sub>3</sub> (&minus;): equivale a \\((P_1-P_2P_3)\\).</p><h5>Lazo con P<sub>5</sub> (negativo) y P<sub>4</sub> a la salida</h5><div class='formula'>$$N=\\frac{P_1-P_2P_3}{1+P_5(P_1-P_2P_3)}\\,X\\qquad Z=P_4\\,N$$</div><div class='formula'>$$\\boxed{\\dfrac{Z}{X}=\\dfrac{P_4\\,(P_1-P_2P_3)}{1+P_5(P_1-P_2P_3)}}$$</div><div class='res'><b>Z/X = P<sub>4</sub>(P<sub>1</sub> − P<sub>2</sub>P<sub>3</sub>) / [1 + P<sub>5</sub>(P<sub>1</sub> − P<sub>2</sub>P<sub>3</sub>)]</b></div>"
    }
   ]
  }
 ]
}

out = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ext_2026_ordinaria.json"))
with open(out, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print("JSON escrito:", out)
