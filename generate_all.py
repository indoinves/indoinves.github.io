import os

categories = [
    "macro-economy", "explainers", "manufacturing", "property", "health", 
    "education", "lifestyle", "hospitality", "tech-media", "smes", "luxury", 
    "whos-who", "international", "local-resources", "politics", "culture", 
    "science", "public-policy", "business-news", "sports", "arts", 
    "celebrities", "automotive", "commentary", "interview"
]

tool_categories = [
    "tools/saham", "tools/kripto", "tools/investasi", "tools/banklocator", 
    "tools/website", "tools/kalkulator", "tools/analisis", "tools/portofolio", 
    "tools/pajak", "tools/budgeting", "tools/forex", "tools/komoditas", 
    "tools/properti", "tools/pensiun", "tools/akuntansi", "tools/emiten", 
    "tools/fintech", "tools/ekuitas"
]

html_template = """<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Indoinves - Global Market, Finance, Macro Economy & Business News</title>
    <meta name="description" content="Indoinves delivers authoritative insights on Market & Finance, Macro Economy, Business News, Technology, Real Estate, and Global Politics." />
    <meta name="keywords" content="Indoinves, Business News, Macro Economy, Market & Finance, Tech, Global Economy" />
    <link rel="manifest" href="https://indoinves.github.io/manifest.json" />
    <link rel="icon" href="https://indoinves.github.io/indoinves.png" type="image/png" />
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8423475960451668" crossorigin="anonymous"></script>
    <meta name="google-adsense-account" content="ca-pub-8423475960451668">
    <meta name="google-site-verification" content="U1VAgdRlZJWlLXGlGnsAGbZA1TVBp2DG0c6XzQJNonY" />
    
    <link rel="icon" type="image/png" href="https://indoinves.github.io/img/indoinves.png">
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
        <nav><a href="https://indoinves.github.io/">Home</a> | <a href="https://indoinves.github.io/contact.html">Kontak</a></nav>
    </header>
    <main>
        <article>
            <h2>Artikel Otomatis Indoinves</h2>
            <img src="https://indoinves.github.io/img/indoinves.jpg" alt="Indoinves" width="600" height="400">
            <p>Selamat datang di pusat informasi eksklusif IndoInves.</p>
        </article>
    </main>
    <footer><p>&copy; 2026 IndoInves.</p></footer>
</body>
</html>
"""

# Generate Kategori Utama
for cat in categories:
    cat_dir = os.path.join(".", cat)
    os.makedirs(cat_dir, exist_ok=True)
    for i in range(10): # Buat 10 halaman per kategori dulu agar cepat
        file_path = os.path.join(cat_dir, f"artikel-{i+1}.html")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html_template)

# Generate Tools
for tool_cat in tool_categories:
    cat_dir = os.path.join(".", tool_cat)
    os.makedirs(cat_dir, exist_ok=True)
    for i in range(10):
        file_path = os.path.join(cat_dir, f"utility-{i+1}.html")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html_template)

print("Berhasil membuat folder dan file!")
