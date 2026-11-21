#!/usr/bin/env python3
"""Valida links relativos e âncoras (estilo GitHub) em todos os arquivos Markdown do repositório.

Uso: python3 ferramentas/verificar_links.py [--externos]
    --externos  também lista os links externos (que não são acessados)."""
import os, re, sys, urllib.parse
from collections import Counter

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FENCE = re.compile(r'^(```|~~~)')
LINK = re.compile(r'(?<!!)\[(?:[^\[\]]|\[[^\]]*\])*\]\(([^()\s]+(?:\([^()]*\))?[^()\s]*)\)')
ANGLE = re.compile(r'<(https?://[^>]+)>')

def strip_code(text):
    out, infence = [], False
    for line in text.split('\n'):
        if FENCE.match(line.strip()):
            infence = not infence; out.append(''); continue
        out.append('' if infence else re.sub(r'`[^`]*`', lambda m: ' ' * len(m.group(0)) if '](' in m.group(0) else m.group(0), line))
    return '\n'.join(out)

def slug(h):
    h = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', h)
    h = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', h)
    h = re.sub(r'<[^>]+>', '', h)
    h = h.strip().lower()
    h = ''.join(c for c in h if c.isalnum() or c in ' -_')
    return h.replace(' ', '-')

_cache = {}
def anchors(path):
    if path in _cache: return _cache[path]
    text = open(path, encoding='utf-8').read()
    seen, res, infence = Counter(), set(), False
    for line in text.split('\n'):
        if FENCE.match(line.strip()): infence = not infence; continue
        if infence: continue
        m = re.match(r'^(#{1,6})\s+(.*?)\s*#*\s*$', line)
        if m:
            s = slug(m.group(2))
            res.add(s if seen[s] == 0 else f"{s}-{seen[s]}")
            seen[s] += 1
    _cache[path] = res
    return res

errors, total, external = [], 0, set()
for dp, dn, fn in os.walk(root):
    dn[:] = [d for d in dn if d not in ('.git', 'node_modules')]
    for f in fn:
        if not f.endswith('.md'): continue
        p = os.path.join(dp, f)
        text = strip_code(open(p, encoding='utf-8').read())
        for ln, line in enumerate(text.split('\n'), 1):
            for m in ANGLE.finditer(line): external.add(m.group(1))
            for m in LINK.finditer(line):
                tgt = m.group(1)
                if re.match(r'^(https?|mailto):', tgt): external.add(tgt); continue
                total += 1
                path_part, _, frag = tgt.partition('#')
                path_dec = urllib.parse.unquote(path_part)
                dest = os.path.normpath(os.path.join(dp, path_dec)) if path_dec else p
                rel = os.path.relpath(p, root)
                if ' ' in path_part:
                    errors.append(f"{rel}:{ln}: espaço não codificado em {tgt}")
                if not os.path.exists(dest):
                    errors.append(f"{rel}:{ln}: destino inexistente {tgt}"); continue
                if not dest.startswith(root):
                    errors.append(f"{rel}:{ln}: aponta para fora do repositório {tgt}"); continue
                if frag:
                    if os.path.isdir(dest) or not dest.endswith('.md'):
                        errors.append(f"{rel}:{ln}: âncora em não-Markdown {tgt}"); continue
                    if urllib.parse.unquote(frag).lower() not in anchors(dest):
                        errors.append(f"{rel}:{ln}: âncora inexistente #{urllib.parse.unquote(frag)} em {os.path.relpath(dest, root)}")

for e in errors: print("ERRO", e)
print(f"LINKS INTERNOS {total} · ERROS {len(errors)} · LINKS EXTERNOS DISTINTOS {len(external)}")
if '--externos' in sys.argv:
    for u in sorted(external): print("EXT", u)
sys.exit(1 if errors else 0)
