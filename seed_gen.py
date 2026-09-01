# -*- coding: utf-8 -*-
import json

def esc(s):
    if s is None:
        return "NULL"
    return "'" + str(s).replace("'", "''") + "'"

def jb(obj):
    return esc(json.dumps(obj, ensure_ascii=False)) + "::jsonb"

CATEGORIES = [
    ("yapistirici-ve-mastikler", "droplet", "Yapıştırıcı ve Mastikler", "Adhesives & Sealants",
     "MS Polimer serisi, ahşap, alüminyum, çelik ve GRP yüzeylerde yüksek mukavemetli, suya dayanıklı yapıştırma ve derzleme çözümleri.",
     "MS Polymer range offering high-strength, water-resistant bonding and sealing for wood, aluminium, steel and GRP.", 1),
    ("deniz-yaglayicilari", "droplet", "Deniz Yağlayıcıları", "Marine Lubricants",
     "Deniz ortamına özel geliştirilmiş yüksek performanslı gres ve yağlayıcılar.",
     "High-performance greases and lubricants engineered for the marine environment.", 2),
    ("dolgu-macunlari", "layers", "Dolgu Macunları", "Fillers",
     "Hızlı kuruyan, kolay zımparalanan profesyonel tekne dolgu macunları.",
     "Fast-curing, easy-to-sand professional boat filler putties.", 3),
    ("tikal-tef-gel", "shield-check", "Tikal Tef-Gel", "Tikal Tef-Gel",
     "Metal bağlantı elemanlarını elektroliz korozyonuna karşı koruyan özel gres.",
     "Special anti-seize gel that protects metal fasteners against galvanic corrosion.", 4),
    ("teak-deck", "anchor", "Teak Deck Sistemleri", "Teak Deck Systems",
     "Teak güverte bakımı, onarımı ve temizliği için komple ürün gamı.",
     "A complete product range for teak deck maintenance, repair and cleaning.", 5),
    ("aletler-ve-aksesuarlar", "tool", "Aletler ve Aksesuarlar", "Tools & Accessories",
     "Uygulama tabancaları, derz aletleri ve yüzey temizleme ürünleri.",
     "Application guns, joint tools and surface cleaning products.", 6),
]

TIKALFLEX_SPECS = [
    ("Kimyasal Yapı", "MS Polimer", "Chemical Base", "MS Polymer"),
    ("Uygulama Sıcaklığı", "0°C ile +40°C arası", "Application Temperature", "0°C to +40°C"),
    ("Yüzey Kuruma Süresi", "10–15 dakika", "Skin Forming Time", "10–15 minutes"),
    ("Kürleşme Hızı", "~2 mm / 24 saat (25°C, %65 bağıl nem)", "Curing Speed", "~2 mm / 24h (25°C, 65% RH)"),
    ("Shore A Sertliği", "60", "Shore A Hardness", "60"),
    ("Çekme Mukavemeti", "2,3 N/mm²", "Tensile Strength", "2.3 N/mm²"),
    ("Kopmada Uzama", "%350", "Elongation at Break", "350%"),
    ("Raf Ömrü", "18 ay (5°C–25°C arasında saklama)", "Shelf Life", "18 months (stored at 5°C–25°C)"),
    ("Tuzlu Su / Hava Şartlarına Dayanım", "Evet", "Saltwater / Weathering Resistance", "Yes"),
    ("UV Dayanımı", "Hayır — üzeri boya/vernik ile kaplanmalı", "UV Resistance", "No — must be overcoated with paint/varnish"),
]
TIKALFLEX_PACK = [
    ("24 × 70 ml kartuş", "24 × 70 ml cartridges"),
    ("12 × 290 ml kartuş", "12 × 290 ml cartridges"),
    ("12 × 600 ml torba/kartuş", "12 × 600 ml pouches/cartridges"),
    ("Renkler: Beyaz, Siyah, Gri", "Colours: White, Black, Grey"),
]
TIKALFLEX_FEATURES = [
    ("Yüksek yapışma mukavemeti, toleransları telafi eder", "High bonding strength, compensates for tolerances"),
    ("Küçülme yapmaz, su altı ve su üstü uygulamalara uygundur", "Shrink-free, suitable for above- and below-water applications"),
    ("Kürleştikten sonra zımparalanabilir, normal boya/vernik ile uyumludur", "Sandable when cured, compatible with normal paint/varnish"),
    ("Nitrik asit, kostik soda, yağ ve dizele karşı dayanıklıdır", "Resistant to nitric acid, caustic soda, oil and diesel"),
]

