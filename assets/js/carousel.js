/* =========================================================
   MF NAUTIC TURKEY — carousel.js
   Basit, bağımlılıksız kayan görsel banner (Ürünlerimiz sayfası
   üstündeki Tikal ürün/kategori banner'ı için).
   ========================================================= */
(function () {
  var INTERVAL_MS = 4200;

  function initCarousel(root) {
    var slides = Array.prototype.slice.call(root.querySelectorAll("img"));
    if (slides.length < 2) return;

    var dotsWrap = document.createElement("div");
    dotsWrap.className = "carousel-dots";
    root.appendChild(dotsWrap);

    var dots = slides.map(function (_, i) {
      var b = document.createElement("button");
      b.type = "button";
      b.setAttribute("aria-label", "Slayt " + (i + 1));
      b.addEventListener("click", function () { goTo(i); resetTimer(); });
      dotsWrap.appendChild(b);
      return b;
    });

    var current = 0;
    function goTo(i) {
      slides[current].classList.remove("is-active");
      dots[current].classList.remove("is-active");
      current = (i + slides.length) % slides.length;
      slides[current].classList.add("is-active");
      dots[current].classList.add("is-active");
    }
    goTo(0);

    var timer = setInterval(function () { goTo(current + 1); }, INTERVAL_MS);
    function resetTimer() {
      clearInterval(timer);
      timer = setInterval(function () { goTo(current + 1); }, INTERVAL_MS);
    }

    var prevBtn = document.createElement("button");
    prevBtn.type = "button";
    prevBtn.className = "carousel-arrow carousel-prev";
    prevBtn.setAttribute("aria-label", "Önceki");
    prevBtn.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"></polyline></svg>';
    prevBtn.addEventListener("click", function () { goTo(current - 1); resetTimer(); });
    root.appendChild(prevBtn);

    var nextBtn = document.createElement("button");
    nextBtn.type = "button";
    nextBtn.className = "carousel-arrow carousel-next";
    nextBtn.setAttribute("aria-label", "Sonraki");
    nextBtn.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"></polyline></svg>';
    nextBtn.addEventListener("click", function () { goTo(current + 1); resetTimer(); });
    root.appendChild(nextBtn);

    root.addEventListener("mouseenter", function () { clearInterval(timer); });
    root.addEventListener("mouseleave", resetTimer);
  }

  document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".carousel").forEach(initCarousel);
  });
})();
