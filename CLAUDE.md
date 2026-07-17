# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Qué es este directorio

No es un proyecto de software con build/test/lint. Es una colección de **solucionarios (dashboards) de exámenes EVAU/PAU** (Comunidad de Madrid, convocatoria 2025-2026) para Física, Matemáticas II y Tecnología e Ingeniería II, más un archivo de enunciados oficiales en PDF y los PDF de solución generados.

- Los `.html` en la raíz son **dashboards autocontenidos**: HTML + CSS inline en `<style>` + KaTeX (vía CDN) para fórmulas. Sin bundler ni framework; cada archivo se abre directamente en el navegador.
- Los enunciados oficiales en PDF viven en `documentos/<asignatura>/` (no en la raíz).
- Los PDF de solución generados viven en `pdf_<asignatura>_<conv>/` (un PDF por cuestión + `soluciones_completas.pdf`).

## Flujo principal: el skill `pau-dashboard`

La forma canónica de producir o actualizar un solucionario NO es escribir el HTML a mano, sino usar el skill `.claude/skills/pau-dashboard/`. Se dispara SIEMPRE que el usuario suba/mencione un examen de PAU/EVAU/EBAU y pida resolverlo o generar dashboard/PDFs. Pipeline (ver `SKILL.md`):

1. Leer el PDF del enunciado y extraerlo fielmente (bloques, cuestiones, opcionalidad, datos, figuras).
2. Resolver cada cuestión (intro + paso a paso + resultado destacado; SVG propio para las figuras).
3. Escribir el contenido en un JSON según `references/esquema_json.md` y generar el HTML:
   ```bash
   python3 .claude/skills/pau-dashboard/scripts/build_dashboard.py examen.json salida/dashboard.html
   ```
4. Generar los PDF (un PDF por cuestión + `soluciones_completas.pdf`) con Playwright/Chromium:
   ```bash
   node .claude/skills/pau-dashboard/scripts/build_pdfs.js dashboard.html pdf_salida/
   ```
   Requiere Playwright; si Chromium no está instalado: `npx playwright install chromium`. En este entorno los módulos de node suelen resolverse vía `NODE_PATH` a un `node_modules` del scratchpad (ver ejemplos en `.claude/settings.local.json`).

Al editar un dashboard existente a mano, mantén el mismo esquema de variables CSS y la carga de KaTeX vía `auto-render`; pero si el cambio es grande, prefiere regenerar desde el JSON con el skill para no divergir de la plantilla (`assets/plantilla_estilos.css`).

## Convenciones de nombres

- Prefijo de asignatura: `fis_` (Física), `mat_` (Matemáticas II), `tec_` (Tecnología e Ingeniería II).
- `26` = convocatoria 2025-2026. `ord` = ordinaria, `ext` = extraordinaria, `coin` = coincidentes.
- **Versión vigente**: puede haber varias versiones del mismo solucionario (p. ej. `tec_26_ord.html` vs `tec_26_ord_old.html`, o `tec_26_ord1.html`). Los sufijos `_old`/numéricos son versiones antiguas; antes de editar, confirma cuál es la vigente (normalmente la de mtime más reciente y sin sufijo).
- Carpetas de PDF generados: `pdf_tec_26_ord/`, `pdf_tec_26_ext/`, con `q1.pdf`, `q2-1.pdf`, … y `soluciones_completas.pdf`.

## Estructura de los dashboards HTML

- `<head>`: fuentes de Google Fonts (Fraunces, Inter, JetBrains Mono) y KaTeX (CSS + JS + `auto-render`) desde CDN (`cdnjs.cloudflare.com` o `cdn.jsdelivr.net`).
- Estilos con variables CSS en `:root` (tema oscuro: `--bg`, `--ink`, `--accent`, …), sin preprocesadores.
- `header.hero` con título/subtítulo y `chip`s de metadatos, barra lateral/índice por bloques, cuerpo con la resolución de cada cuestión, soluciones desplegables y botones "Ver PDF" (abren en pestaña nueva, **nunca** con `download`).
- Fórmulas en LaTeX renderizadas por `auto-render` de KaTeX en carga (requiere internet al abrir el archivo).
- Los PDF de impresión usan tema claro (ver CSS en `build_pdfs.js`), pero los diagramas SVG conservan su fondo oscuro.
