# -*- coding: utf-8 -*-
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------
# ICONS (minimal hand-authored feather-style outline icons)
# ---------------------------------------------------------------
ICONS = {
"chevron-down": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="chev"><polyline points="6 9 12 15 18 9"></polyline></svg>',
"menu": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>',
"phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.362 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.338 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>',
"mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16v16H4z" opacity="0"></path><path d="M22 6c0-1.1-.9-2-2-2H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V6z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>',
"map-pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>',
"arrow-right": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>',
"check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>',
"download": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>',
"file-text": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>',
"whatsapp": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.47 14.38c-.29-.15-1.72-.85-1.99-.95-.27-.1-.46-.15-.66.15-.2.29-.76.94-.93 1.14-.17.2-.34.22-.63.07-.29-.15-1.22-.45-2.33-1.44-.86-.77-1.44-1.71-1.61-2-.17-.29-.02-.45.13-.6.13-.13.29-.34.44-.51.15-.17.2-.29.29-.49.1-.2.05-.37-.02-.51-.07-.15-.66-1.59-.9-2.17-.24-.58-.48-.5-.66-.51-.17-.01-.37-.01-.56-.01-.2 0-.51.07-.78.37-.27.29-1.02 1-1.02 2.43 0 1.43 1.04 2.82 1.19 3.01.15.2 2.05 3.13 4.96 4.39.69.3 1.23.48 1.65.61.69.22 1.32.19 1.82.11.55-.08 1.72-.7 1.96-1.38.24-.68.24-1.26.17-1.38-.07-.12-.27-.2-.56-.34z"></path><path d="M12.02 2.01c-5.51 0-9.98 4.47-9.98 9.98 0 1.76.46 3.48 1.34 4.99L2 22l5.15-1.35a9.94 9.94 0 0 0 4.87 1.24h.01c5.51 0 9.98-4.47 9.98-9.98 0-2.67-1.04-5.18-2.93-7.07a9.93 9.93 0 0 0-7.06-2.83zm0 18.13h-.01a8.28 8.28 0 0 1-4.21-1.15l-.3-.18-3.06.8.82-2.98-.2-.31a8.26 8.26 0 0 1-1.27-4.42c0-4.56 3.71-8.27 8.28-8.27 2.21 0 4.29.86 5.85 2.42a8.2 8.2 0 0 1 2.42 5.86c0 4.56-3.72 8.23-8.32 8.23z"></path></svg>',
"anchor": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="5" r="3"></circle><line x1="12" y1="22" x2="12" y2="8"></line><path d="M5 12H2a10 10 0 0 0 20 0h-3"></path></svg>',
"droplet": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2.69s-7 7.44-7 12.31a7 7 0 0 0 14 0c0-4.87-7-12.31-7-12.31z"></path></svg>',
"layers": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 2 7 12 12 22 7 12 2"></polygon><polyline points="2 17 12 22 22 17"></polyline><polyline points="2 12 12 17 22 12"></polyline></svg>',
"tool": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"></path></svg>',
"package": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="16.5" y1="9.4" x2="7.5" y2="4.21"></line><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path><polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline><line x1="12" y1="22.08" x2="12" y2="12"></line></svg>',
"shield-check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path><polyline points="9 12 11 14 15 10"></polyline></svg>',
"clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>',
"truck": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="1" y="3" width="15" height="13"></rect><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"></polygon><circle cx="5.5" cy="18.5" r="2.5"></circle><circle cx="18.5" cy="18.5" r="2.5"></circle></svg>',
"users": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>',
"award": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="7"></circle><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"></polyline></svg>',
"instagram": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>',
"linkedin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg>',
"facebook": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path></svg>',
"x-close": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>',
"send": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>',
"plus": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>',
}

def icon(name, cls=""):
    svg = ICONS[name]
    if cls:
        svg = svg.replace('viewBox', 'class="%s" viewBox' % cls, 1)
    return svg

# ---------------------------------------------------------------
# NAV DATA
# ---------------------------------------------------------------
PRODUCT_CATS = [
    ("nav.products.adhesives", "urunler/yapistirici-ve-mastikler.html", "droplet", "Yapıştırıcı ve Mastikler"),
    ("nav.products.lubricants", "urunler/deniz-yaglayicilari.html", "droplet", "Deniz Yağlayıcıları"),
    ("nav.products.filler", "urunler/dolgu-macunlari.html", "layers", "Dolgu Macunları"),
    ("nav.products.tefgel", "urunler/tikal-tef-gel.html", "shield-check", "Tikal Tef-Gel"),
    ("nav.products.teak", "urunler/teak-deck.html", "anchor", "Teak Deck Sistemleri"),
    ("nav.products.tools", "urunler/aletler-ve-aksesuarlar.html", "tool", "Aletler ve Aksesuarlar"),
]

def d(depth, path):
    return depth + path

def HEAD(title, desc, depth, extra=""):
    return """<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>%s</title>
<meta name="description" content="%s">
<link rel="icon" href="%sassets/images/logo/mfnautic-logo.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="%sassets/css/site.css">
%s""" % (title, desc, depth, depth, extra)

def TOPBAR(depth):
    return """  <div class="topbar">
    <div class="container">
      <div class="topbar-links">
        <a href="tel:+905414558005">%s<span class="hide-mobile" data-i18n="topbar.phone">+90 541 455 80 05</span></a>
        <a href="mailto:levent@mf-nautic.com" class="hide-mobile">%s<span data-i18n="topbar.email">levent@mf-nautic.com</span></a>
        <span class="hide-mobile" style="opacity:.7" data-i18n="topbar.tag">Resmi Tikal Marine Systems Türkiye Distribütörü</span>
      </div>
      <div class="lang-switch">
        <button type="button" data-lang="tr">TR</button>
        <button type="button" data-lang="en">EN</button>
      </div>
    </div>
  </div>""" % (icon("phone"), icon("mail"))

def HEADER(depth, active=""):
    dropdown_items = "\n".join(
        '              <li><a href="%s"><span class="dot"></span><span data-i18n="%s">%s</span></a></li>' % (d(depth,p), key, label)
        for key,p,_,label in PRODUCT_CATS
    )
    return TOPBAR(depth) + """
  <header class="site-header">
    <div class="container">
      <a href="%s" class="brand">
        <img src="%sassets/images/logo/mfnautic-logo.jpg" alt="MF Nautic Turkey">
        <span class="brand-divider"></span>
        <span class="brand-powered"><img src="%sassets/images/logo/powered-by-tikal.jpg" alt="Powered by Tikal Marine Systems"></span>
      </a>
      <nav class="main-nav">
        <ul>
          <li><a class="nav-link" href="%s" data-i18n="nav.home">Anasayfa</a></li>
          <li class="has-dropdown">
            <a class="nav-link" href="%s"><span data-i18n="nav.products">Ürünler</span>%s</a>
            <div class="dropdown">
              <ul>
%s
              </ul>
            </div>
          </li>
          <li><a class="nav-link" href="%s" data-i18n="nav.docs">Teknik Dökümanlar</a></li>
          <li><a class="nav-link" href="%s" data-i18n="nav.about">Hakkımızda</a></li>
          <li><a class="nav-link" href="%s" data-i18n="nav.contact">İletişim</a></li>
        </ul>
      </nav>
      <div class="header-cta">
        <a href="https://wa.me/905414558005" target="_blank" rel="noopener" class="btn btn-primary btn-sm">%s<span data-i18n="header.cta">Teklif Al</span></a>
        <button type="button" class="burger" aria-label="Menu">%s</button>
      </div>
    </div>
  </header>""" % (
        d(depth,"index.html"), depth, depth,
        d(depth,"index.html"),
        d(depth,"urunler/index.html"), icon("chevron-down"),
        dropdown_items,
        d(depth,"dokumanlar.html"),
        d(depth,"hakkimizda.html"),
        d(depth,"iletisim.html"),
        icon("whatsapp"),
        icon("menu"),
    )

def FOOTER(depth):
    cats = "\n".join(
        '            <li><a href="%s" data-i18n="%s">%s</a></li>' % (d(depth,p), key, label)
        for key,p,_,label in PRODUCT_CATS
    )
    return """  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <img src="%sassets/images/logo/mfnautic-logo.jpg" alt="MF Nautic Turkey">
          <p data-i18n="footer.about.text">MF Nautic Yatçılık Ltd. Şti., Almanya merkezli Tikal Marine Systems GmbH'nin Türkiye'deki resmi distribütörüdür.</p>
          <div class="footer-powered"><img src="%sassets/images/logo/powered-by-tikal.jpg" alt="Tikal Marine Systems"></div>
          <div class="footer-social">
            <a href="https://wa.me/905414558005" target="_blank" rel="noopener" aria-label="WhatsApp">%s</a>
            <a href="#" aria-label="Instagram">%s</a>
            <a href="#" aria-label="LinkedIn">%s</a>
          </div>
        </div>
        <div class="footer-col">
          <h4 data-i18n="footer.products">Ürün Kategorileri</h4>
          <ul>
%s
          </ul>
        </div>
        <div class="footer-col">
          <h4 data-i18n="footer.company">Kurumsal</h4>
          <ul>
            <li><a href="%s" data-i18n="footer.company.about">Hakkımızda</a></li>
            <li><a href="%s" data-i18n="footer.company.docs">Teknik Dökümanlar</a></li>
            <li><a href="%s#bayilik" data-i18n="footer.company.dealers">Bayilik Başvurusu</a></li>
            <li><a href="%s" data-i18n="footer.company.contact">İletişim</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4 data-i18n="footer.contact.title">İletişim</h4>
          <ul class="footer-contact">
            <li>%s<span>Göcek Mahallesi, Likya Caddesi No:22<br>Fethiye / Muğla</span></li>
            <li>%s<a href="tel:+905414558005">+90 541 455 80 05</a></li>
            <li>%s<a href="mailto:levent@mf-nautic.com">levent@mf-nautic.com</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <div>&copy; <span class="js-year">2026</span> MF Nautic Yatçılık Ltd. Şti. — <span data-i18n="footer.rights">Tüm hakları saklıdır.</span></div>
        <div class="footer-legal">
          <a href="%s" data-i18n="footer.legal.privacy">Gizlilik Politikası</a>
          <a href="%s" data-i18n="footer.legal.terms">Kullanım Koşulları</a>
        </div>
      </div>
    </div>
  </footer>
  <a href="https://wa.me/905414558005" target="_blank" rel="noopener" class="wa-float" aria-label="WhatsApp">%s</a>""" % (
        depth, depth,
        icon("whatsapp"), icon("instagram"), icon("linkedin"),
        cats,
        d(depth,"hakkimizda.html"), d(depth,"dokumanlar.html"), d(depth,"hakkimizda.html"), d(depth,"iletisim.html"),
        icon("map-pin"), icon("phone"), icon("mail"),
        d(depth,"gizlilik-politikasi.html"), d(depth,"kullanim-kosullari.html"),
        icon("whatsapp"),
    )

SEP = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"></polyline></svg>'

def BREADCRUMB(depth, trail):
    """trail: list of (i18n_key_or_None, url_or_None, fallback_text)
       Last item should have url=None (current page)."""
    parts = ['<a href="%s" data-i18n="breadcrumb.home">Anasayfa</a>' % d(depth,"index.html")]
    for key, url, fallback in trail:
        parts.append(SEP)
        attr = ('data-i18n="%s"' % key) if key else ""
        if url:
            parts.append('<a href="%s" %s>%s</a>' % (url, attr, fallback))
        else:
            parts.append('<span class="current" %s>%s</span>' % (attr, fallback))
    return '<div class="breadcrumb">' + "\n".join(parts) + "</div>"

def PAGE_SCRIPT(i18n_json_var):
    return """  <script>
    window.PAGE_I18N = %s;
  </script>""" % i18n_json_var

def SITE_JS(depth):
    return '  <script src="%sassets/js/site.js"></script>' % depth

def PAGE(depth, title, desc, body, i18n_json, extra_head=""):
    return """<!DOCTYPE html>
<html lang="tr">
<head>
%s
</head>
<body>
%s
%s
%s
%s
</body>
</html>
""" % (HEAD(title, desc, depth, extra_head), HEADER(depth), body, FOOTER(depth), PAGE_SCRIPT(i18n_json) + "\n" + SITE_JS(depth))

def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", path)

import json

def j(dic):
    return json.dumps(dic, ensure_ascii=False, indent=2)

