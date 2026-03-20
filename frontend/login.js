const sidebar = document.getElementById('sidebar');
const closeBtn = document.getElementById('closeBtn');
const showRegister = document.getElementById('showRegister');
const showLogin = document.getElementById('showLogin');
const mainContainer = document.getElementById('mainContainer');

// Toggle sidebar on click
sidebar.addEventListener('click', function(e) {
  if (e.target.closest('form') || e.target === closeBtn) return;
  sidebar.classList.toggle('expanded');
});

// Close sidebar
closeBtn.addEventListener('click', function() {
  sidebar.classList.remove('expanded');
});

// Show register form
showRegister.addEventListener('click', function(e) {
  e.stopPropagation();
  sidebar.classList.add('expanded');
});

// Show login form
showLogin.addEventListener('click', function(e) {
  e.stopPropagation();
  sidebar.classList.remove('expanded');
});

// Dummy login handler
document.getElementById('loginForm').addEventListener('submit', function(e) {
  e.preventDefault();
  alert('Login functionality would go here');
});

// Dummy register handler
document.getElementById('registerForm').addEventListener('submit', function(e) {
  e.preventDefault();
  alert('Registration functionality would go here');
});
