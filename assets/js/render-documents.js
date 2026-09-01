/* =========================================================
   MF NAUTIC TURKEY — render-documents.js
   dokumanlar.html sayfasındaki döküman listesini Supabase'den
   canlı olarak çeker, kategoriye göre gruplar ve basar.
   ========================================================= */
(function () {
  var ICON_FILE = MF && MF.icon ? MF.icon("file-text") : "";
  var cache = null;

  function groupByCategory(docs) {
    var groups = [];
    var byId = {};
    docs.forEach(function (d) {
      var cat = d.categories;
      var catId = cat ? cat.slug : "diger";
      if (!byId[catId]) {
        byId[catId] = { cat: cat, items: [] };
        groups.push(byId[catId]);
      }
      byId[catId].items.push(d);
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

  function groupHtml(group) {
    var lang = MF.getLang();
    var catTitle = group.cat ? (lang === "en" ? group.cat.title_en : group.cat.title_tr) : (lang === "en" ? "Other" : "Diğer");
    var catIcon = group.cat ? MF.icon(group.cat.icon) : MF.icon("package");
    return (
      '<div class="doc-group"><h3>' + catIcon + "<span>" + MF.escapeHtml(catTitle) + "</span></h3>" +
      group.items.map(docRowHtml).join("") +
      "</div>"
    );
  }

  function render(container, docs) {
    if (!docs || !docs.length) {
      var lang = MF.getLang();
      container.innerHTML = '<p class="form-note">' + (lang === "en" ? "No documents yet." : "Henüz döküman eklenmedi.") + "</p>";
      return;
    }
    var groups = groupByCategory(docs);
    container.innerHTML = groups.map(groupHtml).join("");
  }

  async function init() {
    var container = document.getElementById("doc-list");
    if (!container) return;
    var lang = MF.getLang();
    container.innerHTML = '<div class="form-note">' + (lang === "en" ? "Loading documents..." : "Dökümanlar yükleniyor...") + "</div>";
    var docs = await MF.getDocuments();
    cache = docs;
    render(container, docs);
  }

  document.addEventListener("DOMContentLoaded", function () {
    init();
    document.querySelectorAll(".lang-switch button").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var container = document.getElementById("doc-list");
        if (container && cache) setTimeout(function () { render(container, cache); }, 0);
      });
    });
  });
})();
