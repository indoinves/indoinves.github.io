import os

# Coba melakukan import untuk modul tambahan (plugin & templates store) jika ada
try:
    import plugin
    import templates
    HAS_STORE_MODULES = True
except ImportError:
    HAS_STORE_MODULES = False

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

BASE_URL = "https://indoinves.github.io"

# Fungsi untuk menghasilkan teks panjang terstruktur SEO (30 Bab + Tabel Data)
def generate_long_content(category_name, index):
    paragraphs = []
    
    for chapter in range(1, 31):
        chapter_title = f"Bab {chapter}: Analisis Komprehensif dan Proyeksi Strategis {category_name.replace('-', ' ').title()} Bagian {index}.{chapter}"
        
        body_text = f"""
        Dalam era globalisasi modern, sektor {category_name.replace('-', ' ')} menghadapi transformasi masif yang belum pernah terjadi sebelumnya. 
        Bab ini mengupas tuntas seluruh variabel fundamental, mulai dari regulasi makroekonomi, penetrasi teknologi digital, hingga mitigasi risiko fiskal jangka panjang. 
        Para pelaku industri, investor institusional, dan pembuat kebijakan dituntut untuk memahami pergeseran paradigma ini agar tetap kompetitif di kancah internasional. 
        Analisis mendalam menunjukkan bahwa efisiensi operasional dan adaptasi terhadap tren global menjadi penentu utama keberhasilan finansial korporasi besar maupun usaha skala menengah.
        
        <br><br>
        
        Eksplorasi lanjutan memperlihatkan adanya korelasi kuat antara stabilitas geopolitik dan arus investasi asing langsung (FDI). 
        Berdasarkan data historis dekade terakhir, ketahanan sektor ini sangat bergantung pada fleksibilitas rantai pasok global serta kesiapan infrastruktur digital pendukung. 
        Indoinves secara berkala memantau indikator-indikator krusial ini untuk menyajikan panduan akurat bagi para eksekutif dan analis pasar. 
        Melalui pendekatan multidisiplin, pemangku kepentingan dapat mengantisipasi volatilitas pasar serta mengidentifikasi peluang pertumbuhan baru yang belum tergarap secara optimal di berbagai kawasan strategis dunia.
        """
        
        paragraphs.append(f"<h2>{chapter_title}</h2><p>{body_text}</p>")
        
        # Tambahkan tabel data setiap 5 bab sekali untuk memperkaya bobot konten
        if chapter % 5 == 0:
            table_html = f"""
            <h3>Tabel Komparasi Metrik Global - Sektor {category_name.replace('-', ' ').title()} (Fase {chapter})</h3>
            <table>
                <thead>
                    <tr>
                        <th>Indikator Utama</th>
                        <th>Kuartal I</th>
                        <th>Kuartal II</th>
                        <th>Proyeksi Akhir Tahun</th>
                        <th>Status Analisis</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Indeks Pertumbuhan Fiskal</td>
                        <td>+4.8%</td>
                        <td>+5.2%</td>
                        <td>Stabil Positif</td>
                        <td>Terverifikasi</td>
                    </tr>
                    <tr>
                        <td>Tingkat Likuiditas Pasar</td>
                        <td>High Yield</td>
                        <td>Optimum</td>
                        <td>Ekspansi Kuat</td>
                        <td>Aman</td>
                    </tr>
                    <tr>
                        <td>Mitigasi Risiko Global</td>
                        <td>Standar A</td>
                        <td>Standar A+</td>
                        <td>Fully Compliant</td>
                        <td>Optimal</td>
                    </tr>
                </tbody>
            </table>
            """
            paragraphs.append(table_html)

    return "".join(paragraphs)

