window.addEventListener('scroll', function() {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 50) {
        navbar.classList.add('scrolled', 'navbar-dark', 'bg-dark');
    } else {
        navbar.classList.remove('scrolled', 'navbar-dark', 'bg-dark');
    }
});