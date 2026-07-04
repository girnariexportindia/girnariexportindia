document.addEventListener('DOMContentLoaded', () => {
    
    // --- Mobile Menu Toggle ---
    const menuToggle = document.getElementById('menu-toggle');
    const navLinks = document.querySelector('.nav-links');
    const menuIconUse = menuToggle.querySelector('use');

    menuToggle.addEventListener('click', () => {
        navLinks.classList.toggle('active');
        // Toggle icon between menu and close
        if (navLinks.classList.contains('active')) {
            menuIconUse.setAttribute('href', '#icon-close');
        } else {
            menuIconUse.setAttribute('href', '#icon-menu');
        }
    });

    // Close mobile menu on link click
    document.querySelectorAll('.nav-links a').forEach(link => {
        link.addEventListener('click', () => {
            if (navLinks.classList.contains('active')) {
                navLinks.classList.remove('active');
                menuIconUse.setAttribute('href', '#icon-menu');
            }
        });
    });

    // --- Active Link Highlighting ---
    const navItems = document.querySelectorAll('.nav-links a');
    const currentPath = window.location.pathname.split('/').pop() || 'index.html';
    
    navItems.forEach(a => {
        const linkPath = a.getAttribute('href');
        if (linkPath === currentPath) {
            a.classList.add('active');
        } else {
            a.classList.remove('active');
        }
    });

    // --- Header Scroll Effect ---
    const header = document.getElementById('header');

    window.addEventListener('scroll', () => {
        // Header background
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    });

    // --- Scroll to Top Button ---
    const scrollTopBtn = document.getElementById('scroll-to-top');

    window.addEventListener('scroll', () => {
        if (window.scrollY > 500) {
            scrollTopBtn.classList.add('visible');
        } else {
            scrollTopBtn.classList.remove('visible');
        }
    });

    scrollTopBtn.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });

    // --- Scroll Animations (Intersection Observer) ---
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };

    const fadeObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    document.querySelectorAll('.fade-in-up').forEach(el => {
        fadeObserver.observe(el);
    });

    // --- Counter Animation ---
    const counters = document.querySelectorAll('.counter');
    let hasAnimated = false;

    const counterObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting && !hasAnimated) {
                counters.forEach(counter => {
                    const target = +counter.getAttribute('data-target');
                    const duration = 2000; // ms
                    const increment = target / (duration / 16); // 60fps
                    
                    let current = 0;
                    const updateCounter = () => {
                        current += increment;
                        if (current < target) {
                            counter.innerText = Math.ceil(current);
                            requestAnimationFrame(updateCounter);
                        } else {
                            counter.innerText = target;
                        }
                    };
                    updateCounter();
                });
                hasAnimated = true;
            }
        });
    }, { threshold: 0.5 });

    const statsSection = document.querySelector('.stats-section');
    if (statsSection) {
        counterObserver.observe(statsSection);
    }

    // --- Form Submission (Simple validation & visual feedback) ---
    const contactForm = document.getElementById('contact-form');
    const formStatus = document.getElementById('form-status');

    if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();
            // Basic validation is handled by HTML 'required' attributes
            
            // Visual feedback (simulating submission)
            const submitBtn = contactForm.querySelector('button[type="submit"]');
            const originalText = submitBtn.innerText;
            
            submitBtn.innerText = 'Sending...';
            submitBtn.disabled = true;

            const formData = new FormData(contactForm);
            
            fetch(contactForm.action, {
                method: contactForm.method,
                body: formData,
                headers: {
                    'Accept': 'application/json'
                }
            })
            .then(response => {
                if (response.ok) {
                    formStatus.innerText = 'Message sent successfully! We will get back to you soon.';
                    formStatus.style.color = 'green';
                    contactForm.reset();
                } else {
                    response.json().then(data => {
                        if (Object.hasOwn(data, 'errors')) {
                            formStatus.innerText = data["errors"].map(error => error["message"]).join(", ");
                        } else {
                            formStatus.innerText = 'Oops! There was a problem submitting your form';
                        }
                        formStatus.style.color = 'red';
                    });
                }
            })
            .catch(error => {
                formStatus.innerText = 'Oops! There was a problem submitting your form';
                formStatus.style.color = 'red';
            })
            .finally(() => {
                submitBtn.innerText = originalText;
                submitBtn.disabled = false;
                
                setTimeout(() => {
                    formStatus.innerText = '';
                }, 5000);
            });
        });
    }
});
