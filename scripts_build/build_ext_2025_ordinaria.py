#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera el JSON del examen Extremadura PAU 2025 (ordinaria) para pau-dashboard."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import svg_open, box, summer, arrow, line, txt

# ---------------- FIGURAS ENUNCIADO ----------------

def fig_bloq41():
    s = svg_open('900 380', 820)
    ym = 180
    s += arrow(70, ym, 94, ym)
    s += summer(110, ym)
    s += arrow(126, ym, 184, ym)
    s += summer(200, ym)
    s += arrow(216, ym, 274, ym)
    s += summer(290, ym)
    s += arrow(306, ym, 350, ym)
    s += box(350, ym-22, 82, 44, 'G1', '#22d3ee')
    s += arrow(432, ym, 510, ym)
    s += box(510, ym-22, 82, 44, 'G2', '#22d3ee')
    s += arrow(592, ym, 760, ym)
    s += txt(40, ym+5, 'U', '#e2e8f0', 16); s += txt(772, ym+5, 'V', '#e2e8f0', 16)
    for nx in (470, 640):
        s += f"<circle cx='{nx}' cy='{ym}' r='3.2' fill='#cbd5e1' stroke='none'/>"
    # signos
    s += txt(92, ym-14, '+', '#4ade80', 14); s += txt(96, ym+26, '−', '#fb7185', 16)
    s += txt(182, ym-14, '−', '#fb7185', 16); s += txt(186, ym+26, '+', '#4ade80', 14)
    s += txt(272, ym-14, '+', '#4ade80', 14); s += txt(276, ym+26, '+', '#4ade80', 14)
    # H1 (realim. positiva de G1 hacia sum3)
    s += box(350, 278, 82, 40, 'H1', '#a78bfa')
    s += line(470, ym, 470, 298); s += line(470, 298, 432, 298)
    s += line(350, 298, 290, 298); s += arrow(290, 298, 290, ym+18)
    # realim. superior unitaria (- a sum2) desde la salida
    s += line(640, ym, 640, 90); s += line(640, 90, 200, 90); s += arrow(200, 90, 200, ym-18)
    # realim. inferior unitaria (- a sum1) desde la salida
    s += line(640, ym, 640, 348); s += line(640, 348, 110, 348); s += arrow(110, 348, 110, ym+18)
    s += "</svg>"
    return s

def fig_bloq42():
    s = svg_open('900 360', 820)
    ym = 185
    s += arrow(70, ym, 94, ym)
    s += summer(110, ym)
    s += arrow(126, ym, 170, ym)
    s += box(170, ym-22, 80, 44, 'G1', '#22d3ee')
    s += arrow(250, ym, 292, ym)
    s += box(292, ym-22, 80, 44, 'G2', '#22d3ee')
    s += arrow(372, ym, 470, ym)
    s += f"<circle cx='412' cy='{ym}' r='3.2' fill='#cbd5e1' stroke='none'/>"
    # rama G3 (principal) y G4 (superior)
    s += box(470, ym-22, 80, 44, 'G3', '#22d3ee')
    s += arrow(550, ym, 632, ym)
    s += box(470, 78, 80, 44, 'G4', '#22d3ee')
    s += line(412, ym, 412, 100); s += arrow(412, 100, 470, 100)
    s += line(550, 100, 632, 100); s += arrow(632, 100, 648, ym-18)
    s += summer(650, ym)
    s += arrow(666, ym, 760, ym)
    s += txt(40, ym+5, 'U', '#e2e8f0', 16); s += txt(772, ym+5, 'V', '#e2e8f0', 16)
    s += txt(92, ym-14, '+', '#4ade80', 14); s += txt(96, ym+26, '+', '#4ade80', 14)
    s += txt(632, ym-14, '+', '#4ade80', 14); s += txt(636, ym+26, '+', '#4ade80', 14)
    # H1 realim. positiva
    s += box(250, 272, 82, 40, 'H1', '#a78bfa')
    s += line(412, ym, 412, 292); s += line(412, 292, 332, 292)
    s += line(250, 292, 110, 292); s += arrow(110, 292, 110, ym+18)
    s += "</svg>"
    return s

