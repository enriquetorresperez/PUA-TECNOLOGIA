#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera el JSON del examen Extremadura PAU 2026 (modelo) para pau-dashboard."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# ---------------- FIGURAS ENUNCIADO ----------------

def _nor(x, y, col, w=64, h=58):
    cy = y + h / 2
    r = (f"<path d='M{x} {y} Q{x+w*0.55} {y} {x+w} {cy} Q{x+w*0.55} {y+h} {x} {y+h} "
         f"Q{x+w*0.28} {cy} {x} {y} Z' fill='none' stroke='{col}' stroke-width='2.2'/>")
    r += f"<circle cx='{x+w+6}' cy='{cy}' r='5' fill='none' stroke='{col}' stroke-width='2.2'/>"
    return r

def fig_logic6():
    """Q2.2 · cuatro puertas NOR."""
    s = ("<svg viewBox='0 0 600 340' width='100%' style='max-width:520px;height:auto' "
         "fill='none' font-family='Inter,system-ui,sans-serif' stroke='#e2e8f0' stroke-width='1.8'>")
    # entradas
    s += "<text x='16' y='72' fill='#e2e8f0' font-size='15'>A</text>"
    s += "<text x='16' y='232' fill='#e2e8f0' font-size='15'>B</text>"
    s += "<text x='16' y='300' fill='#e2e8f0' font-size='15'>C</text>"
    # linea A y ramas (dos puntos)
    s += "<line x1='30' y1='67' x2='150' y2='67'/>"
    s += "<circle cx='110' cy='67' r='3.4' fill='#cbd5e1' stroke='none'/>"
    s += "<line x1='110' y1='67' x2='110' y2='97'/><circle cx='110' cy='97' r='3.4' fill='#cbd5e1' stroke='none'/>"
    s += "<line x1='110' y1='67' x2='150' y2='67'/><line x1='110' y1='97' x2='150' y2='97'/>"      # a g1
    s += "<line x1='110' y1='97' x2='110' y2='210'/><line x1='110' y1='210' x2='150' y2='210'/>"    # a g2 top
    # g1 NOR(A,A) = A'
    s += _nor(150, 53, '#38bdf8')
    s += "<line x1='220' y1='82' x2='470' y2='82'/><line x1='470' y1='82' x2='470' y2='135'/>"
    # B a g2
    s += "<line x1='30' y1='227' x2='150' y2='227'/>"
    # g2 NOR(A,B)
    s += _nor(150, 195, '#34d399')
    s += "<line x1='220' y1='224' x2='300' y2='224'/>"
    # g3 NOR(g2, C)
    s += _nor(300, 205, '#a78bfa')
    s += "<line x1='30' y1='293' x2='262' y2='293'/><line x1='262' y1='293' x2='262' y2='262'/><line x1='262' y1='262' x2='300' y2='262'/>"
    s += "<line x1='300' y1='224' x2='300' y2='224'/>"
    s += "<line x1='370' y1='234' x2='470' y2='234'/><line x1='470' y1='234' x2='470' y2='165'/>"
    # g4 NOR(g1,g3) = S
    s += _nor(470, 120, '#f59e0b')
    s += "<line x1='470' y1='135' x2='470' y2='135'/>"
    s += "<line x1='546' y1='149' x2='585' y2='149'/><text x='591' y='154' fill='#e2e8f0' font-size='15'>S</text>"
    s += "</svg>"
    return s

