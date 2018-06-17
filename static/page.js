// Fade in animation
const pageElements = document.getElementsByClassName('page');

if (pageElements.length > 0) {
    const page = pageElements[0];
    setTimeout(function() {
        page.classList.remove('hidden');
    }, 800);
}