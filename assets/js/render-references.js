/* =========================================================
   MF NAUTIC TURKEY — render-references.js
   referanslarimiz.html sayfasındaki referans/işbirliği kartlarını
   Supabase'den canlı olarak çeker ve basar.
   ========================================================= */
(function () {
  function refCardHtml(r) {
    var lang = MF.getLang();
    var title = lang === "en" ? r.title_en : r.title_tr;
    var desc = lang === "en" ? r.desc_en : r.desc_tr;
    var logoHtml = r.logo_url
      ? '<img src="' + MF.escapeHtml(r.logo_url) + '" alt="' + MF.escapeHtml(title) + '" loading="lazy">'
      : '<div class="ic">' + MF.icon("anchor") + "</div>";
    var linkHtml = "";
    if (r.website_url) {
      var label = r.website_url.replace(/^https?:\/\//, "").replace(/\/$/, "");
      linkHtml = '<a href="' + MF.escapeHtml(r.website_url) + '" target="_blank" rel="noopener" class="ref-link">' +
        MF.escapeHtml(label) + MF.icon("arrow-right") + "</a>";
    }
    return (
      '<div class="ref-card">' +
      '<div class="ref-logo">' + logoHtml + "</div>" +
      "<h3>" + MF.escapeHtml(title) + "</h3>" +
      (desc ? "<p>" + MF.escapeHtml(desc) + "</p>" : "<p></p>") +
      linkHtml +
      "</div>"
    );
  }

  function render(container, emptySection, refs) {
    if (!refs || !refs.length) {
      container.style.display = "none";
      if (emptySection) emptySection.style.display = "";
      return;
    }
    container.style.display = "";
    if (emptySection) emptySection.style.display = "none";
    container.innerHTML = refs.map(refCardHtml).join("");
  }

  var cache = null;

  async function init() {
    var container = document.getElementById("ref-grid");
    if (!container) return;
    var emptySection = document.getElementById("ref-empty-section");
    var refs = await MF.getReferences();
    cache = refs;
    render(container, emptySection, refs);
  }

  document.addEventListener("DOMContentLoaded", function () {
    init();
    document.querySelectorAll(".lang-switch button").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var container = document.getElementById("ref-grid");
        var emptySection = document.getElementById("ref-empty-section");
        if (container && cache) setTimeout(function () { render(container, emptySection, cache); }, 0);
      });
    });
  });
})();
