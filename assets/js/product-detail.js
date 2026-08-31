/* =========================================================
   MF NAUTIC TURKEY — product-detail.js
   urunler/urun.html?slug=... sayfasını Supabase verisiyle doldurur.
   ========================================================= */
(function () {
  var currentProduct = null;

  function qs(name) {
    var params = new URLSearchParams(window.location.search);
    return params.get(name);
  }

  function specRow(spec) {
    var lang = MF.getLang();
    var k = lang === "en" ? spec.k_en : spec.k_tr;
    var v = lang === "en" ? spec.v_en : spec.v_tr;
    return "<tr><td>" + MF.escapeHtml(k) + "</td><td>" + MF.escapeHtml(v) + "</td></tr>";
  }

  function checkItem(text) {
    return (
      '<li><span class="tick">' + MF.icon("check") + "</span><span>" + MF.escapeHtml(text) + "</span></li>"
    );
  }

  function render() {
    var p = currentProduct;
    if (!p) return;
    var lang = MF.getLang();
    var title = MF.pick(p, "title");
    var summary = MF.pick(p, "summary");
    var body = MF.pick(p, "body") || summary;
    var tag = MF.pick(p, "tag");
    var catTitle = p.categories ? (lang === "en" ? p.categories.title_en : p.categories.title_tr) : "";
    var catSlug = p.categories ? p.categories.slug : null;

    document.title = title + " Teknik Özellikleri | MF Nautic Turkey";
    var metaDesc = document.querySelector('meta[name="description"]');
    if (metaDesc) metaDesc.setAttribute("content", summary);

    document.getElementById("pd-title").textContent = title;
    document.getElementById("pd-lead").textContent = summary;
    var badge = document.getElementById("pd-badge");
    if (tag) { badge.textContent = tag; badge.style.display = "inline-block"; }
    else { badge.style.display = "none"; }

    document.getElementById("pd-crumb-current").textContent = title;
    var crumb = document.getElementById("pd-breadcrumb");
    if (catSlug && catTitle) {
      var catLink = document.createElement("a");
      catLink.href = catSlug + ".html";
      catLink.textContent = catTitle;
      var sep = document.createElementNS("http://www.w3.org/2000/svg", "svg");
      sep.setAttribute("viewBox", "0 0 24 24");
      sep.setAttribute("fill", "none");
      sep.setAttribute("stroke", "currentColor");
      sep.setAttribute("stroke-width", "2");
      sep.innerHTML = '<polyline points="9 18 15 12 9 6"></polyline>';
      var current = document.getElementById("pd-crumb-current");
      crumb.insertBefore(sep, current);
      crumb.insertBefore(catLink, sep);
    }

    document.getElementById("pd-about-title").textContent = title;
    document.getElementById("pd-about-body").textContent = body;
    var mediaHtml = p.image_url
      ? '<img src="' + MF.escapeHtml(p.image_url) + '" alt="' + MF.escapeHtml(title) + '" loading="lazy">'
      : '<div class="cls">' + MF.icon(p.icon) + "</div>";
    document.getElementById("pd-media").innerHTML = mediaHtml;
    document.getElementById("pd-media-2").innerHTML = mediaHtml;

    var features = Array.isArray(p.features) ? p.features : [];
    document.getElementById("pd-features").innerHTML = features
      .map(function (f) { return checkItem(lang === "en" ? f.en : f.tr); })
      .join("");

    var specs = Array.isArray(p.specs) ? p.specs : [];
    var specSection = document.getElementById("pd-spec-section");
    if (specs.length) {
      document.getElementById("pd-spec-table").innerHTML = specs.map(specRow).join("");
      specSection.style.display = "";
    } else {
      specSection.style.display = "none";
    }

    var packaging = Array.isArray(p.packaging) ? p.packaging : [];
    var packSection = document.getElementById("pd-pack-section");
    if (packaging.length) {
      document.getElementById("pd-packaging").innerHTML = packaging
        .map(function (item) { return checkItem(lang === "en" ? item.en : item.tr); })
        .join("");
      packSection.style.display = "";
    } else {
      packSection.style.display = "none";
    }

    var videoSection = document.getElementById("pd-video-section");
    var embed = MF.youtubeEmbed(p.video_url);
    if (embed) {
      document.getElementById("pd-video-wrap").innerHTML =
        '<iframe src="' + embed + '" title="' + MF.escapeHtml(title) + '" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy"></iframe>';
      videoSection.style.display = "";
    } else {
      videoSection.style.display = "none";
    }

    document.getElementById("pd-cta-title").textContent =
      (lang === "en" ? "Get a quote for " : "") + title + (lang === "en" ? "" : " için teklif alın");
    var waText = (lang === "en" ? "Hello, I would like a price quote for " + title + "." : "Merhaba, " + title + " için fiyat teklifi almak istiyorum.");
    document.getElementById("pd-cta-wa").href = MF.waLink(waText);

    document.body.setAttribute("data-lang-ready", "1");
  }

  async function init() {
    var slug = qs("slug");
    if (!slug) { showNotFound(); return; }
    var p = await MF.getProductBySlug(slug);
    if (!p) { showNotFound(); return; }
    currentProduct = p;
    render();

    document.querySelectorAll(".lang-switch button").forEach(function (btn) {
      btn.addEventListener("click", function () { setTimeout(render, 0); });
    });
  }

  function showNotFound() {
    document.getElementById("pd-content").style.display = "none";
    document.getElementById("pd-notfound").style.display = "";
    document.getElementById("pd-title").textContent = "—";
    document.querySelector(".page-hero p").textContent = "";
  }

  document.addEventListener("DOMContentLoaded", init);
})();
