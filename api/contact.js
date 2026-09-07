/* =========================================================
   MF NAUTIC TURKEY — /api/contact
   Vercel Serverless Function (Node.js runtime).
   Sitedeki iletişim formundan gelen veriyi Resend API üzerinden
   e-posta olarak levent@mf-nautic.com adresine gönderir.

   Gerekli ortam değişkenleri (Vercel proje ayarlarından eklenmeli):
     RESEND_API_KEY   — Resend hesabından alınan API anahtarı (zorunlu)
     CONTACT_TO_EMAIL — Formların gideceği adres (opsiyonel, varsayılan: levent@mf-nautic.com)
     RESEND_FROM      — Gönderen adresi (opsiyonel, varsayılan: "MF Nautic Web <onboarding@resend.dev>")
                        Not: Kendi domain'inizden göndermek için mf-nautic.com'u Resend'de
                        doğrulayıp örn. "MF Nautic Web <no-reply@mf-nautic.com>" kullanın.
   ========================================================= */

function escapeHtml(s) {
  if (s === null || s === undefined) return "";
  return String(s).replace(/[&<>"']/g, function (c) {
    return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
  });
}

module.exports = async function handler(req, res) {
  if (req.method !== "POST") {
    res.setHeader("Allow", "POST");
    res.status(405).json({ error: "Method not allowed" });
    return;
  }

  try {
    var body = req.body;
    if (typeof body === "string") {
      try { body = JSON.parse(body); } catch (e) { body = {}; }
    }
    body = body || {};

    var name = (body.name || "").toString().trim();
    var phone = (body.phone || "").toString().trim();
    var email = (body.email || "").toString().trim();
    var subject = (body.subject || "").toString().trim();
    var message = (body.message || "").toString().trim();
    var company = (body.company || "").toString().trim();
    var formType = (body.formType || "contact").toString().trim();

    if (!name || !phone) {
      res.status(400).json({ error: "Ad Soyad ve Telefon alanları zorunludur." });
      return;
    }

    var apiKey = process.env.RESEND_API_KEY;
    if (!apiKey) {
      console.error("[api/contact] RESEND_API_KEY tanımlı değil.");
      res.status(500).json({ error: "Sunucu e-posta yapılandırması eksik." });
      return;
    }

    var toEmail = process.env.CONTACT_TO_EMAIL || "levent@mf-nautic.com";
    var fromEmail = process.env.RESEND_FROM || "MF Nautic Web <onboarding@resend.dev>";
    var isDealer = formType === "dealer";

    var subjectLine = isDealer
      ? "Yeni Bayilik Başvurusu — " + name
      : "Yeni İletişim Formu — " + (subject || name);

    var rows = [["Ad Soyad", name]];
    if (isDealer && company) rows.push(["Şirket / İşletme", company]);
    rows.push(["Telefon", phone]);
    if (email) rows.push(["E-posta", email]);
    if (!isDealer && subject) rows.push(["Konu", subject]);
    rows.push(["Mesaj", message || "—"]);

    var htmlRows = rows.map(function (r) {
      return (
        '<tr><td style="padding:6px 14px;font-weight:700;color:#1a2b4a;white-space:nowrap;vertical-align:top">' +
        escapeHtml(r[0]) +
        '</td><td style="padding:6px 14px;color:#22293a;white-space:pre-wrap">' +
        escapeHtml(r[1]) +
        "</td></tr>"
      );
    }).join("");

    var html =
      '<div style="font-family:Arial,Helvetica,sans-serif;max-width:560px">' +
      "<h2 style=\"margin:0 0 14px;color:#0b2a52\">" + (isDealer ? "Yeni Bayilik Başvurusu" : "Yeni İletişim Formu") + "</h2>" +
      '<table style="border-collapse:collapse;font-size:14px">' + htmlRows + "</table>" +
      '<p style="margin-top:18px;font-size:12px;color:#8a93a6">mf-nautic.com üzerindeki ' + (isDealer ? "bayilik başvuru" : "iletişim") + " formundan gönderilmiştir.</p>" +
      "</div>";

    var text = rows.map(function (r) { return r[0] + ": " + r[1]; }).join("\n");

    var resendRes = await fetch("https://api.resend.com/emails", {
      method: "POST",
      headers: {
        Authorization: "Bearer " + apiKey,
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        from: fromEmail,
        to: [toEmail],
        reply_to: email || undefined,
        subject: subjectLine,
        html: html,
        text: text
      })
    });

    if (!resendRes.ok) {
      var errBody = await resendRes.text();
      console.error("[api/contact] Resend hata:", resendRes.status, errBody);
      res.status(502).json({ error: "E-posta gönderilemedi." });
      return;
    }

    res.status(200).json({ ok: true });
  } catch (err) {
    console.error("[api/contact] Beklenmeyen hata:", err);
    res.status(500).json({ error: "Beklenmeyen bir hata oluştu." });
  }
};