def fig_viga_dist():
    """Q3.1 viga 8 m con carga distribuida en toda la luz."""
    x0, x1 = 95, 545
    yb = 150
    s = ("<svg viewBox='0 0 620 290' width='100%' style='max-width:560px;height:auto' "
         "fill='none' font-family='Inter,system-ui,sans-serif'>")
    s += f"<text x='{(x0+x1)//2}' y='38' fill='#e2e8f0' font-size='16' text-anchor='middle'>Q = 200 N/m</text>"
    s += f"<line x1='{x0}' y1='52' x2='{x1}' y2='52' stroke='#f59e0b' stroke-width='2'/>"
    n = 10
    for i in range(n + 1):
        xa = x0 + (x1 - x0) * i / n
        s += f"<line x1='{xa:.0f}' y1='52' x2='{xa:.0f}' y2='{yb-2}' stroke='#f59e0b' stroke-width='1.5'/>"
        s += f"<polygon points='{xa-4:.0f},{yb-10} {xa+4:.0f},{yb-10} {xa:.0f},{yb-1}' fill='#f59e0b'/>"
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
    yc = yb + 78
    s += f"<line x1='{x0}' y1='{yc}' x2='{x1}' y2='{yc}' stroke='#94a3b8' stroke-width='1.4'/>"
    s += f"<polygon points='{x0},{yc} {x0+11},{yc-5} {x0+11},{yc+5}' fill='#94a3b8'/>"
    s += f"<polygon points='{x1},{yc} {x1-11},{yc-5} {x1-11},{yc+5}' fill='#94a3b8'/>"
    s += f"<text x='{(x0+x1)//2}' y='{yc-9}' fill='#cbd5e1' font-size='14' text-anchor='middle'>8 m</text>"
    s += "</svg>"
    return s

# ---------------- FIGURAS SOLUCION ----------------

def fig_esfuerzos_dist():
    """Q3.1 cortante triangular y flector parabolico (carga distribuida completa)."""
    x0, x1 = 70, 520
    s = ("<svg viewBox='0 0 560 300' width='100%' style='max-width:520px;height:auto' "
         "fill='none' font-family='Inter,system-ui,sans-serif'>")
    yc = 70
    s += f"<line x1='{x0-5}' y1='{yc}' x2='{x1+10}' y2='{yc}' stroke='#94a3b8' stroke-width='1.4'/>"
    s += f"<text x='{x0-5}' y='{yc-42}' fill='#e2e8f0' font-size='13'>V (N)</text>"
    xm = (x0 + x1) / 2
    s += f"<polygon points='{x0},{yc} {x0},{yc-36} {x1},{yc+36} {x1},{yc}' fill='rgba(56,189,248,.16)' stroke='none'/>"
    s += f"<line x1='{x0}' y1='{yc-36}' x2='{x1}' y2='{yc+36}' stroke='#38bdf8' stroke-width='2.4'/>"
    s += f"<line x1='{x0}' y1='{yc}' x2='{x0}' y2='{yc-36}' stroke='#38bdf8' stroke-width='2.4'/>"
    s += f"<line x1='{x1}' y1='{yc+36}' x2='{x1}' y2='{yc}' stroke='#38bdf8' stroke-width='2.4'/>"
    s += f"<text x='{x0+8}' y='{yc-30}' fill='#7dd3fc' font-size='12'>+800</text>"
    s += f"<text x='{x1-8}' y='{yc+48}' fill='#7dd3fc' font-size='12' text-anchor='end'>-800</text>"
    s += f"<text x='{xm:.0f}' y='{yc+14}' fill='#94a3b8' font-size='11' text-anchor='middle'>x=4 m</text>"
    yf = 240
    s += f"<line x1='{x0-5}' y1='{yf}' x2='{x1+10}' y2='{yf}' stroke='#94a3b8' stroke-width='1.4'/>"
    s += f"<text x='{x0-5}' y='{yf-92}' fill='#e2e8f0' font-size='13'>M (N·m)</text>"
    pts = []
    for k in range(0, 81):
        xx = k / 10.0
        M = 800 * xx - 100 * xx * xx
        px = x0 + (xx / 8) * (x1 - x0)
        py = yf - (M / 1600) * 80
        pts.append(f"{px:.1f},{py:.1f}")
    s += f"<polygon points='{x0},{yf} " + " ".join(pts) + f" {x1},{yf}' fill='rgba(74,222,128,.18)' stroke='none'/>"
    s += f"<polyline points='" + " ".join(pts) + f"' fill='none' stroke='#4ade80' stroke-width='2.4'/>"
    s += f"<line x1='{xm:.0f}' y1='{yf}' x2='{xm:.0f}' y2='{yf-80}' stroke='#4ade80' stroke-width='1' stroke-dasharray='4 3'/>"
    s += f"<text x='{xm:.0f}' y='{yf-86}' fill='#86efac' font-size='12' text-anchor='middle'>1600</text>"
    s += f"<text x='{x0}' y='{yf+18}' fill='#94a3b8' font-size='12' text-anchor='middle'>A</text>"
    s += f"<text x='{x1}' y='{yf+18}' fill='#94a3b8' font-size='12' text-anchor='middle'>B</text>"
    s += "</svg>"
    return s

