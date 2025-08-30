// 🚀 Main JavaScript for Theme1
document.addEventListener('DOMContentLoaded', function() {

    // ⬆️ Scroll to Top Button Functionality
    const scrollToTopBtn = document.getElementById('scrollToTop');

    if (scrollToTopBtn) {
        // Show/hide button based on scroll position
        function toggleScrollButton() {
            if (window.pageYOffset > 300) {
                scrollToTopBtn.classList.add('visible');
            } else {
                scrollToTopBtn.classList.remove('visible');
            }
        }

        // Smooth scroll to top
        function scrollToTop() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        }

        // Event listeners
        window.addEventListener('scroll', toggleScrollButton);
        scrollToTopBtn.addEventListener('click', scrollToTop);

        // Initial check
        toggleScrollButton();
    }

    // 📧 Newsletter Form Functionality
    const newsletterForm = document.getElementById('newsletterForm');
    const newsletterEmail = document.getElementById('newsletterEmail');

    if (newsletterForm && newsletterEmail) {
        newsletterForm.addEventListener('submit', function(e) {
            e.preventDefault();

            const email = newsletterEmail.value.trim();

            if (email && isValidEmail(email)) {
                // Show success message
                showNotification('✅ Thank you for subscribing!', 'success');
                newsletterEmail.value = '';
            } else {
                // Show error message
                showNotification('❌ Please enter a valid email address.', 'error');
            }
        });
    }

    // 🔍 Email validation helper
    function isValidEmail(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }

    // 🔔 Notification system
    function showNotification(message, type = 'info') {
        // Remove existing notifications
        const existingNotifications = document.querySelectorAll('.notification');
        existingNotifications.forEach(notification => notification.remove());

        // Create notification element
        const notification = document.createElement('div');
        notification.className = `notification notification-${type}`;
        notification.textContent = message;

        // Add styles
        Object.assign(notification.style, {
            position: 'fixed',
            top: '20px',
            right: '20px',
            padding: '12px 20px',
            borderRadius: '8px',
            color: 'white',
            fontWeight: '500',
            fontSize: '14px',
            zIndex: '9999',
            transform: 'translateX(100%)',
            transition: 'transform 0.3s ease',
            backgroundColor: type === 'success' ? '#10b981' : type === 'error' ? '#ef4444' : '#3b82f6'
        });

        // Add to DOM
        document.body.appendChild(notification);

        // Animate in
        setTimeout(() => {
            notification.style.transform = 'translateX(0)';
        }, 100);

        // Remove after 3 seconds
        setTimeout(() => {
            notification.style.transform = 'translateX(100%)';
            setTimeout(() => {
                if (notification.parentNode) {
                    notification.parentNode.removeChild(notification);
                }
            }, 300);
        }, 3000);
    }

    // 🎨 Footer Link Animations
    const footerLinks = document.querySelectorAll('.footer-link');

    footerLinks.forEach(link => {
        link.addEventListener('mouseenter', function() {
            this.style.transform = 'translateX(8px)';
        });

        link.addEventListener('mouseleave', function() {
            this.style.transform = 'translateX(0)';
        });
    });

    // 🌐 Social Media Link Analytics (Optional)
    const socialLinks = document.querySelectorAll('.social-link');

    socialLinks.forEach(link => {
        link.addEventListener('click', function() {
            const platform = this.getAttribute('aria-label');
            console.log(`Social media click: ${platform}`);

            // Add your analytics tracking here
            // Example: gtag('event', 'social_click', { platform: platform });
        });
    });

    // 📱 Mobile Footer Accordion (Optional Enhancement)
    function initMobileFooterAccordion() {
        if (window.innerWidth <= 768) {
            const footerTitles = document.querySelectorAll('.footer-title');

            footerTitles.forEach(title => {
                if (!title.classList.contains('accordion-initialized')) {
                    title.classList.add('accordion-initialized');
                    title.style.cursor = 'pointer';

                    title.addEventListener('click', function() {
                        const column = this.parentElement;
                        const links = column.querySelector('.footer-links, .newsletter-form, .social-media');

                        if (links) {
                            const isOpen = links.style.display !== 'none';

                            // Close all other sections
                            document.querySelectorAll('.footer-column').forEach(col => {
                                const otherLinks = col.querySelector('.footer-links, .newsletter-form, .social-media');
                                if (otherLinks && otherLinks !== links) {
                                    otherLinks.style.display = 'none';
                                    col.querySelector('.footer-title').classList.remove('active');
                                }
                            });

                            // Toggle current section
                            links.style.display = isOpen ? 'none' : 'flex';
                            this.classList.toggle('active', !isOpen);
                        }
                    });

                    // Initially hide all sections except the first one
                    const column = title.parentElement;
                    const links = column.querySelector('.footer-links, .newsletter-form, .social-media');
                    if (links && !column.classList.contains('footer-brand')) {
                        links.style.display = 'none';
                    }
                }
            });
        }
    }

    // Initialize mobile accordion
    initMobileFooterAccordion();

    // Re-initialize on window resize
    window.addEventListener('resize', function() {
        if (window.innerWidth > 768) {
            // Reset all footer sections to visible on desktop
            document.querySelectorAll('.footer-links, .newsletter-form, .social-media').forEach(element => {
                element.style.display = '';
            });
            document.querySelectorAll('.footer-title').forEach(title => {
                title.classList.remove('active');
            });
        } else {
            initMobileFooterAccordion();
        }
    });

    // 🎯 Smooth scroll for internal links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // 🌟 Reviews Section Navigation
    const reviewsPrev = document.getElementById('reviewsPrev');
    const reviewsNext = document.getElementById('reviewsNext');
    const reviewsGrid = document.getElementById('reviewsGrid');

    if (reviewsPrev && reviewsNext && reviewsGrid) {
        let currentReviewIndex = 0;
        const reviewCards = reviewsGrid.querySelectorAll('.review-card');
        const totalReviews = reviewCards.length;
        const reviewsPerPage = window.innerWidth <= 768 ? 1 : window.innerWidth <= 1024 ? 2 : 3;

        function updateReviewsDisplay() {
            reviewCards.forEach((card, index) => {
                if (index >= currentReviewIndex && index < currentReviewIndex + reviewsPerPage) {
                    card.style.display = 'flex';
                } else {
                    card.style.display = 'none';
                }
            });

            // Update navigation buttons
            reviewsPrev.disabled = currentReviewIndex === 0;
            reviewsNext.disabled = currentReviewIndex + reviewsPerPage >= totalReviews;
        }

        reviewsPrev.addEventListener('click', () => {
            if (currentReviewIndex > 0) {
                currentReviewIndex = Math.max(0, currentReviewIndex - reviewsPerPage);
                updateReviewsDisplay();
            }
        });

        reviewsNext.addEventListener('click', () => {
            if (currentReviewIndex + reviewsPerPage < totalReviews) {
                currentReviewIndex = Math.min(totalReviews - reviewsPerPage, currentReviewIndex + reviewsPerPage);
                updateReviewsDisplay();
            }
        });

        // Initialize display
        updateReviewsDisplay();

        // Update on window resize
        window.addEventListener('resize', () => {
            const newReviewsPerPage = window.innerWidth <= 768 ? 1 : window.innerWidth <= 1024 ? 2 : 3;
            if (newReviewsPerPage !== reviewsPerPage) {
                currentReviewIndex = 0;
                updateReviewsDisplay();
            }
        });
    }

    // ⭐ Star Rating Interaction (Optional Enhancement)
    const starRatings = document.querySelectorAll('.review-rating');

    starRatings.forEach(rating => {
        const stars = rating.querySelectorAll('.star');

        stars.forEach((star, index) => {
            star.addEventListener('mouseenter', () => {
                stars.forEach((s, i) => {
                    if (i <= index) {
                        s.style.transform = 'scale(1.2)';
                        s.style.color = 'var(--accent-orange)';
                    } else {
                        s.style.transform = 'scale(1)';
                        s.style.color = '#e5e5e5';
                    }
                });
            });
        });

        rating.addEventListener('mouseleave', () => {
            stars.forEach(star => {
                star.style.transform = 'scale(1)';
                if (star.classList.contains('filled')) {
                    star.style.color = 'var(--accent-orange)';
                } else {
                    star.style.color = '#e5e5e5';
                }
            });
        });
    });

    console.log('🎉 Theme1 JavaScript initialized successfully!');
});