# ---------------------------------------------------------------
# Reusable content builders
# ---------------------------------------------------------------
def cat_card(depth, key_title, key_desc, url, icname, fallback_title, fallback_desc):
    return """      <a href="%s" class="cat-card">
        <div class="ic">%s</div>
        <h3 data-i18n="%s">%s</h3>
        <p data-i18n="%s">%s</p>
        <span class="go"><span data-i18n="cat.more">%s</span>%s</span>
      </a>""" % (url, icon(icname), key_title, fallback_title, key_desc, fallback_desc, "İncele", icon("arrow-right"))

CAT_DEFS = [
    ("adhesives", "urunler/yapistirici-ve-mastikler.html", "droplet",
     "Yapıştırıcı ve Mastikler", "Adhesives & Sealants",
     "MS Polimer esaslı, suya dayanıklı, yüksek mukavemetli yapıştırıcı ve mastik serisi.",
     "Water-resistant, high-strength MS Polymer adhesive and sealant range."),
    ("lubricants", "urunler/deniz-yaglayicilari.html", "droplet",
     "Deniz Yağlayıcıları", "Marine Lubricants",
     "Deniz ortamına özel geliştirilmiş yüksek performanslı gres ve yağlayıcılar.",
     "High-performance greases and lubricants engineered for the marine environment."),
    ("filler", "urunler/dolgu-macunlari.html", "layers",
     "Dolgu Macunları", "Fillers",
     "Hızlı kuruyan, kolay zımparalanan profesyonel tekne dolgu macunları.",
     "Fast-curing, easy-to-sand professional boat filler putties."),
    ("tefgel", "urunler/tikal-tef-gel.html", "shield-check",
     "Tikal Tef-Gel", "Tikal Tef-Gel",
     "Metal bağlantı elemanlarını elektroliz korozyonuna karşı koruyan özel gres.",
     "Special anti-seize gel that protects metal fasteners against galvanic corrosion."),
    ("teak", "urunler/teak-deck.html", "anchor",
     "Teak Deck Sistemleri", "Teak Deck Systems",
     "Teak güverte bakımı, onarımı ve temizliği için komple ürün gamı.",
     "A complete product range for teak deck maintenance, repair and cleaning."),
    ("tools", "urunler/aletler-ve-aksesuarlar.html", "tool",
     "Aletler ve Aksesuarlar", "Tools & Accessories",
     "Uygulama tabancaları, derz aletleri ve yüzey temizleme ürünleri.",
     "Application guns, joint tools and surface cleaning products."),
]

def cat_grid(depth, columns=3):
    cards = []
    for key, path, ic, tr_t, en_t, tr_d, en_d in CAT_DEFS:
        cards.append(cat_card(depth, "cat.%s.title"%key, "cat.%s.desc"%key, d(depth,path), ic, tr_t, tr_d))
    cls = "cat-grid" if columns==3 else "cat-grid"
    return '<div class="%s">\n%s\n      </div>' % (cls, "\n".join(cards))

def cat_i18n_entries(lang):
    out = {}
    for key, path, ic, tr_t, en_t, tr_d, en_d in CAT_DEFS:
        out["cat.%s.title"%key] = tr_t if lang=="tr" else en_t
        out["cat.%s.desc"%key] = tr_d if lang=="tr" else en_d
    out["cat.more"] = "İncele" if lang=="tr" else "Explore"
    return out

def prod_card(depth, url, icname, tag, key_title, tr_title, en_title, key_desc, tr_desc, en_desc, cta_key="prod.cta", tr_cta="Detayları Gör", en_cta="View Details"):
    tag_html = ('<span class="tag">%s</span>' % tag) if tag else ""
    return """      <div class="prod-card">
        <div class="prod-media">%s%s</div>
        <div class="prod-body">
          <h3 data-i18n="%s">%s</h3>
          <p data-i18n="%s">%s</p>
          <div class="prod-foot">
            <a href="%s"><span data-i18n="%s">%s</span>%s</a>
          </div>
        </div>
      </div>""" % (tag_html, icon("package"), key_title, tr_title, key_desc, tr_desc, url, cta_key, tr_cta, icon("arrow-right"))