# (cat_slug, slug, title_tr, title_en, summary_tr, summary_en, body_tr, body_en, icon, video_url, tag_tr, tag_en, featured, specs, packaging, features)
PRODUCTS = [
    ("yapistirici-ve-mastikler", "tikalflex-contact-12", "Tikalflex Contact 12", "Tikalflex Contact 12",
     "Küçülme yapmayan, çok güçlü, suya dayanıklı MS Polimer yapıştırıcı. Ahşap, alüminyum, çelik ve GRP yüzeylerde profesyonel yapıştırma için idealdir.",
     "A shrink-free, very strong, waterproof MS Polymer adhesive — ideal for professional bonding on wood, aluminium, steel and GRP.",
     "Tikalflex Contact 12, ahşap, alüminyum, çelik ve GRP (fiberglas) yüzeylerde kalıcı ve esnek bağlantılar oluşturan tek bileşenli bir MS Polimer yapıştırıcıdır. Nemle temas ettiğinde sertleşir ve kürleştikten sonra zımparalanabilir.",
     "Tikalflex Contact 12 is a one-component MS Polymer adhesive that creates permanent, flexible bonds on wood, aluminium, steel and GRP surfaces. It cures on contact with humidity and is sandable once cured.",
     "droplet", "https://www.youtube.com/watch?v=9kLhh4HAotc", "Öne Çıkan Ürün", "Featured Product", True,
     TIKALFLEX_SPECS, TIKALFLEX_PACK, TIKALFLEX_FEATURES),
    ("yapistirici-ve-mastikler", "tikalflex-family", "Tikalflex Yapıştırıcı ve Mastik Ailesi", "Tikalflex Adhesive & Sealant Range",
     "Farklı sertlik, kürleşme hızı ve uygulama alanlarına sahip tam Tikalflex serisi için teknik ekibimizle iletişime geçin.",
     "Contact our technical team to learn about the full Tikalflex range, with different hardness, cure speeds and applications.",
     "Tikalflex ürün ailesi; farklı sertlik, renk ve kürleşme sürelerine sahip MS Polimer yapıştırıcı ve mastik çeşitlerinden oluşur. İhtiyacınıza en uygun ürünü belirlemek için bizimle iletişime geçin.",
     "The Tikalflex range includes MS Polymer adhesives and sealants in various hardness levels, colours and cure times. Contact us to find the right product for your needs.",
     "layers", None, None, None, False, [], [], []),

    ("deniz-yaglayicilari", "hp-mg", "HP-MG Deniz Gresi", "HP-MG Marine Grease",
     "Deniz ortamı için geliştirilmiş, korozyona ve suya karşı yüksek dayanım gösteren özel performans gresi.",
     "A special high-performance grease developed for the marine environment, with strong resistance to corrosion and water.",
     "HP-MG, vinç, ırgat ve hareketli metal aksamlarda kullanılan, deniz suyuna ve neme karşı yüksek direnç gösteren özel bir performans gresidir.",
     "HP-MG is a special high-performance grease used on winches, windlasses and moving metal parts, with strong resistance to seawater and moisture.",
     "droplet", None, None, None, False, [], [], []),

    ("dolgu-macunlari", "fast-patch", "Fast Patch", "Fast Patch",
     "Hızlı kuruyan, kolay zımparalanabilen, tekne gövde ve güverte onarımları için profesyonel dolgu macunu.",
     "A fast-curing, easy-to-sand professional filler putty for hull and deck repairs.",
     "Fast Patch, tekne gövde ve güverte onarımlarında hızlı kürleşme ve kolay zımparalama imkânı sunan profesyonel bir dolgu macunudur.",
     "Fast Patch is a professional filler putty offering fast curing and easy sanding for hull and deck repairs.",
     "layers", None, None, None, False, [], [], []),
    ("dolgu-macunlari", "fast-patch-light", "Fast Patch LIGHT", "Fast Patch LIGHT",
     "Fast Patch'in daha hafif, düşük yoğunluklu versiyonu; büyük yüzey onarımlarında daha az ağırlık artışı sağlar.",
     "A lighter, low-density version of Fast Patch — adds less weight on larger surface repairs.",
     "Fast Patch LIGHT, standart Fast Patch'e göre daha düşük yoğunluğa sahiptir ve büyük yüzey onarımlarında tekneye daha az ağırlık ekler.",
     "Fast Patch LIGHT has a lower density than the standard Fast Patch, adding less weight to the boat on larger surface repairs.",
     "layers", None, None, None, False, [], [], []),

    ("tikal-tef-gel", "tef-gel", "Tikal Tef-Gel", "Tikal Tef-Gel",
     "Vida, cıvata, pervane mili gibi metal bağlantı elemanlarını elektrolitik korozyona karşı koruyan özel anti-sızdırmazlık gresi.",
     "A special anti-seize gel that protects fasteners such as screws, bolts and propeller shafts against galvanic corrosion.",
     "Tikal Tef-Gel, farklı metallerin bir arada kullanıldığı deniz ortamındaki bağlantı elemanlarını elektrolitik (galvanik) korozyona karşı korur ve sökülüp takılmayı kolaylaştırır.",
     "Tikal Tef-Gel protects fasteners used in mixed-metal marine environments against galvanic corrosion and makes disassembly easier.",
     "shield-check", "https://www.youtube.com/watch?v=50jN3mmFOu4", "Öne Çıkan Ürün", "Featured Product", True, [], [], []),

    ("teak-deck", "tsc-plus", "TSC plus", "TSC plus",
     "Teak derzleri için tek bileşenli, esnek ve dayanıklı kalafat (derz dolgu) macunu.",
     "A one-component, flexible and durable caulking compound for teak deck seams.",
     "TSC plus, teak güverte derzlerinin doldurulmasında kullanılan, esnekliğini uzun süre koruyan tek bileşenli bir kalafat macunudur.",
     "TSC plus is a one-component caulking compound used to fill teak deck seams, retaining its flexibility over the long term.",
     "anchor", "https://www.youtube.com/watch?v=xhd5PG7CRV0", "Öne Çıkan Ürün", "Featured Product", True, [], [], []),
    ("teak-deck", "tlb-flex", "TLB Flex", "TLB Flex",
     "Teak güverte yapıştırma sistemlerinde kullanılan esnek, yüksek mukavemetli bağlayıcı.",
     "A flexible, high-strength adhesive used in teak deck bonding systems.",
     "TLB Flex, teak tahtalarının tekne güvertesine yapıştırılmasında kullanılan, yüksek mukavemetli ve esnek bir bağlayıcıdır.",
     "TLB Flex is a high-strength, flexible adhesive used to bond teak planks to the boat deck.",
     "anchor", None, None, None, False, [], [], []),
    ("teak-deck", "synteak-activator", "Synteak Activator", "Synteak Activator",
     "Sentetik teak (suni teak) uygulamalarında yüzey hazırlığı için özel aktivatör astar.",
     "A special activator primer for surface preparation in synthetic teak applications.",
     "Synteak Activator, sentetik teak kaplamalarının uygulanmasından önce yüzey hazırlığı için kullanılan özel bir aktivatör astardır.",
     "Synteak Activator is a special primer used to prepare the surface before applying synthetic teak coverings.",
     "anchor", None, None, None, False, [], [], []),
    ("teak-deck", "cork-teak-protect", "Cork+ Teak Protect", "Cork+ Teak Protect",
     "Teak yüzeyleri UV ışınlarına ve neme karşı koruyan mantar bazlı koruyucu kaplama.",
     "A cork-based protective coating that shields teak surfaces from UV rays and moisture.",
     "Cork+ Teak Protect, teak yüzeyleri UV ışınlarına ve neme karşı koruyan, mantar bazlı özel bir koruyucu kaplamadır.",
     "Cork+ Teak Protect is a special cork-based protective coating that shields teak surfaces from UV rays and moisture.",
     "anchor", None, None, None, False, [], [], []),
    ("teak-deck", "teak-cleaner", "Teak Cleaner", "Teak Cleaner",
     "Teak güvertelerde derinlemesine temizlik yapan, gri lekeleri gideren özel temizleyici.",
     "A deep-cleaning solution that removes grey staining from teak decks.",
     "Teak Cleaner, teak güvertelerde zamanla oluşan gri lekeleri gidererek derinlemesine temizlik sağlayan özel bir temizleyicidir.",
     "Teak Cleaner is a special cleaning solution that removes grey staining that builds up on teak decks over time, providing a deep clean.",
     "anchor", None, None, None, False, [], [], []),
    ("teak-deck", "tlb-pox", "TLB Pox", "TLB Pox",
     "Teak onarımlarında kullanılan, yüksek yapışma mukavemetine sahip iki bileşenli epoksi dolgu sistemi.",
     "A two-component epoxy filling system with high bond strength, used for teak repairs.",
     "TLB Pox, teak güverte onarımlarında kullanılan, yüksek yapışma mukavemetine sahip iki bileşenli bir epoksi dolgu sistemidir.",
     "TLB Pox is a two-component epoxy filling system with high bond strength, used for teak deck repairs.",
     "anchor", None, None, None, False, [], [], []),

    ("aletler-ve-aksesuarlar", "cartridge-guns", "Kartuş ve Tüp Tabancaları", "Cartridge & Tube Guns",
     "Tikalflex ve diğer kartuş/tüp ambalajlı ürünler için profesyonel, ergonomik uygulama tabancaları.",
     "Professional, ergonomic application guns for Tikalflex and other cartridge/tube packaged products.",
     "Tikalflex ve diğer kartuş/tüp ambalajlı Tikal ürünlerinin düzgün ve kontrollü şekilde uygulanmasını sağlayan profesyonel tabancalardır.",
     "Professional guns that allow smooth, controlled application of Tikalflex and other cartridge/tube packaged Tikal products.",
     "tool", None, None, None, False, [], [], []),
    ("aletler-ve-aksesuarlar", "joint-tool", "Derz Aleti (Joint Tool)", "Joint Tool",
     "Mastik ve dolgu derzlerinin düzgün, profesyonel bir görünüm kazanması için özel şekillendirme aleti.",
     "A special shaping tool for a clean, professional finish on sealant and filler joints.",
     "Joint Tool, uygulanan mastik ve dolgu derzlerinin düzgün, pürüzsüz ve profesyonel bir görünüm kazanmasını sağlayan özel bir şekillendirme aletidir.",
     "The Joint Tool is a special shaping tool that gives applied sealant and filler joints a clean, smooth, professional finish.",
     "tool", None, None, None, False, [], [], []),
    ("aletler-ve-aksesuarlar", "magic-clean", "Magic Clean", "Magic Clean",
     "Uygulama sonrası el ve yüzeylerde kalan yapıştırıcı/mastik artıklarını kolayca temizleyen özel temizlik ürünü.",
     "A special cleaning product that easily removes leftover adhesive/sealant residue from hands and surfaces after application.",
     "Magic Clean, uygulama sonrası el ve yüzeylerde kalan Tikalflex ve mastik artıklarını kolayca temizlemenizi sağlayan özel bir temizlik ürünüdür.",
     "Magic Clean is a special cleaning product that easily removes leftover Tikalflex and sealant residue from hands and surfaces after application.",
     "tool", None, None, None, False, [], [], []),
]

