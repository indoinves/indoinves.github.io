import os

categories = [
    "macro-economy", "explainers", "manufacturing", "property", "health", 
    "education", "lifestyle", "hospitality", "tech-media", "smes", "luxury", 
    "whos-who", "international", "local-resources", "politics", "culture", 
    "science", "public-policy", "business-news", "sports", "arts", 
    "celebrities", "automotive", "commentary", "interview"
]

pages = ["desain", "investasi", "keuntungan"]

html_template = """<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Indoinves - Global Market, Finance, Macro Economy & Business News</title>
    <meta name="description" content="Indoinves delivers authoritative insights on Market & Finance, Macro Economy, Business News, Technology, Real Estate, and Global Politics." />
    <meta name="keywords" content="Indoinves, Business News, Macro Economy, Market & Finance, Tech, Global Economy" />
    
    <!-- Open Graph Meta Tags -->
    <meta property="og:title" content="Indoinves - Global Market, Finance & Business News" />
    <meta property="og:description" content="Get the latest updates on Macro Economy, Financial Markets, Technology, and Business News worldwide." />
    <meta property="og:image" content="https://indoinves.github.io/indoinves.jpg" />
    <meta property="og:url" content="https://indoinves.github.io/" />
    <meta property="og:type" content="website" />
    
    <!-- Manifest JSON Link -->
    <link rel="manifest" href="https://indoinves.github.io/manifest.json" />
    
    <!-- Favicon -->
    <link rel="icon" href="https://indoinves.github.io/indoinves.png" type="image/png" />
    
    <!-- Schema JSON-LD -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "NewsMediaOrganization",
      "name": "Indoinves",
      "url": "https://indoinves.github.io/",
      "logo": {
        "@type": "ImageObject",
        "url": "https://indoinves.github.io/indoinves.png"
      },
      "sameAs": [
        "https://facebook.com/indoinves",
        "https://twitter.com/indoinves",
        "https://linkedin.com/company/indoinves"
      ]
    }
    </script>
</head>
<body>
    <header>
        <h1>IndoInves Platform</h1>
        <nav>
            <a href="https://indoinves.github.io/">Home</a> | 
            <a href="https://indoinves.github.io/forum.html">Forum</a> | 
            <a href="https://indoinves.github.io/contact.html">Kontak</a>
        </nav>
    </header>
    
    <main>
        <article>
            <h2>Panduan Komprehensif dan Analisis Mendalam</h2>
            <img src="https://indoinves.github.io/img/indoinves.jpg" alt="Ilustrasi Finansial Global IndoInves" width="600" height="400">
            <p>Selamat datang di pusat informasi eksklusif IndoInves. Artikel ini mengupas tuntas berbagai aspek strategis untuk mendukung keputusan finansial dan investasi Anda.</p>
            
            <h3>1. Pengantar dan Tren Industri</h3>
            <p>Analisis pasar global menunjukkan perubahan dinamis yang menuntut pemahaman mendalam terkait instrumen keuangan modern.</p>
            
            <h3>2. Tabel Ringkasan Metrik Utama</h3>
            <table border="1" cellpadding="8" cellspacing="0">
                <thead>
                    <tr>
                        <th>Komponen</th>
                        <th>Proyeksi</th>
                        <th>Tingkat Risiko</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Analisis Fundamental</td>
                        <td>Stabil</td>
                        <td>Rendah-Menengah</td>
                    </tr>
                    <tr>
                        <td>Valuasi Aset</td>
                        <td>Tumbuh</td>
                        <td>Menengah</td>
                    </tr>
                </tbody>
            </table>
            
            <h3>3. Pertanyaan yang Sering Diajukan (FAQ)</h3>
            <p><strong>Q: Apakah analisis ini dapat diakses secara gratis?</strong><br>A: Ya, seluruh rubrik dan riset di IndoInves dapat diakses tanpa biaya.</p>
        </article>
    </main>

    <footer>
        <p>&copy; 2026 IndoInves. Hak Cipta Dilindungi Undang-Undang.</p>
    </footer>
</body>
</html>
"""

for cat in categories:
    cat_dir = os.path.join(".", cat)
    os.makedirs(cat_dir, exist_ok=True)
    for p in pages:
        file_path = os.path.join(cat_dir, f"{p}.html")
        with open(file_path, "w", encoding="utf-8") as f:
        	f.write(html_template)

print("Semua direktori dan file halaman berhasil dibuat secara otomatis!")