def fig_kmap4():
    """Q1 · mapa de Karnaugh 4 variables (AB filas, CD columnas)."""
    x0, y0, cw, ch = 150, 72, 58, 44
    rows = ['00', '01', '11', '10']
    cols = ['00', '01', '11', '10']
    vals = [[0, 0, 0, 0], [1, 1, 0, 0], [1, 1, 1, 1], [1, 1, 0, 0]]
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
    # grupo A·C' : filas 11,10 (idx2,3) x cols 00,01 (idx0,1)
    s += f"<rect x='{x0-4}' y='{y0+2*ch-4}' width='{2*cw+8}' height='{2*ch+8}' rx='9' fill='none' stroke='#f59e0b' stroke-width='2.2'/>"
    s += f"<text x='{x0+cw-4}' y='{y0+4*ch+18}' fill='#fbbf24' font-size='13' text-anchor='middle'>A&#183;C&#773;</text>"
    # grupo A·B : fila 11 (idx2) x todas cols
    s += f"<rect x='{x0-8}' y='{y0+2*ch-8}' width='{4*cw+16}' height='{ch+16}' rx='11' fill='none' stroke='#a78bfa' stroke-width='2.2'/>"
    s += f"<text x='{x0+4*cw+14}' y='{y0+2*ch+ch/2+5:.0f}' fill='#c4b5fd' font-size='13'>A&#183;B</text>"
    # grupo B·C' : filas 01,11 (idx1,2) x cols 00,01 (idx0,1)
    s += f"<rect x='{x0+2}' y='{y0+ch+2}' width='{2*cw-4}' height='{2*ch-4}' rx='7' fill='none' stroke='#38bdf8' stroke-width='2.2' stroke-dasharray='5 3'/>"
    s += f"<text x='{x0-30}' y='{y0+2*ch+5}' fill='#7dd3fc' font-size='13'>B&#183;C&#773;</text>"
    s += "</svg>"
    return s