# =================================================================
# HOME PAGE
# =================================================================
def build_home():
    depth = ""
    body = """  <section class="hero">
    <div class="container">
      <div class="hero-copy">
        <div class="hero-badge"><img src="assets/images/logo/powered-by-tikal.jpg" alt="Tikal Marine Systems"></div>
        <h1 data-i18n-html="hero.title">Deniz ve Yat Bakımında <em>Almanya Kalitesi</em></h1>
        <p class="lead" data-i18n="hero.lead">MF Nautic, Tikal Marine Systems GmbH'nin Türkiye'deki resmi distribütörü olarak; yapıştırıcı, mastik, teak deck bakım ürünleri ve deniz yağlayıcılarını profesyonel tersane ve yat sahiplerine ulaştırıyor.</p>
        <div class="hero-actions">
          <a href="urunler/index.html" class="btn btn-primary"><span data-i18n="hero.cta1">Ürünleri İncele</span>%s</a>
          <a href="https://wa.me/905414558005" target="_blank" rel="noopener" class="btn btn-outline-light">%s<span data-i18n="hero.cta2">WhatsApp'tan Yaz</span></a>
        </div>
        <div class="hero-stats">
          <div><strong>1</strong><span data-i18n="hero.stat1">Yetkili Distribütör</span></div>
          <div><strong>6</strong><span data-i18n="hero.stat2">Ürün Kategorisi</span></div>
          <div><strong data-i18n="hero.stat3v">Almanya</strong><span data-i18n="hero.stat3">Menşei Kalite</span></div>
          <div><strong>7/24</strong><span data-i18n="hero.stat4">WhatsApp Destek</span></div>
        </div>
      </div>
      <div class="hero-visual">
        <div class="hero-panel">
          <div class="hero-panel-grid">
            <div class="hero-chip"><div class="ic">%s</div><b data-i18n="cat.adhesives.title">Yapıştırıcı ve Mastikler</b><span data-i18n="hero.chip1">MS Polimer teknolojisi</span></div>
            <div class="hero-chip"><div class="ic">%s</div><b data-i18n="cat.teak.title">Teak Deck Sistemleri</b><span data-i18n="hero.chip2">Bakım &amp; onarım</span></div>
            <div class="hero-chip"><div class="ic">%s</div><b data-i18n="cat.tefgel.title">Tikal Tef-Gel</b><span data-i18n="hero.chip3">Korozyon koruması</span></div>
            <div class="hero-chip"><div class="ic">%s</div><b data-i18n="cat.tools.title">Aletler ve Aksesuarlar</b><span data-i18n="hero.chip4">Profesyonel uygulama</span></div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="trust-strip">
    <div class="container">
      <div class="trust-item"><div class="ic">%s</div><div><b data-i18n="trust1.t">Yetkili Distribütör</b><span data-i18n="trust1.s">Türkiye genelinde tek yetkili satış noktası</span></div></div>
      <div class="trust-item"><div class="ic">%s</div><div><b data-i18n="trust2.t">Orijinal Ürün Garantisi</b><span data-i18n="trust2.s">%%100 orijinal, Almanya menşeli ürün</span></div></div>
      <div class="trust-item"><div class="ic">%s</div><div><b data-i18n="trust3.t">Türkiye Geneli Kargo</b><span data-i18n="trust3.s">Hızlı ve güvenli sevkiyat</span></div></div>
      <div class="trust-item"><div class="ic">%s</div><div><b data-i18n="trust4.t">Teknik Danışmanlık</b><span data-i18n="trust4.s">Uygulama öncesi &amp; sonrası destek</span></div></div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head text-center">
        <div class="eyebrow" data-i18n="catsec.eyebrow">Ürün Gamı</div>
        <h2 data-i18n="catsec.title">Tikal Marine Systems Ürün Kategorileri</h2>
        <p data-i18n="catsec.desc">Yapıştırıcıdan teak güverte bakımına, deniz yağlayıcısından uygulama aletlerine kadar denizcilik sektörünün ihtiyaç duyduğu her şey.</p>
      </div>
      %s
    </div>
  </section>

  <section class="section section--alt">
    <div class="container">
      <div class="split">
        <div>
          <div class="eyebrow" data-i18n="why1.eyebrow">Neden Tikal Marine Systems?</div>
          <h2 data-i18n="why1.title">1980'lerden bu yana Almanya'da üretilen deniz kimyasalları</h2>
          <p data-i18n="why1.lead">Tikal Marine Systems GmbH, yapıştırıcı, mastik ve bakım ürünlerini kendi laboratuvarında geliştirip üreten, Avrupa tersaneleri ve yat üreticileri tarafından tercih edilen bir marka.</p>
          <ul class="check-list">
            <li><span class="tick">%s</span><span data-i18n="why1.li1">Deniz suyu, UV ve kimyasallara karşı test edilmiş formüller</span></li>
            <li><span class="tick">%s</span><span data-i18n="why1.li2">Her parti/lot için laboratuvarda son kontrol ve tam izlenebilirlik</span></li>
            <li><span class="tick">%s</span><span data-i18n="why1.li3">Ahşap, alüminyum, çelik ve GRP dahil geniş malzeme uyumluluğu</span></li>
            <li><span class="tick">%s</span><span data-i18n="why1.li4">Avrupa çapında tersaneler ve yat üreticileri tarafından kullanılıyor</span></li>
          </ul>
          <a href="urunler/index.html" class="btn btn-dark"><span data-i18n="why1.cta">Ürün Kataloğuna Göz At</span>%s</a>
        </div>
        <div class="split-media">%s</div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="split reverse">
        <div>
          <div class="eyebrow" data-i18n="why2.eyebrow">MF Nautic Farkı</div>
          <h2 data-i18n="why2.title">Fethiye merkezli, Türkiye geneline hızlı çözüm ortağı</h2>
          <p data-i18n="why2.lead">Göcek/Fethiye merkezimizden, tersaneler, yat işletmeleri ve profesyonel uygulayıcılar için stok, teknik destek ve hızlı sevkiyat sağlıyoruz.</p>
          <ul class="check-list">
            <li><span class="tick">%s</span><span data-i18n="why2.li1">Profesyonel tersane ve yat işletmelerine özel fiyatlandırma</span></li>
            <li><span class="tick">%s</span><span data-i18n="why2.li2">Uygulama öncesi ve sonrası teknik danışmanlık</span></li>
            <li><span class="tick">%s</span><span data-i18n="why2.li3">WhatsApp üzerinden anlık teknik destek hattı</span></li>
            <li><span class="tick">%s</span><span data-i18n="why2.li4">Türkiye'nin her noktasına kargo ile teslimat</span></li>
          </ul>
          <a href="iletisim.html" class="btn btn-dark"><span data-i18n="why2.cta">Bizimle İletişime Geçin</span>%s</a>
        </div>
        <div class="split-media">%s</div>
      </div>
    </div>
  </section>

  <section class="section section--alt">
    <div class="container">
      <div class="section-head text-center">
        <div class="eyebrow" data-i18n="steps.eyebrow">Sipariş Süreci</div>
        <h2 data-i18n="steps.title">Nasıl Sipariş Verilir?</h2>
      </div>
      <div class="steps">
        <div class="step"><div class="n">1</div><h4 data-i18n="steps.s1.t">Ürünü Seçin</h4><p data-i18n="steps.s1.d">Kategori sayfalarından ihtiyacınıza uygun ürünü belirleyin.</p></div>
        <div class="step"><div class="n">2</div><h4 data-i18n="steps.s2.t">Bize Ulaşın</h4><p data-i18n="steps.s2.d">WhatsApp, e-posta veya iletişim formuyla bize yazın.</p></div>
        <div class="step"><div class="n">3</div><h4 data-i18n="steps.s3.t">Teklif ve Onay</h4><p data-i18n="steps.s3.d">Size özel fiyat teklifi ve stok durumunu paylaşalım.</p></div>
        <div class="step"><div class="n">4</div><h4 data-i18n="steps.s4.t">Teslimat</h4><p data-i18n="steps.s4.d">Siparişiniz Türkiye'nin her yerine güvenle gönderilsin.</p></div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="cta-band">
        <div>
          <h2 data-i18n="cta.title">Projenize uygun ürünü birlikte belirleyelim</h2>
          <p data-i18n="cta.desc">Teknik ekibimiz doğru ürün seçimi ve uygulama konusunda size yardımcı olsun.</p>
        </div>
        <div class="cta-actions">
          <a href="iletisim.html" class="btn btn-primary"><span data-i18n="cta.btn1">Teklif Al</span>%s</a>
          <a href="https://wa.me/905414558005" target="_blank" rel="noopener" class="btn btn-outline-light">%s<span data-i18n="cta.btn2">WhatsApp</span></a>
        </div>
      </div>
    </div>
  </section>""" % (
        icon("arrow-right"), icon("whatsapp"),
        icon("droplet"), icon("anchor"), icon("shield-check"), icon("tool"),
        icon("award"), icon("shield-check"), icon("truck"), icon("users"),
        cat_grid(depth),
        icon("check"), icon("check"), icon("check"), icon("check"), icon("arrow-right"), icon("anchor", "cls"),
        icon("check"), icon("check"), icon("check"), icon("check"), icon("arrow-right"), icon("users", "cls"),
        icon("arrow-right"), icon("whatsapp"),
    )

    pi_tr = {
        "hero.title": "Deniz ve Yat Bakımında <em>Almanya Kalitesi</em>",
        "hero.lead": "MF Nautic, Tikal Marine Systems GmbH'nin Türkiye'deki resmi distribütörü olarak; yapıştırıcı, mastik, teak deck bakım ürünleri ve deniz yağlayıcılarını profesyonel tersane ve yat sahiplerine ulaştırıyor.",
        "hero.cta1": "Ürünleri İncele", "hero.cta2": "WhatsApp'tan Yaz",
        "hero.stat1": "Yetkili Distribütör", "hero.stat2": "Ürün Kategorisi",
        "hero.stat3v": "Almanya", "hero.stat3": "Menşei Kalite", "hero.stat4": "WhatsApp Destek",
        "hero.chip1": "MS Polimer teknolojisi", "hero.chip2": "Bakım & onarım",
        "hero.chip3": "Korozyon koruması", "hero.chip4": "Profesyonel uygulama",
        "trust1.t": "Yetkili Distribütör", "trust1.s": "Türkiye genelinde tek yetkili satış noktası",
        "trust2.t": "Orijinal Ürün Garantisi", "trust2.s": "%100 orijinal, Almanya menşeli ürün",
        "trust3.t": "Türkiye Geneli Kargo", "trust3.s": "Hızlı ve güvenli sevkiyat",
        "trust4.t": "Teknik Danışmanlık", "trust4.s": "Uygulama öncesi & sonrası destek",
        "catsec.eyebrow": "Ürün Gamı", "catsec.title": "Tikal Marine Systems Ürün Kategorileri",
        "catsec.desc": "Yapıştırıcıdan teak güverte bakımına, deniz yağlayıcısından uygulama aletlerine kadar denizcilik sektörünün ihtiyaç duyduğu her şey.",
        "why1.eyebrow": "Neden Tikal Marine Systems?",
        "why1.title": "1980'lerden bu yana Almanya'da üretilen deniz kimyasalları",
        "why1.lead": "Tikal Marine Systems GmbH, yapıştırıcı, mastik ve bakım ürünlerini kendi laboratuvarında geliştirip üreten, Avrupa tersaneleri ve yat üreticileri tarafından tercih edilen bir marka.",
        "why1.li1": "Deniz suyu, UV ve kimyasallara karşı test edilmiş formüller",
        "why1.li2": "Her parti/lot için laboratuvarda son kontrol ve tam izlenebilirlik",
        "why1.li3": "Ahşap, alüminyum, çelik ve GRP dahil geniş malzeme uyumluluğu",
        "why1.li4": "Avrupa çapında tersaneler ve yat üreticileri tarafından kullanılıyor",
        "why1.cta": "Ürün Kataloğuna Göz At",
        "why2.eyebrow": "MF Nautic Farkı",
        "why2.title": "Fethiye merkezli, Türkiye geneline hızlı çözüm ortağı",
        "why2.lead": "Göcek/Fethiye merkezimizden, tersaneler, yat işletmeleri ve profesyonel uygulayıcılar için stok, teknik destek ve hızlı sevkiyat sağlıyoruz.",
        "why2.li1": "Profesyonel tersane ve yat işletmelerine özel fiyatlandırma",
        "why2.li2": "Uygulama öncesi ve sonrası teknik danışmanlık",
        "why2.li3": "WhatsApp üzerinden anlık teknik destek hattı",
        "why2.li4": "Türkiye'nin her noktasına kargo ile teslimat",
        "why2.cta": "Bizimle İletişime Geçin",
        "steps.eyebrow": "Sipariş Süreci", "steps.title": "Nasıl Sipariş Verilir?",
        "steps.s1.t": "Ürünü Seçin", "steps.s1.d": "Kategori sayfalarından ihtiyacınıza uygun ürünü belirleyin.",
        "steps.s2.t": "Bize Ulaşın", "steps.s2.d": "WhatsApp, e-posta veya iletişim formuyla bize yazın.",
        "steps.s3.t": "Teklif ve Onay", "steps.s3.d": "Size özel fiyat teklifi ve stok durumunu paylaşalım.",
        "steps.s4.t": "Teslimat", "steps.s4.d": "Siparişiniz Türkiye'nin her yerine güvenle gönderilsin.",
        "cta.title": "Projenize uygun ürünü birlikte belirleyelim",
        "cta.desc": "Teknik ekibimiz doğru ürün seçimi ve uygulama konusunda size yardımcı olsun.",
        "cta.btn1": "Teklif Al", "cta.btn2": "WhatsApp",
    }
    pi_tr.update(cat_i18n_entries("tr"))
    pi_en = {
        "hero.title": "German Engineering for <em>Marine Maintenance</em>",
        "hero.lead": "As the official Turkish distributor of Tikal Marine Systems GmbH, MF Nautic supplies adhesives, sealants, teak deck maintenance products and marine lubricants to professional shipyards and yacht owners.",
        "hero.cta1": "Explore Products", "hero.cta2": "Message us on WhatsApp",
        "hero.stat1": "Authorized Distributor", "hero.stat2": "Product Categories",
        "hero.stat3v": "Germany", "hero.stat3": "Country of Origin", "hero.stat4": "WhatsApp Support",
        "hero.chip1": "MS Polymer technology", "hero.chip2": "Maintenance & repair",
        "hero.chip3": "Corrosion protection", "hero.chip4": "Professional application",
        "trust1.t": "Authorized Distributor", "trust1.s": "The sole authorized sales point in Türkiye",
        "trust2.t": "Genuine Product Guarantee", "trust2.s": "100% genuine, made in Germany",
        "trust3.t": "Nationwide Shipping", "trust3.s": "Fast and secure delivery across Türkiye",
        "trust4.t": "Technical Consultancy", "trust4.s": "Support before & after application",
        "catsec.eyebrow": "Product Range", "catsec.title": "Tikal Marine Systems Product Categories",
        "catsec.desc": "Everything the marine industry needs — from adhesives to teak deck care, marine lubricants to application tools.",
        "why1.eyebrow": "Why Tikal Marine Systems?",
        "why1.title": "Marine chemicals manufactured in Germany since the 1980s",
        "why1.lead": "Tikal Marine Systems GmbH develops and manufactures its adhesives, sealants and maintenance products in-house, trusted by shipyards and yacht builders across Europe.",
        "why1.li1": "Formulas tested against seawater, UV and chemicals",
        "why1.li2": "Final laboratory inspection and full batch traceability",
        "why1.li3": "Broad material compatibility including wood, aluminium, steel and GRP",
        "why1.li4": "Used by shipyards and yacht builders throughout Europe",
        "why1.cta": "Browse the Product Catalogue",
        "why2.eyebrow": "The MF Nautic Difference",
        "why2.title": "Based in Fethiye, a fast partner for all of Türkiye",
        "why2.lead": "From our Göcek/Fethiye base, we provide stock, technical support and fast shipping to shipyards, yacht businesses and professional applicators.",
        "why2.li1": "Special pricing for professional shipyards and yacht businesses",
        "why2.li2": "Technical consultancy before and after application",
        "why2.li3": "Instant technical support via WhatsApp",
        "why2.li4": "Delivery by courier anywhere in Türkiye",
        "why2.cta": "Get in Touch",
        "steps.eyebrow": "Order Process", "steps.title": "How to Order",
        "steps.s1.t": "Choose a Product", "steps.s1.d": "Find the right product on our category pages.",
        "steps.s2.t": "Contact Us", "steps.s2.d": "Reach us via WhatsApp, email or the contact form.",
        "steps.s3.t": "Quote & Confirmation", "steps.s3.d": "We share a tailored price quote and stock availability.",
        "steps.s4.t": "Delivery", "steps.s4.d": "Your order is safely shipped anywhere in Türkiye.",
        "cta.title": "Let's find the right product for your project",
        "cta.desc": "Our technical team can help you choose the right product and application method.",
        "cta.btn1": "Get a Quote", "cta.btn2": "WhatsApp",
    }
    pi_en.update(cat_i18n_entries("en"))

    i18n_js = "{\n  tr: %s,\n  en: %s\n}" % (j(pi_tr), j(pi_en))
    html = PAGE(depth,
        "MF Nautic Turkey | Tikal Marine Systems Türkiye Distribütörü",
        "MF Nautic Yatçılık — Tikal Marine Systems GmbH'nin Türkiye'deki resmi distribütörü. Yapıştırıcı, mastik, teak deck bakım ürünleri ve deniz yağlayıcıları.",
        body, i18n_js)
    write("index.html", html)

from urllib.parse import quote

def wa_link(text_tr):
    return "https://wa.me/905414558005?text=" + quote(text_tr)

# =================================================================
# PRODUCTS INDEX (urunler/index.html)
# =================================================================
def build_urunler_index():
    depth = "../"
    bc = BREADCRUMB(depth, [("nav.products", None, "Ürünler")])
    body = """  <section class="page-hero">
    <div class="container">
      %s
      <h1 data-i18n="pindex.title">Ürünlerimiz</h1>
      <p data-i18n="pindex.desc">Tikal Marine Systems GmbH'nin Almanya'da üretilen yapıştırıcı, mastik, teak deck bakım ürünleri ve deniz yağlayıcıları — MF Nautic güvencesiyle Türkiye'de.</p>
    </div>
  </section>
  <section class="section">
    <div class="container">
      %s
    </div>
  </section>
  <section class="section section--alt">
    <div class="container">
      <div class="cta-band">
        <div>
          <h2 data-i18n="pindex.cta.title">Aradığınız ürünü bulamadınız mı?</h2>
          <p data-i18n="pindex.cta.desc">Tikal'in tam ürün gamı hakkında bilgi almak için teknik ekibimizle iletişime geçin.</p>
        </div>
        <div class="cta-actions">
          <a href="%s" class="btn btn-primary"><span data-i18n="pindex.cta.btn1">İletişime Geç</span>%s</a>
          <a href="%s" target="_blank" rel="noopener" class="btn btn-outline-light">%s<span data-i18n="pindex.cta.btn2">WhatsApp</span></a>
        </div>
      </div>
    </div>
  </section>""" % (bc, cat_grid(depth), d(depth,"iletisim.html"), icon("arrow-right"),
                    wa_link("Merhaba, Tikal ürün gamı hakkında bilgi almak istiyorum."), icon("whatsapp"))

    pi_tr = {
        "pindex.title": "Ürünlerimiz",
        "pindex.desc": "Tikal Marine Systems GmbH'nin Almanya'da üretilen yapıştırıcı, mastik, teak deck bakım ürünleri ve deniz yağlayıcıları — MF Nautic güvencesiyle Türkiye'de.",
        "pindex.cta.title": "Aradığınız ürünü bulamadınız mı?",
        "pindex.cta.desc": "Tikal'in tam ürün gamı hakkında bilgi almak için teknik ekibimizle iletişime geçin.",
        "pindex.cta.btn1": "İletişime Geç", "pindex.cta.btn2": "WhatsApp",
    }
    pi_tr.update(cat_i18n_entries("tr"))
    pi_en = {
        "pindex.title": "Our Products",
        "pindex.desc": "Adhesives, sealants, teak deck maintenance products and marine lubricants manufactured by Tikal Marine Systems GmbH in Germany — available in Türkiye through MF Nautic.",
        "pindex.cta.title": "Can't find what you're looking for?",
        "pindex.cta.desc": "Contact our technical team to learn about Tikal's full product range.",
        "pindex.cta.btn1": "Get in Touch", "pindex.cta.btn2": "WhatsApp",
    }
    pi_en.update(cat_i18n_entries("en"))
    i18n_js = "{\n  tr: %s,\n  en: %s\n}" % (j(pi_tr), j(pi_en))
    html = PAGE(depth, "Ürünlerimiz | MF Nautic Turkey", "Tikal Marine Systems ürün kategorileri: yapıştırıcı, mastik, teak deck, deniz yağlayıcıları, Tef-Gel, aletler.", body, i18n_js)
    write("urunler/index.html", html)

