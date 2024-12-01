// Select the navigation and toggle button
const nav = document.querySelector('nav');
const menuToggle = document.querySelector('.menu-toggle');

// Add click event to toggle navigation visibility
menuToggle.addEventListener('click', () => {
    nav.classList.toggle('open');
});
