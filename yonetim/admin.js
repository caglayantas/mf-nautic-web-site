/* =========================================================
   MF NAUTIC TURKEY — admin.js
   Yönetim paneli: giriş, ürün/döküman/kategori CRUD.
   ========================================================= */
(function () {
  var categoriesCache = [];

  function flash(msg, ok) {
    var el = document.getElementById("admin-flash");
    el.innerHTML = '<div class="' + (ok ? "admin-ok" : "admin-error") + '">' + msg + "</div>";
    setTimeout(function () { el.innerHTML = ""; }, 3500);
  }

  function esc(s) { return MF.escapeHtml(s); }

  /* ---------------- AUTH ---------------- */
  async function boot() {
    var session = await MF.getSession();
    if (session) {
      showDashboard();
    } else {
      document.getElementById("admin-login-screen").style.display = "";
    }
  }

  document.getElementById("login-form").addEventListener("submit", async function (e) {
    e.preventDefault();
    var email = document.getElementById("login-email").value.trim();
    var pass = document.getElementById("login-password").value;
    var errEl = document.getElementById("login-error");
    errEl.style.display = "none";
    var res = await MF.signIn(email, pass);
    if (res.error) {
      errEl.textContent = "Giriş başarısız: E-posta veya şifre hatalı.";
      errEl.style.display = "";
      return;
    }
    document.getElementById("admin-login-screen").style.display = "none";
    showDashboard();
  });

  document.getElementById("logout-btn").addEventListener("click", async function () {
    await MF.signOut();
    location.reload();
  });

  async function showDashboard() {
    document.getElementById("admin-dashboard").style.display = "";
    categoriesCache = await MF.adminListCategories();
    fillCategorySelects();
    loadProducts();
    loadDocuments();
    loadCategories();
    loadReferences();
    loadDealers();
  }

  function fillCategorySelects() {
    var opts = categoriesCache.map(function (c) {
      return '<option value="' + c.id + '">' + esc(c.title_tr) + "</option>";
    }).join("");
    document.getElementById("pf-category").innerHTML = opts;
    document.getElementById("df-category").innerHTML = opts;
  }

  /* ---------------- TABS ---------------- */
  document.querySelectorAll(".tab-btn").forEach(function (btn) {
    btn.addEventListener("click", function () {
      document.querySelectorAll(".tab-btn").forEach(function (b) { b.classList.remove("active"); });
      btn.classList.add("active");
      var tab = btn.getAttribute("data-tab");
      document.querySelectorAll(".tab-panel").forEach(function (p) { p.style.display = "none"; });
      document.getElementById("tab-" + tab).style.display = "";
    });
  });

  /* ==================================================================
     PRODUCTS
     ================================================================== */
  async function loadProducts() {
    var tbody = document.getElementById("products-tbody");
    tbody.innerHTML = '<tr><td colspan="7">Yükleniyor...</td></tr>';
    var rows = await MF.adminListProducts();
    if (!rows.length) { tbody.innerHTML = '<tr><td colspan="7">Henüz ürün yok.</td></tr>'; return; }
    tbody.innerHTML = rows.map(function (p) {
      var catTitle = p.categories ? esc(p.categories.title_tr) : "—";
      return (
        "<tr>" +
        "<td><b>" + esc(p.title_tr) + "</b><br><span style='color:var(--slate-2);font-size:11.5px'>" + esc(p.slug) + "</span></td>" +
        "<td>" + catTitle + "</td>" +
        "<td>" + (p.tag_tr ? esc(p.tag_tr) : "—") + "</td>" +
        "<td>" + (p.featured ? '<span class="admin-badge on">Evet</span>' : '<span class="admin-badge off">Hayır</span>') + "</td>" +
        "<td>" + (p.published ? '<span class="admin-badge on">Yayında</span>' : '<span class="admin-badge off">Taslak</span>') + "</td>" +
        "<td>" + p.sort_order + "</td>" +
        '<td class="admin-actions"><button type="button" data-id="' + p.id + '" class="edit-product">Düzenle</button><button type="button" data-id="' + p.id + '" class="danger delete-product">Sil</button></td>' +
        "</tr>"
      );
    }).join("");

    tbody.querySelectorAll(".edit-product").forEach(function (b) {
      b.addEventListener("click", function () { openProductModal(rows.find(function (r) { return r.id === b.getAttribute("data-id"); })); });
    });
    tbody.querySelectorAll(".delete-product").forEach(function (b) {
      b.addEventListener("click", async function () {
        if (!confirm("Bu ürünü silmek istediğinizden emin misiniz?")) return;
        var res = await MF.adminDeleteProduct(b.getAttribute("data-id"));
        if (res.error) { flash("Silme başarısız: " + res.error.message, false); return; }
        flash("Ürün silindi.", true);
        loadProducts();
      });
    });
  }

  function listEditorRow(containerId, values, placeholders) {
    // values: array of strings matching placeholders length; returns row html string
    var inputs = placeholders.map(function (ph, i) {
      return '<input type="text" placeholder="' + ph + '" value="' + esc(values ? values[i] || "" : "") + '">';
    }).join("");
    return '<div class="row">' + inputs + '<button type="button" class="remove-row">✕</button></div>';
  }

  function wireListEditor(editorId) {
    document.getElementById(editorId).addEventListener("click", function (e) {
      if (e.target.classList.contains("remove-row")) {
        e.target.closest(".row").remove();
      }
    });
  }
  wireListEditor("pf-specs-editor");
  wireListEditor("pf-pack-editor");
  wireListEditor("pf-feat-editor");

  function addSpecRow(vals) {
    document.getElementById("pf-specs-editor").insertAdjacentHTML(
      "beforeend", listEditorRow("pf-specs-editor", vals, ["Özellik (TR)", "Değer (TR)", "Özellik (EN)", "Değer (EN)"])
    );
  }
  function addPackRow(vals) {
    document.getElementById("pf-pack-editor").insertAdjacentHTML(
      "beforeend", listEditorRow("pf-pack-editor", vals, ["Ambalaj (TR)", "Ambalaj (EN)"])
    );
  }
  function addFeatRow(vals) {
    document.getElementById("pf-feat-editor").insertAdjacentHTML(
      "beforeend", listEditorRow("pf-feat-editor", vals, ["Özellik (TR)", "Özellik (EN)"])
    );
  }
  document.getElementById("pf-specs-add").addEventListener("click", function () { addSpecRow(); });
  document.getElementById("pf-pack-add").addEventListener("click", function () { addPackRow(); });
  document.getElementById("pf-feat-add").addEventListener("click", function () { addFeatRow(); });

  function readListEditor(editorId, n) {
    var out = [];
    document.querySelectorAll("#" + editorId + " .row").forEach(function (row) {
      var inputs = row.querySelectorAll("input");
      var vals = [];
      for (var i = 0; i < n; i++) vals.push(inputs[i] ? inputs[i].value.trim() : "");
      if (vals.some(function (v) { return v; })) out.push(vals);
    });
    return out;
  }

  function openProductModal(product) {
    document.getElementById("product-modal-error").style.display = "none";
    document.getElementById("product-modal-title").textContent = product ? "Ürün Düzenle" : "Yeni Ürün";
    document.getElementById("pf-id").value = product ? product.id : "";
    document.getElementById("pf-category").value = product ? (product.category_id || "") : (categoriesCache[0] ? categoriesCache[0].id : "");
    document.getElementById("pf-slug").value = product ? product.slug : "";
    document.getElementById("pf-title-tr").value = product ? product.title_tr : "";
    document.getElementById("pf-title-en").value = product ? product.title_en : "";
    document.getElementById("pf-summary-tr").value = product ? (product.summary_tr || "") : "";
    document.getElementById("pf-summary-en").value = product ? (product.summary_en || "") : "";
    document.getElementById("pf-body-tr").value = product ? (product.body_tr || "") : "";
    document.getElementById("pf-body-en").value = product ? (product.body_en || "") : "";
    document.getElementById("pf-tag-tr").value = product ? (product.tag_tr || "") : "";
    document.getElementById("pf-tag-en").value = product ? (product.tag_en || "") : "";
    document.getElementById("pf-icon").value = product ? (product.icon || "package") : "package";
    document.getElementById("pf-video").value = product ? (product.video_url || "") : "";
    document.getElementById("pf-image").value = product ? (product.image_url || "") : "";
    document.getElementById("pf-sort").value = product ? product.sort_order : 0;
    document.getElementById("pf-featured").checked = product ? !!product.featured : false;
    document.getElementById("pf-published").checked = product ? !!product.published : true;

    document.getElementById("pf-specs-editor").innerHTML = "";
    document.getElementById("pf-pack-editor").innerHTML = "";
    document.getElementById("pf-feat-editor").innerHTML = "";
    var specs = (product && Array.isArray(product.specs)) ? product.specs : [];
    var pack = (product && Array.isArray(product.packaging)) ? product.packaging : [];
    var feats = (product && Array.isArray(product.features)) ? product.features : [];
    if (specs.length) specs.forEach(function (s) { addSpecRow([s.k_tr, s.v_tr, s.k_en, s.v_en]); });
    else addSpecRow();
    if (pack.length) pack.forEach(function (p) { addPackRow([p.tr, p.en]); });
    else addPackRow();
    if (feats.length) feats.forEach(function (f) { addFeatRow([f.tr, f.en]); });
    else addFeatRow();

    document.getElementById("product-modal").style.display = "flex";
  }

  document.getElementById("btn-new-product").addEventListener("click", function () { openProductModal(null); });
  document.getElementById("pf-cancel").addEventListener("click", function () { document.getElementById("product-modal").style.display = "none"; });

  document.getElementById("product-form").addEventListener("submit", async function (e) {
    e.preventDefault();
    var errEl = document.getElementById("product-modal-error");
    errEl.style.display = "none";

    var specsRows = readListEditor("pf-specs-editor", 4).map(function (v) {
      return { k_tr: v[0], v_tr: v[1], k_en: v[2] || v[0], v_en: v[3] || v[1] };
    });
    var packRows = readListEditor("pf-pack-editor", 2).map(function (v) {
      return { tr: v[0], en: v[1] || v[0] };
    });
    var featRows = readListEditor("pf-feat-editor", 2).map(function (v) {
      return { tr: v[0], en: v[1] || v[0] };
    });

    var row = {
      category_id: document.getElementById("pf-category").value,
      slug: document.getElementById("pf-slug").value.trim(),
      title_tr: document.getElementById("pf-title-tr").value.trim(),
      title_en: document.getElementById("pf-title-en").value.trim(),
      summary_tr: document.getElementById("pf-summary-tr").value.trim(),
      summary_en: document.getElementById("pf-summary-en").value.trim(),
      body_tr: document.getElementById("pf-body-tr").value.trim(),
      body_en: document.getElementById("pf-body-en").value.trim(),
      tag_tr: document.getElementById("pf-tag-tr").value.trim() || null,
      tag_en: document.getElementById("pf-tag-en").value.trim() || null,
      icon: document.getElementById("pf-icon").value,
      video_url: document.getElementById("pf-video").value.trim() || null,
      image_url: document.getElementById("pf-image").value.trim() || null,
      sort_order: parseInt(document.getElementById("pf-sort").value, 10) || 0,
      featured: document.getElementById("pf-featured").checked,
      published: document.getElementById("pf-published").checked,
      specs: specsRows,
      packaging: packRows,
      features: featRows
    };
    var id = document.getElementById("pf-id").value;
    if (id) row.id = id;

    var res = await MF.adminUpsertProduct(row);
    if (res.error) { errEl.textContent = "Kaydetme başarısız: " + res.error.message; errEl.style.display = ""; return; }
    document.getElementById("product-modal").style.display = "none";
    flash("Ürün kaydedildi.", true);
    loadProducts();
  });

  /* ==================================================================
     DOCUMENTS
     ================================================================== */
  async function loadDocuments() {
    var tbody = document.getElementById("documents-tbody");
    tbody.innerHTML = '<tr><td colspan="5">Yükleniyor...</td></tr>';
    var rows = await MF.adminListDocuments();
    if (!rows.length) { tbody.innerHTML = '<tr><td colspan="5">Henüz döküman yok.</td></tr>'; return; }
    tbody.innerHTML = rows.map(function (d) {
      var catTitle = d.categories ? esc(d.categories.title_tr) : "—";
      return (
        "<tr>" +
        "<td>" + esc(d.title_tr) + "</td>" +
        "<td>" + catTitle + "</td>" +
        "<td>" + (d.file_url ? '<a href="' + esc(d.file_url) + '" target="_blank" rel="noopener">Link</a>' : '<span style="color:var(--slate-2)">WhatsApp</span>') + "</td>" +
        "<td>" + d.sort_order + "</td>" +
        '<td class="admin-actions"><button type="button" data-id="' + d.id + '" class="edit-document">Düzenle</button><button type="button" data-id="' + d.id + '" class="danger delete-document">Sil</button></td>' +
        "</tr>"
      );
    }).join("");

    tbody.querySelectorAll(".edit-document").forEach(function (b) {
      b.addEventListener("click", function () { openDocumentModal(rows.find(function (r) { return r.id === b.getAttribute("data-id"); })); });
    });
    tbody.querySelectorAll(".delete-document").forEach(function (b) {
      b.addEventListener("click", async function () {
        if (!confirm("Bu dökümanı silmek istediğinizden emin misiniz?")) return;
        var res = await MF.adminDeleteDocument(b.getAttribute("data-id"));
        if (res.error) { flash("Silme başarısız: " + res.error.message, false); return; }
        flash("Döküman silindi.", true);
        loadDocuments();
      });
    });
  }

  function openDocumentModal(doc) {
    document.getElementById("document-modal-error").style.display = "none";
    document.getElementById("document-modal-title").textContent = doc ? "Döküman Düzenle" : "Yeni Döküman";
    document.getElementById("df-id").value = doc ? doc.id : "";
    document.getElementById("df-category").value = doc ? (doc.category_id || "") : (categoriesCache[0] ? categoriesCache[0].id : "");
    document.getElementById("df-title-tr").value = doc ? doc.title_tr : "";
    document.getElementById("df-title-en").value = doc ? doc.title_en : "";
    document.getElementById("df-note-tr").value = doc ? (doc.note_tr || "") : "Teknik Veri Formu (TDS) & Güvenlik Bilgi Formu (SDS)";
    document.getElementById("df-note-en").value = doc ? (doc.note_en || "") : "Technical Data Sheet (TDS) & Safety Data Sheet (SDS)";
    document.getElementById("df-file").value = doc ? (doc.file_url || "") : "";
    document.getElementById("df-sort").value = doc ? doc.sort_order : 0;
    document.getElementById("document-modal").style.display = "flex";
  }

  document.getElementById("btn-new-document").addEventListener("click", function () { openDocumentModal(null); });
  document.getElementById("df-cancel").addEventListener("click", function () { document.getElementById("document-modal").style.display = "none"; });

  document.getElementById("document-form").addEventListener("submit", async function (e) {
    e.preventDefault();
    var errEl = document.getElementById("document-modal-error");
    errEl.style.display = "none";
    var row = {
      category_id: document.getElementById("df-category").value,
      title_tr: document.getElementById("df-title-tr").value.trim(),
      title_en: document.getElementById("df-title-en").value.trim(),
      note_tr: document.getElementById("df-note-tr").value.trim(),
      note_en: document.getElementById("df-note-en").value.trim(),
      file_url: document.getElementById("df-file").value.trim() || null,
      sort_order: parseInt(document.getElementById("df-sort").value, 10) || 0
    };
    var id = document.getElementById("df-id").value;
    if (id) row.id = id;
    var res = await MF.adminUpsertDocument(row);
    if (res.error) { errEl.textContent = "Kaydetme başarısız: " + res.error.message; errEl.style.display = ""; return; }
    document.getElementById("document-modal").style.display = "none";
    flash("Döküman kaydedildi.", true);
    loadDocuments();
  });

  /* ==================================================================
     CATEGORIES
     ================================================================== */
  async function loadCategories() {
    var tbody = document.getElementById("categories-tbody");
    var rows = await MF.adminListCategories();
    categoriesCache = rows;
    fillCategorySelects();
    tbody.innerHTML = rows.map(function (c) {
      return (
        "<tr>" +
        "<td>" + esc(c.title_tr) + "</td>" +
        "<td>" + esc(c.title_en) + "</td>" +
        "<td>" + esc(c.icon) + "</td>" +
        "<td>" + c.sort_order + "</td>" +
        '<td class="admin-actions"><button type="button" data-id="' + c.id + '" class="edit-category">Düzenle</button></td>' +
        "</tr>"
      );
    }).join("");
    tbody.querySelectorAll(".edit-category").forEach(function (b) {
      b.addEventListener("click", function () { openCategoryModal(rows.find(function (r) { return r.id === b.getAttribute("data-id"); })); });
    });
  }

  function openCategoryModal(cat) {
    document.getElementById("category-modal-error").style.display = "none";
    document.getElementById("cf-id").value = cat.id;
    document.getElementById("cf-title-tr").value = cat.title_tr;
    document.getElementById("cf-title-en").value = cat.title_en;
    document.getElementById("cf-desc-tr").value = cat.desc_tr || "";
    document.getElementById("cf-desc-en").value = cat.desc_en || "";
    document.getElementById("category-modal").style.display = "flex";
  }
  document.getElementById("cf-cancel").addEventListener("click", function () { document.getElementById("category-modal").style.display = "none"; });

  document.getElementById("category-form").addEventListener("submit", async function (e) {
    e.preventDefault();
    var errEl = document.getElementById("category-modal-error");
    errEl.style.display = "none";
    var row = {
      id: document.getElementById("cf-id").value,
      title_tr: document.getElementById("cf-title-tr").value.trim(),
      title_en: document.getElementById("cf-title-en").value.trim(),
      desc_tr: document.getElementById("cf-desc-tr").value.trim(),
      desc_en: document.getElementById("cf-desc-en").value.trim()
    };
    var res = await MF.adminUpsertCategory(row);
    if (res.error) { errEl.textContent = "Kaydetme başarısız: " + res.error.message; errEl.style.display = ""; return; }
    document.getElementById("category-modal").style.display = "none";
    flash("Kategori kaydedildi.", true);
    loadCategories();
  });

  /* ==================================================================
     REFERENCES (Referanslarımız)
     ================================================================== */
  async function loadReferences() {
    var tbody = document.getElementById("references-tbody");
    tbody.innerHTML = '<tr><td colspan="6">Yükleniyor...</td></tr>';
    var rows = await MF.adminListReferences();
    if (!rows.length) { tbody.innerHTML = '<tr><td colspan="6">Henüz referans yok.</td></tr>'; return; }
    tbody.innerHTML = rows.map(function (r) {
      return (
        "<tr>" +
        "<td><b>" + esc(r.title_tr) + "</b></td>" +
        "<td>" + (r.type === "company" ? "Firma" : "Proje") + "</td>" +
        "<td>" + (r.website_url ? '<a href="' + esc(r.website_url) + '" target="_blank" rel="noopener">Link</a>' : "—") + "</td>" +
        "<td>" + (r.published ? '<span class="admin-badge on">Yayında</span>' : '<span class="admin-badge off">Taslak</span>') + "</td>" +
        "<td>" + r.sort_order + "</td>" +
        '<td class="admin-actions"><button type="button" data-id="' + r.id + '" class="edit-reference">Düzenle</button><button type="button" data-id="' + r.id + '" class="danger delete-reference">Sil</button></td>' +
        "</tr>"
      );
    }).join("");

    tbody.querySelectorAll(".edit-reference").forEach(function (b) {
      b.addEventListener("click", function () { openReferenceModal(rows.find(function (r) { return r.id === b.getAttribute("data-id"); })); });
    });
    tbody.querySelectorAll(".delete-reference").forEach(function (b) {
      b.addEventListener("click", async function () {
        if (!confirm("Bu referansı silmek istediğinizden emin misiniz?")) return;
        var res = await MF.adminDeleteReference(b.getAttribute("data-id"));
        if (res.error) { flash("Silme başarısız: " + res.error.message, false); return; }
        flash("Referans silindi.", true);
        loadReferences();
      });
    });
  }

  function openReferenceModal(ref) {
    document.getElementById("reference-modal-error").style.display = "none";
    document.getElementById("reference-modal-title").textContent = ref ? "Referans Düzenle" : "Yeni Referans";
    document.getElementById("rf-id").value = ref ? ref.id : "";
    document.getElementById("rf-type").value = ref && ref.type === "company" ? "company" : "project";
    document.getElementById("rf-title-tr").value = ref ? ref.title_tr : "";
    document.getElementById("rf-title-en").value = ref ? ref.title_en : "";
    document.getElementById("rf-desc-tr").value = ref ? (ref.desc_tr || "") : "";
    document.getElementById("rf-desc-en").value = ref ? (ref.desc_en || "") : "";
    document.getElementById("rf-logo").value = ref ? (ref.logo_url || "") : "";
    document.getElementById("rf-website").value = ref ? (ref.website_url || "") : "";
    document.getElementById("rf-sort").value = ref ? ref.sort_order : 0;
    document.getElementById("rf-published").checked = ref ? !!ref.published : true;
    document.getElementById("reference-modal").style.display = "flex";
  }

  document.getElementById("btn-new-reference").addEventListener("click", function () { openReferenceModal(null); });
  document.getElementById("rf-cancel").addEventListener("click", function () { document.getElementById("reference-modal").style.display = "none"; });

  document.getElementById("reference-form").addEventListener("submit", async function (e) {
    e.preventDefault();
    var errEl = document.getElementById("reference-modal-error");
    errEl.style.display = "none";
    var row = {
      type: document.getElementById("rf-type").value === "company" ? "company" : "project",
      title_tr: document.getElementById("rf-title-tr").value.trim(),
      title_en: document.getElementById("rf-title-en").value.trim(),
      desc_tr: document.getElementById("rf-desc-tr").value.trim(),
      desc_en: document.getElementById("rf-desc-en").value.trim(),
      logo_url: document.getElementById("rf-logo").value.trim() || null,
      website_url: document.getElementById("rf-website").value.trim() || null,
      sort_order: parseInt(document.getElementById("rf-sort").value, 10) || 0,
      published: document.getElementById("rf-published").checked
    };
    var id = document.getElementById("rf-id").value;
    if (id) row.id = id;
    var res = await MF.adminUpsertReference(row);
    if (res.error) { errEl.textContent = "Kaydetme başarısız: " + res.error.message; errEl.style.display = ""; return; }
    document.getElementById("reference-modal").style.display = "none";
    flash("Referans kaydedildi.", true);
    loadReferences();
  });

  /* ==================================================================
     DEALERS (Bayilerimiz)
     ================================================================== */
  async function loadDealers() {
    var tbody = document.getElementById("dealers-tbody");
    tbody.innerHTML = '<tr><td colspan="6">Yükleniyor...</td></tr>';
    var rows = await MF.adminListDealers();
    if (!rows.length) { tbody.innerHTML = '<tr><td colspan="6">Henüz bayi yok.</td></tr>'; return; }
    tbody.innerHTML = rows.map(function (d) {
      return (
        "<tr>" +
        "<td><b>" + esc(d.title_tr) + "</b></td>" +
        "<td>" + (d.badge_tr ? esc(d.badge_tr) : "—") + "</td>" +
        "<td>" + (d.phone ? esc(d.phone) : "—") + "</td>" +
        "<td>" + (d.published ? '<span class="admin-badge on">Yayında</span>' : '<span class="admin-badge off">Taslak</span>') + "</td>" +
        "<td>" + d.sort_order + "</td>" +
        '<td class="admin-actions"><button type="button" data-id="' + d.id + '" class="edit-dealer">Düzenle</button><button type="button" data-id="' + d.id + '" class="danger delete-dealer">Sil</button></td>' +
        "</tr>"
      );
    }).join("");

    tbody.querySelectorAll(".edit-dealer").forEach(function (b) {
      b.addEventListener("click", function () { openDealerModal(rows.find(function (r) { return r.id === b.getAttribute("data-id"); })); });
    });
    tbody.querySelectorAll(".delete-dealer").forEach(function (b) {
      b.addEventListener("click", async function () {
        if (!confirm("Bu bayiyi silmek istediğinizden emin misiniz?")) return;
        var res = await MF.adminDeleteDealer(b.getAttribute("data-id"));
        if (res.error) { flash("Silme başarısız: " + res.error.message, false); return; }
        flash("Bayi silindi.", true);
        loadDealers();
      });
    });
  }

  function openDealerModal(dealer) {
    document.getElementById("dealer-modal-error").style.display = "none";
    document.getElementById("dealer-modal-title").textContent = dealer ? "Bayi Düzenle" : "Yeni Bayi";
    document.getElementById("df2-id").value = dealer ? dealer.id : "";
    document.getElementById("df2-title-tr").value = dealer ? dealer.title_tr : "";
    document.getElementById("df2-title-en").value = dealer ? dealer.title_en : "";
    document.getElementById("df2-badge-tr").value = dealer ? (dealer.badge_tr || "") : "";
    document.getElementById("df2-badge-en").value = dealer ? (dealer.badge_en || "") : "";
    document.getElementById("df2-address-tr").value = dealer ? (dealer.address_tr || "") : "";
    document.getElementById("df2-address-en").value = dealer ? (dealer.address_en || "") : "";
    document.getElementById("df2-phone").value = dealer ? (dealer.phone || "") : "";
    document.getElementById("df2-email").value = dealer ? (dealer.email || "") : "";
    document.getElementById("df2-website").value = dealer ? (dealer.website_url || "") : "";
    document.getElementById("df2-sort").value = dealer ? dealer.sort_order : 0;
    document.getElementById("df2-published").checked = dealer ? !!dealer.published : true;
    document.getElementById("dealer-modal").style.display = "flex";
  }

  document.getElementById("btn-new-dealer").addEventListener("click", function () { openDealerModal(null); });
  document.getElementById("df2-cancel").addEventListener("click", function () { document.getElementById("dealer-modal").style.display = "none"; });

  document.getElementById("dealer-form").addEventListener("submit", async function (e) {
    e.preventDefault();
    var errEl = document.getElementById("dealer-modal-error");
    errEl.style.display = "none";
    var row = {
      title_tr: document.getElementById("df2-title-tr").value.trim(),
      title_en: document.getElementById("df2-title-en").value.trim(),
      badge_tr: document.getElementById("df2-badge-tr").value.trim() || null,
      badge_en: document.getElementById("df2-badge-en").value.trim() || null,
      address_tr: document.getElementById("df2-address-tr").value.trim(),
      address_en: document.getElementById("df2-address-en").value.trim(),
      phone: document.getElementById("df2-phone").value.trim() || null,
      email: document.getElementById("df2-email").value.trim() || null,
      website_url: document.getElementById("df2-website").value.trim() || null,
      sort_order: parseInt(document.getElementById("df2-sort").value, 10) || 0,
      published: document.getElementById("df2-published").checked
    };
    var id = document.getElementById("df2-id").value;
    if (id) row.id = id;
    var res = await MF.adminUpsertDealer(row);
    if (res.error) { errEl.textContent = "Kaydetme başarısız: " + res.error.message; errEl.style.display = ""; return; }
    document.getElementById("dealer-modal").style.display = "none";
    flash("Bayi kaydedildi.", true);
    loadDealers();
  });

  boot();
})();