def fig_viga_empotrada():
    """Q4.1 · voladizo empotrado en A con carga en el extremo."""
    x0, x1 = 90, 545
    yb = 130
    s = ("<svg viewBox='0 0 620 260' width='100%' style='max-width:560px;height:auto' "
         "fill='none' font-family='Inter,system-ui,sans-serif'>")
    # muro / empotramiento
    s += f"<line x1='{x0}' y1='{yb-45}' x2='{x0}' y2='{yb+55}' stroke='#e2e8f0' stroke-width='3'/>"
    for i in range(7):
        yy = yb - 42 + i * 15
        s += f"<line x1='{x0}' y1='{yy}' x2='{x0-14}' y2='{yy+12}' stroke='#94a3b8' stroke-width='1.5'/>"
    # viga
    s += f"<rect x='{x0}' y='{yb}' width='{x1-x0}' height='15' rx='2' fill='#1e293b' stroke='#e2e8f0' stroke-width='2'/>"
    s += f"<text x='{x0+16}' y='{yb+38}' fill='#7dd3fc' font-size='15' font-weight='700'>A</text>"
    # carga en el extremo libre
    s += f"<line x1='{x1}' y1='45' x2='{x1}' y2='{yb-2}' stroke='#fb7185' stroke-width='3'/>"
    s += f"<polygon points='{x1-8},{yb-14} {x1+8},{yb-14} {x1},{yb-1}' fill='#fb7185'/>"
    s += f"<text x='{x1}' y='36' fill='#fda4af' font-size='15' font-weight='700' text-anchor='middle'>P = 500 kg</text>"
    # cota 6 m
    yc = yb + 70
    s += f"<line x1='{x0}' y1='{yc}' x2='{x1}' y2='{yc}' stroke='#94a3b8' stroke-width='1.4'/>"
    s += f"<polygon points='{x0},{yc} {x0+11},{yc-5} {x0+11},{yc+5}' fill='#94a3b8'/>"
    s += f"<polygon points='{x1},{yc} {x1-11},{yc-5} {x1-11},{yc+5}' fill='#94a3b8'/>"
    s += f"<text x='{(x0+x1)//2}' y='{yc-9}' fill='#cbd5e1' font-size='14' text-anchor='middle'>6 m</text>"
    s += "</svg>"
    return s

def fig_rc(vlab='220 V / 50 Hz', clab='C = 150 &micro;F', rlab='R = 25 &ohm;'):
    xl, xr, yt, yb = 70, 470, 70, 200
    s = ("<svg viewBox='0 0 540 250' width='100%' style='max-width:470px;height:auto' "
         "fill='none' font-family='Inter,system-ui,sans-serif' stroke='#e2e8f0' stroke-width='2.2'>")
    s += f"<text x='40' y='{yt+5}' fill='#e2e8f0' font-size='15' text-anchor='end'>F</text>"
    s += f"<text x='40' y='125' fill='#e2e8f0' font-size='15' text-anchor='end'>N</text>"
    s += f"<line x1='55' y1='{yt}' x2='{xr}' y2='{yt}'/><line x1='55' y1='120' x2='{xr}' y2='120'/>"
    s += f"<text x='260' y='40' fill='#c4b5fd' font-size='15' font-weight='700' text-anchor='middle'>{vlab}</text>"
    s += f"<circle cx='150' cy='{yt}' r='3.4' fill='#e2e8f0'/><circle cx='{xr}' cy='{yt}' r='3.4' fill='#e2e8f0'/>"
    s += f"<circle cx='150' cy='120' r='3.4' fill='#e2e8f0'/><circle cx='400' cy='120' r='3.4' fill='#e2e8f0'/>"
    s += f"<line x1='150' y1='{yt}' x2='150' y2='{yb-45}'/>"
    s += f"<line x1='130' y1='{yb-45}' x2='170' y2='{yb-45}'/><line x1='130' y1='{yb-30}' x2='170' y2='{yb-30}'/>"
    s += f"<line x1='150' y1='{yb-30}' x2='150' y2='{yb}'/><line x1='150' y1='{yb-45}' x2='150' y2='{yb-60}'/>"
    s += f"<text x='150' y='{yb+28}' fill='#7dd3fc' font-size='14' text-anchor='middle'>{clab}</text>"
    s += f"<line x1='150' y1='{yb}' x2='300' y2='{yb}'/>"
    s += f"<rect x='300' y='{yb-13}' width='70' height='26' fill='none' stroke='#f59e0b' stroke-width='2.2'/>"
    s += f"<line x1='370' y1='{yb}' x2='400' y2='{yb}'/><line x1='400' y1='{yb}' x2='400' y2='120'/>"
    s += f"<text x='335' y='{yb+30}' fill='#fbbf24' font-size='14' text-anchor='middle'>{rlab}</text>"
    s += "</svg>"
    return s

# ---------------- FIGURAS SOLUCION ----------------

def fig_and_ac():
    s = ("<svg viewBox='0 0 320 150' width='100%' style='max-width:300px;height:auto' "
         "fill='none' font-family='Inter,system-ui,sans-serif' stroke='#e2e8f0' stroke-width='2'>")
    s += "<text x='18' y='55' fill='#e2e8f0' font-size='16'>A</text><text x='18' y='108' fill='#e2e8f0' font-size='16'>C</text>"
    s += "<line x1='34' y1='50' x2='120' y2='50'/><line x1='34' y1='103' x2='120' y2='103'/>"
    s += "<path d='M120 34 L165 34 A43 43 0 0 1 165 120 L120 120 Z' fill='none' stroke='#38bdf8' stroke-width='2.4'/>"
    s += "<line x1='208' y1='77' x2='285' y2='77'/><text x='292' y='82' fill='#e2e8f0' font-size='16'>S</text>"
    s += "</svg>"
    return s

