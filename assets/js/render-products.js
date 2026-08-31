/* =========================================================
   MF NAUTIC TURKEY — render-products.js
   Kategori sayfalarındaki ürün kartlarını Supabase'den canlı
   olarak çeker ve basar. Admin panelinden yapılan değişiklikler
   sitede anında (deploy gerekmeden) görünür.
   ========================================================= */
(function () {
  var LOADING_TR = "Ürünler yükleniyor...";
  var LOADING_EN = "Loading products...";
  var EMPTY_TR = "Bu kategoride henüz ürün eklenmedi.";
  var EMPTY_EN = "No products in this category yet.";

  var cache = null; // ürün listesi, dil değişince yeniden basmak için saklanır

  function cardHtml(p, basePath) {
    var title = MF.pick(p, "title");
    var summary = MF.pick(p, "summary");
    var tag = MF.pick(p, "tag");
    var lang = MF.getLang();
    var infoLabel = lang === "en" ? "Request Info" : "Bilgi İste";
    var moreLabel = lang === "en" ? "Details" : "Detayları Gör";
    var waText = (lang === "en" ? "Hello, I would like information about " : "Merhaba, ") +
      (lang === "en" ? title + "." : title + " hakkında bilgi almak istiyorum.");
    var detailHref = basePath + "urun.html?slug=" + encodeURIComponent(p.slug);
    var tagHtml = tag ? '<span class="hero-badge" style="margin-bottom:10px;display:inline-block">' + MF.escapeHtml(tag) + "</span>" : "";
    return (
      '<div class="prod-card">' +
      '<a href="' + detailHref + '" class="prod-media" aria-label="' + MF.escapeHtml(title) + '">' + MF.icon(p.icon) + "</a>" +
      '<div class="prod-body">' +
      tagHtml +
      '<h3><a href="' + detailHref + '" style="color:inherit;text-decoration:none">' + MF.escapeHtml(title) + "</a></h3>" +
      "<p>" + MF.escapeHtml(summary) + "</p>" +
      '<div class="prod-foot">' +
      '<a href="' + detailHref + '">' + moreLabel + MF.icon("arrow-right") + "</a>" +
      '<a href="' + MF.waLink(waText) + '" target="_blank" rel="noopener" class="wa-link">' + infoLabel + "</a>" +
      "</div></div></div>"
    );
  }

  function render(container, products) {
    var basePath = container.getAttribute("data-base") || "";
    if (!products || !products.length) {
      var lang = MF.getLang();
      container.innerHTML = '<p class="form-note">' + (lang === "en" ? EMPTY_EN : EMPTY_TR) + "</p>";
      return;
    }
    container.innerHTML = products.map(function (p) { return cardHtml(p, basePath); }).join("");
  }

  async function init() {
    var container = document.getElementById("prod-grid");
    if (!container) return;
    var catSlug = container.getAttribute("data-cat-slug");
    var lang = MF.getLang();
    container.innerHTML = '<div class="form-note">' + (lang === "en" ? LOADING_EN : LOADING_TR) + "</div>";

    var products;
    if (catSlug === "*") {
      products = await MF.getAllProducts();
    } else {
      products = await MF.getProductsByCategorySlug(catSlug);
    }
    cache = products;
    render(container, products);
  }

  // Dil değiştirildiğinde kartları yeniden bas (site.js kendi çevirisini uygular,
  // biz de dinamik içeriği güncelleriz)
  document.addEventListener("DOMContentLoaded", function () {
    init();
    document.querySelectorAll(".lang-switch button").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var container = document.getElementById("prod-grid");
        if (container && cache) {
          setTimeout(function () { render(container, cache); }, 0);
        }
      });
    });
  });
})();
