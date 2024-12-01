function openLightbox(src, caption, detail) {
  const lightbox = document.getElementById("lightbox");
  const lightboxImage = document.getElementById("lightbox-image");
  const lightboxCaption = document.getElementById("lightbox-caption");

  lightbox.style.display = "block";
  lightboxImage.src = src;
  lightboxCaption.innerHTML = `<h3>${caption}</h3><p>${detail}</p>`;
}

function closeLightbox() {
  document.getElementById("lightbox").style.display = "none";
}