# Template untuk index direktori agar terhindar dari Error 404
def get_directory_index_template(title, description):
    return f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Indoinves Global Intelligence</title>
    <meta name="description" content="{description}" />
    <link rel="icon" type="image/png" href="{BASE_URL}/img/indoinves.png">
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; margin: 0; padding: 0; background: #f9f9f9; }}
        header {{ background: #111; color: #fff; padding: 20px; text-align: center; }}
        .container {{ max-width: 800px; margin: 40px auto; padding: 20px; background: #fff; box-shadow: 0 0 10px rgba(0,0,0,0.05); border-radius: 6px; }}
        h1 {{ color: #111; }}
        a {{ color: #0056b3; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
        footer {{ background: #111; color: #fff; text-align: center; padding: 20px; margin-top: 40px; }}
    </style>
</head>
<body>
    <header>
        <h1>{title}</h1>
        <p>Direktori Resmi Indoinves Global Intelligence</p>
    </header>
    <div class="container">
        <h2>Selamat Datang di Pusat Informasi Direktori Ini</h2>
        <p>{description}</p>
        <p>Silakan kembali ke halaman utama atau akses daftar artikel dan perangkat di bawah:</p>
        <ul>
            <li><a href="{BASE_URL}/">Kembali ke Beranda Utama (Home)</a></li>
            {f'<li><a href="{BASE_URL}/store/plugins.html">Kunjungi Toko 1.000+ Plugins</a></li>' if HAS_STORE_MODULES else ''}
            {f'<li><a href="{BASE_URL}/store/templates.html">Kunjungi Toko 17.000+ Templates</a></li>' if HAS_STORE_MODULES else ''}
        </ul>
    </div>
    <footer>
        <p>&copy; 2026 Indoinves. All Rights Reserved.</p>
    </footer>
</body>
</html>
"""

# Template Utama Artikel / Utility (Full Layout dengan Integrasi Konten Masif)
def get_html_template(title, category_name, index):
    long_article_content = generate_long_content(category_name, index)
    
    return f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Indoinves Global Intelligence</title>
    <meta name="description" content="Laporan lengkap dan eksklusif mengenai {category_name}, analisis mendalam pasar global, investasi, dan makroekonomi bersama Indoinves." />
    <meta name="keywords" content="Indoinves, {category_name}, Business News, Macro Economy, Market & Finance, Global Report" />
    
    <!-- Google AdSense & Verification Meta Tags -->
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8423475960451668" crossorigin="anonymous"></script>
    <meta name="google-adsense-account" content="ca-pub-8423475960451668">
    <meta name="google-site-verification" content="U1VAgdRlZJWlLXGlGnsAGbZA1TVBp2DG0c6XzQJNonY" />
    
    <!-- Favicon & Manifest -->
    <link rel="icon" type="image/png" href="{BASE_URL}/img/indoinves.png">
    <link rel="manifest" href="{BASE_URL}/manifest.json" />

    <style>
        :root {{ --primary: #0056b3; --bg: #f9f9f9; --text: #333; }}
        body {{ font-family: Arial, sans-serif; line-height: 1.8; color: var(--text); margin: 0; padding: 0; background: var(--bg); }}
        header {{ background: #111; color: #fff; padding: 15px 20px; }}
        .header-container {{ display: flex; justify-content: space-between; align-items: center; max-width: 1200px; margin: 0 auto; flex-wrap: wrap; }}
        .logo-area {{ display: flex; align-items: center; text-decoration: none; color: #fff; }}
        .logo-area img {{ width: 40px; height: 40px; margin-right: 10px; }}
        .logo-area span {{ font-size: 1.2rem; font-weight: bold; }}
        .nav-slider-container {{ background: #222; overflow-x: auto; white-space: nowrap; padding: 10px 20px; }}
        .nav-slider a {{ color: #4da6ff; text-decoration: none; margin-right: 20px; font-size: 0.95rem; }}
        .nav-slider a:hover {{ text-decoration: underline; }}
        .container {{ display: flex; max-width: 1200px; margin: 20px auto; padding: 0 15px; gap: 30px; }}
        main {{ flex: 3; background: #fff; padding: 40px; box-shadow: 0 0 10px rgba(0,0,0,0.05); }}
        aside {{ flex: 1; background: #fff; padding: 20px; box-shadow: 0 0 10px rgba(0,0,0,0.05); height: fit-content; }}
        h1, h2, h3 {{ color: #111; margin-top: 30px; }}
        table {{ width: 100%; border-collapse: collapse; margin: 20px 0; }}
        table, th, td {{ border: 1px solid #ddd; padding: 12px; text-align: left; }}
        th {{ background: #f4f4f4; }}
        .contact-form {{ background: #f9f9f9; padding: 25px; margin-top: 30px; border: 1px solid #ddd; }}
        .contact-form input, .contact-form textarea {{ width: 100%; padding: 12px; margin: 10px 0; border: 1px solid #ccc; box-sizing: border-box; }}
        .social-share {{ margin: 25px 0; font-weight: bold; }}
        .social-share a {{ margin-right: 15px; color: #0056b3; text-decoration: none; }}
        footer {{ background: #111; color: #fff; text-align: center; padding: 30px 20px; margin-top: 40px; }}
        .footer-links {{ margin-bottom: 15px; }}
        .footer-links a {{ color: #4da6ff; text-decoration: none; margin: 0 10px; font-size: 0.9rem; }}
        @media(max-width: 768px) {{ .container {{ flex-direction: column; }} }}
    </style>
</head>
<body>

    <!-- Header -->
    <header>
        <div class="header-container">
            <a href="{BASE_URL}/" class="logo-area">
                <img src="{BASE_URL}/img/indoinves.png" alt="Indoinves Logo" onerror="this.src='{BASE_URL}/img/indoinves.jpg'">
                <span>Indoinves Global Intelligence</span>
            </a>
            <div style="font-size: 0.9rem; font-weight: bold; color: #4da6ff;">Laporan Eksklusif • Analisis Mendalam</div>
        </div>
    </header>
    
    <!-- Navigation Slider -->
    <div class="nav-slider-container">
        <div class="nav-slider">
            <a href="{BASE_URL}/">Home</a>
            <a href="{BASE_URL}/macro-economy/artikel-1.html">Macro Economy</a>
            <a href="{BASE_URL}/property/artikel-1.html">Property</a>
            <a href="{BASE_URL}/tech-media/artikel-1.html">Tech & Media</a>
            <a href="{BASE_URL}/tools/saham/utility-1.html">Saham Tools</a>
            <a href="{BASE_URL}/tools/kripto/utility-1.html">Kripto Tools</a>
            <a href="{BASE_URL}/business-news/artikel-1.html">Business News</a>
            <a href="{BASE_URL}/international/artikel-1.html">International</a>
            <a href="{BASE_URL}/contact.html">Contact Us</a>
        </div>
    </div>

    <!-- Container Utama & Sidebar -->
    <div class="container">
        <main>
            <article>
                <h1>{title}</h1>
                <p><em>Oleh Tim Riset Global Indoinves | Dokumen Resmi Sektor: {category_name.replace('-', ' ').title()}</em></p>
                <img src="{BASE_URL}/img/indoinves.jpg" alt="{title}" style="width:100%; height:auto; border-radius:6px; margin: 15px 0;">
                
                <!-- Unit Iklan Banner AdSense -->
                <div style="margin: 25px 0;">
                    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8423475960451668" crossorigin="anonymous"></script>
                    <ins class="adsbygoogle"
                         style="display:block"
                         data-ad-client="ca-pub-8423475960451668"
                         data-ad-slot="6147545291"
                         data-ad-format="auto"
                         data-full-width-responsive="true"></ins>
                    <script>
                         (adsbygoogle = window.adsbygoogle || []).push({{}});
                    </script>
                </div>

                <!-- ISI ARTIKEL MASIF -->
                {long_article_content}

                <!-- Unit Iklan Autorelaxed AdSense -->
                <div style="margin: 25px 0;">
                    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8423475960451668" crossorigin="anonymous"></script>
                    <ins class="adsbygoogle"
                         style="display:block"
                         data-ad-format="autorelaxed"
                         data-ad-client="ca-pub-8423475960451668"
                         data-ad-slot="7183276396"></ins>
                    <script>
                         (adsbygoogle = window.adsbygoogle || []).push({{}});
                    </script>
                </div>

                <h3>Tautan Internal Terkait (Internal Links)</h3>
                <ul>
                    <li><a href="{BASE_URL}/">Pusat Direktori Utama Indoinves</a></li>
                    <li><a href="{BASE_URL}/macro-economy/artikel-1.html">Analisis Makro Ekonomi Global</a></li>
                    <li><a href="{BASE_URL}/property/artikel-1.html">Laporan Properti dan Real Estate</a></li>
                    <li><a href="{BASE_URL}/tools/saham/utility-1.html">Kalkulator dan Analisis Saham</a></li>
                    <li><a href="{BASE_URL}/business-news/artikel-1.html">Kabar Berita Bisnis Internasional</a></li>
                </ul>

                <h3>Tautan Eksternal Otoritatif (External Links)</h3>
                <ul>
                    <li><a href="https://www.reuters.com" target="_blank" rel="noopener">Reuters Global Financial Markets</a></li>
                    <li><a href="https://www.bloomberg.com" target="_blank" rel="noopener">Bloomberg Business & Economics</a></li>
                    <li><a href="https://www.imf.org" target="_blank" rel="noopener">International Monetary Fund (IMF)</a></li>
                    <li><a href="https://www.worldbank.org" target="_blank" rel="noopener">World Bank Open Data & Reports</a></li>
                </ul>

                <!-- Social Share -->
                <div class="social-share">
                    <span>Sebarkan Laporan Ini:</span>
                    <a href="https://facebook.com/sharer/sharer.php?u={BASE_URL}/" target="_blank">Facebook</a>
                    <a href="https://twitter.com/intent/tweet?text=Baca%20laporan%20eksklusif%20di%20Indoinves" target="_blank">Twitter</a>
                    <a href="https://www.linkedin.com/shareArticle?mini=true&url={BASE_URL}/" target="_blank">LinkedIn</a>
                    <a href="https://api.whatsapp.com/send?text=Kunjungi%20laporan%20lengkap%20Indoinves" target="_blank">WhatsApp</a>
                </div>

                <!-- Formulir Kontak -->
                <div class="contact-form">
                    <h3>Formulir Konsultasi Riset & Kolaborasi Redaksi</h3>
                    <form action="{BASE_URL}/contact.html" method="GET">
                        <input type="text" name="name" placeholder="Nama Lengkap Anda / Instansi" required>
                        <input type="email" name="email" placeholder="Alamat Email Korporat / Pribadi" required>
                        <textarea name="message" rows="4" placeholder="Tuliskan permintaan data spesifik atau pertanyaan Anda..." required></textarea>
                        <button type="submit" style="background:#0056b3; color:#fff; padding:12px 25px; border:none; cursor:pointer; font-weight:bold;">Kirim Permintaan</button>
                    </form>
                </div>
            </article>
        </main>

        <!-- Sidebar -->
        <aside>
            <div style="margin-bottom: 30px;">
                <h3 style="border-bottom: 2px solid #0056b3; padding-bottom: 5px; font-size: 1.1rem;">🔥 Artikel Populer</h3>
                <ul style="padding-left: 18px; font-size: 0.9rem; line-height: 1.8;">
                    <li><a href="{BASE_URL}/macro-economy/artikel-1.html" style="color:#0056b3; text-decoration:none;">Proyeksi Makro Ekonomi Global</a></li>
                    <li><a href="{BASE_URL}/property/artikel-1.html" style="color:#0056b3; text-decoration:none;">Eksklusif: Real Estate Komersial</a></li>
                    <li><a href="{BASE_URL}/tech-media/artikel-1.html" style="color:#0056b3; text-decoration:none;">Transformasi Digital Finansial</a></li>
                    <li><a href="{BASE_URL}/tools/saham/utility-1.html" style="color:#0056b3; text-decoration:none;">Valuasi Saham Blue Chip Dunia</a></li>
                </ul>
            </div>
        </aside>
    </div>

    <!-- Footer -->
    <footer>
        <div class="footer-links">
            <a href="{BASE_URL}/">Home</a>
            <a href="{BASE_URL}/contact.html">Contact Us</a>
            <a href="{BASE_URL}/sitemap.html">Sitemap</a>
        </div>
        <p>&copy; 2026 Indoinves. All Rights Reserved. Global Intelligence Report & Explorer Tools.</p>
    </footer>

</body>
</html>
"""

# Inisialisasi Daftar URL Sitemap
urls_for_sitemap = [
    f"{BASE_URL}/", 
    f"{BASE_URL}/contact.html"
]

# 1. Generate Toko (Jika plugin & templates tersedia)
if HAS_STORE_MODULES:
    plugin.generate_plugin_store()
    templates.generate_templates_store()
    
    store_dir = os.path.join(".", "store")
    os.makedirs(store_dir, exist_ok=True)
    with open(os.path.join(store_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(get_directory_index_template("Indoinves Store Directory", "Pusat unduhan plugin dan templates profesional."))
    urls_for_sitemap.append(f"{BASE_URL}/store/")

# 2. Proses Generate Kategori Utama Artikel (Total 10 file per kategori)
for cat in categories:
    cat_dir = os.path.join(".", cat)
    os.makedirs(cat_dir, exist_ok=True)
    
    # Buat index.html di setiap direktori kategori untuk mencegah 404
    with open(os.path.join(cat_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(get_directory_index_template(f"Kategori {cat.replace('-', ' ').title()}", f"Arsip dan laporan eksklusif untuk kategori {cat}."))
    urls_for_sitemap.append(f"{BASE_URL}/{cat}/")

    for i in range(10):
        file_name = f"artikel-{i+1}.html"
        file_path = os.path.join(cat_dir, file_name)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(get_html_template(f"Laporan Eksklusif {cat.replace('-', ' ').title()} - Edisi {i+1}", cat, i+1))
        urls_for_sitemap.append(f"{BASE_URL}/{cat}/{file_name}")

# 3. Proses Generate Tools (Total 10 file per tool category)
for tool_cat in tool_categories:
    cat_dir = os.path.join(".", tool_cat)
    os.makedirs(cat_dir, exist_ok=True)
    
    # Buat index.html di setiap subfolder tools
    tool_name_clean = tool_cat.split('/')[-1]
    with open(os.path.join(cat_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(get_directory_index_template(f"Tools {tool_name_clean.title()}", f"Kumpulan perangkat dan kalkulator utilitas untuk {tool_name_clean}."))
    urls_for_sitemap.append(f"{BASE_URL}/{tool_cat}/")

    for i in range(10):
        file_name = f"utility-{i+1}.html"
        file_path = os.path.join(cat_dir, file_name)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(get_html_template(f"Analisis Sistem {tool_name_clean.title()} - Utility {i+1}", tool_name_clean, i+1))
        urls_for_sitemap.append(f"{BASE_URL}/{tool_cat}/{file_name}")

# 4. Buat File sitemap.xml Secara Otomatis
sitemap_content = ['<?xml version="1.0" encoding="UTF-8"?>']
sitemap_content.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

for url in urls_for_sitemap:
    sitemap_content.append("  <url>")
    sitemap_content.append(f"    <loc>{url}</loc>")
    sitemap_content.append("    <changefreq>weekly</changefreq>")
    sitemap_content.append("    <priority>0.8</priority>")
    sitemap_content.append("  </url>")

sitemap_content.append("</urlset>")

with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write("\n".join(sitemap_content))

print("Generator file HTML, direktori indeks, dan sitemap.xml berhasil dijalankan tanpa celah!")
