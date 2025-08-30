// Navbar functionality
document.addEventListener('DOMContentLoaded', function() {
  const hamburger = document.querySelector('.hamburger');
  const navLinks = document.querySelector('.nav-links');
  
  // Toggle mobile menu
  if (hamburger && navLinks) {
    hamburger.addEventListener('click', function() {
      this.classList.toggle('active');
      navLinks.classList.toggle('active');
    });
    
    // Close menu when clicking a link
    document.querySelectorAll('.nav-link').forEach(link => {
      link.addEventListener('click', () => {
        if (navLinks.classList.contains('active')) {
          navLinks.classList.remove('active');
          hamburger.classList.remove('active');
        }
      });
    });
  }
  
  // Update cart count (example functionality)
  window.updateCartCount = function(count) {
    const cartCount = document.querySelector('.cart-btn .item-count');
    if (cartCount) {
      cartCount.textContent = count;
      cartCount.style.display = count > 0 ? 'flex' : 'none';
    }
  }
  
  // Update wishlist count (example functionality)
  window.updateWishlistCount = function(count) {
    const wishlistCount = document.querySelector('.wishlist-btn .item-count');
    if (wishlistCount) {
      wishlistCount.textContent = count;
      wishlistCount.style.display = count > 0 ? 'flex' : 'none';
    }
  }
});