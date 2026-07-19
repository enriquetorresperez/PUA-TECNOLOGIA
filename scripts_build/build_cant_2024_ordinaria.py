#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera el JSON del examen Cantabria EBAU 2024 · Ordinaria (Junio)."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import svg_open, box, summer, arrow, line, txt
from cyllib import gate

FIG = "fig"


def img(name, alt, maxw=430, cap=None):
    """Figura del enunciado incrustada como imagen (recorte fiel del original)."""
    c = f"<figcaption>{cap}</figcaption>" if cap else ""
    return (f"<figure class='fig'><img src='fig/{name}' alt='{alt}' "
            f"style='max-width:{maxw}px;width:100%;background:#fff;border-radius:8px;padding:8px'>"
            f"{c}</figure>")


def fig_nand():
    """Implementación de S = a + b'c con 4 NAND de 2 entradas (norma ASA)."""
    s = svg_open('520 260', 520)
    # entradas
    s += txt(16, 70, 'a', '#e2e8f0', 15)
    s += txt(16, 150, 'b', '#e2e8f0', 15)
    s += txt(16, 205, 'c', '#e2e8f0', 15)
    # N2 = NAND(b,b) = b'
    g2, (o2x, o2y) = gate(70, 118, 'NAND')
    s += line(30, 150, 70, 132) + line(30, 150, 70, 158) + g2
    s += txt(90, 112, "b'", '#94a3c0', 12)
    # N3 = NAND(b', c) = (b'c)'
    g3, (o3x, o3y) = gate(180, 150, 'NAND')
    s += line(o2x, o2y, 180, 160) + line(30, 205, 180, 190) + g3
    # N1 = NAND(a,a) = a'
    g1, (o1x, o1y) = gate(180, 44, 'NAND')
    s += line(30, 70, 180, 56) + line(30, 70, 180, 74) + g1
    s += txt(200, 38, "a'", '#94a3c0', 12)
    # N4 = NAND(a', (b'c)') = a + b'c = S
    g4, (o4x, o4y) = gate(330, 96, 'NAND')
    s += line(o1x, o1y, 330, 106) + line(o3x, o3y, 330, 138) + g4
    s += arrow(o4x, o4y, o4x + 40, o4y)
    s += txt(o4x + 48, o4y + 5, 'S', '#4ade80', 16)
    return s + "</svg>"


def fig_bloques_simpl():
    """Diagrama reducido de Ej9 tras simplificar (rama paralela G2+G4, lazo interno)."""
    s = svg_open('720 210', 640)
    ym = 110
    s += txt(20, ym + 5, 'R', '#e2e8f0', 15)
    s += arrow(36, ym, 70, ym)
    s += summer(88, ym)
    s += txt(72, ym - 12, '+', '#4ade80', 15) + txt(74, ym + 30, '−', '#fb7185', 17)
    s += arrow(104, ym, 195, ym)
    s += box(195, 88, 96, 44, 'G<tspan dy="4" font-size="11">eq</tspan>', '#22d3ee', 16)
    s += txt(243, ym + 40, 'G₁G₃(G₂+G₄) / (1+G₂H₁H₂)', '#94a3c0', 11, 'middle')
    s += arrow(291, ym, 470, ym)
    s += "<circle cx='470' cy='110' r='3.4' fill='#cbd5e1'/>"
    s += arrow(470, ym, 520, ym)
    s += txt(532, ym + 5, 'C', '#e2e8f0', 15)
    s += line(470, ym, 470, 180) + line(470, 180, 88, 180)
    s += arrow(88, 180, 88, 125)
    s += txt(279, 175, 'realimentación unitaria (H = 1)', '#94a3c0', 12, 'middle')
    return s + "</svg>"