# =================================================================
# GENERIC CATEGORY PAGE
# =================================================================
def build_category(slug, cat_key, cat_icon, tr_title, en_title, tr_intro, en_intro, products, meta_desc):
    depth = "../"
    bc = BREADCRUMB(depth, [("nav.products", d(depth,"urunler/index.html"), "Ürünler"), (cat_key, None, tr_title)])

    cards = []
    for p in products:
        tag_html = ('<span class="tag" data-i18n="%s.tag">%s</span>' % (p["id"], p["tag_tr"])) if p.get("tag_tr") else ""
        cta_key = "%s.cta" % p["id"]
        cards.append("""      <div class="prod-card">
        <div class="prod-media">%s%s</div>
        <div class="prod-body">
          <h3 data-i18n="%s.title">%s</h3>
          <p data-i18n="%s.desc">%s</p>
          <div class="prod-foot">
            <a href="%s"%s><span data-i18n="%s">%s</span>%s</a>
          </div>
        </div>
      </div>""" % (
            tag_html, icon(p.get("icon","package")),
            p["id"], p["tr_title"],
            p["id"], p["tr_desc"],
            p["url"],
            ' target="_blank" rel="noopener"' if p["url"].startswith("http") else "",
            cta_key, p["cta_tr"], icon("arrow-right"),
        ))

    body = """  <section class="page-hero">
    <div class="container">
      %s
      <h1 data-i18n="%s.h1">%s</h1>
      <p data-i18n="%s.lead">%s</p>
    </div>
  </section>
  <section class="section">
    <div class="container">
      <div class="prod-grid">
%s
      </div>
    </div>
  </section>
  <section class="section section--alt">
    <div class="container">
      <div class="cta-band">
        <div>
          <h2 data-i18n="catp.cta.title">Teknik bilgi formu (TDS) mi lazım?</h2>
          <p data-i18n="catp.cta.desc">Bu kategorideki ürünlerin güncel teknik veri formları için bize ulaşın, size hemen iletelim.</p>
        </div>
        <div class="cta-actions">
          <a href="%s" class="btn btn-primary"><span data-i18n="catp.cta.btn1">Teknik Döküman İste</span>%s</a>
          <a href="%s" class="btn btn-outline-light"><span data-i18n="catp.cta.btn2">Tüm Ürünler</span>%s</a>
        </div>
      </div>
    </div>
  </section>""" % (
        bc, cat_key, tr_title, cat_key+".lead", tr_intro,
        "\n".join(cards),
        d(depth,"dokumanlar.html"), icon("arrow-right"),
        d(depth,"urunler/index.html"), icon("arrow-right"),
    )

    pi_tr = {cat_key: tr_title, cat_key+".lead": tr_intro,
              "catp.cta.title": "Teknik bilgi formu (TDS) mi lazım?",
              "catp.cta.desc": "Bu kategorideki ürünlerin güncel teknik veri formları için bize ulaşın, size hemen iletelim.",
              "catp.cta.btn1": "Teknik Döküman İste", "catp.cta.btn2": "Tüm Ürünler"}
    pi_en = {cat_key: en_title, cat_key+".lead": en_intro,
              "catp.cta.title": "Need a technical data sheet (TDS)?",
              "catp.cta.desc": "Contact us for the latest technical data sheets of the products in this category — we'll send them right away.",
              "catp.cta.btn1": "Request Technical Documents", "catp.cta.btn2": "All Products"}
    for p in products:
        pi_tr[p["id"]+".title"] = p["tr_title"]; pi_en[p["id"]+".title"] = p["en_title"]
        pi_tr[p["id"]+".desc"] = p["tr_desc"];   pi_en[p["id"]+".desc"] = p["en_desc"]
        pi_tr[p["id"]+".cta"] = p["cta_tr"];     pi_en[p["id"]+".cta"] = p["cta_en"]
        if p.get("tag_tr"):
            pi_tr[p["id"]+".tag"] = p["tag_tr"]; pi_en[p["id"]+".tag"] = p.get("tag_en", p["tag_tr"])

    i18n_js = "{\n  tr: %s,\n  en: %s\n}" % (j(pi_tr), j(pi_en))
    html = PAGE(depth, "%s | MF Nautic Turkey" % tr_title, meta_desc, body, i18n_js)
    write("urunler/%s.html" % slug, html)

# =================================================================
# CATEGORY DATA + BUILD CALLS
# =================================================================
def P(id, icon, tr_title, en_title, tr_desc, en_desc, url, cta_tr="Bilgi İste", cta_en="Request Info", tag_tr=None, tag_en=None):
    o = dict(id=id, icon=icon, tr_title=tr_title, en_title=en_title, tr_desc=tr_desc, en_desc=en_desc,
              url=url, cta_tr=cta_tr, cta_en=cta_en)
    if tag_tr: o["tag_tr"]=tag_tr; o["tag_en"]=tag_en or tag_tr
    return o

def build_all_categories():
    # 1) Yapıştırıcı ve Mastikler
    build_category(
        "yapistirici-ve-mastikler", "cat.adhesives.title", "droplet",
        "Yapıştırıcı ve Mastikler", "Adhesives & Sealants",
        "Tikalflex serisi, MS Polimer teknolojisiyle geliştirilmiş; ahşap, alüminyum, çelik ve GRP yüzeylerde yüksek mukavemetli, suya ve deniz koşullarına dayanıklı yapıştırma ve derzleme çözümleri sunar.",
        "The Tikalflex range is built on MS Polymer technology, offering high-strength, water- and weather-resistant bonding and sealing solutions for wood, aluminium, steel and GRP surfaces.",
        [
            P("tikalflex-contact-12", "droplet", "Tikalflex Contact 12", "Tikalflex Contact 12",
              "Küçülme yapmayan, çok güçlü, suya dayanıklı MS Polimer yapıştırıcı. Ahşap, alüminyum, çelik ve GRP yüzeylerde profesyonel yapıştırma için idealdir.",
              "A shrink-free, very strong, waterproof MS Polymer adhesive — ideal for professional bonding on wood, aluminium, steel and GRP.",
              "tikalflex-contact-12.html", "Detayları Gör", "View Details", "Öne Çıkan Ürün", "Featured Product"),
            P("tikalflex-family", "layers", "Tikalflex Yapıştırıcı ve Mastik Ailesi", "Tikalflex Adhesive & Sealant Range",
              "Farklı sertlik, kürleşme hızı ve uygulama alanlarına sahip tam Tikalflex serisi için teknik ekibimizle iletişime geçin.",
              "Contact our technical team to learn about the full Tikalflex range, with different hardness, cure speeds and applications.",
              wa_link("Merhaba, Tikalflex yapıştırıcı/mastik ürün ailesi hakkında bilgi almak istiyorum.")),
        ],
        "Tikalflex MS Polimer yapıştırıcı ve mastik serisi — Tikal Marine Systems Türkiye distribütörü MF Nautic."
    )

    # 2) Deniz Yağlayıcıları
    build_category(
        "deniz-yaglayicilari", "cat.lubricants.title", "droplet",
        "Deniz Yağlayıcıları", "Marine Lubricants",
        "Deniz ortamının zorlu koşullarına — tuzlu su, nem ve yüksek yük — dayanacak şekilde geliştirilmiş yüksek performanslı gres ve yağlayıcılar.",
        "High-performance greases and lubricants engineered to withstand the harsh conditions of the marine environment — salt water, moisture and high loads.",
        [
            P("hp-mg", "droplet", "HP-MG Deniz Gresi", "HP-MG Marine Grease",
              "Deniz ortamı için geliştirilmiş, korozyona ve suya karşı yüksek dayanım gösteren özel performans gresi. Vinç, ırgat ve hareketli metal aksamlarda kullanılır.",
              "A special high-performance grease developed for the marine environment, with strong resistance to corrosion and water — used on winches, windlasses and moving metal parts.",
              wa_link("Merhaba, HP-MG deniz gresi hakkında bilgi almak istiyorum.")),
        ],
        "HP-MG deniz gresi ve Tikal Marine Systems yağlayıcı ürün gamı — MF Nautic Türkiye distribütörlüğü."
    )

    # 3) Dolgu Macunları
    build_category(
        "dolgu-macunlari", "cat.filler.title", "layers",
        "Dolgu Macunları", "Fillers",
        "Fast Patch serisi, tekne gövde ve güverte onarımlarında hızlı kürleşme ve kolay zımparalama imkânı sunan profesyonel dolgu macunlarıdır.",
        "The Fast Patch range offers professional filler putties with fast curing and easy sanding for hull and deck repairs.",
        [
            P("fast-patch", "layers", "Fast Patch", "Fast Patch",
              "Hızlı kuruyan, kolay zımparalanabilen, tekne gövde ve güverte onarımları için profesyonel dolgu macunu.",
              "A fast-curing, easy-to-sand professional filler putty for hull and deck repairs.",
              wa_link("Merhaba, Fast Patch dolgu macunu hakkında bilgi almak istiyorum.")),
            P("fast-patch-light", "layers", "Fast Patch LIGHT", "Fast Patch LIGHT",
              "Fast Patch'in daha hafif, düşük yoğunluklu versiyonu; büyük yüzey onarımlarında daha az ağırlık artışı sağlar.",
              "A lighter, low-density version of Fast Patch — adds less weight on larger surface repairs.",
              wa_link("Merhaba, Fast Patch LIGHT dolgu macunu hakkında bilgi almak istiyorum.")),
        ],
        "Fast Patch ve Fast Patch LIGHT tekne dolgu macunları — Tikal Marine Systems, MF Nautic Türkiye distribütörlüğü."
    )

    # 4) Tikal Tef-Gel
    build_category(
        "tikal-tef-gel", "cat.tefgel.title", "shield-check",
        "Tikal Tef-Gel", "Tikal Tef-Gel",
        "Farklı metallerin bir arada kullanıldığı deniz ortamındaki bağlantı elemanlarını elektrolitik (galvanik) korozyona karşı koruyan özel bir bakım ürünüdür.",
        "A special maintenance product that protects fasteners used in mixed-metal marine environments against galvanic corrosion.",
        [
            P("tef-gel", "shield-check", "Tikal Tef-Gel", "Tikal Tef-Gel",
              "Vida, cıvata, pervane mili gibi metal bağlantı elemanlarını elektrolitik korozyona karşı koruyan, sökülüp takılmayı kolaylaştıran özel anti-sızdırmazlık gresi.",
              "A special anti-seize gel that protects fasteners such as screws, bolts and propeller shafts against galvanic corrosion and makes disassembly easier.",
              wa_link("Merhaba, Tikal Tef-Gel hakkında bilgi almak istiyorum.")),
        ],
        "Tikal Tef-Gel — deniz ortamında metal bağlantı elemanları için korozyon koruması. MF Nautic Türkiye distribütörlüğü."
    )

    # 5) Teak Deck Sistemleri
    build_category(
        "teak-deck", "cat.teak.title", "anchor",
        "Teak Deck Sistemleri", "Teak Deck Systems",
        "Teak güverte yapıştırma, derzleme, onarım, aktivasyon ve temizlik ihtiyaçlarınızın tamamı için komple bir sistem: TSC, TLB Flex, Cork+ ve daha fazlası.",
        "A complete system for all your teak deck bonding, seaming, repair, activation and cleaning needs — TSC, TLB Flex, Cork+ and more.",
        [
            P("tsc-plus", "anchor", "TSC plus", "TSC plus",
              "Teak derzleri için tek bileşenli, esnek ve dayanıklı kalafat (derz dolgu) macunu.",
              "A one-component, flexible and durable caulking compound for teak deck seams.",
              wa_link("Merhaba, TSC plus teak derz macunu hakkında bilgi almak istiyorum.")),
            P("tlb-flex", "anchor", "TLB Flex", "TLB Flex",
              "Teak güverte yapıştırma sistemlerinde kullanılan esnek, yüksek mukavemetli bağlayıcı.",
              "A flexible, high-strength adhesive used in teak deck bonding systems.",
              wa_link("Merhaba, TLB Flex hakkında bilgi almak istiyorum.")),
            P("synteak-activator", "anchor", "Synteak Activator", "Synteak Activator",
              "Sentetik teak (suni teak) uygulamalarında yüzey hazırlığı için özel aktivatör astar.",
              "A special activator primer for surface preparation in synthetic teak applications.",
              wa_link("Merhaba, Synteak Activator hakkında bilgi almak istiyorum.")),
            P("cork-teak-protect", "anchor", "Cork+ Teak Protect", "Cork+ Teak Protect",
              "Teak yüzeyleri UV ışınlarına ve neme karşı koruyan mantar bazlı koruyucu kaplama.",
              "A cork-based protective coating that shields teak surfaces from UV rays and moisture.",
              wa_link("Merhaba, Cork+ Teak Protect hakkında bilgi almak istiyorum.")),
            P("teak-cleaner", "anchor", "Teak Cleaner", "Teak Cleaner",
              "Teak güvertelerde derinlemesine temizlik yapan, gri lekeleri gideren özel temizleyici.",
              "A deep-cleaning solution that removes grey staining from teak decks.",
              wa_link("Merhaba, Teak Cleaner hakkında bilgi almak istiyorum.")),
            P("tlb-pox", "anchor", "TLB Pox", "TLB Pox",
              "Teak onarımlarında kullanılan, yüksek yapışma mukavemetine sahip iki bileşenli epoksi dolgu sistemi.",
              "A two-component epoxy filling system with high bond strength, used for teak repairs.",
              wa_link("Merhaba, TLB Pox epoksi dolgu sistemi hakkında bilgi almak istiyorum.")),
        ],
        "Teak Deck Sistemleri: TSC plus, TLB Flex, Synteak Activator, Cork+ Teak Protect, Teak Cleaner, TLB Pox — MF Nautic Türkiye."
    )

    # 6) Aletler ve Aksesuarlar
    build_category(
        "aletler-ve-aksesuarlar", "cat.tools.title", "tool",
        "Aletler ve Aksesuarlar", "Tools & Accessories",
        "Tikalflex ve diğer Tikal ürünlerinin profesyonel şekilde uygulanması için tabancalar, derz aletleri ve temizlik ürünleri.",
        "Guns, joint tools and cleaning products for the professional application of Tikalflex and other Tikal products.",
        [
            P("cartridge-guns", "tool", "Kartuş ve Tüp Tabancaları", "Cartridge & Tube Guns",
              "Tikalflex ve diğer kartuş/tüp ambalajlı ürünler için profesyonel, ergonomik uygulama tabancaları.",
              "Professional, ergonomic application guns for Tikalflex and other cartridge/tube packaged products.",
              wa_link("Merhaba, kartuş/tüp tabancaları hakkında bilgi almak istiyorum.")),
            P("joint-tool", "tool", "Derz Aleti (Joint Tool)", "Joint Tool",
              "Mastik ve dolgu derzlerinin düzgün, profesyonel bir görünüm kazanması için özel şekillendirme aleti.",
              "A special shaping tool for a clean, professional finish on sealant and filler joints.",
              wa_link("Merhaba, derz aleti (Joint Tool) hakkında bilgi almak istiyorum.")),
            P("magic-clean", "tool", "Magic Clean", "Magic Clean",
              "Uygulama sonrası el ve yüzeylerde kalan yapıştırıcı/mastik artıklarını kolayca temizleyen özel temizlik ürünü.",
              "A special cleaning product that easily removes leftover adhesive/sealant residue from hands and surfaces after application.",
              wa_link("Merhaba, Magic Clean temizlik ürünü hakkında bilgi almak istiyorum.")),
        ],
        "Uygulama tabancaları, derz aleti ve Magic Clean temizlik ürünü — Tikal Marine Systems aletler ve aksesuarlar."
    )

