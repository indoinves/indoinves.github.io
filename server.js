const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

const htmlTemplate = `<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IndoInves - Platform Pintar Investasi & Keuangan</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: system-ui, sans-serif; background-color: #f8fafc; color: #1e293b; display: flex; min-height: 100vh; justify-content: center; align-items: center; text-align: center; padding: 20px; }
        .container { max-width: 600px; background: #ffffff; padding: 40px; border-radius: 12px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); }
        img.logo { width: 100px; height: 100px; margin-bottom: 20px; border-radius: 50%; }
        h1 { font-size: 24px; margin-bottom: 10px; color: #0f172a; }
        p { color: #64748b; margin-bottom: 25px; }
        .btn-group { display: flex; gap: 10px; justify-content: center; flex-wrap: wrap; }
        .btn { display: inline-block; background-color: #2563eb; color: white; padding: 10px 20px; border-radius: 6px; text-decoration: none; font-weight: 600; }
        .btn-secondary { background-color: #e2e8f0; color: #475569; }
        footer { margin-top: 30px; font-size: 14px; color: #94a3b8; }
    </style>
</head>
<body>
    <div class="container">
        <img src="https://indoinves.github.io/img/indoinves.png" alt="IndoInves Logo" class="logo">
        <h1>Selamat Datang di IndoInves</h1>
        <p>Platform pintar investasi, keuangan, dan kumpulan tools finansial modern.</p>
        <div class="btn-group">
            <a href="https://indoinves.github.io/" class="btn">Buka Website Utama</a>
            <a href="https://indoinves.github.io/tools/investasi.html" class="btn btn-secondary">Jelajahi Tools</a>
        </div>
        <footer>&copy; ${new Date().getFullYear()} IndoInves. All rights reserved.</footer>
    </div>
</body>
</html>`;

app.get('/', (req, res) => {
    res.send(htmlTemplate);
});

app.listen(PORT, () => {
    console.log(`Server Express berjalan di http://localhost:${PORT}`);
});
