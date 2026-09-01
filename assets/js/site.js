/* =========================================================
   MF NAUTIC TURKEY — site.js
   Ortak navigasyon, mobil menü, TR/EN dil değiştirici, FAQ
   ========================================================= */
(function(){

  /* ---------------- Ortak (header/footer/nav) çeviri sözlüğü ---------------- */
  var COMMON_I18N = {
    tr: {
      "nav.home": "Anasayfa",
      "nav.products": "Ürünler",
      "nav.products.adhesives": "Yapıştırıcı ve Mastikler",
      "nav.products.lubricants": "Deniz Yağlayıcıları",
      "nav.products.filler": "Dolgu Macunları",
      "nav.products.tefgel": "Tikal Tef-Gel",
      "nav.products.teak": "Teak Deck Sistemleri",
      "nav.products.tools": "Aletler ve Aksesuarlar",
      "nav.docs": "Teknik Dökümanlar",
      "nav.references": "Referanslarımız",
      "nav.dealers": "Bayilerimiz",
      "nav.about": "Hakkımızda",
      "nav.contact": "İletişim",
      "topbar.phone": "+90 541 455 80 05",
      "topbar.email": "levent@mf-nautic.com",
      "topbar.tag": "Resmi Tikal Marine Systems Türkiye Distribütörü",
      "header.cta": "Teklif Al",
      "footer.about.title": "MF NAUTIC TURKEY",
      "footer.about.text": "MF Nautic Yatçılık Ltd. Şti., Almanya merkezli Tikal Marine Systems GmbH'nin Türkiye'deki resmi distribütörüdür. Yapıştırıcı, mastik, teak deck bakım ürünleri ve deniz yağlayıcılarında profesyonel çözümler sunuyoruz.",
      "footer.products": "Ürün Kategorileri",
      "footer.company": "Kurumsal",
      "footer.company.about": "Hakkımızda",
      "footer.company.docs": "Teknik Dökümanlar",
      "footer.company.references": "Referanslarımız",
      "footer.company.dealers": "Bayilik Başvurusu",
      "footer.company.dealersmap": "Bayilerimiz",
      "footer.company.contact": "İletişim",
      "footer.contact.title": "İletişim",
      "footer.rights": "Tüm hakları saklıdır.",
      "footer.legal.privacy": "Gizlilik Politikası",
      "footer.legal.terms": "Kullanım Koşulları",
      "footer.legal.kvkk": "KVKK Aydınlatma Metni",
      "footer.legal.cookies": "Çerez Politikası",
      "footer.madeby": "Tikal Marine Systems ürünleri için Türkiye yetkili distribütörü.",
      "breadcrumb.home": "Anasayfa"
    },
    en: {
      "nav.home": "Home",
      "nav.products": "Products",
      "nav.products.adhesives": "Adhesives & Sealants",
      "nav.products.lubricants": "Marine Lubricants",
      "nav.products.filler": "Fillers",
      "nav.products.tefgel": "Tikal Tef-Gel",
      "nav.products.teak": "Teak Deck Systems",
      "nav.products.tools": "Tools & Accessories",
      "nav.docs": "Technical Documents",
      "nav.references": "Our References",
      "nav.dealers": "Our Dealers",
      "nav.about": "About Us",
      "nav.contact": "Contact",
      "topbar.phone": "+90 541 455 80 05",
      "topbar.email": "levent@mf-nautic.com",
      "topbar.tag": "Official Tikal Marine Systems Distributor for Türkiye",
      "header.cta": "Get a Quote",
      "footer.about.title": "MF NAUTIC TURKEY",
      "footer.about.text": "MF Nautic Yatçılık Ltd. Şti. is the official Turkish distributor of Germany-based Tikal Marine Systems GmbH. We supply professional adhesives, sealants, teak deck maintenance products and marine lubricants.",
      "footer.products": "Product Categories",
      "footer.company": "Company",
      "footer.company.about": "About Us",
      "footer.company.docs": "Technical Documents",
      "footer.company.references": "Our References",
      "footer.company.dealers": "Become a Dealer",
      "footer.company.dealersmap": "Our Dealers",
      "footer.company.contact": "Contact",
      "footer.contact.title": "Contact",
      "footer.rights": "All rights reserved.",
      "footer.legal.privacy": "Privacy Policy",
      "footer.legal.terms": "Terms of Use",
      "footer.legal.kvkk": "Personal Data Notice (KVKK)",
      "footer.legal.cookies": "Cookie Policy",
      "footer.madeby": "Authorized Turkish distributor for Tikal Marine Systems products.",
      "breadcrumb.home": "Home"
    }
  };

  var LANG_KEY = "mf_lang";

  function getLang(){
    return localStorage.getItem(LANG_KEY) || "tr";
  }

  function mergeDict(lang){
    var pageDict = (window.PAGE_I18N && window.PAGE_I18N[lang]) ? window.PAGE_I18N[lang] : {};
    var out = {};
    var common = COMMON_I18N[lang] || {};
    for (var k in common) out[k] = common[k];
    for (var k2 in pageDict) out[k2] = pageDict[k2];
    return out;
  }

  function applyI18n(){
    var lang = getLang();
    var dict = mergeDict(lang);
    document.documentElement.setAttribute("lang", lang === "tr" ? "tr" : "en");

    document.querySelectorAll("[data-i18n]").forEach(function(el){
      var key = el.getAttribute("data-i18n");
      if (dict[key] !== undefined) el.textContent = dict[key];
    });
    document.querySelectorAll("[data-i18n-html]").forEach(function(el){
      var key = el.getAttribute("data-i18n-html");
      if (dict[key] !== undefined) el.innerHTML = dict[key];
    });
    document.querySelectorAll("[data-i18n-placeholder]").forEach(function(el){
      var key = el.getAttribute("data-i18n-placeholder");
      if (dict[key] !== undefined) el.setAttribute("placeholder", dict[key]);
    });
    document.querySelectorAll("[data-i18n-title]").forEach(function(el){
      var key = el.getAttribute("data-i18n-title");
      if (dict[key] !== undefined) el.setAttribute("title", dict[key]);
    });

    document.querySelectorAll(".lang-switch button").forEach(function(btn){
      btn.classList.toggle("active", btn.getAttribute("data-lang") === lang);
    });

    document.body.setAttribute("data-lang-ready", "1");
  }

  function setLang(lang){
    localStorage.setItem(LANG_KEY, lang);
    applyI18n();
  }

  /* ---------------- Mobil menü ---------------- */
  function initMobileNav(){
    var burger = document.querySelector(".burger");
    var nav = document.querySelector(".main-nav");
    if (!burger || !nav) return;
    burger.addEventListener("click", function(){
      nav.classList.toggle("open");
    });
    document.querySelectorAll(".main-nav li.has-dropdown > a.nav-link").forEach(function(link){
      link.addEventListener("click", function(e){
        if (window.innerWidth <= 760){
          e.preventDefault();
          link.parentElement.classList.toggle("open");
        }
      });
    });
  }

  /* ---------------- WhatsApp'a giden formlar ---------------- */
  function initWaForms(){
    document.querySelectorAll(".js-wa-form").forEach(function(form){
      form.addEventListener("submit", function(e){
        e.preventDefault();
        var intro = form.getAttribute("data-wa-intro") || "Merhaba,";
        var lines = [intro];
        form.querySelectorAll("[data-wa-field]").forEach(function(field){
          var label = field.getAttribute("data-wa-field");
          var val = (field.value || "").trim();
          if (val) lines.push(label + ": " + val);
        });
        var msg = lines.join("\n");
        var url = "https://wa.me/905414558005?text=" + encodeURIComponent(msg);
        window.open(url, "_blank", "noopener");
      });
    });
  }

  /* ---------------- FAQ accordion ---------------- */
  function initFaq(){
    document.querySelectorAll(".faq-q").forEach(function(q){
      q.addEventListener("click", function(){
        var item = q.closest(".faq-item");
        var wasOpen = item.classList.contains("open");
        item.parentElement.querySelectorAll(".faq-item").forEach(function(i){ i.classList.remove("open"); });
        if (!wasOpen) item.classList.add("open");
      });
    });
  }

  /* ---------------- Footer year ---------------- */
  function initYear(){
    document.querySelectorAll(".js-year").forEach(function(el){
      el.textContent = new Date().getFullYear();
    });
  }

  /* ---------------- Lang switch buttons ---------------- */
  function initLangSwitch(){
    document.querySelectorAll(".lang-switch button").forEach(function(btn){
      btn.addEventListener("click", function(){
        setLang(btn.getAttribute("data-lang"));
      });
    });
  }

  document.addEventListener("DOMContentLoaded", function(){
    initMobileNav();
    initFaq();
    initYear();
    initLangSwitch();
    initWaForms();
    applyI18n();
  });

})();