def fig_esf_empotrada():
    x0, x1 = 70, 520
    s = ("<svg viewBox='0 0 560 300' width='100%' style='max-width:520px;height:auto' "
         "fill='none' font-family='Inter,system-ui,sans-serif'>")
    yc = 70
    s += f"<line x1='{x0-5}' y1='{yc}' x2='{x1+10}' y2='{yc}' stroke='#94a3b8' stroke-width='1.4'/>"
    s += f"<text x='{x0-5}' y='{yc-42}' fill='#e2e8f0' font-size='13'>V (kg)</text>"
    s += f"<polygon points='{x0},{yc} {x0},{yc-40} {x1},{yc-40} {x1},{yc}' fill='rgba(56,189,248,.18)' stroke='none'/>"
    s += f"<polyline points='{x0},{yc-40} {x1},{yc-40}' fill='none' stroke='#38bdf8' stroke-width='2.4'/>"
    s += f"<line x1='{x0}' y1='{yc}' x2='{x0}' y2='{yc-40}' stroke='#38bdf8' stroke-width='2.4'/>"
    s += f"<line x1='{x1}' y1='{yc}' x2='{x1}' y2='{yc-40}' stroke='#38bdf8' stroke-width='2.4'/>"
    s += f"<text x='{(x0+x1)//2}' y='{yc-46}' fill='#7dd3fc' font-size='12' text-anchor='middle'>+500 kg</text>"
    yf = 240
    s += f"<line x1='{x0-5}' y1='{yf}' x2='{x1+10}' y2='{yf}' stroke='#94a3b8' stroke-width='1.4'/>"
    s += f"<text x='{x0-5}' y='{yf-92}' fill='#e2e8f0' font-size='13'>M (kg·m)</text>"
    # momento: -3000 en A, 0 en extremo (dibujado hacia abajo)
    ym = yf + 80
    s += f"<polygon points='{x0},{yf} {x0},{ym} {x1},{yf}' fill='rgba(251,113,133,.18)' stroke='none'/>"
    s += f"<polyline points='{x0},{ym} {x1},{yf}' fill='none' stroke='#fb7185' stroke-width='2.4'/>"
    s += f"<line x1='{x0}' y1='{yf}' x2='{x0}' y2='{ym}' stroke='#fb7185' stroke-width='2.4'/>"
    s += f"<text x='{x0+8}' y='{ym+14}' fill='#fda4af' font-size='12'>-3000</text>"
    s += f"<text x='{x0}' y='{yf-6}' fill='#94a3b8' font-size='12' text-anchor='middle'>A</text>"
    s += "</svg>"
    return s

TV_AC = ("<table class='dat'><tr><th>A</th><th>B</th><th>C</th><th>S</th></tr>"
         "<tr><td>0</td><td>0</td><td>0</td><td>0</td></tr>"
         "<tr><td>0</td><td>0</td><td>1</td><td>0</td></tr>"
         "<tr><td>0</td><td>1</td><td>0</td><td>0</td></tr>"
         "<tr><td>0</td><td>1</td><td>1</td><td>0</td></tr>"
         "<tr><td>1</td><td>0</td><td>0</td><td>0</td></tr>"
         "<tr style='background:rgba(74,222,128,.14)'><td>1</td><td>0</td><td>1</td><td>1</td></tr>"
         "<tr><td>1</td><td>1</td><td>0</td><td>0</td></tr>"
         "<tr style='background:rgba(74,222,128,.14)'><td>1</td><td>1</td><td>1</td><td>1</td></tr></table>")

# ---------------- CONTENIDO ----------------

