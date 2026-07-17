# -*- coding: utf-8 -*-
"""Utilidades SVG compartidas para los dashboards de Andalucía (tema oscuro)."""

MARK = ("<defs><marker id='ar' markerWidth='9' markerHeight='8' refX='7' refY='3' "
        "orient='auto'><path d='M0,0 L7,3 L0,6 Z' fill='#cbd5e1'/></marker></defs>")

def svg_open(vb, maxw):
    return (f"<svg viewBox='0 0 {vb}' width='100%' style='max-width:{maxw}px;height:auto' "
            "fill='none' stroke='#cbd5e1' stroke-width='2' "
            "font-family='Inter,system-ui,sans-serif' font-size='14'>" + MARK)

def box(x, y, w, h, label, color='#22d3ee', fs=15):
    cx, cy = x + w/2, y + h/2
    return (f"<rect x='{x}' y='{y}' width='{w}' height='{h}' rx='5' stroke='{color}'/>"
            f"<text x='{cx}' y='{cy+5}' fill='#e2e8f0' font-size='{fs}' text-anchor='middle'>{label}</text>")

def summer(cx, cy, r=15):
    return (f"<circle cx='{cx}' cy='{cy}' r='{r}' stroke='#e2e8f0'/>"
            f"<line x1='{cx-r*0.7:.0f}' y1='{cy-r*0.7:.0f}' x2='{cx+r*0.7:.0f}' y2='{cy+r*0.7:.0f}' stroke='#94a3b8'/>"
            f"<line x1='{cx+r*0.7:.0f}' y1='{cy-r*0.7:.0f}' x2='{cx-r*0.7:.0f}' y2='{cy+r*0.7:.0f}' stroke='#94a3b8'/>")

def arrow(x1, y1, x2, y2, color='#cbd5e1'):
    return f"<line x1='{x1}' y1='{y1}' x2='{x2}' y2='{y2}' stroke='{color}' marker-end='url(#ar)'/>"

def line(x1, y1, x2, y2, color='#cbd5e1'):
    return f"<line x1='{x1}' y1='{y1}' x2='{x2}' y2='{y2}' stroke='{color}'/>"

def txt(x, y, s, color='#e2e8f0', fs=14, anchor='start'):
    return f"<text x='{x}' y='{y}' fill='{color}' font-size='{fs}' text-anchor='{anchor}'>{s}</text>"