# documents: (cat_slug, title, note optional None=default)
DOCUMENTS = [
    ("yapistirici-ve-mastikler", "Tikalflex Contact 12"),
    ("yapistirici-ve-mastikler", "Tikalflex Ürün Ailesi / Product Range"),
    ("deniz-yaglayicilari", "HP-MG Deniz Gresi / Marine Grease"),
    ("dolgu-macunlari", "Fast Patch"),
    ("dolgu-macunlari", "Fast Patch LIGHT"),
    ("tikal-tef-gel", "Tikal Tef-Gel"),
    ("teak-deck", "TSC plus"),
    ("teak-deck", "TLB Flex"),
    ("teak-deck", "Synteak Activator"),
    ("teak-deck", "Cork+ Teak Protect"),
    ("teak-deck", "Teak Cleaner"),
    ("teak-deck", "TLB Pox"),
    ("aletler-ve-aksesuarlar", "Kartuş ve Tüp Tabancaları"),
    ("aletler-ve-aksesuarlar", "Derz Aleti (Joint Tool)"),
    ("aletler-ve-aksesuarlar", "Magic Clean"),
]

out = []
out.append("-- categories")
for i, (slug, icon, ttr, ten, dtr, den, order) in enumerate(CATEGORIES):
    out.append(
        f"insert into public.categories (slug, icon, title_tr, title_en, desc_tr, desc_en, sort_order) values "
        f"({esc(slug)}, {esc(icon)}, {esc(ttr)}, {esc(ten)}, {esc(dtr)}, {esc(den)}, {order});"
    )

