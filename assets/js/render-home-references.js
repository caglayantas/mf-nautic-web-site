/* =========================================================
   MF NAUTIC TURKEY — render-home-references.js
   Ana sayfadaki "Referanslarımız" bölümünü (sağ/sol ok ile
   kaydırılabilir kart karuseli) Supabase'den canlı olarak
   çeker ve basar.
   ========================================================= */
(function () {
  function cardHtml(r) {
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

  var cache = null;
  var track = null;

  function render(refs) {
    if (!track) return;
    var section = document.getElementById("home-references");
    if (!refs || !refs.length) {
      if (section) section.style.display = "none";
      return;
    }
    if (section) section.style.display = "";
    track.innerHTML = refs.map(cardHtml).join("");
  }

  async function init() {
    track = document.getElementById("home-ref-track");
    if (!track) return;
    var refs = await MF.getReferences();
    // Ana sayfada sadece referans PROJELERİ (yat/refit) gösterilir; referans
    // firmaları (tersane/marina vb.) sadece Referanslarımız sayfasında listelenir.
    refs = (refs || []).filter(function (r) { return r.type !== "company"; });
    cache = refs;
    render(refs);

    var prevBtn = document.querySelector(".ref-car-prev");
    var nextBtn = document.querySelector(".ref-car-next");
    function scrollByCard(dir) {
      var card = track.querySelector(".ref-card");
      var step = card ? card.getBoundingClientRect().width + 20 : 300;
      track.scrollBy({ left: dir * step, behavior: "smooth" });
    }
    if (prevBtn) prevBtn.addEventListener("click", function () { scrollByCard(-1); });
    if (nextBtn) nextBtn.addEventListener("click", function () { scrollByCard(1); });
  }

  document.addEventListener("DOMContentLoaded", function () {
    init();
    document.querySelectorAll(".lang-switch button").forEach(function (btn) {
      btn.addEventListener("click", function () {
        if (track && cache) setTimeout(function () { render(cache); }, 0);
      });
    });
  });
})();