data = {
 "meta": {
  "titulo": "Tecnología e Ingeniería II",
  "subtitulo": "Prueba de Acceso a la Universidad · Cantabria · Ordinaria (Junio) 2024 · Examen resuelto y comentado",
  "cabecera_titulo": "EBAU 2024 · <span>Tecnología e Ingeniería II</span> · Cantabria · Ordinaria",
  "pill": "Elige 5 de 10 ejercicios · 2 puntos cada uno",
  "enunciado_pdf": "../../examens/Cantabria/Tecnologia_Cantabria_2024_ordinaria.pdf",
  "pdf_dir": "pdf_cant_2024_ordinaria",
  "footer": "Solucionario EBAU · Cantabria · Tecnología e Ingeniería II (Ordinaria 2024)",
  "intro_inicio": "El alumno debe escoger <b>cinco ejercicios de los diez</b> propuestos (cada uno vale 2 puntos). Aquí se resuelven <b>todos</b>. Selecciona un bloque o un ejercicio en la barra lateral: cada uno incluye el enunciado oficial, una introducción con los conceptos que se aplican y la solución paso a paso.",
  "indice_nombre": "Exámenes de Cantabria",
  "indice_url": "index.html"
 },
 "bloques": [
  {
   "id": "b1", "titulo": "Bloque 1 · Materiales y termodinámica", "color": "#f59e0b",
   "descripcion_tarjeta": "Ensayo de resiliencia (Charpy), diagrama Hierro-Carbono y una máquina frigorífica ideal.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#f59e0b' stroke-width='3'><path d='M8 46 L40 46 40 40 46 40 46 46 82 46'/><path d='M20 20 L70 20'/><circle cx='20' cy='20' r='3' fill='#f59e0b' stroke='none'/></svg>",
   "cuestiones": [
    {
     "id": "q1", "titulo": "Ejercicio 1 · Resiliencia (ensayo Charpy)", "etiqueta": "MATERIALES",
     "menu": "E1 · Ensayo Charpy", "titulo_corto": "E1",
     "meta": "Ejercicio de 2 puntos (a 0,7 · b 0,8 · c 0,5)",
     "enunciado_html": "<p>En el estudio de resiliencia de un material mediante el <b>ensayo Charpy</b>, la maza de <b>35 kg</b> cae desde una altura de <b>750 mm</b> sobre la probeta cuyas dimensiones se presentan en la figura. Después de romper la probeta, la maza se ha elevado hasta una altura de <b>46 cm</b>. Se pide:</p><ol type='a'><li>Calcular la energía absorbida por la probeta en la rotura. <span class='pts'>(0,7 ptos.)</span></li><li>Resiliencia del material de la probeta. <span class='pts'>(0,8 ptos.)</span></li><li>Si la resiliencia del material fuese nula, indica hasta qué altura se elevaría la maza, suponiendo que no existe rozamiento. <span class='pts'>(0,5 ptos.)</span></li></ol>",
     "figura_enunciado_svg": img("cant24ord_probeta.png", "Probeta Charpy: vista frontal (55 mm) y sección (10×10 mm, entalla)", 470, "Vista frontal (55 mm) y sección transversal de la probeta (10 mm de ancho; altura resistente bajo la entalla de 9 mm)."),
     "aplica_html": "<p>El péndulo de Charpy mide la <b>energía absorbida</b> en la rotura por diferencia de energía potencial de la maza entre la altura inicial y la final: \\(E_a=m\\,g\\,(h_1-h_2)\\). La <b>resiliencia</b> es esa energía por unidad de sección resistente bajo la entalla: \\(\\rho=E_a/S\\).</p>",
     "solucion_html":
       "<h5>a) Energía absorbida en la rotura</h5>"
       "<p>La maza pierde energía potencial entre la altura de partida \\(h_1=0{,}75\\text{ m}\\) y la de rebote \\(h_2=0{,}46\\text{ m}\\); esa diferencia es la energía que ha consumido en romper la probeta:</p>"
       "<div class='formula'>$$E_a=m\\,g\\,(h_1-h_2)=35\\cdot 9{,}8\\cdot(0{,}75-0{,}46)$$</div>"
       "<div class='formula'>$$E_a=35\\cdot 9{,}8\\cdot 0{,}29=99{,}5\\ \\text{J}$$</div>"
       "<div class='res'><b>E<sub>a</sub> ≈ 99,5 J</b> (con g = 9,8 m/s²)</div>"
       "<h5>b) Resiliencia del material</h5>"
       "<p>La sección resistente es la de la probeta bajo la entalla: ancho 10 mm por altura resistente 9 mm (la entalla reduce 1 mm los 10 mm de canto):</p>"
       "<div class='formula'>$$S=10\\ \\mathrm{mm}\\times 9\\ \\mathrm{mm}=90\\ \\mathrm{mm^2}=0{,}9\\ \\mathrm{cm^2}=0{,}9\\cdot10^{-4}\\ \\mathrm{m^2}$$</div>"
       "<div class='formula'>$$\\rho=\\dfrac{E_a}{S}=\\dfrac{99{,}5\\ \\mathrm{J}}{0{,}9\\ \\mathrm{cm^2}}\\approx 110{,}5\\ \\mathrm{J/cm^2}$$</div>"
       "<div class='res'><b>ρ ≈ 110,5 J/cm² ≈ 1,105·10⁶ J/m² (1105 kJ/m²)</b></div>"
       "<h5>c) Altura de rebote si la resiliencia fuese nula</h5>"
       "<p>Resiliencia nula significa que la probeta <b>no absorbe energía</b>: la maza conservaría toda su energía mecánica. Sin rozamiento, subiría de nuevo hasta la <b>altura de partida</b>:</p>"
       "<div class='formula'>$$h=h_1=750\\ \\text{mm}$$</div>"
       "<div class='res'><b>h = 750 mm (la maza recupera la altura inicial)</b></div>"
    },
    {
     "id": "q2", "titulo": "Ejercicio 2 · Diagrama Hierro-Carbono", "etiqueta": "MATERIALES",
     "menu": "E2 · Diagrama Fe-C", "titulo_corto": "E2",
     "meta": "Ejercicio de 2 puntos (a 0,8 · b 0,6 · c 0,6)",
     "enunciado_html": "<p>El diagrama de equilibrio de la figura representa el diagrama <b>Hierro-Carbono</b> en la zona de los aceros. Disponemos de una aleación de <b>300 kg</b> con un <b>1,20 % de Carbono</b>. Para los tres puntos indicados en la gráfica se pide:</p><ol type='a'><li>Masa de cementita libre (proeutectoide). <span class='pts'>(0,8 ptos.)</span></li><li>Masa de perlita. <span class='pts'>(0,6 ptos.)</span></li><li>Masa de ferrita y cementita dentro de la perlita. <span class='pts'>(0,6 ptos.)</span></li></ol>",
     "figura_enunciado_svg": img("cant24ord_fases.png", "Diagrama Hierro-Carbono con los puntos 1 (1130 ºC), 2 (723,1 ºC) y 3 (722,9 ºC) a 1,20 % C", 470, "Diagrama Fe-C: acero hipereutectoide de 1,20 % C. Punto 1 (1130 ºC), Punto 2 (723,1 ºC, justo por encima de la eutectoide) y Punto 3 (722,9 ºC, justo por debajo)."),
     "aplica_html": "<p>Es un <b>acero hipereutectoide</b> (1,20 % &gt; 0,89 % de la eutectoide). Al enfriar, entre la línea A<sub>cm</sub> y la eutectoide (723 ºC) precipita <b>cementita proeutectoide (libre)</b> en el borde de grano; al cruzar la eutectoide, la austenita restante (0,89 % C) se transforma en <b>perlita</b>. Todo se calcula con la <b>regla de la palanca</b> (cementita 6,67 % C, ferrita ≈ 0 % C).</p>",
     "solucion_html":
       "<h5>a) Cementita libre (proeutectoide)</h5>"
       "<p>Justo por encima de la eutectoide (Punto 2, 723,1 ºC) coexisten austenita (0,89 % C) y cementita (6,67 % C). La fracción de cementita proeutectoide se obtiene con la palanca respecto a 1,20 % C:</p>"
       "<div class='formula'>$$x_{Fe_3C}^{libre}=\\dfrac{1{,}20-0{,}89}{6{,}67-0{,}89}=\\dfrac{0{,}31}{5{,}78}=0{,}0536$$</div>"
       "<div class='formula'>$$m_{Fe_3C}^{libre}=0{,}0536\\cdot 300=16{,}1\\ \\text{kg}$$</div>"
       "<div class='res'><b>Cementita libre ≈ 16,1 kg</b></div>"
       "<h5>b) Masa de perlita</h5>"
       "<p>La perlita procede de toda la austenita (0,89 % C) que quedaba justo antes de la eutectoide; su fracción es el resto:</p>"
       "<div class='formula'>$$x_{perlita}=\\dfrac{6{,}67-1{,}20}{6{,}67-0{,}89}=\\dfrac{5{,}47}{5{,}78}=0{,}9464$$</div>"
       "<div class='formula'>$$m_{perlita}=0{,}9464\\cdot 300=283{,}9\\ \\text{kg}$$</div>"
       "<div class='res'><b>Perlita ≈ 283,9 kg</b> (comprobación: 16,1 + 283,9 = 300 kg)</div>"
       "<h5>c) Ferrita y cementita dentro de la perlita</h5>"
       "<p>La perlita (0,89 % C) es una mezcla de ferrita (≈ 0 % C) y cementita (6,67 % C). Aplicando la palanca dentro de la perlita:</p>"
       "<div class='formula'>$$x_{\\alpha}=\\dfrac{6{,}67-0{,}89}{6{,}67-0}=0{,}867 \\qquad x_{Fe_3C}=\\dfrac{0{,}89-0}{6{,}67}=0{,}133$$</div>"
       "<div class='formula'>$$m_{\\alpha}=0{,}867\\cdot 283{,}9=246{,}1\\ \\text{kg} \\qquad m_{Fe_3C}^{eut}=0{,}133\\cdot 283{,}9=37{,}8\\ \\text{kg}$$</div>"
       "<div class='res'><b>Ferrita en la perlita ≈ 246,1 kg · Cementita en la perlita ≈ 37,8 kg</b></div>"
    },
    {
     "id": "q3", "titulo": "Ejercicio 3 · Máquina frigorífica ideal", "etiqueta": "TERMODINÁMICA",
     "menu": "E3 · Máquina frigorífica", "titulo_corto": "E3",
     "meta": "Ejercicio de 2 puntos (a 0,8 · b 0,6 · c 0,6)",
     "enunciado_html": "<p>Para conservar las verduras, una cámara frigorífica ideal debe mantener su interior a <b>2 ºC</b>. La máquina está en un almacén a <b>22 ºC</b> y absorbe <b>36 cal por segundo</b> del foco frío. Se pide:</p><ol type='a'><li>Eficiencia de la cámara frigorífica. <span class='pts'>(0,8 ptos.)</span></li><li>Calor cedido por la máquina al recinto, en calorías. <span class='pts'>(0,6 ptos.)</span></li><li>Trabajo consumido por el compresor eléctrico. <span class='pts'>(0,6 ptos.)</span></li></ol>",
     "aplica_html": "<p>Una máquina frigorífica <b>ideal</b> trabaja según el <b>ciclo de Carnot</b> inverso. Su eficiencia (COP frigorífico) depende solo de las temperaturas absolutas: \\(\\varepsilon=\\dfrac{T_f}{T_c-T_f}\\). El balance energético es \\(Q_c=Q_f+W\\), con \\(W=Q_f/\\varepsilon\\).</p>",
     "solucion_html":
       "<h5>a) Eficiencia (COP frigorífico de Carnot)</h5>"
       "<p>Pasamos a kelvin: \\(T_f=2+273=275\\text{ K}\\), \\(T_c=22+273=295\\text{ K}\\).</p>"
       "<div class='formula'>$$\\varepsilon=\\dfrac{T_f}{T_c-T_f}=\\dfrac{275}{295-275}=\\dfrac{275}{20}=13{,}75$$</div>"
       "<div class='res'><b>ε = 13,75</b></div>"
       "<h5>b) Calor cedido al recinto (foco caliente)</h5>"
       "<p>En un ciclo de Carnot \\(\\dfrac{Q_c}{Q_f}=\\dfrac{T_c}{T_f}\\), luego:</p>"
       "<div class='formula'>$$Q_c=Q_f\\dfrac{T_c}{T_f}=36\\cdot\\dfrac{295}{275}=38{,}62\\ \\text{cal/s}$$</div>"
       "<div class='res'><b>Q<sub>c</sub> ≈ 38,62 cal por segundo</b></div>"
       "<h5>c) Trabajo consumido por el compresor</h5>"
       "<p>Por el balance energético \\(W=Q_c-Q_f\\):</p>"
       "<div class='formula'>$$W=38{,}62-36=2{,}62\\ \\text{cal/s}$$</div>"
       "<div class='formula'>$$W=2{,}62\\ \\tfrac{\\text{cal}}{\\text{s}}\\cdot 4{,}18\\ \\tfrac{\\text{J}}{\\text{cal}}\\approx 10{,}9\\ \\text{W}$$</div>"
       "<div class='res'><b>W ≈ 2,62 cal/s ≈ 10,9 W</b> (comprobación: W = Q<sub>f</sub>/ε = 36/13,75 = 2,62 cal/s)</div>"
    }
   ]
  },
  {
   "id": "b2", "titulo": "Bloque 2 · Neumática", "color": "#38bdf8",
   "descripcion_tarjeta": "Identificación de componentes y funcionamiento de una instalación neumática con cilindro de doble efecto.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#38bdf8' stroke-width='3'><rect x='12' y='22' width='40' height='16' rx='2'/><path d='M52 30h16'/><path d='M20 30h24'/><circle cx='68' cy='30' r='4'/></svg>",
   "cuestiones": [
    {
     "id": "q4", "titulo": "Ejercicio 4 · Instalación neumática", "etiqueta": "NEUMÁTICA",
     "menu": "E4 · Instalación neumática", "titulo_corto": "E4",
     "meta": "Ejercicio de 2 puntos (a 1 · b 1)",
     "enunciado_html": "<p>En la instalación neumática de la figura se pide:</p><ol type='a'><li>Para cada componente del circuito, nómbralo y explica brevemente su funcionamiento. <span class='pts'>(1 pto.)</span></li><li>Explica el funcionamiento de la instalación. <span class='pts'>(1 pto.)</span></li></ol>",
     "figura_enunciado_svg": img("cant24ord_neumatica.png", "Instalación neumática: cilindro de doble efecto, válvula 5/2 y válvulas 3/2", 560, "Circuito neumático: cilindro de doble efecto 1.0, distribuidor 5/2 (1.1), válvula selectora 1.01, válvula de simultaneidad 1.02 y cuatro válvulas 3/2 (1.2, 1.3, 1.4 y 1.5)."),
     "aplica_html": "<p>Hay que reconocer la <b>simbología neumática</b> (norma ISO 1219): el actuador, el distribuidor principal y las válvulas auxiliares, y razonar la <b>lógica de mando</b> (funciones Y/O) que gobierna el avance y el retroceso del vástago.</p>",
     "solucion_html":
       "<h5>a) Componentes del circuito</h5>"
       "<ul>"
       "<li><b>1.0 · Cilindro de doble efecto</b> (con amortiguación regulable). Es el actuador: el aire a presión entra por una u otra cámara para producir el <b>avance</b> o el <b>retroceso</b> del vástago con fuerza en ambos sentidos.</li>"
       "<li><b>1.1 · Válvula distribuidora 5/2</b> (biestable, pilotada neumáticamente por sus dos extremos). Es el elemento de mando principal: dirige el aire a una u otra cámara del cilindro y comunica la contraria con el escape. Tiene <b>5 vías</b> (1 alimentación, 2 y 4 utilización, 3 y 5 escapes) y <b>2 posiciones</b>.</li>"
       "<li><b>1.01 · Válvula selectora \"O\" (OR)</b>. Deja pasar la señal si recibe pilotaje por <b>cualquiera</b> de sus dos entradas; su salida pilota un extremo de la 5/2.</li>"
       "<li><b>1.02 · Válvula de simultaneidad \"Y\" (AND)</b>. Solo da señal de salida si recibe presión por sus <b>dos</b> entradas a la vez; pilota el otro extremo de la 5/2.</li>"
       "<li><b>1.2, 1.3, 1.4 y 1.5 · Válvulas 3/2</b> (3 vías, 2 posiciones, normalmente cerradas, con retorno por muelle). Son los <b>elementos de mando/finales de carrera</b> que generan las señales: 1.2 y 1.4 accionan la selectora \"O\" (avance) y 1.3 y 1.5 la de simultaneidad \"Y\" (retroceso).</li>"
       "</ul>"
       "<h5>b) Funcionamiento de la instalación</h5>"
       "<p>Las válvulas 1.2 y 1.4 están conectadas a la <b>válvula selectora \"O\" (1.01)</b>: basta accionar <b>una</b> de ellas para que su señal pilote la 5/2 y el cilindro <b>avance</b> (mando en paralelo, función <b>lógica O</b>).</p>"
       "<p>Las válvulas 1.3 y 1.5 están conectadas a la <b>válvula de simultaneidad \"Y\" (1.02)</b>: es necesario accionar <b>las dos a la vez</b> para que la 5/2 conmute a la posición contraria y el cilindro <b>retroceda</b> (mando en serie, función <b>lógica Y</b>, típica de seguridad a dos manos).</p>"
       "<p>Como la 5/2 es <b>biestable</b>, mantiene la última posición ordenada hasta que llega la señal contraria, de modo que el vástago permanece en avance o en retroceso sin necesidad de mantener pulsadas las válvulas.</p>"
       "<div class='res'><b>Avance = 1.2 <i>O</i> 1.4 · Retroceso = 1.3 <i>Y</i> 1.5</b></div>"
    }
   ]
  },
  {
   "id": "b3", "titulo": "Bloque 3 · Sistemas digitales", "color": "#a78bfa",
   "descripcion_tarjeta": "Función canónica, simplificación por Karnaugh, implementación con NAND y análisis de un circuito lógico.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#a78bfa' stroke-width='3'><path d='M18 18 h14 a12 12 0 0 1 0 24 h-14 z'/><path d='M6 24h12M6 36h12M56 30h14'/><circle cx='74' cy='30' r='3'/></svg>",
   "cuestiones": [
    {
     "id": "q5", "titulo": "Ejercicio 5 · Función lógica: Karnaugh y NAND", "etiqueta": "DIGITAL",
     "menu": "E5 · Karnaugh y NAND", "titulo_corto": "E5",
     "meta": "Ejercicio de 2 puntos (a 0,8 · b 0,6 · c 0,6)",
     "enunciado_html": "<p>Dada la siguiente tabla de verdad, se pide:</p><ol type='a'><li>Obtener la función canónica en minterms. <span class='pts'>(0,8 ptos.)</span></li><li>Obtener la función simplificada mediante el método de Karnaugh. <span class='pts'>(0,6 ptos.)</span></li><li>Implementar la función simplificada utilizando únicamente puertas NAND de dos entradas. <span class='pts'>(0,6 ptos.)</span></li></ol>"
      "<table class='dat'><thead><tr><th>a</th><th>b</th><th>c</th><th>S</th></tr></thead><tbody>"
      "<tr><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>1</td><td>1</td></tr>"
      "<tr><td>0</td><td>1</td><td>0</td><td>0</td></tr><tr><td>0</td><td>1</td><td>1</td><td>0</td></tr>"
      "<tr><td>1</td><td>0</td><td>0</td><td>1</td></tr><tr><td>1</td><td>0</td><td>1</td><td>1</td></tr>"
      "<tr><td>1</td><td>1</td><td>0</td><td>1</td></tr><tr><td>1</td><td>1</td><td>1</td><td>1</td></tr>"
      "</tbody></table>",
     "aplica_html": "<p>La <b>función canónica en minterms</b> es la suma (OR) de los términos producto de las filas con salida 1. El <b>mapa de Karnaugh</b> agrupa unos adyacentes en potencias de 2 para simplificar. Por último, aplicando <b>doble negación</b> y De Morgan, cualquier función se implementa solo con puertas <b>NAND</b>.</p>",
     "solucion_html":
       "<h5>a) Función canónica en minterms</h5>"
       "<p>Salida 1 en las filas 1, 4, 5, 6 y 7:</p>"
       "<div class='formula'>$$S=\\sum m(1,4,5,6,7)=\\bar a\\,\\bar b\\,c+a\\,\\bar b\\,\\bar c+a\\,\\bar b\\,c+a\\,b\\,\\bar c+a\\,b\\,c$$</div>"
       "<h5>b) Simplificación por Karnaugh</h5>"
       "<p>Colocando los unos en el mapa (filas = a; columnas = bc en código Gray):</p>"
       "<table class='dat'><thead><tr><th>a\\bc</th><th>00</th><th>01</th><th>11</th><th>10</th></tr></thead><tbody>"
       "<tr><td><b>0</b></td><td>0</td><td>1</td><td>0</td><td>0</td></tr>"
       "<tr><td><b>1</b></td><td>1</td><td>1</td><td>1</td><td>1</td></tr>"
       "</tbody></table>"
       "<p>La fila <b>a = 1</b> está entera de unos &rarr; agrupa <b>a</b>. Los unos de la columna <b>bc = 01</b> (m1 y m5) agrupan <b>\\(\\bar b\\,c\\)</b>:</p>"
       "<div class='formula'>$$\\boxed{\\ S=a+\\bar b\\,c\\ }$$</div>"
       "<h5>c) Implementación con NAND de dos entradas</h5>"
       "<p>Usando \\(x=\\overline{\\overline{x}}\\) y De Morgan, \\(S=a+\\bar b c=\\overline{\\bar a\\cdot\\overline{\\bar b c}}\\):</p>"
       "<div class='formula'>$$\\bar a=\\overline{a\\cdot a},\\quad \\bar b=\\overline{b\\cdot b},\\quad \\overline{\\bar b c}=\\overline{\\bar b\\cdot c},\\quad S=\\overline{\\bar a\\cdot\\overline{\\bar b c}}$$</div>"
       "<p>Son <b>4 puertas NAND de 2 entradas</b>:</p>"
       "<figure class='fig'>" + fig_nand() + "<figcaption>S = a + b'c con 4 NAND-2 (símbolos ASA).</figcaption></figure>"
       "<div class='res'><b>S = a + b′c &nbsp;=&nbsp; NAND( NAND(a,a) , NAND( NAND(b,b) , c ) )</b></div>"
    },
    {
     "id": "q6", "titulo": "Ejercicio 6 · Función lógica de un circuito", "etiqueta": "DIGITAL",
     "menu": "E6 · Función de un circuito", "titulo_corto": "E6",
     "meta": "Ejercicio de 2 puntos (a 1,4 · b 0,6)",
     "enunciado_html": "<p>Dado el circuito de la figura, se pide:</p><ol type='a'><li>Obtén la función lógica y simplifícala algebraicamente si es posible. <span class='pts'>(1,4 ptos.)</span></li><li>Confecciona la tabla de verdad correspondiente. <span class='pts'>(0,6 ptos.)</span></li></ol>",
     "figura_enunciado_svg": img("cant24ord_logica.png", "Circuito lógico con puertas NOT, OR (≥1), XOR (=1), AND (&) y NOR final", 560, "Circuito lógico: A y C pasan por sendos inversores; puertas OR (≥1), XOR (=1), AND (&) y una NOR (≥1 con círculo) que da la salida S."),
     "aplica_html": "<p>Se recorre el circuito de la entrada a la salida, escribiendo la salida de cada puerta según su tipo (NOT, OR = ≥1, XOR = =1, AND = &, NOR = ≥1 con círculo). Después se simplifica el álgebra de Boole y se comprueba con la tabla de verdad.</p>",
     "solucion_html":
       "<h5>a) Función lógica</h5>"
       "<p>Los inversores dan \\(\\bar A\\) y \\(\\bar C\\). Las tres puertas de la izquierda producen:</p>"
       "<div class='formula'>$$P=\\bar A+C\\ (\\text{OR}),\\qquad Q=A\\oplus B\\ (\\text{XOR}),\\qquad R=\\bar A+\\bar C\\ (\\text{OR})$$</div>"
       "<p>Las dos puertas AND y la NOR final:</p>"
       "<div class='formula'>$$S=\\overline{\\;\\big[(\\bar A+C)(A\\oplus B)\\big]+\\big[B\\,(\\bar A+\\bar C)\\big]\\;}$$</div>"
       "<p>Desarrollando y agrupando (o directamente por tabla de verdad) se obtiene la forma mínima:</p>"
       "<div class='formula'>$$\\boxed{\\ S=\\bar A\\,\\bar B+\\bar B\\,\\bar C+A\\,B\\,C\\ }$$</div>"
       "<p>Es decir, \\(S=\\bar B\\,(\\overline{AC})+A\\,B\\,C\\): la salida vale 1 cuando <b>B = 0</b> y no se cumple <i>A y C</i> a la vez, o cuando <b>A = B = C = 1</b>.</p>"
       "<h5>b) Tabla de verdad</h5>"
       "<table class='dat'><thead><tr><th>A</th><th>B</th><th>C</th><th>P=Ā+C</th><th>Q=A⊕B</th><th>R=Ā+C̄</th><th>S</th></tr></thead><tbody>"
       "<tr><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td><b>1</b></td></tr>"
       "<tr><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>1</td><td><b>1</b></td></tr>"
       "<tr><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td><b>0</b></td></tr>"
       "<tr><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td><b>0</b></td></tr>"
       "<tr><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td><b>1</b></td></tr>"
       "<tr><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td><b>0</b></td></tr>"
       "<tr><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td><b>0</b></td></tr>"
       "<tr><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td><b>1</b></td></tr>"
       "</tbody></table>"
       "<div class='res'><b>S = 1 en (A,B,C) = 000, 001, 100 y 111 &nbsp;→&nbsp; S = Ā·B̄ + B̄·C̄ + A·B·C</b></div>"
    }
   ]
  },
  {
   "id": "b4", "titulo": "Bloque 4 · Ciberseguridad e Inteligencia Artificial", "color": "#4ade80",
   "descripcion_tarjeta": "Amenazas comunes de ciberseguridad y concepto y aplicaciones de la inteligencia artificial.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#4ade80' stroke-width='3'><path d='M45 10 L68 20 V32 C68 45 45 52 45 52 C45 52 22 45 22 32 V20 Z'/><path d='M37 30l6 6 12-13'/></svg>",
   "cuestiones": [
    {
     "id": "q7", "titulo": "Ejercicio 7 · Amenazas de ciberseguridad", "etiqueta": "CIBERSEGURIDAD",
     "menu": "E7 · Amenazas de ciberseguridad", "titulo_corto": "E7",
     "meta": "Ejercicio de 2 puntos · pregunta teórica",
     "enunciado_html": "<p>Describe <b>4 amenazas comunes</b> para la ciberseguridad.</p>",
     "aplica_html": "<p>Se trata de identificar y describir brevemente amenazas habituales que comprometen la confidencialidad, integridad o disponibilidad de la información.</p>",
     "solucion_html":
       "<ul>"
       "<li><b>Malware</b> (software malicioso): virus, troyanos, gusanos o <b>ransomware</b> que se instalan sin permiso para dañar el equipo, robar datos o secuestrarlos cifrándolos y pedir un rescate.</li>"
       "<li><b>Phishing e ingeniería social</b>: correos, mensajes o webs falsos que suplantan a entidades de confianza para engañar al usuario y obtener contraseñas, datos bancarios o que instale malware.</li>"
       "<li><b>Ataques de denegación de servicio (DoS/DDoS)</b>: saturan un servidor o red con peticiones masivas hasta dejarlo inoperativo para los usuarios legítimos.</li>"
       "<li><b>Ataque de intermediario (Man-in-the-Middle)</b>: el atacante se interpone en una comunicación (p. ej. una wifi pública) para interceptar o modificar la información que circula, robando credenciales o datos.</li>"
       "</ul>"
       "<div class='res'>Otras amenazas válidas: inyección SQL, robo/fuga de credenciales, exploits de vulnerabilidades <i>zero-day</i>, amenazas internas.</div>"
    },
    {
     "id": "q8", "titulo": "Ejercicio 8 · Inteligencia artificial", "etiqueta": "IA",
     "menu": "E8 · Inteligencia artificial", "titulo_corto": "E8",
     "meta": "Ejercicio de 2 puntos · pregunta teórica",
     "enunciado_html": "<p>¿Qué es la inteligencia artificial? Describe <b>4 aplicaciones</b> de la inteligencia artificial.</p>",
     "aplica_html": "<p>Definir el concepto de IA y citar campos reales donde se aplica, explicando brevemente cada uno.</p>",
     "solucion_html":
       "<h5>¿Qué es la inteligencia artificial?</h5>"
       "<p>La <b>inteligencia artificial (IA)</b> es la rama de la informática que desarrolla sistemas capaces de realizar tareas que normalmente requieren <b>inteligencia humana</b> —aprender de los datos, razonar, reconocer patrones, tomar decisiones o comprender el lenguaje— mejorando su comportamiento con la experiencia (aprendizaje automático).</p>"
       "<h5>Cuatro aplicaciones</h5>"
       "<ul>"
       "<li><b>Asistentes virtuales y reconocimiento del habla</b> (Siri, Alexa, traducción automática): interpretan el lenguaje natural y responden.</li>"
       "<li><b>Visión artificial y diagnóstico médico</b>: reconocimiento de imágenes para detectar objetos, rostros o patologías en radiografías.</li>"
       "<li><b>Vehículos autónomos</b>: perciben el entorno con sensores y cámaras y toman decisiones de conducción en tiempo real.</li>"
       "<li><b>Sistemas de recomendación</b> (Netflix, tiendas <i>online</i>): analizan el comportamiento del usuario para sugerir contenidos o productos.</li>"
       "</ul>"
       "<div class='res'>Otras: detección de fraude bancario, robótica industrial, IA generativa (texto e imágenes), mantenimiento predictivo.</div>"
    }
   ]
  },
  {
   "id": "b5", "titulo": "Bloque 5 · Sistemas de control", "color": "#22d3ee",
   "descripcion_tarjeta": "Simplificación de un diagrama de bloques con lazos y rama en paralelo, y estabilidad por el criterio de Routh.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#22d3ee' stroke-width='3'><rect x='34' y='22' width='24' height='16' rx='3'/><path d='M8 30h26M58 30h24'/><circle cx='20' cy='30' r='6'/></svg>",
   "cuestiones": [
    {
     "id": "q9", "titulo": "Ejercicio 9 · Diagrama de bloques", "etiqueta": "CONTROL",
     "menu": "E9 · Función de transferencia", "titulo_corto": "E9",
     "meta": "Ejercicio de 2 puntos (a 1 · b 1)",
     "enunciado_html": "<p>Dado el sistema de control de la figura, se pide:</p><ol type='a'><li>Simplifica el sistema de control. <span class='pts'>(1 pto.)</span></li><li>Obtén su función de transferencia. <span class='pts'>(1 pto.)</span></li></ol>",
     "figura_enunciado_svg": img("cant24ord_control.png", "Diagrama de bloques con G1, G2, G3, G4, realimentaciones H1, H2 y lazo unitario", 620, "Diagrama de bloques: G4 en paralelo con G2, lazo interno realimentado por H1·H2 y lazo externo de realimentación unitaria."),
     "aplica_html": "<p>Se reducen los bloques por pasos: las ramas en <b>paralelo</b> se suman (G<sub>2</sub>+G<sub>4</sub>); el <b>lazo interno</b> con realimentación H<sub>1</sub>H<sub>2</sub> aplica \\(\\frac{G}{1+GH}\\); y el <b>lazo externo</b> unitario cierra la función global.</p>",
     "solucion_html":
       "<h5>a) Simplificación por pasos</h5>"
       "<p>Sea \\(E_2\\) la salida del segundo sumador. La rama \\(G_4\\) va en <b>paralelo</b> con \\(G_2\\) (misma entrada \\(E_2\\)) y ambas se suman en el tercer sumador: la trayectoria directa equivale a \\((G_2+G_4)\\).</p>"
       "<p>La cementación del <b>lazo interno</b> (la realimentación \\(H_1H_2\\) se toma tras \\(G_2\\) y entra en negativo al segundo sumador) da:</p>"
       "<div class='formula'>$$E_2=\\dfrac{W}{1+G_2H_1H_2},\\qquad W=G_1(R-C)$$</div>"
       "<figure class='fig'>" + fig_bloques_simpl() + "<figcaption>Sistema equivalente: un único bloque directo con realimentación unitaria.</figcaption></figure>"
       "<h5>b) Función de transferencia</h5>"
       "<p>La salida es \\(C=G_3\\,(G_2+G_4)\\,E_2\\). Sustituyendo \\(E_2\\) y \\(W\\):</p>"
       "<div class='formula'>$$C=\\dfrac{G_1G_3(G_2+G_4)}{1+G_2H_1H_2}\\,(R-C)$$</div>"
       "<p>Llamando \\(T=\\dfrac{G_1G_3(G_2+G_4)}{1+G_2H_1H_2}\\), el lazo externo unitario da \\(\\frac{C}{R}=\\frac{T}{1+T}\\):</p>"
       "<div class='formula'>$$\\boxed{\\ \\dfrac{C(s)}{R(s)}=\\dfrac{G_1G_3(G_2+G_4)}{1+G_2H_1H_2+G_1G_3(G_2+G_4)}\\ }$$</div>"
       "<div class='res'><b>C/R = G₁G₃(G₂+G₄) / [ 1 + G₂H₁H₂ + G₁G₃(G₂+G₄) ]</b></div>"
    },
    {
     "id": "q10", "titulo": "Ejercicio 10 · Estabilidad (criterio de Routh)", "etiqueta": "CONTROL",
     "menu": "E10 · Criterio de Routh", "titulo_corto": "E10",
     "meta": "Ejercicio de 2 puntos",
     "enunciado_html": "<p>Determina, aplicando el <b>método de Routh</b>, si el sistema dado por la ecuación característica siguiente es estable:</p><div class='formula'>$$2s^5+3s^4+2s^3+4s^2+6s+7=0$$</div>",
     "aplica_html": "<p>El <b>criterio de Routh-Hurwitz</b> analiza la estabilidad sin resolver la ecuación: se construye la tabla de Routh y se cuentan los <b>cambios de signo</b> en la primera columna; cada cambio es un polo con parte real positiva. El sistema es estable solo si <b>todos</b> los términos de la primera columna son positivos (sin cambios de signo).</p>",
     "solucion_html":
       "<h5>Construcción de la tabla de Routh</h5>"
       "<p>Coeficientes: 2, 3, 2, 4, 6, 7. Filas s⁵ y s⁴ directas; el resto por la fórmula del determinante:</p>"
       "<table class='dat'><tbody>"
       "<tr><th>s⁵</th><td>2</td><td>2</td><td>6</td></tr>"
       "<tr><th>s⁴</th><td>3</td><td>4</td><td>7</td></tr>"
       "<tr><th>s³</th><td>−0,667</td><td>1,333</td><td>0</td></tr>"
       "<tr><th>s²</th><td>10</td><td>7</td><td></td></tr>"
       "<tr><th>s¹</th><td>1,8</td><td>0</td><td></td></tr>"
       "<tr><th>s⁰</th><td>7</td><td></td><td></td></tr>"
       "</tbody></table>"
       "<div class='formula'>$$b_1=\\dfrac{3\\cdot2-2\\cdot4}{3}=-0{,}667,\\quad b_2=\\dfrac{3\\cdot6-2\\cdot7}{3}=1{,}333$$</div>"
       "<div class='formula'>$$c_1=\\dfrac{b_1\\cdot4-3\\cdot b_2}{b_1}=10,\\quad c_2=7;\\quad d_1=\\dfrac{c_1 b_2-b_1 c_2}{c_1}=1{,}8;\\quad e_1=7$$</div>"
       "<h5>Conclusión</h5>"
       "<p>Primera columna: \\(2,\\ 3,\\ -0{,}667,\\ 10,\\ 1{,}8,\\ 7\\). Hay <b>dos cambios de signo</b> (de 3 a −0,667 y de −0,667 a 10), luego el sistema tiene <b>2 polos con parte real positiva</b>.</p>"
       "<div class='res'><b>El sistema es INESTABLE</b> (2 cambios de signo → 2 raíces en el semiplano derecho).</div>"
    }
   ]
  }
 ]
}

out = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "cant_2024_ordinaria.json"))
with open(out, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print("JSON escrito:", out)