out.append("-- products")
for i, (cat_slug, slug, ttr, ten, sumtr, sumen, bodytr, bodyen, icon, video, tagtr, tagen, featured, specs, pack, feats) in enumerate(PRODUCTS):
    specs_json = [{"k_tr": a, "v_tr": b, "k_en": c, "v_en": d} for (a, b, c, d) in specs]
    pack_json = [{"tr": a, "en": b} for (a, b) in pack]
    feats_json = [{"tr": a, "en": b} for (a, b) in feats]
    out.append(
        "insert into public.products (category_id, slug, title_tr, title_en, summary_tr, summary_en, body_tr, body_en, "
        "icon, video_url, tag_tr, tag_en, featured, specs, packaging, features, sort_order) values ("
        f"(select id from public.categories where slug={esc(cat_slug)}), {esc(slug)}, {esc(ttr)}, {esc(ten)}, "
        f"{esc(sumtr)}, {esc(sumen)}, {esc(bodytr)}, {esc(bodyen)}, {esc(icon)}, {esc(video)}, {esc(tagtr)}, {esc(tagen)}, "
        f"{'true' if featured else 'false'}, {jb(specs_json)}, {jb(pack_json)}, {jb(feats_json)}, {i});"
    )

out.append("-- documents")
for i, (cat_slug, title) in enumerate(DOCUMENTS):
    out.append(
        "insert into public.documents (category_id, title_tr, title_en, sort_order) values ("
        f"(select id from public.categories where slug={esc(cat_slug)}), {esc(title)}, {esc(title)}, {i});"
    )

sql = "\n".join(out)
with open("/root/mfnautic-site/seed.sql", "w", encoding="utf-8") as f:
    f.write(sql)
print("bytes:", len(sql.encode("utf-8")))
print("lines:", len(out))
