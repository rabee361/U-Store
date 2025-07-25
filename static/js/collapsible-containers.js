// 📦 Collapsible Containers with Accordion Effect
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
            
            // Add click event listener with accordion effect
            header.addEventListener('click', () => {
                const currentState = container.getAttribute('data-collapsed') === 'true';
                const newState = !currentState;
                
                // Accordion effect: close other containers in the same parent
                if (!newState) {
                    closeOtherContainers(container);
                }
                
                container.setAttribute('data-collapsed', newState.toString());
                updateContainerStateWithAnimation(container, content, icon, newState);
                
                // Add animation feedback
                addToggleAnimation(toggle);
            });
        });
    }

    // 🔄 Close other containers (accordion effect)
    function closeOtherContainers(activeContainer) {
        const parentElement = activeContainer.parentElement;
        const siblingContainers = parentElement.querySelectorAll('.collapsible-container');
        
        siblingContainers.forEach(container => {
            if (container !== activeContainer) {
                const content = container.querySelector('.collapsible-content');
                const toggle = container.querySelector('.collapsible-toggle');
                const icon = toggle.querySelector('i');
                
                container.setAttribute('data-collapsed', 'true');
                updateContainerStateWithAnimation(container, content, icon, true);
            }
        });
    }

    // 🔄 Update container state with smooth animation
    function updateContainerStateWithAnimation(container, content, icon, isCollapsed) {
        if (isCollapsed) {
            // Collapse animation
            content.style.height = content.scrollHeight + 'px';
            content.offsetHeight; // Force reflow
            content.style.transition = 'height 0.3s ease-out, opacity 0.3s ease-out';
            content.style.height = '0px';
            content.style.opacity = '0';
            
            setTimeout(() => {
                content.style.display = 'none';
                content.style.height = '';
                content.style.opacity = '';
                content.style.transition = '';
            }, 300);
            
            icon.className = 'fas fa-chevron-down';
            container.setAttribute('aria-expanded', 'false');
        } else {
            // Expand animation
            content.style.display = 'block';
            content.style.height = '0px';
            content.style.opacity = '0';
            content.style.transition = 'height 0.3s ease-out, opacity 0.3s ease-out';
            
            const targetHeight = content.scrollHeight + 'px';
            
            setTimeout(() => {
                content.style.height = targetHeight;
                content.style.opacity = '1';
            }, 10);
            
            setTimeout(() => {
                content.style.height = '';
                content.style.opacity = '';
                content.style.transition = '';
            }, 300);
            
            icon.className = 'fas fa-chevron-up';
            container.setAttribute('aria-expanded', 'true');
        }
    }

    // 🔄 Update container state (fallback for non-animated)
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

    // 🎯 Keyboard accessibility
    document.addEventListener('keydown', (e) => {
        if (e.target.classList.contains('collapsible-header')) {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                e.target.click();
            }
        }
    });

    // 🚀 Initialize collapsible containers
    initCollapsibleContainers();
    
    console.log('📦 Collapsible containers with accordion effect initialized!');
});