data = {
 "meta": {
  "titulo": "Tecnología e Ingeniería II",
  "subtitulo": "Prueba de Acceso a la Universidad (PAU) · Universidad de Extremadura · Curso 2025-2026 · Examen modelo resuelto y comentado",
  "cabecera_titulo": "PAU 2026 · <span>Tecnología e Ingeniería II</span> · Extremadura · Modelo",
  "pill": "90 min · 4 preguntas · 2,5 pt/pregunta",
  "enunciado_pdf": "../../examens/Extremadura/Tecnologia_Extremadura_2026_modelo.pdf",
  "pdf_dir": "pdf_ext_2026_modelo",
  "footer": "Dpto. Tecnología · Solucionario PAU 2026 · Extremadura · Tecnología e Ingeniería II (Modelo)",
  "intro_inicio": "El examen consta de <b>4 preguntas obligatorias</b> de 2,5 puntos. La primera es de opción única; en las otras tres se elige <b>una de las dos</b> cuestiones. Aquí se resuelven <b>todas</b> para repasar. Selecciona un apartado o una pregunta en la barra lateral.",
  "indice_nombre": "Exámenes de Extremadura",
  "indice_url": "index.html"
 },
 "bloques": [
  {
   "id": "b1", "titulo": "Pregunta 1 · Sistemas mecánicos (neumática)", "color": "#f59e0b",
   "descripcion_tarjeta": "Cilindro de simple efecto para elevar una plataforma: verificación de la carga y consumo de aire.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#f59e0b' stroke-width='3'><rect x='14' y='24' width='36' height='18'/><path d='M50 33h24'/><path d='M22 24v-8M32 24v-8'/></svg>",
   "cuestiones": [
    {
     "id": "q1", "titulo": "Pregunta 1 · Plataforma elevadora (cilindro simple efecto)", "etiqueta": "SISTEMAS MECÁNICOS",
     "menu": "P1 · Plataforma neumática", "titulo_corto": "P1",
     "meta": "Pregunta única y obligatoria · 2,5 puntos (a: 1,25 · b: 1,25)",
     "enunciado_html": "<p>Un cilindro de <b>simple efecto</b> eleva una plataforma. Tiene diámetro de 80 mm, presión de trabajo 8 bar, carrera 150 mm y rendimiento del 85 %; realiza 6 elevaciones por minuto. La plataforma debe elevar hasta <b>300 kp</b>. Averigua:</p><ol type='1' style='padding-left:1.2em'><li>Si la instalación está bien planificada para esa tarea. <span class='pts'>(1,25 puntos)</span></li><li>El consumo de aire en condiciones normales, en l/min. <span class='pts'>(1,25 puntos)</span></li></ol>",
     "figura_enunciado_svg": "",
     "aplica_html": "<p>La fuerza real de avance es \\(F=\\eta\\,p\\,\\frac{\\pi D^2}{4}\\); se compara con el peso a elevar. En un cilindro de simple efecto solo el <b>avance</b> consume aire; el consumo normal multiplica el volumen por la relación de compresión \\(n=\\frac{p+1}{1}\\).</p>",
     "solucion_html": "<p>Datos: \\(D=0{,}08\\,\\mathrm{m}\\), \\(p=8\\,\\mathrm{bar}=8\\cdot10^5\\,\\mathrm{Pa}\\), carrera \\(=0{,}15\\,\\mathrm{m}\\), \\(\\eta=0{,}85\\).</p><h5>1. ¿Está bien planificada?</h5><div class='formula'>$$A=\\frac{\\pi\\cdot 0{,}08^2}{4}=5{,}027\\cdot10^{-3}\\,\\mathrm{m^2}$$</div><div class='formula'>$$F=\\eta\\,p\\,A=0{,}85\\cdot 8\\cdot10^5\\cdot 5{,}027\\cdot10^{-3}=3418\\,\\mathrm{N}$$</div><p>Carga a elevar: \\(300\\,\\mathrm{kp}=300\\cdot 9{,}81=2943\\,\\mathrm{N}\\). Como \\(3418>2943\\,\\mathrm{N}\\), el cilindro <b>sí puede</b> elevar la plataforma: la instalación está bien planificada.</p><div class='res'><b>F = 3418 N &gt; 2943 N &rArr; sí, correcta</b></div><h5>2. Consumo de aire (condiciones normales)</h5><p>Solo consume en el avance: \\(V=A\\cdot L=5{,}027\\cdot10^{-3}\\cdot 0{,}15=7{,}54\\cdot10^{-4}\\,\\mathrm{m^3}=0{,}754\\,\\mathrm{L}\\).</p><p>Relación de compresión \\(n=\\frac{8+1}{1}=9\\); con 6 ciclos/min:</p><div class='formula'>$$Q=n\\,V\\cdot 6=9\\cdot 0{,}754\\cdot 6=40{,}7\\,\\mathrm{L/min}$$</div><div class='res'><b>Q &asymp; 40,7 l/min</b></div>"
    }
   ]
  },
  {
   "id": "b2", "titulo": "Pregunta 2 · Sistemas eléctricos y electrónicos", "color": "#22d3ee",
   "descripcion_tarjeta": "Opción A: circuito RC serie (triángulos de impedancia y tensiones). Opción B: circuito lógico con puertas NOR.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#22d3ee' stroke-width='3'><path d='M8 30q10-16 20 0t20 0 20 0'/></svg>",
   "cuestiones": [
    {
     "id": "q2a", "titulo": "Pregunta 2.1 (Opción A) · Circuito RC serie", "etiqueta": "OPCIÓN A",
     "menu": "P2.1 (A) · Circuito RC serie", "titulo_corto": "P2.1",
     "meta": "2,5 puntos (a: 0,75 · b: 0,75 · c: 1,0)",
     "enunciado_html": "<p>Un circuito serie RC con condensador de 150 &micro;F y resistencia de 25 &ohm; se conecta a 220 V / 50 Hz. Calcula:</p><ol type='a'><li>La impedancia y su triángulo de impedancia. <span class='pts'>(0,75 puntos)</span></li><li>La caída de tensión en ambos elementos y su triángulo de tensiones. <span class='pts'>(0,75 puntos)</span></li><li>El desfase entre intensidad y tensión. <span class='pts'>(1 punto)</span></li></ol>",
     "figura_enunciado_svg": "<figure class='fig'>" + fig_rc() + "<figcaption>Circuito RC serie: C = 150 &micro;F y R = 25 &ohm; a 220 V / 50 Hz.</figcaption></figure>",
     "aplica_html": "<p>\\(X_C=\\frac{1}{2\\pi f C}\\); \\(Z=\\sqrt{R^2+X_C^2}\\); \\(I=\\frac{V}{Z}\\); las caídas \\(V_R=IR\\), \\(V_C=IX_C\\); el desfase \\(\\varphi=\\arctan\\frac{X_C}{R}\\).</p>",
     "solucion_html": "<h5>a) Impedancia</h5><div class='formula'>$$X_C=\\frac{1}{2\\pi\\cdot 50\\cdot 150\\cdot10^{-6}}=21{,}22\\,\\Omega$$</div><div class='formula'>$$Z=\\sqrt{25^2+21{,}22^2}=32{,}79\\,\\Omega$$</div><p>Triángulo de impedancia: catetos \\(R=25\\,\\Omega\\) y \\(X_C=21{,}22\\,\\Omega\\), hipotenusa \\(Z=32{,}79\\,\\Omega\\).</p><div class='res'><b>Z &asymp; 32,79 &ohm;</b></div><h5>b) Caídas de tensión</h5><div class='formula'>$$I=\\frac{220}{32{,}79}=6{,}71\\,\\mathrm{A}$$</div><div class='formula'>$$V_R=IR=167{,}7\\,\\mathrm{V}\\qquad V_C=IX_C=142{,}4\\,\\mathrm{V}$$</div><p>Triángulo de tensiones: \\(V=\\sqrt{V_R^2+V_C^2}\\approx220\\,\\mathrm{V}\\).</p><div class='res'><b>V<sub>R</sub> &asymp; 167,7 V &nbsp;·&nbsp; V<sub>C</sub> &asymp; 142,4 V</b></div><h5>c) Desfase</h5><div class='formula'>$$\\varphi=\\arctan\\frac{X_C}{R}=\\arctan\\frac{21{,}22}{25}=40{,}3^\\circ$$</div><div class='res'><b>&phi; &asymp; 40,3° (la corriente adelanta a la tensión)</b></div>"
    },
    {
     "id": "q2b", "titulo": "Pregunta 2.2 (Opción B) · Circuito lógico con puertas NOR", "etiqueta": "OPCIÓN B",
     "menu": "P2.2 (B) · Circuito lógico (NOR)", "titulo_corto": "P2.2",
     "meta": "2,5 puntos (a: 1,0 · b: 0,75 · c: 0,75)",
     "enunciado_html": "<p>Dado el circuito de la figura, obtén:</p><ol type='a'><li>La ecuación de la función de salida (S). <span class='pts'>(1 punto)</span></li><li>La tabla de verdad. <span class='pts'>(0,75 puntos)</span></li><li>La implementación de la función simplificada. <span class='pts'>(0,75 puntos)</span></li></ol>",
     "figura_enunciado_svg": "<figure class='fig'>" + fig_logic6() + "<figcaption>Cuatro puertas NOR: la primera con las dos entradas unidas a A.</figcaption></figure>",
     "aplica_html": "<p>Se sigue la señal por las puertas NOR y se aplica el álgebra de Boole (De Morgan) para simplificar. Una NOR con las dos entradas unidas actúa como <b>inversor</b>.</p>",
     "solucion_html": "<h5>a) Función de salida</h5><p>Puerta a puerta: \\(g_1=\\overline{A+A}=\\bar A\\); \\(g_2=\\overline{A+B}\\); \\(g_3=\\overline{g_2+C}=\\overline{\\overline{A+B}+C}=(A+B)\\bar C\\); \\(S=\\overline{g_1+g_3}=\\overline{\\bar A+(A+B)\\bar C}\\).</p><div class='formula'>$$S=\\overline{\\bar A}\\cdot\\overline{(A+B)\\bar C}=A\\,\\big(\\overline{A+B}+C\\big)=A(\\bar A\\bar B+C)=A\\,C$$</div><div class='res'><b>S = A · C</b></div><h5>b) Tabla de verdad</h5>" + TV_AC + "<h5>c) Implementación simplificada</h5><p>La función se reduce a una única <b>puerta AND</b> de entradas A y C:</p><figure class='fig'>" + fig_and_ac() + "<figcaption>Implementación de S = A·C con una puerta AND.</figcaption></figure>"
    }
   ]
  },
  {
   "id": "b3", "titulo": "Pregunta 3 · Materiales y fabricación", "color": "#a78bfa",
   "descripcion_tarjeta": "Opción A: ensayo Brinell (huella por superficie). Opción B: cable de acero (ley de Hooke).",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#a78bfa' stroke-width='3'><circle cx='45' cy='26' r='11'/><path d='M45 4v11'/></svg>",
   "cuestiones": [
    {
     "id": "q3a", "titulo": "Pregunta 3.1 (Opción A) · Ensayo de dureza Brinell", "etiqueta": "OPCIÓN A",
     "menu": "P3.1 (A) · Dureza Brinell", "titulo_corto": "P3.1",
     "meta": "2,5 puntos (a: 1,25 · b: 1,25)",
     "enunciado_html": "<p>En un ensayo Brinell se aplica una carga de 275 kp con un penetrador de 6 mm, obteniéndose una huella de <b>3,68 mm²</b> de superficie. Se pide:</p><ol type='a'><li>Determinar el resultado del ensayo. <span class='pts'>(1,25 puntos)</span></li><li>Comprobar si se acertó al elegir el penetrador y la carga. <span class='pts'>(1,25 puntos)</span></li></ol>",
     "figura_enunciado_svg": "",
     "aplica_html": "<p>La dureza Brinell es la carga entre la <b>superficie</b> del casquete de la huella: \\(\\mathrm{HB}=\\frac{F}{S}\\). Para que el ensayo sea válido, el diámetro de huella debe cumplir \\(0{,}24D\\le d\\le 0{,}6D\\).</p>",
     "solucion_html": "<h5>a) Resultado (dureza)</h5><div class='formula'>$$\\mathrm{HB}=\\frac{F}{S}=\\frac{275}{3{,}68}=74{,}7\\,\\mathrm{kp/mm^2}$$</div><div class='res'><b>HB &asymp; 74,7 kp/mm²</b></div><h5>b) ¿Penetrador y carga adecuados?</h5><p>De \\(S=\\pi D h\\) se obtiene la profundidad \\(h=\\frac{S}{\\pi D}=\\frac{3{,}68}{\\pi\\cdot 6}=0{,}195\\,\\mathrm{mm}\\), y el diámetro de huella:</p><div class='formula'>$$d=2\\sqrt{h(D-h)}=2\\sqrt{0{,}195\\,(6-0{,}195)}=2{,}13\\,\\mathrm{mm}$$</div><p>La relación \\(d/D=\\frac{2{,}13}{6}=0{,}355\\) está dentro del rango válido \\((0{,}24\\!-\\!0{,}6)\\), por lo que la huella es <b>correcta</b> y la elección del penetrador y la carga fue <b>adecuada</b>.</p><div class='res'><b>d/D = 0,355 &isin; [0,24 ; 0,6] &rArr; elección correcta</b></div>"
    },
    {
     "id": "q3b", "titulo": "Pregunta 3.2 (Opción B) · Cable de acero (ley de Hooke)", "etiqueta": "OPCIÓN B",
     "menu": "P3.2 (B) · Cable de acero", "titulo_corto": "P3.2",
     "meta": "2,5 puntos (a: 1,25 · b: 1,25)",
     "enunciado_html": "<p>Un cable de acero de 10 m de longitud y 80 mm² de sección se alarga 80 mm (en campo elástico) al aplicarle una carga axial de 120 kN. Se pide:</p><ol type='a'><li>El alargamiento unitario y el módulo de elasticidad del acero. <span class='pts'>(1,25 puntos)</span></li><li>La carga necesaria para que se alargue elásticamente 38 mm. <span class='pts'>(1,25 puntos)</span></li></ol>",
     "figura_enunciado_svg": "",
     "aplica_html": "<p>Alargamiento unitario \\(\\varepsilon=\\frac{\\Delta L}{L}\\). Por la ley de Hooke \\(\\sigma=E\\,\\varepsilon\\), con \\(\\sigma=\\frac{F}{S}\\). En régimen elástico el alargamiento es proporcional a la carga.</p>",
     "solucion_html": "<p>Datos: \\(L=10\\,\\mathrm{m}=10000\\,\\mathrm{mm}\\), \\(S=80\\,\\mathrm{mm^2}\\), \\(F=120\\,\\mathrm{kN}=120000\\,\\mathrm{N}\\), \\(\\Delta L=80\\,\\mathrm{mm}\\).</p><h5>a) Alargamiento unitario y módulo E</h5><div class='formula'>$$\\varepsilon=\\frac{\\Delta L}{L}=\\frac{80}{10000}=0{,}008=0{,}8\\,\\%$$</div><div class='formula'>$$\\sigma=\\frac{F}{S}=\\frac{120000}{80}=1500\\,\\mathrm{N/mm^2}$$</div><div class='formula'>$$E=\\frac{\\sigma}{\\varepsilon}=\\frac{1500}{0{,}008}=187\\,500\\,\\mathrm{MPa}\\approx187{,}5\\,\\mathrm{GPa}$$</div><div class='res'><b>&epsilon; = 0,8 % &nbsp;·&nbsp; E &asymp; 187,5 GPa</b></div><h5>b) Carga para un alargamiento de 38 mm</h5><p>El alargamiento es proporcional a la carga:</p><div class='formula'>$$F'=F\\cdot\\frac{\\Delta L'}{\\Delta L}=120\\cdot\\frac{38}{80}=57\\,\\mathrm{kN}$$</div><div class='res'><b>F&rsquo; = 57 kN</b></div>"
    }
   ]
  },
  {
   "id": "b4", "titulo": "Pregunta 4 · Sistemas mecánicos", "color": "#34d399",
   "descripcion_tarjeta": "Opción A: viga empotrada (voladizo). Opción B: máquina frigorífica de Carnot.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#34d399' stroke-width='3'><path d='M14 30h60'/><path d='M14 18v24'/><path d='M74 20v10'/></svg>",
   "cuestiones": [
    {
     "id": "q4a", "titulo": "Pregunta 4.1 (Opción A) · Viga empotrada (voladizo)", "etiqueta": "OPCIÓN A",
     "menu": "P4.1 (A) · Viga empotrada", "titulo_corto": "P4.1",
     "meta": "2,5 puntos (a: 1,25 · b: 1,25)",
     "enunciado_html": "<p>Para la viga empotrada de la figura (voladizo de 6 m con carga P = 500 kg en el extremo libre):</p><ol type='a'><li>Calcula las fuerzas de reacción. <span class='pts'>(1,25 puntos)</span></li><li>Dibuja los diagramas de momentos flectores y esfuerzos cortantes. <span class='pts'>(1,25 puntos)</span></li></ol>",
     "figura_enunciado_svg": "<figure class='fig'>" + fig_viga_empotrada() + "<figcaption>Viga empotrada en A, voladizo de 6 m con carga P = 500 kg en el extremo libre.</figcaption></figure>",
     "aplica_html": "<p>En un empotramiento hay <b>dos reacciones</b>: una fuerza vertical \\(R_A=P\\) y un momento de empotramiento \\(M_A=P\\cdot L\\). El cortante es constante e igual a \\(P\\); el momento crece linealmente hasta el empotramiento.</p>",
     "solucion_html": "<p>Datos: \\(P=500\\,\\mathrm{kg}\\), \\(L=6\\,\\mathrm{m}\\).</p><h5>a) Reacciones en el empotramiento</h5><div class='formula'>$$R_A=P=500\\,\\mathrm{kg}\\qquad M_A=P\\cdot L=500\\cdot 6=3000\\,\\mathrm{kg\\cdot m}$$</div><div class='res'><b>R<sub>A</sub> = 500 kg &nbsp;·&nbsp; M<sub>A</sub> = 3000 kg&middot;m</b></div><h5>b) Diagramas</h5><p>El cortante es constante (\\(V=500\\,\\mathrm{kg}\\)) en toda la viga. El momento flector varía de \\(-3000\\,\\mathrm{kg\\cdot m}\\) en el empotramiento a 0 en el extremo libre:</p><figure class='fig'>" + fig_esf_empotrada() + "<figcaption>Cortante constante (+500 kg) y momento flector lineal (máx. &minus;3000 kg&middot;m en A).</figcaption></figure>"
    },
    {
     "id": "q4b", "titulo": "Pregunta 4.2 (Opción B) · Máquina frigorífica de Carnot", "etiqueta": "OPCIÓN B",
     "menu": "P4.2 (B) · Máquina frigorífica", "titulo_corto": "P4.2",
     "meta": "2,5 puntos (a: 1,0 · b: 0,75 · c: 0,75)",
     "enunciado_html": "<p>Una máquina frigorífica absorbe 15000 J/min del foco frío, a &minus;23 &deg;C, siendo el foco caliente de 27 &deg;C. Determina:</p><ol type='a'><li>El calor cedido al foco caliente, sabiendo que su eficiencia es la mitad de la de Carnot. <span class='pts'>(1 punto)</span></li><li>La potencia del motor necesaria. <span class='pts'>(0,75 puntos)</span></li><li>La eficiencia ideal y real si actuara como bomba de calor. <span class='pts'>(0,75 puntos)</span></li></ol>",
     "figura_enunciado_svg": "",
     "aplica_html": "<p>\\(\\mathrm{COP}_C=\\frac{T_f}{T_c-T_f}\\); la real es la mitad. Con \\(\\mathrm{COP}=\\frac{Q_f}{W}\\) se obtiene \\(W\\) y \\(Q_c=Q_f+W\\). Como bomba de calor, \\(\\mathrm{COP}_{BC}=\\mathrm{COP}_R+1\\) y \\(\\mathrm{COP}_{BC,ideal}=\\frac{T_c}{T_c-T_f}\\).</p>",
     "solucion_html": "<p>Datos: \\(\\dot Q_f=15000\\,\\mathrm{J/min}\\), \\(T_f=250\\,\\mathrm{K}\\), \\(T_c=300\\,\\mathrm{K}\\).</p><h5>a) Calor cedido al foco caliente</h5><div class='formula'>$$\\mathrm{COP}_C=\\frac{250}{50}=5\\;\\Rightarrow\\;\\mathrm{COP}=2{,}5$$</div><div class='formula'>$$\\dot W=\\frac{15000}{2{,}5}=6000\\,\\mathrm{J/min}\\;\\Rightarrow\\;\\dot Q_c=15000+6000=21000\\,\\mathrm{J/min}$$</div><div class='res'><b>Q<sub>c</sub> = 21000 J/min</b></div><h5>b) Potencia del motor</h5><div class='formula'>$$P=\\dot W=6000\\,\\mathrm{J/min}=100\\,\\mathrm{W}$$</div><div class='res'><b>P = 100 W</b></div><h5>c) Eficiencia como bomba de calor</h5><div class='formula'>$$\\mathrm{COP}_{BC,ideal}=\\frac{T_c}{T_c-T_f}=\\frac{300}{50}=6\\qquad \\mathrm{COP}_{BC,real}=\\mathrm{COP}_R+1=3{,}5$$</div><div class='res'><b>Ideal = 6 &nbsp;·&nbsp; Real = 3,5</b></div>"
    }
   ]
  }
 ]
}

out = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ext_2026_modelo.json"))
with open(out, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print("JSON escrito:", out)