def fig_circ_logic():
    """Q1.4 · S = AB + AC' + BC'."""
    s = ("<svg viewBox='0 0 500 300' width='100%' style='max-width:470px;height:auto' "
         "fill='none' font-family='Inter,system-ui,sans-serif' stroke='#e2e8f0' stroke-width='1.8'>")
    def andg(x, y, col, w=42, h=40):
        return f"<path d='M{x} {y} L{x+w-h/2} {y} A{h/2} {h/2} 0 0 1 {x+w-h/2} {y+h} L{x} {y+h} Z' fill='none' stroke='{col}' stroke-width='2.2'/>"
    # entradas
    s += "<text x='16' y='45' fill='#e2e8f0' font-size='14'>A</text><text x='16' y='120' fill='#e2e8f0' font-size='14'>B</text><text x='16' y='210' fill='#e2e8f0' font-size='14'>C</text>"
    # NOT C
    s += "<line x1='30' y1='205' x2='70' y2='205'/>"
    s += "<polygon points='70,192 70,218 96,205' fill='none' stroke='#a78bfa' stroke-width='2'/><circle cx='101' cy='205' r='4' fill='none' stroke='#a78bfa' stroke-width='2'/>"
    s += "<text x='108' y='198' fill='#c4b5fd' font-size='12'>C&#773;</text>"
    # AND1 = A·B
    s += andg(200, 30, '#38bdf8')
    s += "<line x1='30' y1='40' x2='200' y2='40'/><line x1='30' y1='120' x2='120' y2='120'/><line x1='120' y1='120' x2='120' y2='60'/><line x1='120' y1='60' x2='200' y2='60'/>"
    s += "<line x1='242' y1='50' x2='300' y2='50'/>"
    # AND2 = A·C'
    s += andg(200, 110, '#34d399')
    s += "<line x1='50' y1='40' x2='50' y2='130'/><line x1='50' y1='130' x2='200' y2='130'/>"
    s += "<line x1='106' y1='205' x2='150' y2='205'/><line x1='150' y1='205' x2='150' y2='150'/><line x1='150' y1='150' x2='200' y2='150'/>"
    s += "<line x1='242' y1='130' x2='300' y2='130'/>"
    # AND3 = B·C'
    s += andg(200, 200, '#f59e0b')
    s += "<line x1='90' y1='120' x2='90' y2='210'/><line x1='90' y1='210' x2='200' y2='210'/>"
    s += "<line x1='150' y1='205' x2='150' y2='230'/><line x1='150' y1='230' x2='200' y2='230'/>"
    s += "<line x1='242' y1='220' x2='300' y2='220'/>"
    # OR de 3 entradas
    s += "<path d='M300 30 Q350 30 400 135 Q350 240 300 240 Q328 135 300 30 Z' fill='none' stroke='#fb7185' stroke-width='2.2'/>"
    s += "<line x1='300' y1='50' x2='318' y2='50'/><line x1='300' y1='130' x2='312' y2='130'/><line x1='300' y1='220' x2='318' y2='220'/>"
    s += "<line x1='400' y1='135' x2='460' y2='135'/><text x='466' y='140' fill='#e2e8f0' font-size='15'>S</text>"
    s += "</svg>"
    return s

TV4 = "<table class='dat'><tr><th>A</th><th>B</th><th>C</th><th>D</th><th>S</th></tr>"
_S = {4, 5, 8, 9, 12, 13, 14, 15}
for i in range(16):
    A, B, C, D = (i >> 3) & 1, (i >> 2) & 1, (i >> 1) & 1, i & 1
    v = 1 if i in _S else 0
    bg = " style='background:rgba(74,222,128,.14)'" if v else ""
    TV4 += f"<tr{bg}><td>{A}</td><td>{B}</td><td>{C}</td><td>{D}</td><td>{v}</td></tr>"
TV4 += "</table>"

# ---------------- CONTENIDO ----------------