# =================================================================
# PRODUCT DETAIL: Tikalflex Contact 12
# =================================================================
def build_tikalflex_detail():
    depth = "../"
    bc = BREADCRUMB(depth, [
        ("nav.products", d(depth,"urunler/index.html"), "Ürünler"),
        ("cat.adhesives.title", d(depth,"urunler/yapistirici-ve-mastikler.html"), "Yapıştırıcı ve Mastikler"),
        (None, None, "Tikalflex Contact 12"),
    ])

    spec_rows_tr = [
        ("Kimyasal Yapı", "MS Polimer"),
        ("Uygulama Sıcaklığı", "0°C ile +40°C arası"),
        ("Yüzey Kuruma Süresi", "10–15 dakika"),
        ("Kürleşme Hızı", "~2 mm / 24 saat (25°C, %65 bağıl nem)"),
        ("Shore A Sertliği", "60"),
        ("Çekme Mukavemeti", "2,3 N/mm²"),
        ("Kopmada Uzama", "%350"),
        ("Raf Ömrü", "18 ay (5°C–25°C arasında saklama)"),
        ("Tuzlu Su / Hava Şartlarına Dayanım", "Evet"),
        ("UV Dayanımı", "Hayır — üzeri boya/vernik ile kaplanmalı"),
    ]
    spec_rows_en = [
        ("Chemical Base", "MS Polymer"),
        ("Application Temperature", "0°C to +40°C"),
        ("Skin Forming Time", "10–15 minutes"),
        ("Curing Speed", "~2 mm / 24h (25°C, 65% RH)"),
        ("Shore A Hardness", "60"),
        ("Tensile Strength", "2.3 N/mm²"),
        ("Elongation at Break", "350%"),
        ("Shelf Life", "18 months (stored at 5°C–25°C)"),
        ("Saltwater / Weathering Resistance", "Yes"),
        ("UV Resistance", "No — must be overcoated with paint/varnish"),
    ]
    spec_html = "\n".join(
        '        <tr><td data-i18n="spec.%d.k">%s</td><td data-i18n="spec.%d.v">%s</td></tr>' % (i, tr[0], i, tr[1])
        for i, tr in enumerate(spec_rows_tr)
    )

    body = """  <section class="page-hero">
    <div class="container">
      %s
      <span class="hero-badge" style="margin-bottom:14px" data-i18n="pd.badge">Öne Çıkan Ürün — Yapıştırıcı ve Mastikler</span>
      <h1 data-i18n="pd.h1">Tikalflex Contact 12</h1>
      <p data-i18n="pd.lead">Küçülme yapmayan, çok güçlü, suya dayanıklı MS Polimer yapıştırıcı — deniz ve mobil ortamda hemen her türlü yapıştırma işi için.</p>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="split">
        <div>
          <div class="eyebrow" data-i18n="pd.about.eyebrow">Ürün Hakkında</div>
          <h2 data-i18n="pd.about.title">Profesyonel tekne yapıştırma için MS Polimer teknolojisi</h2>
          <p data-i18n="pd.about.p1">Tikalflex Contact 12, ahşap, alüminyum, çelik ve GRP (fiberglas) yüzeylerde kalıcı ve esnek bağlantılar oluşturan tek bileşenli bir MS Polimer yapıştırıcıdır. Nemle temas ettiğinde sertleşir ve kürleştikten sonra zımparalanabilir.</p>
          <ul class="check-list">
            <li><span class="tick">%s</span><span data-i18n="pd.li1">Yüksek yapışma mukavemeti, toleransları telafi eder</span></li>
            <li><span class="tick">%s</span><span data-i18n="pd.li2">Küçülme yapmaz, su altı ve su üstü uygulamalara uygundur</span></li>
            <li><span class="tick">%s</span><span data-i18n="pd.li3">Kürleştikten sonra zımparalanabilir, normal boya/vernik ile uyumludur</span></li>
            <li><span class="tick">%s</span><span data-i18n="pd.li4">Nitrik asit, kostik soda, yağ ve dizele karşı dayanıklıdır</span></li>
          </ul>
        </div>
        <div class="split-media">%s</div>
      </div>
    </div>
  </section>

  <section class="section section--alt">
    <div class="container">
      <div class="section-head">
        <div class="eyebrow" data-i18n="pd.spec.eyebrow">Teknik Özellikler</div>
        <h2 data-i18n="pd.spec.title">Teknik Veriler</h2>
      </div>
      <table class="spec-table">
%s
      </table>
      <p class="form-note" style="margin-top:14px" data-i18n="pd.spec.note">* Değerler yaklaşık laboratuvar koşullarında ölçülmüştür. Güncel ve resmi teknik veri formu (TDS) için bizimle iletişime geçin.</p>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="split reverse">
        <div class="split-media">%s</div>
        <div>
          <div class="eyebrow" data-i18n="pd.pack.eyebrow">Ambalaj ve Kullanım</div>
          <h2 data-i18n="pd.pack.title">Ambalaj Seçenekleri &amp; Renkler</h2>
          <ul class="check-list">
            <li><span class="tick">%s</span><span data-i18n="pd.pack.li1">24 × 70 ml kartuş</span></li>
            <li><span class="tick">%s</span><span data-i18n="pd.pack.li2">12 × 290 ml kartuş</span></li>
            <li><span class="tick">%s</span><span data-i18n="pd.pack.li3">12 × 600 ml torba/kartuş</span></li>
            <li><span class="tick">%s</span><span data-i18n="pd.pack.li4">Renkler: Beyaz, Siyah, Gri</span></li>
          </ul>
          <p data-i18n="pd.pack.p1">Kullanım alanları: Ahşap, alüminyum, çelik ve GRP yüzeylerde yapıştırma; deniz araçları ve karavan uygulamaları.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--alt">
    <div class="container">
      <div class="cta-band">
        <div>
          <h2 data-i18n="pd.cta.title">Tikalflex Contact 12 için teklif alın</h2>
          <p data-i18n="pd.cta.desc">Stok durumu, ambalaj seçenekleri ve fiyat bilgisi için hemen bize ulaşın.</p>
        </div>
        <div class="cta-actions">
          <a href="%s" target="_blank" rel="noopener" class="btn btn-primary">%s<span data-i18n="pd.cta.btn1">WhatsApp'tan Sor</span></a>
          <a href="%s" class="btn btn-outline-light"><span data-i18n="pd.cta.btn2">İletişim Formu</span>%s</a>
        </div>
      </div>
    </div>
  </section>""" % (
        bc, icon("check"), icon("check"), icon("check"), icon("check"), icon("droplet","cls"),
        spec_html,
        icon("layers","cls"), icon("check"), icon("check"), icon("check"), icon("check"),
        wa_link("Merhaba, Tikalflex Contact 12 için fiyat teklifi almak istiyorum."), icon("whatsapp"),
        d(depth,"iletisim.html"), icon("arrow-right"),
    )

    pi_tr = {
        "pd.badge": "Öne Çıkan Ürün — Yapıştırıcı ve Mastikler",
        "pd.h1": "Tikalflex Contact 12",
        "pd.lead": "Küçülme yapmayan, çok güçlü, suya dayanıklı MS Polimer yapıştırıcı — deniz ve mobil ortamda hemen her türlü yapıştırma işi için.",
        "pd.about.eyebrow": "Ürün Hakkında",
        "pd.about.title": "Profesyonel tekne yapıştırma için MS Polimer teknolojisi",
        "pd.about.p1": "Tikalflex Contact 12, ahşap, alüminyum, çelik ve GRP (fiberglas) yüzeylerde kalıcı ve esnek bağlantılar oluşturan tek bileşenli bir MS Polimer yapıştırıcıdır. Nemle temas ettiğinde sertleşir ve kürleştikten sonra zımparalanabilir.",
        "pd.li1": "Yüksek yapışma mukavemeti, toleransları telafi eder",
        "pd.li2": "Küçülme yapmaz, su altı ve su üstü uygulamalara uygundur",
        "pd.li3": "Kürleştikten sonra zımparalanabilir, normal boya/vernik ile uyumludur",
        "pd.li4": "Nitrik asit, kostik soda, yağ ve dizele karşı dayanıklıdır",
        "pd.spec.eyebrow": "Teknik Özellikler", "pd.spec.title": "Teknik Veriler",
        "pd.spec.note": "* Değerler yaklaşık laboratuvar koşullarında ölçülmüştür. Güncel ve resmi teknik veri formu (TDS) için bizimle iletişime geçin.",
        "pd.pack.eyebrow": "Ambalaj ve Kullanım", "pd.pack.title": "Ambalaj Seçenekleri & Renkler",
        "pd.pack.li1": "24 × 70 ml kartuş", "pd.pack.li2": "12 × 290 ml kartuş",
        "pd.pack.li3": "12 × 600 ml torba/kartuş", "pd.pack.li4": "Renkler: Beyaz, Siyah, Gri",
        "pd.pack.p1": "Kullanım alanları: Ahşap, alüminyum, çelik ve GRP yüzeylerde yapıştırma; deniz araçları ve karavan uygulamaları.",
        "pd.cta.title": "Tikalflex Contact 12 için teklif alın",
        "pd.cta.desc": "Stok durumu, ambalaj seçenekleri ve fiyat bilgisi için hemen bize ulaşın.",
        "pd.cta.btn1": "WhatsApp'tan Sor", "pd.cta.btn2": "İletişim Formu",
        "cat.adhesives.title": "Yapıştırıcı ve Mastikler",
    }
    for i, tr in enumerate(spec_rows_tr):
        pi_tr["spec.%d.k"%i] = tr[0]; pi_tr["spec.%d.v"%i] = tr[1]

    pi_en = {
        "pd.badge": "Featured Product — Adhesives & Sealants",
        "pd.h1": "Tikalflex Contact 12",
        "pd.lead": "A shrink-free, very strong, waterproof MS Polymer adhesive — for nearly all bonding tasks in the marine and mobile environment.",
        "pd.about.eyebrow": "About the Product",
        "pd.about.title": "MS Polymer technology for professional boat bonding",
        "pd.about.p1": "Tikalflex Contact 12 is a one-component MS Polymer adhesive that creates permanent, flexible bonds on wood, aluminium, steel and GRP surfaces. It cures on contact with humidity and is sandable once cured.",
        "pd.li1": "High bonding strength, compensates for tolerances",
        "pd.li2": "Shrink-free, suitable for above- and below-water applications",
        "pd.li3": "Sandable when cured, compatible with normal paint/varnish",
        "pd.li4": "Resistant to nitric acid, caustic soda, oil and diesel",
        "pd.spec.eyebrow": "Technical Specifications", "pd.spec.title": "Technical Data",
        "pd.spec.note": "* Values are approximate, measured under laboratory conditions. Contact us for the current official technical data sheet (TDS).",
        "pd.pack.eyebrow": "Packaging & Use", "pd.pack.title": "Packaging Options & Colours",
        "pd.pack.li1": "24 × 70 ml cartridges", "pd.pack.li2": "12 × 290 ml cartridges",
        "pd.pack.li3": "12 × 600 ml pouches/cartridges", "pd.pack.li4": "Colours: White, Black, Grey",
        "pd.pack.p1": "Applications: bonding wood, aluminium, steel and GRP surfaces; marine and caravan applications.",
        "pd.cta.title": "Get a quote for Tikalflex Contact 12",
        "pd.cta.desc": "Contact us now for stock availability, packaging options and pricing.",
        "pd.cta.btn1": "Ask on WhatsApp", "pd.cta.btn2": "Contact Form",
        "cat.adhesives.title": "Adhesives & Sealants",
    }
    for i, tr in enumerate(spec_rows_en):
        pi_en["spec.%d.k"%i] = tr[0]; pi_en["spec.%d.v"%i] = tr[1]

    i18n_js = "{\n  tr: %s,\n  en: %s\n}" % (j(pi_tr), j(pi_en))
    html = PAGE(depth, "Tikalflex Contact 12 Teknik Özellikleri | MF Nautic Turkey",
                "Tikalflex Contact 12 MS Polimer yapıştırıcı teknik özellikleri, ambalaj seçenekleri ve kullanım alanları.",
                body, i18n_js)
    write("urunler/tikalflex-contact-12.html", html)

