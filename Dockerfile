# Tahap 1: Build aplikasi (misal menggunakan Node.js jika ada aset Vue/React/HTML)
FROM node:18-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
# Jika menggunakan framework build, jalankan: npm run build

# Tahap 2: Serving dengan Nginx Alpine yang ringan
FROM nginx:alpine
# Salin file statis atau hasil build ke direktori publik nginx
COPY . /usr/share/nginx/html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
