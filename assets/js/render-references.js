/* =========================================================
   MF NAUTIC TURKEY — render-references.js
   referanslarimiz.html sayfasındaki "Referans Projelerimiz" ve
   "Referans Firmalarımız" bölümlerini Supabase'den canlı olarak
   çeker ve iki ayrı grid halinde basar.
   ========================================================= */
(function () {
  function refCardHtml(r) {
    var lang = MF.getLang();
    var title = lang === "en" ? r.title_en : r.title_tr;
    var desc = lang === "en" ? r.desc_en : r.desc_tr;
    var isCompany = r.type === "company";
    var logoHtml = r.logo_url
      ? '<img src="' + MF.escapeHtml(r.logo_url) + '" alt="' + MF.escapeHtml(title) + '" loading="lazy">'
      : '<div class="ic">' + MF.icon(isCompany ? "package" : "anchor") + "</div>";
    var linkHtml = "";
    if (r.website_url) {
      var label = r.website_url.replace(/^https?:\/\//, "").replace(/\/$/, "");
      linkHtml = '<a href="' + MF.escapeHtml(r.website_url) + '" target="_blank" rel="noopener" class="ref-link">' +
        MF.escapeHtml(label) + MF.icon("arrow-right") + "</a>";
    }
    return (
      '<div class="ref-card' + (isCompany ? " ref-card--company" : "") + '">' +
      '<div class="ref-logo">' + logoHtml + "</div>" +
      "<h3>" + MF.escapeHtml(title) + "</h3>" +
      (desc ? "<p>" + MF.escapeHtml(desc) + "</p>" : "<p></p>") +
      linkHtml +
      "</div>"
    );
  }

  function renderGroup(grid, emptyEl, items) {
    if (!grid) return;
    if (!items || !items.length) {
      grid.style.display = "none";
      if (emptyEl) emptyEl.style.display = "";
      return;
    }
    grid.style.display = "";
    if (emptyEl) emptyEl.style.display = "none";
    grid.innerHTML = items.map(refCardHtml).join("");
  }

  var cache = null;

  function renderAll(refs) {
    var projectsGrid = document.getElementById("ref-projects-grid");
    var companiesGrid = document.getElementById("ref-companies-grid");
    if (!projectsGrid && !companiesGrid) return;
    var projects = (refs || []).filter(function (r) { return r.type !== "company"; });
    var companies = (refs || []).filter(function (r) { return r.type === "company"; });
    renderGroup(projectsGrid, document.getElementById("ref-projects-empty"), projects);
    renderGroup(companiesGrid, document.getElementById("ref-companies-empty"), companies);
  }

  async function init() {
    var projectsGrid = document.getElementById("ref-projects-grid");
    var companiesGrid = document.getElementById("ref-companies-grid");
    if (!projectsGrid && !companiesGrid) return;
    var refs = await MF.getReferences();
    cache = refs;
    renderAll(refs);
  }

  document.addEventListener("DOMContentLoaded", function () {
    init();
    document.querySelectorAll(".lang-switch button").forEach(function (btn) {
      btn.addEventListener("click", function () {
        if (cache) setTimeout(function () { renderAll(cache); }, 0);
      });
    });
  });
})();