// 🍔 Mobile Menu Toggle
const mobileMenuToggle = document.getElementById('mobileMenuToggle');
const mobileMenu = document.getElementById('mobileMenu');

mobileMenuToggle.addEventListener('click', () => {
    mobileMenu.classList.toggle('active');
});

// 🔍 Search Toggle
const searchToggle = document.getElementById('searchToggle');
const searchOverlay = document.getElementById('searchOverlay');
const searchInput = document.getElementById('searchInput');

searchToggle.addEventListener('click', () => {
    searchOverlay.classList.toggle('active');
    if (searchOverlay.classList.contains('active')) {
        searchInput.focus();
    }
});

// 🧭 Navbar Scroll Effect
const navbar = document.getElementById('navbar');

window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});

// 🎨 Color Option Selection
document.querySelectorAll('.color-option').forEach(option => {
    option.addEventListener('click', function() {
        // Remove active class from siblings
        this.parentNode.querySelectorAll('.color-option').forEach(sibling => {
            sibling.classList.remove('active');
        });
        // Add active class to clicked option
        this.classList.add('active');
    });
});

// 🔧 Filter Buttons
document.querySelectorAll('.filter-btn').forEach(btn => {
    btn.addEventListener('click', function() {
        document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
        this.classList.add('active');
    });
});

// 🎯 View Toggle
document.querySelectorAll('.view-toggle-btn').forEach(btn => {
    btn.addEventListener('click', function() {
        document.querySelectorAll('.view-toggle-btn').forEach(b => b.classList.remove('active'));
        this.classList.add('active');
    });
});