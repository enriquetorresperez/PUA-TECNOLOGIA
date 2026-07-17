/*
 * Convierte un archivo SVG a PNG para poder inspeccionarlo con `view` y
 * compararlo con la figura original del enunciado. Esencial para verificar que
 * un diagrama reproducido es fiel antes de darlo por bueno.
 *
 * Uso:
 *   node svg_to_png.js figura.svg figura.png [ancho_px]
 *
 * Acepta tanto un archivo .svg como un fragmento SVG suelto (se envuelve solo).
 */
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const src = process.argv[2];
const out = process.argv[3] || (src ? src.replace(/\.svg$/i, '') + '.png' : 'figura.png');
const width = parseInt(process.argv[4] || '900', 10);
if (!src) { console.error('Uso: node svg_to_png.js figura.svg figura.png [ancho_px]'); process.exit(1); }

let svg = fs.readFileSync(src, 'utf8').trim();
if (!svg.startsWith('<svg')) {
  // por si se pasa solo el interior
  svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 400">${svg}</svg>`;
}

// Fondo oscuro como el de las cajas .fig, para ver los trazos claros tal cual saldrán.
const html = `<!DOCTYPE html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600&family=Sora:wght@600;700&display=swap" rel="stylesheet">
<style>body{margin:0;background:#0d1220;display:flex;justify-content:center;padding:16px}
svg{max-width:${width}px;height:auto}</style></head>
<body>${svg}</body></html>`;

(async () => {
  const b = await chromium.launch();
  const ctx = await b.newContext({ ignoreHTTPSErrors: true, deviceScaleFactor: 2 });
  const page = await ctx.newPage();
  await page.setContent(html, { waitUntil: 'networkidle' });
  await page.waitForTimeout(400);
  const el = await page.$('svg');
  fs.mkdirSync(path.dirname(path.resolve(out)), { recursive: true });
  await el.screenshot({ path: out });
  console.log('PNG generado:', out, '— ábrelo con `view` y compáralo con la figura original.');
  await b.close();
})();