# =================================================================
# HAKKIMIZDA
# =================================================================
def build_hakkimizda():
    depth = ""
    bc = BREADCRUMB(depth, [(None, None, "Hakkımızda")])
    body = """  <section class="page-hero">
    <div class="container">
      %s
      <h1 data-i18n="ab.h1">Hakkımızda</h1>
      <p data-i18n="ab.lead">MF Nautic Yatçılık Ltd. Şti., Almanya merkezli Tikal Marine Systems GmbH'nin Türkiye'deki resmi distribütörüdür.</p>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="split">
        <div>
          <div class="eyebrow" data-i18n="ab.mf.eyebrow">MF Nautic Yatçılık</div>
          <h2 data-i18n="ab.mf.title">Fethiye merkezli, denizcilik sektörüne adanmış bir ekip</h2>
          <p data-i18n="ab.mf.p1">Göcek / Fethiye merkezli MF Nautic Yatçılık Ltd. Şti. olarak, Tikal Marine Systems GmbH'nin Türkiye'deki resmi distribütörlüğünü yürütüyoruz. Tersaneler, yat işletmeleri, marina servisleri ve profesyonel uygulayıcılara; yapıştırıcı, mastik, teak deck bakım ürünleri ve deniz yağlayıcıları konusunda orijinal ürün ve teknik destek sağlıyoruz.</p>
          <p data-i18n="ab.mf.p2">Amacımız; Türkiye'deki tekne bakım ve üretim sektörüne, Avrupa standartlarında test edilmiş, güvenilir ürünleri hızlı ve profesyonel bir hizmet anlayışıyla ulaştırmak.</p>
        </div>
        <div class="split-media">%s</div>
      </div>
    </div>
  </section>

  <section class="section section--alt">
    <div class="container">
      <div class="split reverse">
        <div class="split-media">%s</div>
        <div>
          <div class="eyebrow" data-i18n="ab.tikal.eyebrow">Tikal Marine Systems GmbH</div>
          <h2 data-i18n="ab.tikal.title">Almanya'da üretilen, Avrupa'da güvenilen bir marka</h2>
          <p data-i18n="ab.tikal.p1">Tikal Marine Systems GmbH, denizcilik sektörüne yönelik yapıştırıcı, mastik, dolgu macunu ve bakım ürünlerini kendi laboratuvarında geliştirip üreten bir Alman firmasıdır. Ürünler, sürekli son kontrol ve kalite güvence süreçlerinden geçer; her ürüne parti ve üretim numarası verilerek hammadde alımına kadar tam izlenebilirlik sağlanır.</p>
          <p data-i18n="ab.tikal.p2">Bu titiz üretim anlayışı sayesinde Tikal ürünleri, Avrupa genelinde tersaneler ve yat üreticileri tarafından tercih edilmektedir.</p>
          <div class="footer-powered" style="margin-top:8px"><img src="assets/images/logo/powered-by-tikal.jpg" alt="Tikal Marine Systems"></div>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head text-center">
        <div class="eyebrow" data-i18n="ab.values.eyebrow">Değerlerimiz</div>
        <h2 data-i18n="ab.values.title">Neden MF Nautic ile çalışmalısınız?</h2>
      </div>
      <div class="steps">
        <div class="step"><div class="n">%s</div><h4 data-i18n="ab.v1.t">Orijinallik</h4><p data-i18n="ab.v1.d">%%100 orijinal, Almanya menşeli Tikal ürünleri.</p></div>
        <div class="step"><div class="n">%s</div><h4 data-i18n="ab.v2.t">Teknik Bilgi</h4><p data-i18n="ab.v2.d">Doğru ürün seçimi ve uygulama konusunda uzman desteği.</p></div>
        <div class="step"><div class="n">%s</div><h4 data-i18n="ab.v3.t">Hız</h4><p data-i18n="ab.v3.d">Türkiye'nin her yerine hızlı kargo ve stok takibi.</p></div>
        <div class="step"><div class="n">%s</div><h4 data-i18n="ab.v4.t">Güven</h4><p data-i18n="ab.v4.d">Şeffaf iletişim ve uzun soluklu iş ortaklıkları.</p></div>
      </div>
    </div>
  </section>

  <section class="section section--alt" id="bayilik">
    <div class="container">
      <div class="split">
        <div>
          <div class="eyebrow" data-i18n="ab.dealer.eyebrow">Bayilik Başvurusu</div>
          <h2 data-i18n="ab.dealer.title">Chandlery, tersane veya marina işletmeniz mi var?</h2>
          <p data-i18n="ab.dealer.p1">Tikal Marine Systems ürünlerini kendi mağazanızda veya işletmenizde satmak/kullanmak ister misiniz? Bayilik ve toptan satış koşullarımız hakkında bilgi almak için formu doldurun, size dönüş yapalım.</p>
          <ul class="check-list">
            <li><span class="tick">%s</span><span data-i18n="ab.dealer.li1">Bayilere özel fiyatlandırma</span></li>
            <li><span class="tick">%s</span><span data-i18n="ab.dealer.li2">Ürün eğitimi ve teknik destek</span></li>
            <li><span class="tick">%s</span><span data-i18n="ab.dealer.li3">Pazarlama ve ürün materyali desteği</span></li>
          </ul>
        </div>
        <div class="form-card">
          <form class="js-wa-form" data-wa-intro="Merhaba, bayilik başvurusunda bulunmak istiyorum.">
            <div class="form-field">
              <label data-i18n="ab.form.name">Ad Soyad</label>
              <input type="text" required data-wa-field="Ad Soyad">
            </div>
            <div class="form-field">
              <label data-i18n="ab.form.company">Şirket / İşletme Adı</label>
              <input type="text" required data-wa-field="Şirket">
            </div>
            <div class="form-field">
              <label data-i18n="ab.form.phone">Telefon</label>
              <input type="tel" required data-wa-field="Telefon">
            </div>
            <div class="form-field">
              <label data-i18n="ab.form.msg">Mesajınız</label>
              <textarea data-wa-field="Mesaj" data-i18n-placeholder="ab.form.msg.ph" placeholder="İşletmeniz ve talebiniz hakkında kısaca bilgi verin"></textarea>
            </div>
            <button type="submit" class="btn btn-primary btn-block">%s<span data-i18n="ab.form.submit">WhatsApp ile Gönder</span></button>
            <p class="form-note" data-i18n="ab.form.note">Gönder butonuna bastığınızda WhatsApp üzerinden bize ulaşacaksınız.</p>
          </form>
        </div>
      </div>
    </div>
  </section>""" % (
        bc, icon("users","cls"), icon("award","cls"),
        "1","2","3","4",
        icon("check"), icon("check"), icon("check"),
        icon("whatsapp"),
    )

    pi_tr = {
        "ab.h1": "Hakkımızda",
        "ab.lead": "MF Nautic Yatçılık Ltd. Şti., Almanya merkezli Tikal Marine Systems GmbH'nin Türkiye'deki resmi distribütörüdür.",
        "ab.mf.eyebrow": "MF Nautic Yatçılık",
        "ab.mf.title": "Fethiye merkezli, denizcilik sektörüne adanmış bir ekip",
        "ab.mf.p1": "Göcek / Fethiye merkezli MF Nautic Yatçılık Ltd. Şti. olarak, Tikal Marine Systems GmbH'nin Türkiye'deki resmi distribütörlüğünü yürütüyoruz. Tersaneler, yat işletmeleri, marina servisleri ve profesyonel uygulayıcılara; yapıştırıcı, mastik, teak deck bakım ürünleri ve deniz yağlayıcıları konusunda orijinal ürün ve teknik destek sağlıyoruz.",
        "ab.mf.p2": "Amacımız; Türkiye'deki tekne bakım ve üretim sektörüne, Avrupa standartlarında test edilmiş, güvenilir ürünleri hızlı ve profesyonel bir hizmet anlayışıyla ulaştırmak.",
        "ab.tikal.eyebrow": "Tikal Marine Systems GmbH",
        "ab.tikal.title": "Almanya'da üretilen, Avrupa'da güvenilen bir marka",
        "ab.tikal.p1": "Tikal Marine Systems GmbH, denizcilik sektörüne yönelik yapıştırıcı, mastik, dolgu macunu ve bakım ürünlerini kendi laboratuvarında geliştirip üreten bir Alman firmasıdır. Ürünler, sürekli son kontrol ve kalite güvence süreçlerinden geçer; her ürüne parti ve üretim numarası verilerek hammadde alımına kadar tam izlenebilirlik sağlanır.",
        "ab.tikal.p2": "Bu titiz üretim anlayışı sayesinde Tikal ürünleri, Avrupa genelinde tersaneler ve yat üreticileri tarafından tercih edilmektedir.",
        "ab.values.eyebrow": "Değerlerimiz", "ab.values.title": "Neden MF Nautic ile çalışmalısınız?",
        "ab.v1.t": "Orijinallik", "ab.v1.d": "%100 orijinal, Almanya menşeli Tikal ürünleri.",
        "ab.v2.t": "Teknik Bilgi", "ab.v2.d": "Doğru ürün seçimi ve uygulama konusunda uzman desteği.",
        "ab.v3.t": "Hız", "ab.v3.d": "Türkiye'nin her yerine hızlı kargo ve stok takibi.",
        "ab.v4.t": "Güven", "ab.v4.d": "Şeffaf iletişim ve uzun soluklu iş ortaklıkları.",
        "ab.dealer.eyebrow": "Bayilik Başvurusu",
        "ab.dealer.title": "Chandlery, tersane veya marina işletmeniz mi var?",
        "ab.dealer.p1": "Tikal Marine Systems ürünlerini kendi mağazanızda veya işletmenizde satmak/kullanmak ister misiniz? Bayilik ve toptan satış koşullarımız hakkında bilgi almak için formu doldurun, size dönüş yapalım.",
        "ab.dealer.li1": "Bayilere özel fiyatlandırma", "ab.dealer.li2": "Ürün eğitimi ve teknik destek",
        "ab.dealer.li3": "Pazarlama ve ürün materyali desteği",
        "ab.form.name": "Ad Soyad", "ab.form.company": "Şirket / İşletme Adı", "ab.form.phone": "Telefon",
        "ab.form.msg": "Mesajınız", "ab.form.msg.ph": "İşletmeniz ve talebiniz hakkında kısaca bilgi verin",
        "ab.form.submit": "WhatsApp ile Gönder",
        "ab.form.note": "Gönder butonuna bastığınızda WhatsApp üzerinden bize ulaşacaksınız.",
    }
    pi_en = {
        "ab.h1": "About Us",
        "ab.lead": "MF Nautic Yatçılık Ltd. Şti. is the official Turkish distributor of Germany-based Tikal Marine Systems GmbH.",
        "ab.mf.eyebrow": "MF Nautic Yatçılık",
        "ab.mf.title": "Based in Fethiye, a team dedicated to the marine industry",
        "ab.mf.p1": "Based in Göcek / Fethiye, MF Nautic Yatçılık Ltd. Şti. is the official Turkish distributor of Tikal Marine Systems GmbH. We provide shipyards, yacht businesses, marina services and professional applicators with genuine products and technical support for adhesives, sealants, teak deck maintenance products and marine lubricants.",
        "ab.mf.p2": "Our goal is to bring Europe-tested, reliable products to Türkiye's boat maintenance and manufacturing industry with fast and professional service.",
        "ab.tikal.eyebrow": "Tikal Marine Systems GmbH",
        "ab.tikal.title": "Manufactured in Germany, trusted across Europe",
        "ab.tikal.p1": "Tikal Marine Systems GmbH is a German company that develops and manufactures adhesives, sealants, fillers and maintenance products for the marine industry in-house. Products go through continuous final inspection and quality assurance; each product is given a batch and production number for full traceability back to raw material purchase.",
        "ab.tikal.p2": "Thanks to this meticulous manufacturing approach, Tikal products are trusted by shipyards and yacht builders across Europe.",
        "ab.values.eyebrow": "Our Values", "ab.values.title": "Why work with MF Nautic?",
        "ab.v1.t": "Genuine Products", "ab.v1.d": "100% genuine, German-made Tikal products.",
        "ab.v2.t": "Technical Knowledge", "ab.v2.d": "Expert support on the right product choice and application.",
        "ab.v3.t": "Speed", "ab.v3.d": "Fast shipping and stock tracking anywhere in Türkiye.",
        "ab.v4.t": "Trust", "ab.v4.d": "Transparent communication and long-term partnerships.",
        "ab.dealer.eyebrow": "Become a Dealer",
        "ab.dealer.title": "Do you run a chandlery, shipyard or marina business?",
        "ab.dealer.p1": "Want to sell or use Tikal Marine Systems products at your own business? Fill out the form to learn about our dealership and wholesale terms — we'll get back to you.",
        "ab.dealer.li1": "Special dealer pricing", "ab.dealer.li2": "Product training and technical support",
        "ab.dealer.li3": "Marketing and product material support",
        "ab.form.name": "Full Name", "ab.form.company": "Company / Business Name", "ab.form.phone": "Phone",
        "ab.form.msg": "Your Message", "ab.form.msg.ph": "Briefly tell us about your business and request",
        "ab.form.submit": "Send via WhatsApp",
        "ab.form.note": "Clicking send will open WhatsApp to reach us.",
    }
    i18n_js = "{\n  tr: %s,\n  en: %s\n}" % (j(pi_tr), j(pi_en))
    html = PAGE(depth, "Hakkımızda | MF Nautic Turkey",
                "MF Nautic Yatçılık Ltd. Şti. — Tikal Marine Systems GmbH'nin Türkiye'deki resmi distribütörü. Bayilik başvuruları için bize ulaşın.",
                body, i18n_js)
    write("hakkimizda.html", html)

