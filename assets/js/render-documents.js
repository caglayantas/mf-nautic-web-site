/* =========================================================
   MF NAUTIC TURKEY — render-documents.js
   dokumanlar.html sayfasında her ÜRÜNÜ akordeon (aç/kapa) başlığı
   olarak listeler; başlık açıldığında sadece o ürüne ait dökümanlar
   (tüm dil linkleriyle, indirilebilir) görünür. Kataloglar (genel
   ürün kataloğu, uygulama kılavuzu vb.) bu sayfada DEĞİL, ayrı
   kataloglar.html sayfasında listelenir.
   ========================================================= */
(function () {
  var uid = 0;

  function groupByCategory(products) {
    var groups = [];
    var byId = {};
    products.forEach(function (p) {
      var cat = p.categories;
      var catId = cat ? cat.slug : "diger";
      if (!byId[catId]) {
        byId[catId] = { cat: cat, items: [] };
        groups.push(byId[catId]);
      }
      byId[catId].items.push(p);
    });
    groups.sort(function (a, b) {
      var oa = a.cat ? a.cat.sort_order : 999, ob = b.cat ? b.cat.sort_order : 999;
      return oa - ob;
    });
    return groups;
  }

  function docRowHtml(doc) {
    var lang = MF.getLang();
    var title = lang === "en" ? doc.title_en : doc.title_tr;
    var note = lang === "en" ? doc.note_en : doc.note_tr;
    var links = Array.isArray(doc.links) ? doc.links.filter(function (l) { return l && l.url; }) : [];

    if (links.length) {
      var langsHtml = links
        .map(function (l) {
          var isLocalFile = l.url && l.url.indexOf("/assets/") === 0;
          var attrs = isLocalFile ? " download" : ' target="_blank" rel="noopener"';
          return (
            '<a href="' + MF.escapeHtml(l.url) + '"' + attrs + ' class="lang-pill">' +
            MF.icon("download") + "<span>" + MF.escapeHtml(l.label || l.lang) + "</span></a>"
          );
        })
        .join("");
      return (
        '<div class="doc-row doc-row--multi">' +
        '<div class="doc-row-left"><div class="doc-ic">' + MF.icon("file-text") + "</div>" +
        "<div><b>" + MF.escapeHtml(title) + "</b>" + (note ? "<span>" + MF.escapeHtml(note) + "</span>" : "") + "</div></div>" +
        '<div class="pd-doc-langs doc-row-langs">' + langsHtml + "</div>" +
        "</div>"
      );
    }

    var reqLabel = lang === "en" ? "Request" : "İste";
    var waText = (lang === "en" ? "Hello, I would like the technical data sheet (TDS) for " + title + "." : "Merhaba, " + title + " için teknik veri formu (TDS) istiyorum.");
    var actionHref = doc.file_url ? doc.file_url : MF.waLink(waText);
    var isLocalFile = doc.file_url && doc.file_url.indexOf("/assets/") === 0;
    var actionTarget = doc.file_url ? (isLocalFile ? ' download' : ' target="_blank" rel="noopener"') : ' target="_blank" rel="noopener"';
    var actionIcon = MF.icon("download");
    return (
      '<div class="doc-row">' +
      '<div class="doc-row-left"><div class="doc-ic">' + MF.icon("file-text") + "</div>" +
      "<div><b>" + MF.escapeHtml(title) + "</b><span>" + MF.escapeHtml(note) + "</span></div></div>" +
      '<a href="' + actionHref + '"' + actionTarget + ' class="btn btn-outline btn-sm">' + actionIcon + "<span>" + reqLabel + "</span></a>" +
      "</div>"
    );
  }

  function productAccordionHtml(product, docs) {
    var lang = MF.getLang();
    var title = lang === "en" ? product.title_en : product.title_tr;
    var panelId = "doc-panel-" + (uid++);
    var countLabel = docs.length + " " + (lang === "en" ? (docs.length === 1 ? "document" : "documents") : "döküman");
    return (
      '<div class="doc-product">' +
      '<button type="button" class="doc-product-head" aria-expanded="false" aria-controls="' + panelId + '">' +
      '<span class="doc-ic">' + MF.icon(product.icon || "package") + "</span>" +
      '<span class="doc-product-title">' + MF.escapeHtml(title) + "</span>" +
      '<span class="doc-count">' + countLabel + "</span>" +
      '<svg class="chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>' +
      "</button>" +
      '<div class="doc-product-body" id="' + panelId + '" hidden>' +
      docs.map(docRowHtml).join("") +
      "</div>" +
      "</div>"
    );
  }

  function groupHtml(group) {
    var lang = MF.getLang();
    var catTitle = group.cat ? (lang === "en" ? group.cat.title_en : group.cat.title_tr) : (lang === "en" ? "Other" : "Diğer");
    var catIcon = group.cat ? MF.icon(group.cat.icon) : MF.icon("package");
    return (
      '<div class="doc-group"><h3>' + catIcon + "<span>" + MF.escapeHtml(catTitle) + "</span></h3>" +
      group.items.map(function (item) { return productAccordionHtml(item.product, item.docs); }).join("") +
      "</div>"
    );
  }

  function wireAccordions(container) {
    container.querySelectorAll(".doc-product-head").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var wrap = btn.closest(".doc-product");
        var body = wrap.querySelector(".doc-product-body");
        var isOpen = wrap.classList.toggle("is-open");
        btn.setAttribute("aria-expanded", isOpen ? "true" : "false");
        body.hidden = !isOpen;
      });
    });
  }

  function render(container, products, docsByProduct) {
    var lang = MF.getLang();
    var withDocs = products
      .map(function (p) { return { product: p, docs: docsByProduct[p.id] || [] }; })
      .filter(function (item) { return item.docs.length > 0; });

    if (!withDocs.length) {
      container.innerHTML = '<p class="form-note">' + (lang === "en" ? "No documents yet." : "Henüz döküman eklenmedi.") + "</p>";
      return;
    }

    var groups = [];
    var byId = {};
    withDocs.forEach(function (item) {
      var cat = item.product.categories;
      var catId = cat ? cat.slug : "diger";
      if (!byId[catId]) {
        byId[catId] = { cat: cat, items: [] };
        groups.push(byId[catId]);
      }
      byId[catId].items.push(item);
    });
    groups.sort(function (a, b) {
      var oa = a.cat ? a.cat.sort_order : 999, ob = b.cat ? b.cat.sort_order : 999;
      return oa - ob;
    });

    uid = 0;
    container.innerHTML = groups.map(groupHtml).join("");
    wireAccordions(container);
  }

  var cache = null;

  async function init() {
    var container = document.getElementById("doc-list");
    if (!container) return;
    var lang = MF.getLang();
    container.innerHTML = '<div class="form-note">' + (lang === "en" ? "Loading documents..." : "Dökümanlar yükleniyor...") + "</div>";

    var results = await Promise.all([MF.getAllProducts(), MF.getDocuments()]);
    var products = results[0] || [];
    var docs = results[1] || [];

    var docsByProduct = {};
    docs.forEach(function (d) {
      if (!d.product_id) return;
      if (!docsByProduct[d.product_id]) docsByProduct[d.product_id] = [];
      docsByProduct[d.product_id].push(d);
    });

    cache = { products: products, docsByProduct: docsByProduct };
    render(container, products, docsByProduct);
  }

  document.addEventListener("DOMContentLoaded", function () {
    init();
    document.querySelectorAll(".lang-switch button").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var container = document.getElementById("doc-list");
        if (container && cache) setTimeout(function () { render(container, cache.products, cache.docsByProduct); }, 0);
      });
    });
  });
})();
