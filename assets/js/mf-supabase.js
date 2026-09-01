/* =========================================================
   MF NAUTIC TURKEY — mf-supabase.js
   Supabase bağlantısı + veri okuma/yazma yardımcı fonksiyonları.
   Bu dosyadan önce https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2
   CDN script'i yüklenmiş olmalıdır.
   ========================================================= */
(function (global) {
  var SUPABASE_URL = "https://bawkhuehmbskhjikjztg.supabase.co";
  var SUPABASE_KEY = "sb_publishable_3g4Ij5yTpHS5nHy5fwQ5yQ_npYr2nb7";

  var _client = null;
  function client() {
    if (_client) return _client;
    if (!global.supabase || !global.supabase.createClient) {
      console.error("[MF] Supabase JS SDK yüklenemedi.");
      return null;
    }
    _client = global.supabase.createClient(SUPABASE_URL, SUPABASE_KEY, {
      auth: { persistSession: true, autoRefreshToken: true }
    });
    return _client;
  }

  /* ---------------- ICON SET (kart/detay sayfalarında kullanılan SVG'ler) ---------------- */
  var ICONS = {
    "droplet": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2.69s-7 7.44-7 12.31a7 7 0 0 0 14 0c0-4.87-7-12.31-7-12.31z"></path></svg>',
    "layers": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 2 7 12 12 22 7 12 2"></polygon><polyline points="2 17 12 22 22 17"></polyline><polyline points="2 12 12 17 22 12"></polyline></svg>',
    "tool": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"></path></svg>',
    "anchor": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="5" r="3"></circle><line x1="12" y1="22" x2="12" y2="8"></line><path d="M5 12H2a10 10 0 0 0 20 0h-3"></path></svg>',
    "shield-check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path><polyline points="9 12 11 14 15 10"></polyline></svg>',
    "package": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="16.5" y1="9.4" x2="7.5" y2="4.21"></line><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path><polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline><line x1="12" y1="22.08" x2="12" y2="12"></line></svg>',
    "file-text": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>',
    "download": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>',
    "arrow-right": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>',
    "check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>',
    "whatsapp": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.47 14.38c-.29-.15-1.72-.85-1.99-.95-.27-.1-.46-.15-.66.15-.2.29-.76.94-.93 1.14-.17.2-.34.22-.63.07-.29-.15-1.22-.45-2.33-1.44-.86-.77-1.44-1.71-1.61-2-.17-.29-.02-.45.13-.6.13-.13.29-.34.44-.51.15-.17.2-.29.29-.49.1-.2.05-.37-.02-.51-.07-.15-.66-1.59-.9-2.17-.24-.58-.48-.5-.66-.51-.17-.01-.37-.01-.56-.01-.2 0-.51.07-.78.37-.27.29-1.02 1-1.02 2.43 0 1.43 1.04 2.82 1.19 3.01.15.2 2.05 3.13 4.96 4.39.69.3 1.23.48 1.65.61.69.22 1.32.19 1.82.11.55-.08 1.72-.7 1.96-1.38.24-.68.24-1.26.17-1.38-.07-.12-.27-.2-.56-.34z"></path><path d="M12.02 2.01c-5.51 0-9.98 4.47-9.98 9.98 0 1.76.46 3.48 1.34 4.99L2 22l5.15-1.35a9.94 9.94 0 0 0 4.87 1.24h.01c5.51 0 9.98-4.47 9.98-9.98 0-2.67-1.04-5.18-2.93-7.07a9.93 9.93 0 0 0-7.06-2.83zm0 18.13h-.01a8.28 8.28 0 0 1-4.21-1.15l-.3-.18-3.06.8.82-2.98-.2-.31a8.26 8.26 0 0 1-1.27-4.42c0-4.56 3.71-8.27 8.28-8.27 2.21 0 4.29.86 5.85 2.42a8.2 8.2 0 0 1 2.42 5.86c0 4.56-3.72 8.23-8.32 8.23z"></path></svg>',
    "play": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"></path></svg>',
    "map-pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>',
    "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.362 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.338 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>',
    "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 6c0-1.1-.9-2-2-2H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V6z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>',
    "globe": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>'
  };
  function icon(name) { return ICONS[name] || ICONS["package"]; }

  /* ---------------- Genel okuma fonksiyonları (herkese açık) ---------------- */
  async function getCategories() {
    var sb = client();
    if (!sb) return [];
    var res = await sb.from("categories").select("*").order("sort_order");
    if (res.error) { console.error(res.error); return []; }
    return res.data || [];
  }

  async function getCategoryBySlug(slug) {
    var sb = client();
    if (!sb) return null;
    var res = await sb.from("categories").select("*").eq("slug", slug).maybeSingle();
    if (res.error) { console.error(res.error); return null; }
    return res.data;
  }

  async function getProductsByCategorySlug(catSlug) {
    var sb = client();
    if (!sb) return [];
    var cat = await getCategoryBySlug(catSlug);
    if (!cat) return [];
    var res = await sb.from("products").select("*").eq("category_id", cat.id).eq("published", true).order("sort_order");
    if (res.error) { console.error(res.error); return []; }
    return res.data || [];
  }

  async function getAllProducts() {
    var sb = client();
    if (!sb) return [];
    var res = await sb.from("products").select("*, categories(slug, title_tr, title_en)").eq("published", true).order("sort_order");
    if (res.error) { console.error(res.error); return []; }
    return res.data || [];
  }

  async function getProductBySlug(slug) {
    var sb = client();
    if (!sb) return null;
    var res = await sb.from("products").select("*, categories(slug, title_tr, title_en)").eq("slug", slug).maybeSingle();
    if (res.error) { console.error(res.error); return null; }
    return res.data;
  }

  async function getDocuments() {
    var sb = client();
    if (!sb) return [];
    // Genel döküman listesi: TÜM dökümanlar (kategori bazlı + ürüne özel + genel
    // katalog vb.) — ilgili ürüne ait tüm dillerdeki dökümanlar burada, kategorisi
    // altında, tüm dil linkleriyle birlikte indirilebilir olarak gösterilir.
    var res = await sb.from("documents").select("*, categories(slug, title_tr, title_en, icon, sort_order)").order("sort_order");
    if (res.error) { console.error(res.error); return []; }
    return res.data || [];
  }

  async function getDocumentsByProductId(productId) {
    var sb = client();
    if (!sb || !productId) return [];
    var res = await sb.from("documents").select("*").eq("product_id", productId).order("sort_order");
    if (res.error) { console.error(res.error); return []; }
    return res.data || [];
  }

  async function getReferences() {
    var sb = client();
    if (!sb) return [];
    var res = await sb.from("client_references").select("*").eq("published", true).order("sort_order");
    if (res.error) { console.error(res.error); return []; }
    return res.data || [];
  }

  async function getDealers() {
    var sb = client();
    if (!sb) return [];
    var res = await sb.from("dealers").select("*").eq("published", true).order("sort_order");
    if (res.error) { console.error(res.error); return []; }
    return res.data || [];
  }

  async function getCatalogs() {
    var sb = client();
    if (!sb) return [];
    var res = await sb.from("catalogs").select("*").eq("published", true).order("sort_order");
    if (res.error) { console.error(res.error); return []; }
    return res.data || [];
  }

  /* ---------------- Admin: auth ---------------- */
  async function signIn(email, password) {
    var sb = client();
    if (!sb) return { error: { message: "Supabase yüklenemedi" } };
    return await sb.auth.signInWithPassword({ email: email, password: password });
  }
  async function signOut() {
    var sb = client();
    if (!sb) return;
    return await sb.auth.signOut();
  }
  async function getSession() {
    var sb = client();
    if (!sb) return null;
    var res = await sb.auth.getSession();
    return res.data ? res.data.session : null;
  }
  function onAuthChange(cb) {
    var sb = client();
    if (!sb) return;
    sb.auth.onAuthStateChange(function (event, session) { cb(event, session); });
  }

  /* ---------------- Admin: CRUD (RLS ile korunur — sadece admin kullanıcısı yazabilir) ---------------- */
  async function adminListProducts() {
    var sb = client();
    var res = await sb.from("products").select("*, categories(slug, title_tr)").order("sort_order");
    if (res.error) { console.error(res.error); return []; }
    return res.data || [];
  }
  async function adminUpsertProduct(row) {
    var sb = client();
    return await sb.from("products").upsert(row).select().single();
  }
  async function adminDeleteProduct(id) {
    var sb = client();
    return await sb.from("products").delete().eq("id", id);
  }

  async function adminListDocuments() {
    var sb = client();
    var res = await sb.from("documents").select("*, categories(slug, title_tr)").order("sort_order");
    if (res.error) { console.error(res.error); return []; }
    return res.data || [];
  }
  async function adminUpsertDocument(row) {
    var sb = client();
    return await sb.from("documents").upsert(row).select().single();
  }
  async function adminDeleteDocument(id) {
    var sb = client();
    return await sb.from("documents").delete().eq("id", id);
  }

  async function adminListCategories() {
    var sb = client();
    var res = await sb.from("categories").select("*").order("sort_order");
    if (res.error) { console.error(res.error); return []; }
    return res.data || [];
  }
  async function adminUpsertCategory(row) {
    var sb = client();
    return await sb.from("categories").upsert(row).select().single();
  }

  async function adminListReferences() {
    var sb = client();
    var res = await sb.from("client_references").select("*").order("sort_order");
    if (res.error) { console.error(res.error); return []; }
    return res.data || [];
  }
  async function adminUpsertReference(row) {
    var sb = client();
    return await sb.from("client_references").upsert(row).select().single();
  }
  async function adminDeleteReference(id) {
    var sb = client();
    return await sb.from("client_references").delete().eq("id", id);
  }

  async function adminListDealers() {
    var sb = client();
    var res = await sb.from("dealers").select("*").order("sort_order");
    if (res.error) { console.error(res.error); return []; }
    return res.data || [];
  }
  async function adminUpsertDealer(row) {
    var sb = client();
    return await sb.from("dealers").upsert(row).select().single();
  }
  async function adminDeleteDealer(id) {
    var sb = client();
    return await sb.from("dealers").delete().eq("id", id);
  }

  async function adminListCatalogs() {
    var sb = client();
    var res = await sb.from("catalogs").select("*").order("sort_order");
    if (res.error) { console.error(res.error); return []; }
    return res.data || [];
  }
  async function adminUpsertCatalog(row) {
    var sb = client();
    return await sb.from("catalogs").upsert(row).select().single();
  }
  async function adminDeleteCatalog(id) {
    var sb = client();
    return await sb.from("catalogs").delete().eq("id", id);
  }

  /* ---------------- Ortak yardımcılar ---------------- */
  function getLang() {
    return localStorage.getItem("mf_lang") || "tr";
  }
  function pick(row, field) {
    var lang = getLang();
    var key = field + "_" + (lang === "en" ? "en" : "tr");
    return (row && row[key] !== undefined && row[key] !== null) ? row[key] : (row ? row[field + "_tr"] : "");
  }
  function youtubeEmbed(url) {
    if (!url) return null;
    var m = url.match(/(?:youtu\.be\/|v=|embed\/)([A-Za-z0-9_-]{6,})/);
    if (!m) return null;
    return "https://www.youtube-nocookie.com/embed/" + m[1];
  }
  function waLink(text) {
    return "https://wa.me/905414558005?text=" + encodeURIComponent(text);
  }
  function escapeHtml(s) {
    if (s === null || s === undefined) return "";
    return String(s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }

  global.MF = {
    client: client,
    icon: icon,
    getCategories: getCategories,
    getCategoryBySlug: getCategoryBySlug,
    getProductsByCategorySlug: getProductsByCategorySlug,
    getAllProducts: getAllProducts,
    getProductBySlug: getProductBySlug,
    getDocuments: getDocuments,
    getDocumentsByProductId: getDocumentsByProductId,
    getReferences: getReferences,
    getDealers: getDealers,
    getCatalogs: getCatalogs,
    signIn: signIn,
    signOut: signOut,
    getSession: getSession,
    onAuthChange: onAuthChange,
    adminListProducts: adminListProducts,
    adminUpsertProduct: adminUpsertProduct,
    adminDeleteProduct: adminDeleteProduct,
    adminListDocuments: adminListDocuments,
    adminUpsertDocument: adminUpsertDocument,
    adminDeleteDocument: adminDeleteDocument,
    adminListCategories: adminListCategories,
    adminUpsertCategory: adminUpsertCategory,
    adminListReferences: adminListReferences,
    adminUpsertReference: adminUpsertReference,
    adminDeleteReference: adminDeleteReference,
    adminListDealers: adminListDealers,
    adminUpsertDealer: adminUpsertDealer,
    adminDeleteDealer: adminDeleteDealer,
    adminListCatalogs: adminListCatalogs,
    adminUpsertCatalog: adminUpsertCatalog,
    adminDeleteCatalog: adminDeleteCatalog,
    getLang: getLang,
    pick: pick,
    youtubeEmbed: youtubeEmbed,
    waLink: waLink,
    escapeHtml: escapeHtml
  };
})(window);
