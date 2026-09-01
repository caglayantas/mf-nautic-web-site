/* =========================================================
   MF NAUTIC TURKEY — render-catalogs.js
   kataloglar.html sayfasındaki genel katalog / kılavuz listesini
   Supabase'den canlı olarak çeker ve basar.
   ========================================================= */
(function () {
  function catalogRowHtml(c) {
    var lang = MF.getLang();
    var title = lang === "en" ? c.title_en : c.title_tr;
    var note = lang === "en" ? c.note_en : c.note_tr;
    var pills = "";
    if (c.file_url_tr) {
      var isLocalTr = c.file_url_tr.indexOf("/assets/") === 0;
      pills += '<a href="' + MF.escapeHtml(c.file_url_tr) + '"' + (isLocalTr ? " download" : ' target="_blank" rel="noopener"') + ' class="lang-pill">' + MF.icon("download") + "<span>" + (lang === "en" ? "Turkish (PDF)" : "Türkçe (PDF)") + "</span></a>";
    }
    if (c.file_url_en) {
      var isLocalEn = c.file_url_en.indexOf("/assets/") === 0;
      pills += '<a href="' + MF.escapeHtml(c.file_url_en) + '"' + (isLocalEn ? " download" : ' target="_blank" rel="noopener"') + ' class="lang-pill">' + MF.icon("download") + "<span>" + (lang === "en" ? "English (PDF)" : "İngilizce (PDF)") + "</span></a>";
    }
    return (
      '<div class="doc-row doc-row--multi">' +
      '<div class="doc-row-left"><div class="doc-ic">' + MF.icon("file-text") + "</div>" +
      "<div><b>" + MF.escapeHtml(title) + "</b>" + (note ? "<span>" + MF.escapeHtml(note) + "</span>" : "") + "</div></div>" +
      '<div class="pd-doc-langs doc-row-langs">' + pills + "</div>" +
      "</div>"
    );
  }

  function render(container, catalogs) {
    var lang = MF.getLang();
    if (!catalogs || !catalogs.length) {
      container.innerHTML = '<p class="form-note">' + (lang === "en" ? "No catalogues added yet." : "Henüz katalog eklenmedi.") + "</p>";
      return;
    }
    container.innerHTML = catalogs.map(catalogRowHtml).join("");
  }

  var cache = null;

  async function init() {
    var container = document.getElementById("catalog-list");
    if (!container) return;
    var catalogs = await MF.getCatalogs();
    cache = catalogs;
    render(container, catalogs);
  }

  document.addEventListener("DOMContentLoaded", function () {
    init();
    document.querySelectorAll(".lang-switch button").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var container = document.getElementById("catalog-list");
        if (container && cache) setTimeout(function () { render(container, cache); }, 0);
      });
    });
  });
})();
