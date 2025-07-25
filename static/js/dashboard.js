// 📊 Dashboard Collapsible Functionality
document.addEventListener('DOMContentLoaded', function() {
    'use strict';

    // 🎯 Initialize collapsible containers
    function initCollapsibleContainers() {
        const containers = document.querySelectorAll('.collapsible-container');
        
        containers.forEach(container => {
            const header = container.querySelector('.collapsible-header');
            const toggle = container.querySelector('.collapsible-toggle');
            const content = container.querySelector('.collapsible-content');
            const icon = toggle.querySelector('i');
            
            // Set initial state
            const isCollapsed = container.getAttribute('data-collapsed') === 'true';
            updateContainerState(container, content, icon, isCollapsed);
            
            // Add click event listener
            header.addEventListener('click', () => {
                const currentState = container.getAttribute('data-collapsed') === 'true';
                const newState = !currentState;
                
                container.setAttribute('data-collapsed', newState.toString());
                updateContainerState(container, content, icon, newState);
                
                // Add animation feedback
                addToggleAnimation(toggle);
            });
        });
    }

    // 🔄 Update container state
    function updateContainerState(container, content, icon, isCollapsed) {
        if (isCollapsed) {
            content.style.display = 'none';
            icon.className = 'fas fa-chevron-down';
            container.setAttribute('aria-expanded', 'false');
        } else {
            content.style.display = 'block';
            icon.className = 'fas fa-chevron-up';
            container.setAttribute('aria-expanded', 'true');
        }
    }

    // ✨ Add toggle animation
    function addToggleAnimation(toggle) {
        toggle.style.transform = 'scale(0.9)';
        
        setTimeout(() => {
            toggle.style.transform = 'scale(1)';
        }, 150);
    }

    // 📈 Animate stat cards on scroll
    function initStatCardAnimations() {
        const statCards = document.querySelectorAll('.stat-card');
        
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }
            });
        }, {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        });

        statCards.forEach((card, index) => {
            // Set initial state
            card.style.opacity = '0';
            card.style.transform = 'translateY(20px)';
            card.style.transition = `opacity 0.6s ease ${index * 0.1}s, transform 0.6s ease ${index * 0.1}s`;
            
            observer.observe(card);
        });
    }

    // 🎯 Animate cover stats
    function animateCoverStats() {
        const statNumbers = document.querySelectorAll('.stat-number');
        
        statNumbers.forEach(stat => {
            const finalValue = parseInt(stat.textContent.replace(/,/g, ''));
            let currentValue = 0;
            const increment = finalValue / 50;
            const duration = 2000;
            const stepTime = duration / 50;
            
            const timer = setInterval(() => {
                currentValue += increment;
                if (currentValue >= finalValue) {
                    currentValue = finalValue;
                    clearInterval(timer);
                }
                stat.textContent = Math.floor(currentValue).toLocaleString('ar-EG');
            }, stepTime);
        });
    }

    // 🚀 Initialize dashboard
    function initDashboard() {
        initCollapsibleContainers();
        initStatCardAnimations();
        
        // Animate stats after a short delay
        setTimeout(animateCoverStats, 500);
        
        console.log('📊 Dashboard initialized successfully!');
    }

    // 🎯 Keyboard accessibility
    document.addEventListener('keydown', (e) => {
        if (e.target.classList.contains('collapsible-header')) {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                e.target.click();
            }
        }
    });

    // 🚀 Initialize when DOM is ready
    initDashboard();
});