# =================================================================
# ILETISIM
# =================================================================
def build_iletisim():
    depth = ""
    bc = BREADCRUMB(depth, [(None, None, "İletişim")])
    map_q = quote("Gocek Mahallesi Likya Caddesi No22 Fethiye Mugla")
    body = """  <section class="page-hero">
    <div class="container">
      %s
      <h1 data-i18n="ct.h1">İletişim</h1>
      <p data-i18n="ct.lead">Sorularınız, teknik destek talepleriniz veya sipariş talepleriniz için bize ulaşın — en kısa sürede dönüş yapalım.</p>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="contact-grid">
        <div>
          <div class="contact-card">
            <div class="row"><div class="ic">%s</div><div><b data-i18n="ct.addr.t">Adres</b><span>Göcek Mahallesi, Likya Caddesi No:22<br>Fethiye / Muğla</span></div></div>
            <div class="row"><div class="ic">%s</div><div><b data-i18n="ct.phone.t">Telefon &amp; WhatsApp</b><a href="tel:+905414558005">+90 541 455 80 05</a></div></div>
            <div class="row"><div class="ic">%s</div><div><b data-i18n="ct.mail.t">E-posta</b><a href="mailto:levent@mf-nautic.com">levent@mf-nautic.com</a></div></div>
            <div class="row"><div class="ic">%s</div><div><b data-i18n="ct.hours.t">Çalışma Saatleri</b><span data-i18n="ct.hours.v">Hafta içi 09:00 – 18:00</span></div></div>
          </div>
          <div class="map-frame"><iframe src="https://www.google.com/maps?q=%s&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="MF Nautic Turkey Konum"></iframe></div>
          <a href="https://wa.me/905414558005" target="_blank" rel="noopener" class="btn btn-primary btn-block" style="margin-top:18px">%s<span data-i18n="ct.wa.btn">WhatsApp'tan Yazın</span></a>
        </div>

        <div class="form-card">
          <div class="eyebrow" data-i18n="ct.form.eyebrow">Formu Doldurun</div>
          <h2 data-i18n="ct.form.title">Size Nasıl Yardımcı Olabiliriz?</h2>
          <form class="js-wa-form" data-wa-intro="Merhaba, iletişim formu üzerinden yazıyorum.">
            <div class="form-grid">
              <div class="form-field">
                <label data-i18n="ct.form.name">Ad Soyad</label>
                <input type="text" required data-wa-field="Ad Soyad">
              </div>
              <div class="form-field">
                <label data-i18n="ct.form.phone">Telefon</label>
                <input type="tel" required data-wa-field="Telefon">
              </div>
              <div class="form-field full">
                <label data-i18n="ct.form.email">E-posta</label>
                <input type="email" data-wa-field="E-posta">
              </div>
              <div class="form-field full">
                <label data-i18n="ct.form.subject">Konu</label>
                <select data-wa-field="Konu">
                  <option data-i18n="ct.form.opt1">Ürün / Fiyat Bilgisi</option>
                  <option data-i18n="ct.form.opt2">Teknik Döküman Talebi</option>
                  <option data-i18n="ct.form.opt3">Bayilik Başvurusu</option>
                  <option data-i18n="ct.form.opt4">Diğer</option>
                </select>
              </div>
              <div class="form-field full">
                <label data-i18n="ct.form.msg">Mesajınız</label>
                <textarea data-wa-field="Mesaj" data-i18n-placeholder="ct.form.msg.ph" placeholder="Talebinizi kısaca açıklayın"></textarea>
              </div>
            </div>
            <button type="submit" class="btn btn-primary btn-block">%s<span data-i18n="ct.form.submit">WhatsApp ile Gönder</span></button>
            <p class="form-note" data-i18n="ct.form.note">Gönder butonuna bastığınızda WhatsApp üzerinden bize ulaşacaksınız. Formu e-posta ile göndermek isterseniz levent@mf-nautic.com adresine yazabilirsiniz.</p>
          </form>
        </div>
      </div>
    </div>
  </section>""" % (
        bc, icon("map-pin"), icon("phone"), icon("mail"), icon("clock"),
        map_q, icon("whatsapp"), icon("whatsapp"),
    )

    pi_tr = {
        "ct.h1": "İletişim",
        "ct.lead": "Sorularınız, teknik destek talepleriniz veya sipariş talepleriniz için bize ulaşın — en kısa sürede dönüş yapalım.",
        "ct.addr.t": "Adres", "ct.phone.t": "Telefon & WhatsApp", "ct.mail.t": "E-posta",
        "ct.hours.t": "Çalışma Saatleri", "ct.hours.v": "Hafta içi 09:00 – 18:00",
        "ct.wa.btn": "WhatsApp'tan Yazın",
        "ct.form.eyebrow": "Formu Doldurun", "ct.form.title": "Size Nasıl Yardımcı Olabiliriz?",
        "ct.form.name": "Ad Soyad", "ct.form.phone": "Telefon", "ct.form.email": "E-posta", "ct.form.subject": "Konu",
        "ct.form.opt1": "Ürün / Fiyat Bilgisi", "ct.form.opt2": "Teknik Döküman Talebi",
        "ct.form.opt3": "Bayilik Başvurusu", "ct.form.opt4": "Diğer",
        "ct.form.msg": "Mesajınız", "ct.form.msg.ph": "Talebinizi kısaca açıklayın",
        "ct.form.submit": "WhatsApp ile Gönder",
        "ct.form.note": "Gönder butonuna bastığınızda WhatsApp üzerinden bize ulaşacaksınız. Formu e-posta ile göndermek isterseniz levent@mf-nautic.com adresine yazabilirsiniz.",
    }
    pi_en = {
        "ct.h1": "Contact",
        "ct.lead": "Reach out with your questions, technical support needs or order requests — we'll get back to you as soon as possible.",
        "ct.addr.t": "Address", "ct.phone.t": "Phone & WhatsApp", "ct.mail.t": "Email",
        "ct.hours.t": "Working Hours", "ct.hours.v": "Weekdays 09:00 – 18:00",
        "ct.wa.btn": "Message on WhatsApp",
        "ct.form.eyebrow": "Fill the Form", "ct.form.title": "How Can We Help?",
        "ct.form.name": "Full Name", "ct.form.phone": "Phone", "ct.form.email": "Email", "ct.form.subject": "Subject",
        "ct.form.opt1": "Product / Price Info", "ct.form.opt2": "Technical Document Request",
        "ct.form.opt3": "Dealer Application", "ct.form.opt4": "Other",
        "ct.form.msg": "Your Message", "ct.form.msg.ph": "Briefly describe your request",
        "ct.form.submit": "Send via WhatsApp",
        "ct.form.note": "Clicking send will open WhatsApp to reach us. To send by email instead, write to levent@mf-nautic.com.",
    }
    i18n_js = "{\n  tr: %s,\n  en: %s\n}" % (j(pi_tr), j(pi_en))
    html = PAGE(depth, "İletişim | MF Nautic Turkey",
                "MF Nautic Yatçılık iletişim bilgileri: adres, telefon, WhatsApp ve e-posta. Fethiye / Muğla.",
                body, i18n_js)
    write("iletisim.html", html)

# =================================================================
# DOKUMANLAR (TDS / SDS request page)
# =================================================================
DOC_GROUPS = [
    ("cat.adhesives.title", "Yapıştırıcı ve Mastikler", "Adhesives & Sealants", "droplet",
     ["Tikalflex Contact 12", "Tikalflex Ürün Ailesi / Product Range"]),
    ("cat.lubricants.title", "Deniz Yağlayıcıları", "Marine Lubricants", "droplet",
     ["HP-MG Deniz Gresi / Marine Grease"]),
    ("cat.filler.title", "Dolgu Macunları", "Fillers", "layers",
     ["Fast Patch", "Fast Patch LIGHT"]),
    ("cat.tefgel.title", "Tikal Tef-Gel", "Tikal Tef-Gel", "shield-check",
     ["Tikal Tef-Gel"]),
    ("cat.teak.title", "Teak Deck Sistemleri", "Teak Deck Systems", "anchor",
     ["TSC plus", "TLB Flex", "Synteak Activator", "Cork+ Teak Protect", "Teak Cleaner", "TLB Pox"]),
    ("cat.tools.title", "Aletler ve Aksesuarlar", "Tools & Accessories", "tool",
     ["Kartuş ve Tüp Tabancaları", "Derz Aleti (Joint Tool)", "Magic Clean"]),
]

