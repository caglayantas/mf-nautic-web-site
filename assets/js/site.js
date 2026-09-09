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
      "nav.docs": "İndirilebilirler",
      "nav.catalogs": "Kataloglar",
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
      "footer.company.catalogs": "Kataloglar",
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
      "nav.docs": "Downloads",
      "nav.catalogs": "Catalogues",
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
      "footer.company.catalogs": "Catalogues",
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

  /* ---------------- E-postaya giden formlar (Resend API üzerinden, /api/contact) ---------------- */
  function setFormStatus(el, msg, state){
    if (!el) return;
    el.textContent = msg || "";
    el.style.display = msg ? "" : "none";
    el.classList.remove("is-error", "is-success");
    if (state) el.classList.add(state);
  }

  /* ---------------- Telefon alanı: ülke kodu + 5xx xxx xx xx maskesi ---------------- */
  function formatPhoneNumber(raw){
    var digits = (raw || "").replace(/\D/g, "").slice(0, 10);
    var parts = [];
    if (digits.length > 0) parts.push(digits.slice(0, 3));
    if (digits.length > 3) parts.push(digits.slice(3, 6));
    if (digits.length > 6) parts.push(digits.slice(6, 8));
    if (digits.length > 8) parts.push(digits.slice(8, 10));
    return parts.join(" ");
  }

  function initPhoneFields(){
    document.querySelectorAll(".js-phone-number").forEach(function(numInput){
      var wrap = numInput.closest(".form-field");
      if (!wrap) return;
      var codeSelect = wrap.querySelector(".js-phone-code");
      var hidden = wrap.querySelector('[data-field="phone"]');
      if (!codeSelect || !hidden) return;

      function sync(){
        var digits = numInput.value.replace(/\D/g, "");
        hidden.value = digits ? ("+" + codeSelect.value + " " + numInput.value.trim()) : "";
      }

      numInput.addEventListener("input", function(){
        numInput.value = formatPhoneNumber(numInput.value);
        sync();
      });
      codeSelect.addEventListener("change", sync);
      numInput.closest("form").addEventListener("reset", function(){
        setTimeout(sync, 0);
      });
      sync();
    });
  }

  /* ---------------- Ülke kodu seçici: gerçek bayrak ikonları (flagcdn.com) ----------------
     Emoji bayraklar Windows'ta çoğu tarayıcıda görüntülenmediği için (harf kutucuğuna
     dönüşüyor), native <select>'i JS ile gerçek <img> bayraklı özel bir açılır listeyle
     zenginleştiriyoruz. JS çalışmazsa native select olduğu gibi kalır ve çalışmaya devam eder. */
  function flagUrl(iso){
    return "https://flagcdn.com/w40/" + iso + ".png";
  }

  function initPhoneCodePicker(){
    document.querySelectorAll(".phone-code-picker").forEach(function(picker){
      var select = picker.querySelector(".js-phone-code");
      if (!select || !select.options.length) return;
      var options = Array.prototype.slice.call(select.options);

      function optionName(opt){ return opt.getAttribute("data-name") || opt.textContent; }
      function optionIso(opt){ return opt.getAttribute("data-iso") || ""; }

      function makeFlagImg(opt){
        var img = document.createElement("img");
        img.className = "flag-ic";
        img.alt = "";
        img.loading = "lazy";
        var iso = optionIso(opt);
        if (iso) img.src = flagUrl(iso);
        img.addEventListener("error", function(){ img.style.visibility = "hidden"; });
        return img;
      }

      var trigger = document.createElement("button");
      trigger.type = "button";
      trigger.className = "phone-code-trigger";
      trigger.setAttribute("aria-haspopup", "listbox");
      trigger.setAttribute("aria-expanded", "false");
      var triggerFlag = document.createElement("img");
      triggerFlag.className = "flag-ic";
      triggerFlag.alt = "";
      triggerFlag.addEventListener("error", function(){ triggerFlag.style.visibility = "hidden"; });
      var triggerVal = document.createElement("span");
      triggerVal.className = "phone-code-val";
      var chev = document.createElementNS("http://www.w3.org/2000/svg", "svg");
      chev.setAttribute("class", "chev");
      chev.setAttribute("viewBox", "0 0 24 24");
      chev.setAttribute("fill", "none");
      chev.setAttribute("stroke", "currentColor");
      chev.setAttribute("stroke-width", "2");
      chev.innerHTML = '<polyline points="6 9 12 15 18 9"></polyline>';
      trigger.appendChild(triggerFlag);
      trigger.appendChild(triggerVal);
      trigger.appendChild(chev);

      var menu = document.createElement("ul");
      menu.className = "phone-code-menu";
      menu.setAttribute("role", "listbox");

      function updateTrigger(){
        var opt = select.options[select.selectedIndex];
        if (!opt) return;
        var iso = optionIso(opt);
        triggerFlag.style.visibility = "";
        if (iso) triggerFlag.src = flagUrl(iso);
        triggerFlag.alt = optionName(opt);
        triggerVal.textContent = "+" + opt.value;
      }

      options.forEach(function(opt, i){
        var li = document.createElement("li");
        li.className = "phone-code-option";
        li.setAttribute("role", "option");
        li.appendChild(makeFlagImg(opt));
        var nameSpan = document.createElement("span");
        nameSpan.className = "opt-name";
        nameSpan.textContent = optionName(opt);
        var codeSpan = document.createElement("span");
        codeSpan.className = "opt-code";
        codeSpan.textContent = "+" + opt.value;
        li.appendChild(nameSpan);
        li.appendChild(codeSpan);
        li.addEventListener("click", function(){
          select.selectedIndex = i;
          updateTrigger();
          closeMenu();
          select.dispatchEvent(new Event("change", { bubbles: true }));
        });
        menu.appendChild(li);
      });

      function onDocClick(e){ if (!picker.contains(e.target)) closeMenu(); }
      function onKeydown(e){ if (e.key === "Escape") { closeMenu(); trigger.focus(); } }
      function openMenu(){
        picker.classList.add("is-open");
        trigger.setAttribute("aria-expanded", "true");
        document.addEventListener("click", onDocClick, true);
        document.addEventListener("keydown", onKeydown, true);
      }
      function closeMenu(){
        picker.classList.remove("is-open");
        trigger.setAttribute("aria-expanded", "false");
        document.removeEventListener("click", onDocClick, true);
        document.removeEventListener("keydown", onKeydown, true);
      }
      trigger.addEventListener("click", function(){
        if (picker.classList.contains("is-open")) closeMenu(); else openMenu();
      });

      picker.appendChild(trigger);
      picker.appendChild(menu);
      picker.classList.add("js-enhanced");
      updateTrigger();
    });
  }

  function initEmailForms(){
    document.querySelectorAll(".js-email-form").forEach(function(form){
      var btn = form.querySelector("button[type=submit]");
      var btnLabel = btn ? btn.querySelector("span") : null;
      var statusEl = form.querySelector(".form-status");
      var defaultBtnText = btnLabel ? btnLabel.textContent : "";

      form.addEventListener("submit", function(e){
        e.preventDefault();
        var lang = getLang();
        var payload = { formType: form.getAttribute("data-form-type") || "contact" };
        var missing = false;
        form.querySelectorAll("[data-field]").forEach(function(field){
          var key = field.getAttribute("data-field");
          var val = (field.value || "").trim();
          payload[key] = val;
          if (field.hasAttribute("required") && !val) missing = true;
        });
        if (missing) {
          setFormStatus(statusEl, lang === "en" ? "Please fill in the required fields." : "Lütfen zorunlu alanları doldurun.", "is-error");
          return;
        }

        if (btn) { btn.disabled = true; }
        if (btnLabel) { btnLabel.textContent = lang === "en" ? "Sending..." : "Gönderiliyor..."; }
        setFormStatus(statusEl, "", null);

        fetch("/api/contact", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(payload)
        }).then(function(r){
          return r.json().catch(function(){ return {}; }).then(function(data){ return { ok: r.ok, data: data }; });
        }).then(function(res){
          if (btn) { btn.disabled = false; }
          if (btnLabel) { btnLabel.textContent = defaultBtnText; }
          if (res.ok) {
            form.reset();
            setFormStatus(statusEl, lang === "en" ? "Your message has been sent — we'll get back to you soon." : "Mesajınız gönderildi — en kısa sürede size dönüş yapacağız.", "is-success");
          } else {
            setFormStatus(statusEl, lang === "en" ? "Something went wrong. You can also reach us on WhatsApp." : "Bir sorun oluştu. WhatsApp üzerinden de bize ulaşabilirsiniz.", "is-error");
          }
        }).catch(function(){
          if (btn) { btn.disabled = false; }
          if (btnLabel) { btnLabel.textContent = defaultBtnText; }
          setFormStatus(statusEl, lang === "en" ? "Connection error. You can also reach us on WhatsApp." : "Bağlantı hatası. WhatsApp üzerinden de bize ulaşabilirsiniz.", "is-error");
        });
      });
    });
  }

  /* ---------------- İletişim formu: URL üzerinden konu/mesaj ön doldurma ---------------- */
  function initContactPrefill(){
    var subjectSelect = document.getElementById("ct-subject");
    var messageField = document.getElementById("ct-message");
    if (!subjectSelect && !messageField) return;
    var params;
    try { params = new URLSearchParams(window.location.search); } catch (e) { return; }
    var subjectMap = { urun: 0, dokuman: 1, bayilik: 2, diger: 3 };
    var subjectKey = params.get("subject");
    if (subjectSelect && subjectKey && Object.prototype.hasOwnProperty.call(subjectMap, subjectKey)) {
      subjectSelect.selectedIndex = subjectMap[subjectKey];
    }
    var msg = params.get("msg");
    if (messageField && msg) {
      messageField.value = msg;
    }
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

  /* ---------------- SEO: BreadcrumbList JSON-LD ---------------- */
  function initBreadcrumbSchema(){
    var crumb = document.querySelector(".breadcrumb");
    if (!crumb) return;
    var items = [];
    var position = 1;
    crumb.querySelectorAll("a[href]").forEach(function(a){
      items.push({
        "@type": "ListItem",
        "position": position++,
        "name": a.textContent.trim(),
        "item": a.href
      });
    });
    var current = crumb.querySelector(".current");
    if (current && current.textContent.trim()) {
      items.push({
        "@type": "ListItem",
        "position": position++,
        "name": current.textContent.trim(),
        "item": window.location.origin + window.location.pathname
      });
    }
    if (items.length < 2) return;
    var existing = document.getElementById("breadcrumb-jsonld");
    if (!existing) {
      existing = document.createElement("script");
      existing.type = "application/ld+json";
      existing.id = "breadcrumb-jsonld";
      document.head.appendChild(existing);
    }
    existing.textContent = JSON.stringify({
      "@context": "https://schema.org",
      "@type": "BreadcrumbList",
      "itemListElement": items
    });
  }
  /* Exposed so pages that build their breadcrumb dynamically (e.g. the
     Supabase-driven product detail page) can refresh the schema after
     their own render finishes, since it runs after this file's
     DOMContentLoaded handler already fired once with placeholder data. */
  window.MFRefreshBreadcrumbSchema = initBreadcrumbSchema;

  document.addEventListener("DOMContentLoaded", function(){
    initMobileNav();
    initFaq();
    initYear();
    initLangSwitch();
    initWaForms();
    initPhoneFields();
    initPhoneCodePicker();
    initEmailForms();
    initContactPrefill();
    applyI18n();
    initBreadcrumbSchema();
  });

})();
