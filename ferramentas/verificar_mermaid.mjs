// Valida a sintaxe de todos os diagramas ```mermaid do repositório.
// Uso: node ferramentas/verificar_mermaid.mjs   (requer `npm ci` em ferramentas/)
import { readFileSync, readdirSync, statSync } from 'node:fs';
import { createRequire } from 'node:module';
import { dirname, join, relative } from 'node:path';
import { fileURLToPath } from 'node:url';
const aqui = dirname(fileURLToPath(import.meta.url));
const raiz = dirname(aqui);
const require = createRequire(join(aqui, 'package.json'));
const { JSDOM } = require('jsdom');
const dom = new JSDOM('<!doctype html><html><body></body></html>');
globalThis.window = dom.window;
globalThis.document = dom.window.document;
globalThis.DOMPurify = undefined;
const mermaid = (await import(join(aqui, 'node_modules/mermaid/dist/mermaid.core.mjs'))).default;
function mds(d) { return readdirSync(d).flatMap(n => { const p = join(d, n); if (['.git', 'node_modules'].includes(n)) return []; return statSync(p).isDirectory() ? mds(p) : (n.endsWith('.md') ? [p] : []); }); }
mermaid.initialize({ startOnLoad: false });
let fails = 0, total = 0;
for (const f of (process.argv.length > 2 ? process.argv.slice(2) : mds(raiz))) {
  const txt = readFileSync(f, 'utf8');
  const re = /```mermaid\n([\s\S]*?)```/g;
  let m, i = 0;
  while ((m = re.exec(txt))) {
    i++; total++;
    try { await mermaid.parse(m[1]); console.log(`OK   ${relative(raiz, f)} #${i}`); }
    catch (e) { fails++; console.log(`FAIL ${relative(raiz, f)} #${i}: ${String(e.message || e).split('\n').slice(0,4).join(' | ')}`); }
  }
}
console.log(`TOTAL ${total} FAIL ${fails}`);
process.exit(fails ? 1 : 0);
