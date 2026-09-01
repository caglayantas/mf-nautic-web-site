# -*- coding: utf-8 -*-
import re, os

FILES = {
    "urunler/yapistirici-ve-mastikler.html": "yapistirici-ve-mastikler",
    "urunler/deniz-yaglayicilari.html": "deniz-yaglayicilari",
    "urunler/dolgu-macunlari.html": "dolgu-macunlari",
    "urunler/tikal-tef-gel.html": "tikal-tef-gel",
    "urunler/teak-deck.html": "teak-deck",
    "urunler/aletler-ve-aksesuarlar.html": "aletler-ve-aksesuarlar",
}

def find_matching_close(html, open_idx):
    # open_idx points at the '<' of the opening <div ...> tag we want to match
    depth = 0
    i = open_idx
    tag_re = re.compile(r"<(/?)div\b[^>]*?(/?)>")
    for m in tag_re.finditer(html, open_idx):
        closing, selfclose = m.group(1), m.group(2)
        if selfclose:
            continue
        if not closing:
            depth += 1
        else:
            depth -= 1
            if depth == 0:
                return m.end()
    raise ValueError("no matching close found")

for path, cat_slug in FILES.items():
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    marker = '<div class="prod-grid">'
    start = html.index(marker)
    end = find_matching_close(html, start)

    replacement = (
        '<div class="prod-grid" id="prod-grid" data-cat-slug="%s" data-base="">'
        '<div class="form-note">Ürünler yükleniyor...</div></div>' % cat_slug
    )
    html = html[:start] + replacement + html[end:]

    # inject supabase scripts before site.js include
    old_script = '<script src="../assets/js/site.js"></script>'
    new_script = (
        '<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2/dist/umd/supabase.min.js"></script>\n'
        '  <script src="../assets/js/mf-supabase.js"></script>\n'
        '  <script src="../assets/js/site.js"></script>\n'
        '  <script src="../assets/js/render-products.js"></script>'
    )
    assert old_script in html, path
    html = html.replace(old_script, new_script)

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("OK", path)
