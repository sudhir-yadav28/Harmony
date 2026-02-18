document.addEventListener('DOMContentLoaded', function () {

    // Navbar scroll effect & Scroll Spy
    const navbar = document.getElementById('mainNav');
    const sections = document.querySelectorAll('section');
    const navLinks = document.querySelectorAll('.nav-link');

    function updateActiveNav() {
        let current = '';

        // Handle scroll class
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }

        // Scroll Spy Logic
        let foundSection = false;

        // Iterate backwards to find the current section
        // (This often works better than forward iteration for scrollspy)
        for (let i = sections.length - 1; i >= 0; i--) {
            const section = sections[i];
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;

            // Check if we are within the section (with offset for header)
            if (window.scrollY >= (sectionTop - 150)) {
                current = section.getAttribute('id');
                foundSection = true;
                break; // Stop once we find the bottom-most visible section
            }
        }

        // Remove active class from all
        navLinks.forEach(link => {
            link.classList.remove('active');
            link.classList.remove('active-home');
        });

        // Apply active class
        if (!foundSection || window.scrollY < 100) {
            // Default to Home if near top or no section found
            navLinks.forEach(link => {
                if (link.getAttribute('href') === '#' || link.getAttribute('href') === '#hero') {
                    link.classList.add('active');
                }
            });
        } else {
            // Find link matching current section ID
            navLinks.forEach(link => {
                const href = link.getAttribute('href');
                if (href === `#${current}`) {
                    link.classList.add('active');
                }
            });
        }
    }


    window.addEventListener('scroll', updateActiveNav);
    // Initial call
    updateActiveNav();

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();

            const targetId = this.getAttribute('href');
            if (targetId === '#') return;

            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth'
                });

                // Close mobile menu if open
                const navbarToggler = document.querySelector('.navbar-toggler');
                const navbarCollapse = document.querySelector('.navbar-collapse');
                if (navbarCollapse.classList.contains('show')) {
                    navbarToggler.click();
                }
            }
        });
    });

});
