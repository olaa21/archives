function filterGallery(category) {
    // Remove 'active' class from all buttons
    document.querySelectorAll('.filter-button').forEach(button => button.classList.remove('active'));

    // Add 'active' class to the clicked button
    const activeButton = Array.from(document.querySelectorAll('.filter-button'))
        .find(button => button.textContent === category || (category === 'all' && button.textContent === 'All'));
    if (activeButton) activeButton.classList.add('active');

    // Get all figures in the gallery
    const figures = document.querySelectorAll('.gallery figure');

    // Filter based on category
    figures.forEach(figure => {
        const figureCategory = figure.getAttribute('data-category').toLowerCase(); // Ensure case insensitivity
        if (category === 'all' || figureCategory === category.toLowerCase()) {
            figure.style.display = 'block'; // Show matching figures
        } else {
            figure.style.display = 'none'; // Hide non-matching figures
        }
    });
}

// Initialize gallery with all items visible on DOMContentLoaded
document.addEventListener('DOMContentLoaded', () => filterGallery('all'));