data = {
 "meta": {
  "titulo": "Tecnología e Ingeniería II",
  "subtitulo": "Prueba de Acceso a la Universidad (PAU) · Universidad de Extremadura · Curso 2024-2025 · Examen resuelto y comentado",
  "cabecera_titulo": "PAU 2025 · <span>Tecnología e Ingeniería II</span> · Extremadura · Ordinaria",
  "pill": "90 min · 4 preguntas · 2,5 pt/pregunta",
  "enunciado_pdf": "../../examens/Extremadura/Tecnologia_Extremadura_2025_ordinaria.pdf",
  "pdf_dir": "pdf_ext_2025_ordinaria",
  "footer": "Dpto. Tecnología · Solucionario PAU 2025 · Extremadura · Tecnología e Ingeniería II (Ordinaria)",
  "intro_inicio": "El examen consta de <b>4 preguntas obligatorias</b> de 2,5 puntos. La primera es de opción única; en las otras tres se elige <b>una de las dos</b> cuestiones. Aquí se resuelven <b>todas</b> para repasar. Selecciona un apartado o una pregunta en la barra lateral.",
  "indice_nombre": "Exámenes de Extremadura",
  "indice_url": "index.html"
 },
 "bloques": [
  {
   "id": "b1", "titulo": "Pregunta 1 · Sistemas eléctricos y electrónicos", "color": "#f59e0b",
   "descripcion_tarjeta": "Sistema de alarma de un depósito de gas con cuatro sensores: tabla de verdad, canónica, Karnaugh y circuito.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#f59e0b' stroke-width='3'><path d='M45 12l16 28H29z'/><path d='M45 24v8M45 36v2'/></svg>",
   "cuestiones": [
    {
     "id": "q1", "titulo": "Pregunta 1 · Alarma de un depósito de gas (lógica)", "etiqueta": "SISTEMAS ELÉCTRICOS",
     "menu": "P1 · Alarma (lógica 4 variables)", "titulo_corto": "P1",
     "meta": "Pregunta única y obligatoria · 2,5 puntos (a: 1,0 · b: 0,5 · c: 0,5 · d: 0,5)",
     "enunciado_html": "<p>Un depósito de gas propano tiene cuatro sensores: temperatura (A), presión (B), nivel (C) y peso/masa (D); a valor alto le corresponde &laquo;1&raquo; y a valor bajo &laquo;0&raquo;. La alarma S actúa cuando:</p><ul><li>Alta temperatura, bajo nivel y alto peso.</li><li>Alta temperatura, bajo nivel y bajo peso.</li><li>Alta temperatura, alta presión y alto nivel.</li><li>Baja temperatura, alta presión y bajo nivel.</li></ul><ol type='a'><li>Elaborar la tabla de verdad. <span class='pts'>(1 punto)</span></li><li>Función lógica en primera forma canónica. <span class='pts'>(0,5 puntos)</span></li><li>Simplificar por Karnaugh. <span class='pts'>(0,5 puntos)</span></li><li>Representar el circuito lógico. <span class='pts'>(0,5 puntos)</span></li></ol>",
     "figura_enunciado_svg": "",
     "aplica_html": "<p>Traducimos cada condición a variables (las no citadas son &laquo;don't care&raquo;, cubren ambos valores). La primera forma canónica es la suma de minterms con S=1 y el mapa de Karnaugh de 4 variables permite agrupar y simplificar.</p>",
     "solucion_html": "<h5>a) Tabla de verdad</h5><p>Las dos primeras condiciones se resumen en <b>A alta y C bajo</b> (peso indiferente). S=1 en los minterms 4, 5, 8, 9, 12, 13, 14 y 15:</p>" + TV4 + "<h5>b) Primera forma canónica</h5><div class='formula'>$$S=\\bar ABC\\bar D+\\bar ABC D+A\\bar B\\bar C\\bar D+A\\bar B\\bar CD+AB\\bar C\\bar D+AB\\bar CD+ABC\\bar D+ABCD$$</div><h5>c) Simplificación por Karnaugh</h5><figure class='fig'>" + fig_kmap4() + "<figcaption>Grupos A&#183;C&#773; (naranja), A&#183;B (violeta) y B&#183;C&#773; (azul). La variable D se elimina.</figcaption></figure><div class='formula'>$$S=A\\bar C+AB+B\\bar C$$</div><div class='res'><b>S = A·C&#773; + A·B + B·C&#773;</b></div><h5>d) Circuito lógico</h5><figure class='fig'>" + fig_circ_logic() + "<figcaption>Tres puertas AND (una con C&#773;) y una OR de tres entradas.</figcaption></figure>"
    }
   ]
  },
  {
   "id": "b2", "titulo": "Pregunta 2 · Materiales y fabricación", "color": "#22d3ee",
   "descripcion_tarjeta": "Opción A: dureza Brinell. Opción B: ensayo Charpy y resiliencia.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#22d3ee' stroke-width='3'><circle cx='45' cy='26' r='11'/><path d='M45 4v11'/></svg>",
   "cuestiones": [
    {
     "id": "q2a", "titulo": "Pregunta 2.1 (Opción A) · Dureza Brinell", "etiqueta": "OPCIÓN A",
     "menu": "P2.1 (A) · Dureza Brinell", "titulo_corto": "P2.1",
     "meta": "2,5 puntos (a: 1,25 · b: 1,25)",
     "enunciado_html": "<p>En un ensayo Brinell se usa una bola de 6 mm y constante K = 25, obteniéndose una huella de 1,90 mm. Calcula:</p><ol type='a'><li>Dureza Brinell del material. <span class='pts'>(1,25 puntos)</span></li><li>Profundidad de la huella. <span class='pts'>(1,25 puntos)</span></li></ol>",
     "figura_enunciado_svg": "",
     "aplica_html": "<p>La carga es \\(F=K\\,D^2\\) y \\(\\mathrm{HB}=\\frac{2F}{\\pi D(D-\\sqrt{D^2-d^2})}\\). La profundidad de la huella es \\(h=\\frac{D-\\sqrt{D^2-d^2}}{2}\\).</p>",
     "solucion_html": "<h5>a) Dureza Brinell</h5><div class='formula'>$$F=K D^2=25\\cdot 36=900\\,\\mathrm{kp}$$</div><div class='formula'>$$\\sqrt{D^2-d^2}=\\sqrt{36-1{,}9^2}=5{,}691\\,\\mathrm{mm}$$</div><div class='formula'>$$\\mathrm{HB}=\\frac{2\\cdot 900}{\\pi\\cdot 6\\,(6-5{,}691)}=\\frac{1800}{5{,}828}=308{,}9$$</div><div class='res'><b>HB &asymp; 309 kp/mm²</b></div><h5>b) Profundidad de la huella</h5><div class='formula'>$$h=\\frac{6-5{,}691}{2}=0{,}155\\,\\mathrm{mm}$$</div><div class='res'><b>h &asymp; 0,155 mm</b></div>"
    },
    {
     "id": "q2b", "titulo": "Pregunta 2.2 (Opción B) · Ensayo Charpy y resiliencia", "etiqueta": "OPCIÓN B",
     "menu": "P2.2 (B) · Ensayo Charpy", "titulo_corto": "P2.2",
     "meta": "2,5 puntos (a: 1,25 · b: 1,25)",
     "enunciado_html": "<p>En un ensayo Charpy, una maza de 30 kg cae desde 100 cm y, tras romper una probeta de sección cuadrada de 10 mm de lado y 2 mm de profundidad de entalla, se eleva hasta 60 cm. Calcula:</p><ol type='a'><li>La energía empleada en la rotura. <span class='pts'>(1,25 puntos)</span></li><li>La resiliencia del material. <span class='pts'>(1,25 puntos)</span></li></ol>",
     "figura_enunciado_svg": "",
     "aplica_html": "<p>La energía absorbida es la diferencia de energía potencial de la maza: \\(E=m\\,g\\,(h_1-h_2)\\). La resiliencia es esa energía por unidad de sección resistente (bajo la entalla): \\(\\rho=\\frac{E}{S}\\).</p>",
     "solucion_html": "<h5>a) Energía de rotura</h5><div class='formula'>$$E=m\\,g\\,(h_1-h_2)=30\\cdot 9{,}81\\cdot(1-0{,}6)=117{,}7\\,\\mathrm{J}$$</div><div class='res'><b>E &asymp; 117,7 J</b></div><h5>b) Resiliencia</h5><p>Sección resistente bajo la entalla: \\(S=10\\cdot(10-2)=80\\,\\mathrm{mm^2}=0{,}8\\,\\mathrm{cm^2}\\).</p><div class='formula'>$$\\rho=\\frac{E}{S}=\\frac{117{,}7}{0{,}8}=147{,}1\\,\\mathrm{J/cm^2}$$</div><div class='res'><b>&rho; &asymp; 147,1 J/cm² (&asymp; 1,47 J/mm²)</b></div>"
    }
   ]
  },
  {
   "id": "b3", "titulo": "Pregunta 3 · Sistemas mecánicos", "color": "#a78bfa",
   "descripcion_tarjeta": "Opción A: viga con carga distribuida. Opción B: eficiencia real de un congelador.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#a78bfa' stroke-width='3'><path d='M10 34h70'/><path d='M20 34v-10M34 34v-10M48 34v-10M62 34v-10'/></svg>",
   "cuestiones": [
    {
     "id": "q3a", "titulo": "Pregunta 3.1 (Opción A) · Viga con carga distribuida", "etiqueta": "OPCIÓN A",
     "menu": "P3.1 (A) · Viga distribuida", "titulo_corto": "P3.1",
     "meta": "2,5 puntos (a: 1,25 · b: 1,25)",
     "enunciado_html": "<p>La viga simplemente apoyada de la figura soporta una carga uniformemente distribuida de 200 N/m. Se pide:</p><ol type='a'><li>Ecuaciones de esfuerzos cortantes y momentos flectores. <span class='pts'>(1,25 puntos)</span></li><li>Dibujar los diagramas correspondientes. <span class='pts'>(1,25 puntos)</span></li></ol>",
     "figura_enunciado_svg": "<figure class='fig'>" + fig_viga_dist() + "<figcaption>Viga biapoyada de 8 m con carga uniforme de 200 N/m en toda su longitud.</figcaption></figure>",
     "aplica_html": "<p>Por simetría \\(R_A=R_B=\\frac{qL}{2}\\). El cortante \\(V(x)=R_A-qx\\) varía linealmente y el momento \\(M(x)=R_Ax-\\frac{qx^2}{2}\\) es parabólico, máximo en el centro donde el cortante se anula.</p>",
     "solucion_html": "<p>Datos: \\(q=200\\,\\mathrm{N/m}\\), \\(L=8\\,\\mathrm{m}\\).</p><h5>Reacciones</h5><div class='formula'>$$R_A=R_B=\\frac{qL}{2}=\\frac{200\\cdot 8}{2}=800\\,\\mathrm{N}$$</div><h5>a) Ecuaciones (origen en A)</h5><div class='formula'>$$V(x)=800-200\\,x\\quad(\\mathrm{N})\\qquad M(x)=800\\,x-100\\,x^2\\quad(\\mathrm{N\\cdot m})$$</div><h5>Valores máximos</h5><p>El cortante se anula en \\(x=4\\,\\mathrm{m}\\):</p><div class='formula'>$$V_{max}=800\\,\\mathrm{N}\\;(\\text{en apoyos})\\qquad M_{max}=800\\cdot 4-100\\cdot 4^2=1600\\,\\mathrm{N\\cdot m}$$</div><div class='res'><b>V<sub>máx</sub> = 800 N &nbsp;·&nbsp; M<sub>máx</sub> = 1600 N&middot;m (centro)</b></div><h5>b) Diagramas</h5><figure class='fig'>" + fig_esfuerzos_dist() + "<figcaption>Cortante lineal (de +800 a &minus;800 N) y momento flector parabólico (máx. 1600 N&middot;m).</figcaption></figure>"
    },
    {
     "id": "q3b", "titulo": "Pregunta 3.2 (Opción B) · Eficiencia real de un congelador", "etiqueta": "OPCIÓN B",
     "menu": "P3.2 (B) · Congelador real", "titulo_corto": "P3.2",
     "meta": "2,5 puntos (a: 1,0 · b: 0,75 · c: 0,75)",
     "enunciado_html": "<p>Un congelador se mantiene a &minus;7 &deg;C con aire circundante a 18 &deg;C. La cesión de calor del congelador al fluido es de 27,8 kW y la potencia del ciclo es 8,35 kW. Se pide:</p><ol type='a'><li>El coeficiente de operación (eficiencia real). <span class='pts'>(1 punto)</span></li><li>La eficiencia máxima entre esas temperaturas. <span class='pts'>(0,75 puntos)</span></li><li>El calor entregado al aire durante una hora, en kJ. <span class='pts'>(0,75 puntos)</span></li></ol>",
     "figura_enunciado_svg": "",
     "aplica_html": "<p>Eficiencia real \\(\\mathrm{COP}=\\frac{\\dot Q_f}{\\dot W}\\); eficiencia máxima (Carnot) \\(\\mathrm{COP}_C=\\frac{T_f}{T_c-T_f}\\). El calor cedido al foco caliente es \\(\\dot Q_c=\\dot Q_f+\\dot W\\).</p>",
     "solucion_html": "<p>Datos: \\(\\dot Q_f=27{,}8\\,\\mathrm{kW}\\), \\(\\dot W=8{,}35\\,\\mathrm{kW}\\), \\(T_f=266\\,\\mathrm{K}\\), \\(T_c=291\\,\\mathrm{K}\\).</p><h5>a) Eficiencia real</h5><div class='formula'>$$\\mathrm{COP}=\\frac{\\dot Q_f}{\\dot W}=\\frac{27{,}8}{8{,}35}=3{,}33$$</div><div class='res'><b>COP<sub>real</sub> &asymp; 3,33</b></div><h5>b) Eficiencia máxima (Carnot)</h5><div class='formula'>$$\\mathrm{COP}_C=\\frac{T_f}{T_c-T_f}=\\frac{266}{291-266}=\\frac{266}{25}=10{,}64$$</div><div class='res'><b>COP<sub>máx</sub> &asymp; 10,64</b></div><h5>c) Calor entregado al aire en 1 hora</h5><div class='formula'>$$\\dot Q_c=\\dot Q_f+\\dot W=27{,}8+8{,}35=36{,}15\\,\\mathrm{kW}$$</div><div class='formula'>$$Q_c=36{,}15\\cdot 3600=130\\,140\\,\\mathrm{kJ}$$</div><div class='res'><b>Q<sub>c</sub> &asymp; 130 140 kJ</b></div>"
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
     "figura_enunciado_svg": "<figure class='fig'>" + fig_bloq41() + "<figcaption>Dos comparadores realimentados por la salida (unitarios, negativos) y H<sub>1</sub> en realimentación positiva sobre G<sub>1</sub>.</figcaption></figure>",
     "aplica_html": "<p>Se reduce por lazos. El lazo positivo de \\(G_1\\) con \\(H_1\\) da \\(\\frac{G_1}{1-G_1H_1}\\). Las dos realimentaciones unitarias de la salida se suman en los comparadores; se plantean las ecuaciones y se despeja \\(V/U\\).</p>",
     "solucion_html": "<p>Sea \\(X\\) la señal a la entrada de \\(G_1\\) y \\(V=G_1G_2X\\).</p><h5>Comparadores</h5><p>Primer sumador: \\(U-V\\). Segundo sumador: \\((U-V)-V=U-2V\\). Tercer sumador (con \\(H_1\\) positivo): \\(X=(U-2V)+H_1G_1X\\).</p><div class='formula'>$$X=\\frac{U-2V}{1-G_1H_1}$$</div><h5>Salida</h5><div class='formula'>$$V=G_1G_2X=\\frac{G_1G_2(U-2V)}{1-G_1H_1}$$</div><div class='formula'>$$V(1-G_1H_1)+2G_1G_2V=G_1G_2U$$</div><div class='formula'>$$\\boxed{\\dfrac{V}{U}=\\dfrac{G_1G_2}{1-G_1H_1+2G_1G_2}}$$</div><div class='res'><b>V/U = G<sub>1</sub>G<sub>2</sub> / (1 − G<sub>1</sub>H<sub>1</sub> + 2 G<sub>1</sub>G<sub>2</sub>)</b></div>"
    },
    {
     "id": "q4b", "titulo": "Pregunta 4.2 (Opción B) · Reducción de un sistema de control", "etiqueta": "OPCIÓN B",
     "menu": "P4.2 (B) · Sistema de control", "titulo_corto": "P4.2",
     "meta": "2,5 puntos",
     "enunciado_html": "<p>Simplifica el siguiente sistema de control hasta conseguir la función de transferencia. <span class='pts'>(2,5 puntos)</span></p>",
     "figura_enunciado_svg": "<figure class='fig'>" + fig_bloq42() + "<figcaption>Cadena G<sub>1</sub>G<sub>2</sub> con H<sub>1</sub> en realimentación positiva y dos ramas de salida en paralelo (G<sub>3</sub> y G<sub>4</sub>).</figcaption></figure>",
     "aplica_html": "<p>Los bloques \\(G_3\\) y \\(G_4\\) están en <b>paralelo</b> (mismo origen, se suman): equivalen a \\(G_3+G_4\\). El lazo positivo de \\(G_1G_2\\) con \\(H_1\\) da \\(\\frac{G_1G_2}{1-G_1G_2H_1}\\).</p>",
     "solucion_html": "<h5>Lazo interno (H<sub>1</sub>, positivo)</h5><p>Sea \\(N\\) la señal tras \\(G_2\\): \\(N=G_1G_2(U+H_1N)\\Rightarrow N=\\dfrac{G_1G_2}{1-G_1G_2H_1}\\,U\\).</p><h5>Ramas en paralelo</h5><p>La salida es \\(V=(G_3+G_4)\\,N\\):</p><div class='formula'>$$\\boxed{\\dfrac{V}{U}=\\dfrac{G_1G_2\\,(G_3+G_4)}{1-G_1G_2H_1}}$$</div><div class='res'><b>V/U = G<sub>1</sub>G<sub>2</sub>(G<sub>3</sub> + G<sub>4</sub>) / (1 − G<sub>1</sub>G<sub>2</sub>H<sub>1</sub>)</b></div>"
    }
   ]
  }
 ]
}

out = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ext_2025_ordinaria.json"))
with open(out, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print("JSON escrito:", out)
