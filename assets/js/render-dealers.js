/* =========================================================
   MF NAUTIC TURKEY — render-dealers.js
   bayilerimiz.html sayfasındaki bayi listesini Supabase'den
   canlı olarak çeker ve basar.
   ========================================================= */
(function () {
  function dealerCardHtml(d) {
    var lang = MF.getLang();
    var title = lang === "en" ? d.title_en : d.title_tr;
    var badge = lang === "en" ? d.badge_en : d.badge_tr;
    var address = lang === "en" ? d.address_en : d.address_tr;
    var items = [];
    if (address) {
      items.push('<li>' + MF.icon("map-pin") + "<span>" + MF.escapeHtml(address) + "</span></li>");
    }
    if (d.phone) {
      var telHref = "tel:" + d.phone.replace(/[^0-9+]/g, "");
      items.push('<li>' + MF.icon("phone") + '<a href="' + MF.escapeHtml(telHref) + '">' + MF.escapeHtml(d.phone) + "</a></li>");
    }
    if (d.email) {
      items.push('<li>' + MF.icon("mail") + '<a href="mailto:' + MF.escapeHtml(d.email) + '">' + MF.escapeHtml(d.email) + "</a></li>");
    }
    if (d.website_url) {
      var label = d.website_url.replace(/^https?:\/\//, "").replace(/\/$/, "");
      items.push('<li>' + MF.icon("globe") + '<a href="' + MF.escapeHtml(d.website_url) + '" target="_blank" rel="noopener">' + MF.escapeHtml(label) + "</a></li>");
    }
    return (
      '<div class="dealer-card">' +
      (badge ? '<div class="tag-badge">' + MF.escapeHtml(badge) + "</div>" : "") +
      "<h3>" + MF.escapeHtml(title) + "</h3>" +
      "<ul>" + items.join("") + "</ul>" +
      "</div>"
    );
  }

  function render(container, emptySection, dealers) {
    if (!dealers || !dealers.length) {
      container.style.display = "none";
      if (emptySection) emptySection.style.display = "";
      return;
    }
    container.style.display = "";
    if (emptySection) emptySection.style.display = "none";
    container.innerHTML = dealers.map(dealerCardHtml).join("");
  }

  var cache = null;

  async function init() {
    var container = document.getElementById("dealer-grid");
    if (!container) return;
    var emptySection = document.getElementById("dealer-empty-section");
    var dealers = await MF.getDealers();
    cache = dealers;
    render(container, emptySection, dealers);
  }

  document.addEventListener("DOMContentLoaded", function () {
    init();
    document.querySelectorAll(".lang-switch button").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var container = document.getElementById("dealer-grid");
        var emptySection = document.getElementById("dealer-empty-section");
        if (container && cache) setTimeout(function () { render(container, emptySection, cache); }, 0);
      });
    });
  });
})();
