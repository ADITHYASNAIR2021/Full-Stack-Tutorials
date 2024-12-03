document.addEventListener('DOMContentLoaded', function () {
    const currentPath = window.location.pathname;
    const navbarLinks = document.querySelectorAll('.nav-link, .dropdown-item');

    navbarLinks.forEach(link => {
        const linkPath = link.getAttribute('href');

        if (currentPath.startsWith(linkPath) && linkPath !== '/') {
            link.classList.add('active');

            const dropdown = link.closest('.dropdown');
            if (dropdown) {
                const toggle = dropdown.querySelector('.dropdown-toggle');
                toggle.classList.add('active');
            }
        }
    });
});

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();

        const targetElement = document.querySelector(this.getAttribute('href'));
        if (targetElement) {
            window.scrollTo({
                top: targetElement.offsetTop - 70, 
                behavior: 'smooth'
            });
        }
    });
});

document.querySelectorAll('.dropdown-item').forEach(item => {
    item.addEventListener('click', function () {
        const dropdown = this.closest('.dropdown');
        if (dropdown) {
            const toggle = dropdown.querySelector('.dropdown-toggle');
            toggle.click(); 
        }
    });
});


var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl);
});
