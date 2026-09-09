/* =========================================================
   MF NAUTIC TURKEY — /api/sitemap
   Vercel Serverless Function (Node.js runtime).
   Statik sayfaları sabit bir listeden, ürün detay sayfalarını
   (urunler/urun.html?slug=...) ise Supabase'ten canlı olarak
   çekip sitemap.xml çıktısı üretir.

   /sitemap.xml isteği vercel.json'daki rewrite kuralıyla bu
   fonksiyona yönlendirilir (bkz. vercel.json).

   Not: "tikalflex-contact-12" ürünü hem kendi özel statik sayfasına
   (urunler/tikalflex-contact-12.html, aşağıdaki STATIC_PAGES içinde)
   hem de Supabase'teki genel ürün kaydına sahip. Aynı içerik için iki
   ayrı URL'nin sitemap'e girip mükerrer kayıt oluşturmaması için bu
   slug, dinamik ürün listesinden hariç tutulur.
   ========================================================= */

var SUPABASE_URL = "https://bawkhuehmbskhjikjztg.supabase.co";
var SUPABASE_KEY = "sb_publishable_3g4Ij5yTpHS5nHy5fwQ5yQ_npYr2nb7";
var SITE_ORIGIN = "https://mfnautic.com";

/* Kendi özel statik sayfası olan, bu yüzden dinamik listeden hariç
   tutulması gereken ürün slug'ları. */
var EXCLUDE_PRODUCT_SLUGS = ["tikalflex-contact-12"];

var STATIC_PAGES = [
  { loc: "/", changefreq: "weekly", priority: "1.0" },
  { loc: "/urunler/index.html", changefreq: "weekly", priority: "0.9" },
  { loc: "/urunler/yapistirici-ve-mastikler.html", changefreq: "monthly", priority: "0.8" },
  { loc: "/urunler/deniz-yaglayicilari.html", changefreq: "monthly", priority: "0.8" },
  { loc: "/urunler/dolgu-macunlari.html", changefreq: "monthly", priority: "0.8" },
  { loc: "/urunler/tikal-tef-gel.html", changefreq: "monthly", priority: "0.8" },
  { loc: "/urunler/teak-deck.html", changefreq: "monthly", priority: "0.8" },
  { loc: "/urunler/aletler-ve-aksesuarlar.html", changefreq: "monthly", priority: "0.8" },
  { loc: "/urunler/tikalflex-contact-12.html", changefreq: "monthly", priority: "0.7" },
  { loc: "/dokumanlar.html", changefreq: "monthly", priority: "0.7" },
  { loc: "/kataloglar.html", changefreq: "monthly", priority: "0.7" },
  { loc: "/referanslarimiz.html", changefreq: "monthly", priority: "0.7" },
  { loc: "/bayilerimiz.html", changefreq: "monthly", priority: "0.7" },
  { loc: "/hakkimizda.html", changefreq: "monthly", priority: "0.6" },
  { loc: "/iletisim.html", changefreq: "monthly", priority: "0.6" },
  { loc: "/gizlilik-politikasi.html", changefreq: "yearly", priority: "0.3" },
  { loc: "/kullanim-kosullari.html", changefreq: "yearly", priority: "0.3" },
  { loc: "/kvkk-aydinlatma-metni.html", changefreq: "yearly", priority: "0.3" },
  { loc: "/cerez-politikasi.html", changefreq: "yearly", priority: "0.3" }
];

function escapeXml(s) {
  return String(s).replace(/[&<>"']/g, function (c) {
    return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
  });
}

function toLastmod(isoTimestamp) {
  if (!isoTimestamp) return null;
  var d = new Date(isoTimestamp);
  if (isNaN(d.getTime())) return null;
  return d.toISOString().slice(0, 10);
}

async function fetchPublishedProducts() {
  var url =
    SUPABASE_URL +
    "/rest/v1/products?select=slug,updated_at&published=eq.true&order=slug.asc";
  var res = await fetch(url, {
    headers: {
      apikey: SUPABASE_KEY,
      Authorization: "Bearer " + SUPABASE_KEY
    }
  });
  if (!res.ok) {
    throw new Error("Supabase sitemap sorgusu başarısız: " + res.status + " " + (await res.text()));
  }
  return res.json();
}

function buildXml(staticPages, products) {
  var urls = [];

  staticPages.forEach(function (p) {
    urls.push(
      "<url><loc>" + escapeXml(SITE_ORIGIN + p.loc) + "</loc>" +
      "<changefreq>" + p.changefreq + "</changefreq>" +
      "<priority>" + p.priority + "</priority></url>"
    );
  });

  products.forEach(function (p) {
    if (!p.slug || EXCLUDE_PRODUCT_SLUGS.indexOf(p.slug) !== -1) return;
    var loc = SITE_ORIGIN + "/urunler/urun.html?slug=" + encodeURIComponent(p.slug);
    var lastmod = toLastmod(p.updated_at);
    urls.push(
      "<url><loc>" + escapeXml(loc) + "</loc>" +
      (lastmod ? "<lastmod>" + lastmod + "</lastmod>" : "") +
      "<changefreq>monthly</changefreq>" +
      "<priority>0.7</priority></url>"
    );
  });

  return (
    '<?xml version="1.0" encoding="UTF-8"?>\n' +
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n  ' +
    urls.join("\n  ") +
    "\n</urlset>\n"
  );
}

module.exports = async function handler(req, res) {
  var products = [];
  try {
    products = await fetchPublishedProducts();
  } catch (err) {
    // Supabase erişilemezse bile statik sayfalarla dolu bir sitemap
    // döndürmeye devam et — sitemap'in tamamen kaybolması SEO açısından
    // ürün sayfalarının eksik olmasından daha kötüdür.
    console.error("[api/sitemap]", err);
  }

  var xml = buildXml(STATIC_PAGES, products);

  res.setHeader("Content-Type", "application/xml; charset=utf-8");
  // Edge'de 1 saat cache'le, arka planda 24 saate kadar bayat içerik
  // sunarak yenile — her arama motoru taramasında Supabase'e gitmeyi önler.
  res.setHeader("Cache-Control", "public, max-age=0, s-maxage=3600, stale-while-revalidate=86400");
  res.status(200).send(xml);
};
