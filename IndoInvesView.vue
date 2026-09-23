<template>
  <div class="indoinves-wrapper">
    <div class="indoinves-card">
      <img src="https://indoinves.github.io/img/indoinves.png" alt="IndoInves Logo" class="logo-img" />
      <h1>Selamat Datang di IndoInves</h1>
      <p class="subtitle">Platform pintar investasi, keuangan, dan kumpulan tools finansial modern.</p>
      
      <div class="button-group">
        <a href="https://indoinves.github.io/" class="btn btn-primary" target="_blank" rel="noopener">Buka Website Utama</a>
        <a href="https://indoinves.github.io/tools/investasi.html" class="btn btn-secondary" target="_blank" rel="noopener">Jelajahi Tools</a>
      </div>

      <footer class="footer-text">
        &copy; {{ currentYear }} IndoInves. All rights reserved.
      </footer>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
const currentYear = ref(new Date().getFullYear())
</script>

<style scoped>
.indoinves-wrapper {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  background-color: #f8fafc;
  color: #1e293b;
  display: flex;
  min-height: 100vh;
  justify-content: center;
  align-items: center;
  text-align: center;
  padding: 20px;
  margin: 0;
}
.indoinves-card {
  max-width: 600px;
  width: 100%;
  background: #ffffff;
  padding: 40px;
  border-radius: 12px;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
}
.logo-img {
  width: 100px;
  height: 100px;
  margin-bottom: 20px;
  border-radius: 50%;
  object-fit: cover;
}
h1 {
  font-size: 24px;
  margin-bottom: 10px;
  color: #0f172a;
}
.subtitle {
  color: #64748b;
  margin-bottom: 25px;
  font-size: 15px;
}
.button-group {
  display: flex;
  gap: 10px;
  justify-content: center;
  flex-wrap: wrap;
}
.btn {
  display: inline-block;
  padding: 10px 20px;
  border-radius: 6px;
  text-decoration: none;
  font-weight: 600;
  transition: background-color 0.2s;
}
.btn-primary {
  background-color: #2563eb;
  color: white;
}
.btn-primary:hover {
  background-color: #1d4ed8;
}
.btn-secondary {
  background-color: #e2e8f0;
  color: #475569;
}
.btn-secondary:hover {
  background-color: #cbd5e1;
}
.footer-text {
  margin-top: 30px;
  font-size: 14px;
  color: #94a3b8;
}
</style>