def build_dokumanlar():
    depth = ""
    bc = BREADCRUMB(depth, [(None, None, "Teknik Dökümanlar")])

    groups_html = []
    pi_tr = {}
    pi_en = {}
    for gi, (cat_key, cat_tr, cat_en, ic, items) in enumerate(DOC_GROUPS):
        rows = []
        for pi, name in enumerate(items):
            rid = "doc.%d.%d" % (gi, pi)
            pi_tr[rid] = name; pi_en[rid] = name
            rows.append("""        <div class="doc-row">
          <div class="doc-row-left"><div class="doc-ic">%s</div><div><b data-i18n="%s">%s</b><span data-i18n="doc.sub">Teknik Veri Formu (TDS) &amp; Güvenlik Bilgi Formu (SDS)</span></div></div>
          <a href="%s" target="_blank" rel="noopener" class="btn btn-outline btn-sm">%s<span data-i18n="doc.req">İste</span></a>
        </div>""" % (icon("file-text"), rid, name, wa_link("Merhaba, %s için teknik veri formu (TDS) istiyorum." % name), icon("download")))
        groups_html.append("""      <div class="doc-group">
        <h3>%s<span data-i18n="%s">%s</span></h3>
%s
      </div>""" % (icon(ic), cat_key, cat_tr, "\n".join(rows)))
        pi_tr[cat_key] = cat_tr; pi_en[cat_key] = cat_en

    body = """  <section class="page-hero">
    <div class="container">
      %s
      <h1 data-i18n="dc.h1">Teknik Dökümanlar</h1>
      <p data-i18n="dc.lead">Ürünlerimizin teknik veri formu (TDS) ve güvenlik bilgi formunu (SDS) güncel haliyle iletebilmek için talebinizi WhatsApp veya e-posta ile alıyoruz.</p>
    </div>
  </section>
  <section class="section">
    <div class="container">
      <div class="chip-row">
        <span class="chip active" data-i18n="dc.chip.all">Tüm Dökümanlar</span>
      </div>
%s
    </div>
  </section>
  <section class="section section--alt">
    <div class="container">
      <div class="cta-band">
        <div>
          <h2 data-i18n="dc.cta.title">İhtiyacınız olan dökümanı bulamadınız mı?</h2>
          <p data-i18n="dc.cta.desc">Tüm ürün gamı için TDS/SDS dökümanlarını sizin için derleyip gönderelim.</p>
        </div>
        <div class="cta-actions">
          <a href="%s" target="_blank" rel="noopener" class="btn btn-primary">%s<span data-i18n="dc.cta.btn1">WhatsApp'tan İste</span></a>
          <a href="mailto:levent@mf-nautic.com" class="btn btn-outline-light">%s<span data-i18n="dc.cta.btn2">E-posta Gönder</span></a>
        </div>
      </div>
    </div>
  </section>""" % (bc, "\n".join(groups_html),
                    wa_link("Merhaba, ihtiyacım olan ürün için teknik döküman (TDS/SDS) talep etmek istiyorum."),
                    icon("whatsapp"), icon("mail"))

    pi_tr.update({
        "dc.h1": "Teknik Dökümanlar",
        "dc.lead": "Ürünlerimizin teknik veri formu (TDS) ve güvenlik bilgi formunu (SDS) güncel haliyle iletebilmek için talebinizi WhatsApp veya e-posta ile alıyoruz.",
        "dc.chip.all": "Tüm Dökümanlar",
        "doc.sub": "Teknik Veri Formu (TDS) & Güvenlik Bilgi Formu (SDS)", "doc.req": "İste",
        "dc.cta.title": "İhtiyacınız olan dökümanı bulamadınız mı?",
        "dc.cta.desc": "Tüm ürün gamı için TDS/SDS dökümanlarını sizin için derleyip gönderelim.",
        "dc.cta.btn1": "WhatsApp'tan İste", "dc.cta.btn2": "E-posta Gönder",
    })
    pi_en.update({
        "dc.h1": "Technical Documents",
        "dc.lead": "To always send you the current technical data sheet (TDS) and safety data sheet (SDS), we handle document requests via WhatsApp or email.",
        "dc.chip.all": "All Documents",
        "doc.sub": "Technical Data Sheet (TDS) & Safety Data Sheet (SDS)", "doc.req": "Request",
        "dc.cta.title": "Can't find the document you need?",
        "dc.cta.desc": "We'll compile and send the TDS/SDS documents for the full product range for you.",
        "dc.cta.btn1": "Request on WhatsApp", "dc.cta.btn2": "Send an Email",
    })
    i18n_js = "{\n  tr: %s,\n  en: %s\n}" % (j(pi_tr), j(pi_en))
    html = PAGE(depth, "Teknik Dökümanlar | MF Nautic Turkey",
                "Tikal Marine Systems ürünleri için teknik veri formu (TDS) ve güvenlik bilgi formu (SDS) talebi.",
                body, i18n_js)
    write("dokumanlar.html", html)

# =================================================================
# LEGAL PAGES
# =================================================================
def build_legal(slug, title_key, title_tr, title_en, sections_tr, sections_en, meta_desc):
    depth = ""
    bc = BREADCRUMB(depth, [(None, None, title_tr)])

    body_secs = []
    pi_tr = {}
    pi_en = {}
    for i, (h_tr, ps_tr) in enumerate(sections_tr):
        hid = "leg.%d.h" % i
        pi_tr[hid] = h_tr
        p_html = []
        for pj, p_tr in enumerate(ps_tr):
            pid = "leg.%d.%d" % (i, pj)
            pi_tr[pid] = p_tr
            p_html.append('        <p data-i18n="%s">%s</p>' % (pid, p_tr))
        body_secs.append('      <h2 data-i18n="%s">%s</h2>\n%s' % (hid, h_tr, "\n".join(p_html)))

    for i, (h_en, ps_en) in enumerate(sections_en):
        pi_en["leg.%d.h" % i] = h_en
        for pj, p_en in enumerate(ps_en):
            pi_en["leg.%d.%d" % (i, pj)] = p_en

    body = """  <section class="page-hero">
    <div class="container">
      %s
      <h1 data-i18n="%s">%s</h1>
    </div>
  </section>
  <section class="section">
    <div class="container">
      <div class="prose">
%s
      </div>
    </div>
  </section>""" % (bc, title_key, title_tr, "\n".join(body_secs))

    pi_tr[title_key] = title_tr
    pi_en[title_key] = title_en
    i18n_js = "{\n  tr: %s,\n  en: %s\n}" % (j(pi_tr), j(pi_en))
    html = PAGE(depth, "%s | MF Nautic Turkey" % title_tr, meta_desc, body, i18n_js)
    write(slug, html)

def build_gizlilik():
    sections_tr = [
        ("1. Veri Sorumlusu", [
            "Bu internet sitesi MF Nautic Yatçılık Ltd. Şti. (\"MF Nautic\", \"biz\") tarafından işletilmektedir. Adres: Göcek Mahallesi, Likya Caddesi No:22, Fethiye/Muğla. İletişim: levent@mf-nautic.com."]),
        ("2. Toplanan Veriler", [
            "İletişim formu veya WhatsApp üzerinden bizimle iletişime geçtiğinizde ad-soyad, telefon numarası, e-posta adresi, şirket bilgisi ve mesaj içeriğiniz gibi verileri işleyebiliriz.",
            "Site kullanımı sırasında tarayıcınızın teknik bilgileri (dil tercihi gibi) yalnızca tarayıcınızın yerel belleğinde (localStorage) tutulur ve tarafımıza otomatik olarak iletilmez."]),
        ("3. Verilerin Kullanım Amacı", [
            "Talebinizi yanıtlamak, teklif hazırlamak, teknik döküman iletmek ve sizinle iletişimi sürdürmek amacıyla paylaştığınız verileri kullanırız."]),
        ("4. Verilerin Paylaşımı", [
            "Kişisel verileriniz, yasal zorunluluklar dışında üçüncü taraflarla paylaşılmaz. İletişim formu WhatsApp üzerinden gönderildiğinde, mesaj içeriği WhatsApp/Meta altyapısı üzerinden iletilir."]),
        ("5. Haklarınız", [
            "6698 sayılı Kişisel Verilerin Korunması Kanunu (KVKK) kapsamında verilerinize erişim, düzeltme veya silme talebinde bulunmak için levent@mf-nautic.com adresinden bizimle iletişime geçebilirsiniz."]),
    ]
    sections_en = [
        ("1. Data Controller", [
            "This website is operated by MF Nautic Yatçılık Ltd. Şti. (\"MF Nautic\", \"we\"). Address: Göcek Mahallesi, Likya Caddesi No:22, Fethiye/Muğla, Türkiye. Contact: levent@mf-nautic.com."]),
        ("2. Data We Collect", [
            "When you contact us via the contact form or WhatsApp, we may process data such as your name, phone number, email address, company information and message content.",
            "Technical information such as your language preference is stored only in your browser's local storage (localStorage) and is not automatically transmitted to us."]),
        ("3. Purpose of Processing", [
            "We use the data you share to respond to your request, prepare quotes, send technical documents and maintain communication with you."]),
        ("4. Data Sharing", [
            "Your personal data is not shared with third parties except where legally required. When the contact form is sent via WhatsApp, the message content is transmitted through WhatsApp/Meta infrastructure."]),
        ("5. Your Rights", [
            "Under Turkish Law No. 6698 on the Protection of Personal Data (KVKK), you may contact us at levent@mf-nautic.com to request access, correction or deletion of your data."]),
    ]
    build_legal("gizlilik-politikasi.html", "leg.title", "Gizlilik Politikası", "Privacy Policy",
                sections_tr, sections_en,
                "MF Nautic Turkey gizlilik politikası ve kişisel verilerin korunması hakkında bilgi.")

def build_kullanim():
    sections_tr = [
        ("1. Genel", [
            "Bu internet sitesi (\"Site\"), MF Nautic Yatçılık Ltd. Şti. tarafından, Tikal Marine Systems GmbH ürünlerinin Türkiye'deki resmi distribütörlüğü kapsamında bilgilendirme amacıyla işletilmektedir.",
            "Bu Site, Tikal Marine Systems GmbH'nin resmi kurumsal web sitesi değildir; Tikal markasına ait ürün görselleri ve marka unsurları, resmi distribütörlük ilişkisi çerçevesinde bilgilendirme amacıyla kullanılmaktadır."]),
        ("2. İçeriklerin Doğruluğu", [
            "Sitede yer alan ürün açıklamaları ve teknik bilgiler genel bilgilendirme amaçlıdır. Güncel ve bağlayıcı teknik veriler için lütfen ürünün resmi teknik veri formunu (TDS) talep edin veya bizimle iletişime geçin.",
            "MF Nautic, site içeriğinin güncelliğini sağlamak için makul özeni gösterir ancak olası hata veya eksikliklerden sorumlu tutulamaz."]),
        ("3. Fikri Mülkiyet", [
            "Sitedeki MF Nautic marka, logo ve özgün içerikler MF Nautic Yatçılık Ltd. Şti.'ye aittir. Tikal, Tikalflex ve ilgili marka/logo unsurları Tikal Marine Systems GmbH'nin fikri mülkiyetidir."]),
        ("4. İletişim Formu ve WhatsApp Kullanımı", [
            "Site üzerindeki formları kullanarak veya WhatsApp hattımız üzerinden bizimle iletişime geçtiğinizde, paylaştığınız bilgilerin doğru olduğunu kabul etmiş sayılırsınız."]),
        ("5. Uygulanacak Hukuk", [
            "Bu kullanım koşulları Türkiye Cumhuriyeti kanunlarına tabidir. Uyuşmazlıklarda Fethiye (Muğla) mahkemeleri ve icra daireleri yetkilidir."]),
    ]
    sections_en = [
        ("1. General", [
            "This website (\"Site\") is operated by MF Nautic Yatçılık Ltd. Şti. for informational purposes, as the official Turkish distributor of Tikal Marine Systems GmbH products.",
            "This Site is not the official corporate website of Tikal Marine Systems GmbH; Tikal-branded product imagery and brand elements are used for informational purposes within the scope of the official distributorship relationship."]),
        ("2. Accuracy of Content", [
            "Product descriptions and technical information on this Site are for general informational purposes. For current and binding technical data, please request the product's official technical data sheet (TDS) or contact us.",
            "MF Nautic takes reasonable care to keep site content up to date but cannot be held liable for possible errors or omissions."]),
        ("3. Intellectual Property", [
            "The MF Nautic brand, logo and original content on this Site belong to MF Nautic Yatçılık Ltd. Şti. Tikal, Tikalflex and related brand/logo elements are the intellectual property of Tikal Marine Systems GmbH."]),
        ("4. Contact Form and WhatsApp Use", [
            "By using the forms on this Site or contacting us via our WhatsApp line, you confirm that the information you provide is accurate."]),
        ("5. Governing Law", [
            "These terms of use are governed by the laws of the Republic of Türkiye. The courts and enforcement offices of Fethiye (Muğla) have jurisdiction over any disputes."]),
    ]
    build_legal("kullanim-kosullari.html", "leg.title", "Kullanım Koşulları", "Terms of Use",
                sections_tr, sections_en,
                "MF Nautic Turkey web sitesi kullanım koşulları.")

print("generator core loaded, ICONS:", len(ICONS))
build_home()
build_urunler_index()
build_all_categories()
build_tikalflex_detail()
build_hakkimizda()
build_iletisim()
build_dokumanlar()
build_gizlilik()
build_kullanim()
print("ALL PAGES BUILT")
