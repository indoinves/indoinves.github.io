# Menggunakan image Nginx Alpine yang ringan
FROM nginx:alpine

# Menyalin seluruh file proyek ke direktori public html Nginx
COPY . /usr/share/nginx/html

# Membuka port 80 untuk akses web
EXPOSE 80

# Menjalankan Nginx di foreground
CMD ["nginx", "-g", "daemon off;"]
