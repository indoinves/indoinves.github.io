import os
import plugin
import templates

# Daftar Kategori Artikel & Tools
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
urls_for_sitemap = [
    f"{BASE_URL}/", 
    f"{BASE_URL}/contact.html", 
    f"{BASE_URL}/sitemap.html", 
    f"{BASE_URL}/store/plugins.html", 
    f"{BASE_URL}/store/templates.html"
]

# 1. Jalankan fungsi pembuat Store (Plugin & Templates)
try:
    plugin.generate_plugin_store()
    templates.generate_templates_store()
except Exception as e:
    print(f"Catatan modul store: {e}")

# Buat file index.html untuk folder store utama
store_dir = os.path.join(".", "store")
os.makedirs(store_dir, exist_ok=True)
with open(os.path.join(store_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write("""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Indoinves Store Directory - Indoinves Global Intelligence</title>
    <meta name="description" content="Pusat unduhan plugin dan 17.000+ templates profesional." />
    <link rel="icon" type="image/png" href="https://indoinves.github.io/img/indoinves.png">
<!-- Google AdSense & Verification Meta Tags -->
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8423475960451668" crossorigin="anonymous"></script>
    <meta name="google-adsense-account" content="ca-pub-8423475960451668">
    <meta name="google-site-verification" content="U1VAgdRlZJWlLXGlGnsAGbZA1TVBp2DG0c6XzQJNonY" />
    
    <!-- Favicon & Manifest -->
    <link rel="icon" type="image/png" href="https://indoinves.github.io/img/indoinves.png">
    <link rel="icon" href="https://indoinves.github.io/indoinves.png" type="image/png" />
    <link rel="manifest" href="https://indoinves.github.io/manifest.json" />

</head>
<body>
    <header style="background: #111; color: #fff; padding: 20px; text-align: center;">
        <h1>Indoinves Store Directory</h1>
        <p>Direktori Resmi Indoinves Global Intelligence</p>
    </header>
    <div style="max-width: 800px; margin: 40px auto; padding: 20px; background: #fff; box-shadow: 0 0 10px rgba(0,0,0,0.05); border-radius: 6px;">
        <h2>Selamat Datang di Pusat Toko & Direktori</h2>
        <p>Pusat unduhan plugin dan 17.000+ templates profesional.</p>
        <ul>
            <li><a href="https://indoinves.github.io/">Kembali ke Beranda Utama (Home)</a></li>
            <li><a href="https://indoinves.github.io/store/plugins.html">Kunjungi Toko 1.000+ Plugins</a></li>
            <li><a href="https://indoinves.github.io/store/templates.html">Kunjungi Toko 17.000+ Templates</a></li>
            <li><a href="https://indoinves.github.io/sitemap.html">Lihat Peta Situs (Sitemap)</a></li>
        </ul>
    </div>
</body>
</html>""")
urls_for_sitemap.append(f"{BASE_URL}/store/")


# Template untuk index direktori agar tidak 404
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
    </style><!-- Google AdSense & Verification Meta Tags -->
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8423475960451668" crossorigin="anonymous"></script>
    <meta name="google-adsense-account" content="ca-pub-8423475960451668">
    <meta name="google-site-verification" content="U1VAgdRlZJWlLXGlGnsAGbZA1TVBp2DG0c6XzQJNonY" />
    
    <!-- Favicon & Manifest -->
    <link rel="icon" type="image/png" href="https://indoinves.github.io/img/indoinves.png">
    <link rel="icon" href="https://indoinves.github.io/indoinves.png" type="image/png" />
    <link rel="manifest" href="https://indoinves.github.io/manifest.json" />

</head>
<body>
    <header>
        <h1>{title}</h1>
        <p>Direktori Resmi Indoinves Global Intelligence</p>
    </header>
    <div class="container">
        <h2>Selamat Datang di Pusat Informasi Direktori Ini</h2>
        <p>{description}</p>
        <p>Silakan akses halaman utama atau direktori terkait melalui tautan berikut:</p>
        <ul>
            <li><a href="{BASE_URL}/">Kembali ke Beranda Utama (Home)</a></li>
            <li><a href="{BASE_URL}/store/plugins.html">Kunjungi Toko 1.000+ Plugins</a></li>
            <li><a href="{BASE_URL}/store/templates.html">Kunjungi Toko 17.000+ Templates</a></li>
            <li><a href="{BASE_URL}/sitemap.html">Lihat Peta Situs (Sitemap)</a></li>
        </ul>
    </div>
<!-- Footer -->
    <footer>
        <div class="footer-links">
            <a href="https://indoinves.github.io/">Home</a>
            <a href="https://indoinves.github.io/about.html">About Us</a>
            <a href="https://indoinves.github.io/contact.html">Contact Us</a>
            <a href="https://indoinves.github.io/privacy.html">Privacy Policy</a>
            <a href="https://indoinves.github.io/sitemap.html">Sitemap</a>
            <a href="https://indoinves.github.io/disclaimer.html">Disclaimer</a>
            <a href="https://indoinves.github.io/terms.html">Terms on Conditional License</a>
        </div>
        <p>&copy; 2026 Indoinves. All Rights Reserved. Global Intelligence Report & Explorer Tools.</p>
    </footer>

</body>
</html>
"""


# Fungsi generator konten artikel masif berstruktur SEO tinggi
def generate_long_content(category_name, index):
    paragraphs = []
    for chapter in range(1, 31):
        chapter_title = f"Bab {chapter}: Analisis Komprehensif dan Proyeksi Strategis {category_name.replace('-', ' ').title()} Bagian {index}.{chapter}"
        body_text = f"""
        Dalam era globalisasi modern, sektor {category_name} menghadapi transformasi masif yang belum pernah terjadi sebelumnya. 
        Bab ini mengupas tuntas seluruh variabel fundamental, mulai dari regulasi makroekonomi, penetrasi teknologi digital, hingga mitigasi risiko fiskal jangka panjang. 
        Para pelaku industri, investor institusional, dan pembuat kebijakan dituntut untuk memahami pergeseran paradigma ini agar tetap kompetitif di kancah internasional. 
        Analisis mendalam menunjukkan bahwa efisiensi operasional dan adaptasi terhadap tren global menjadi penentu utama keberhasilan finansial korporasi besar maupun usaha skala menengah.
        
        <br><br>
        
        Eksplorasi lanjutan terhadap {category_name} memperlihatkan adanya korelasi kuat antara stabilitas geopolitik dan arus investasi asing langsung (FDI). 
        Berdasarkan data historis dekade terakhir, ketahanan sektor ini sangat bergantung pada fleksibilitas rantai pasok global serta kesiapan infrastruktur digital pendukung. 
        Indoinves secara berkala memantau indikator-indikator krusial ini untuk menyajikan panduan akurat bagi para eksekutif dan analis pasar. 
        Melalui pendekatan multidisiplin, pemangku kepentingan dapat mengantisipasi volatilitas pasar serta mengidentifikasi peluang pertumbuhan baru yang belum tergarap secara optimal di berbagai kawasan strategis dunia.
        """
        paragraphs.append(f"<h2>{chapter_title}</h2><p>{body_text}</p>")
        
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
                        <td>Espansi Kuat</td>
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


# Template HTML Artikel & Utility Utama
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

    <header>
        <div class="header-container">
            <a href="{BASE_URL}/" class="logo-area">
                <img src="{BASE_URL}/img/indoinves.png" alt="Indoinves Logo" onerror="this.src='{BASE_URL}/img/indoinves.jpg'">
                <span>Indoinves Global Intelligence</span>
            </a>
            <div style="font-size: 0.9rem; font-weight: bold; color: #4da6ff;">Laporan Eksklusif • Analisis Mendalam</div>
        </div>
    </header>
    
    <div class="nav-slider-container">
        <div class="nav-slider">
            <a href="{BASE_URL}/">Home</a>
            <a href="{BASE_URL}/macro-economy/artikel-1.html">Macro Economy</a>
            <a href="{BASE_URL}/property/artikel-1.html">Property</a>
            <a href="{BASE_URL}/tech-media/artikel-1.html">Tech & Media</a>
            <a href="{BASE_URL}/tools/saham/utility-1.html">Saham Tools</a>
            <a href="{BASE_URL}/tools/kripto/utility-1.html">Kripto Tools</a>
            <a href="{BASE_URL}/tools/banklocator/utility-1.html">Bank Locator</a>
            <a href="{BASE_URL}/business-news/artikel-1.html">Business News</a>
            <a href="{BASE_URL}/international/artikel-1.html">International</a>
            <a href="{BASE_URL}/contact.html">Contact Us</a>
        </div>
    </div>

    <div class="container">
        <main>
            <article>
                <h1>{title}</h1>
                <p><em>Oleh Tim Riset Global Indoinves | Dokumen Resmi Sektor: {category_name.replace('-', ' ').title()}</em></p>
                <img src="{BASE_URL}/img/indoinves.jpg" alt="{title}" style="width:100%; height:auto; border-radius:6px; margin: 15px 0;">
                
                {long_article_content}

                <h3>7 Tautan Internal Terkait (Internal Links)</h3>
                <ul>
                    <li><a href="{BASE_URL}/">Pusat Direktori Utama Indoinves</a></li>
                    <li><a href="{BASE_URL}/macro-economy/artikel-1.html">Analisis Makro Ekonomi Global</a></li>
                    <li><a href="{BASE_URL}/property/artikel-1.html">Laporan Properti dan Real Estate</a></li>
                    <li><a href="{BASE_URL}/tools/saham/utility-1.html">Kalkulator dan Analisis Saham</a></li>
                    <li><a href="{BASE_URL}/tools/banklocator/utility-1.html">Direktori Pemetaan Bank Dunia</a></li>
                    <li><a href="{BASE_URL}/business-news/artikel-1.html">Kabar Berita Bisnis Internasional</a></li>
                    <li><a href="{BASE_URL}/contact.html">Kontak Resmi Layanan Redaksi</a></li>
                </ul>

                <h3>7 Tautan Eksternal Otoritatif (External Links)</h3>
                <ul>
                    <li><a href="https://www.reuters.com" target="_blank" rel="noopener">Reuters Global Financial Markets</a></li>
                    <li><a href="https://www.bloomberg.com" target="_blank" rel="noopener">Bloomberg Business & Economics</a></li>
                    <li><a href="https://www.wsj.com" target="_blank" rel="noopener">The Wall Street Journal Intelligence</a></li>
                    <li><a href="https://www.ft.com" target="_blank" rel="noopener">Financial Times Global Desk</a></li>
                    <li><a href="https://www.cnbc.com" target="_blank" rel="noopener">CNBC International Markets</a></li>
                    <li><a href="https://www.imf.org" target="_blank" rel="noopener">International Monetary Fund (IMF)</a></li>
                    <li><a href="https://www.worldbank.org" target="_blank" rel="noopener">World Bank Open Data & Reports</a></li>
                </ul>

                <div class="social-share">
                    <span>Sebarkan Laporan Ini:</span>
                    <a href="https://facebook.com/sharer/sharer.php?u={BASE_URL}/" target="_blank">Facebook</a>
                    <a href="https://twitter.com/intent/tweet?text=Baca%20laporan%20eksklusif%20di%20Indoinves" target="_blank">Twitter</a>
                    <a href="https://www.linkedin.com/shareArticle?mini=true&url={BASE_URL}/" target="_blank">LinkedIn</a>
                    <a href="https://api.whatsapp.com/send?text=Kunjungi%20laporan%20lengkap%20Indoinves" target="_blank">WhatsApp</a>
                </div>

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

        <aside>
            <div style="margin-bottom: 30px;">
                <h3 style="border-bottom: 2px solid #0056b3; padding-bottom: 5px; font-size: 1.1rem;">🔥 7 Artikel Populer</h3>
                <ul style="padding-left: 18px; font-size: 0.9rem; line-height: 1.8;">
                    <li><a href="{BASE_URL}/macro-economy/artikel-1.html" style="color:#0056b3; text-decoration:none;">Proyeksi Makro Ekonomi Global</a></li>
                    <li><a href="{BASE_URL}/property/artikel-1.html" style="color:#0056b3; text-decoration:none;">Eksklusif: Real Estate Komersial</a></li>
                    <li><a href="{BASE_URL}/tech-media/artikel-1.html" style="color:#0056b3; text-decoration:none;">Transformasi Digital Finansial</a></li>
                    <li><a href="{BASE_URL}/tools/saham/utility-1.html" style="color:#0056b3; text-decoration:none;">Valuasi Saham Blue Chip Dunia</a></li>
                    <li><a href="{BASE_URL}/business-news/artikel-1.html" style="color:#0056b3; text-decoration:none;">Megamerger Korporasi Global</a></li>
                    <li><a href="{BASE_URL}/international/artikel-1.html" style="color:#0056b3; text-decoration:none;">Dinamika Suku Bunga Bank Sentral</a></li>
                    <li><a href="{BASE_URL}/tools/banklocator/utility-1.html" style="color:#0056b3; text-decoration:none;">Direktori Bank Multinasional</a></li>
                </ul>
            </div>

            <div>
                <h3 style="border-bottom: 2px solid #333; padding-bottom: 5px; font-size: 1.1rem;">📂 7 Arsip Artikel</h3>
                <ul style="padding-left: 18px; font-size: 0.9rem; line-height: 1.8;">
                    <li><a href="{BASE_URL}/macro-economy/artikel-2.html" style="color:#333; text-decoration:none;">Arsip Edisi Triwulan I</a></li>
                    <li><a href="{BASE_URL}/property/artikel-2.html" style="color:#333; text-decoration:none;">Arsip Tinjauan Properti Lama</a></li>
                    <li><a href="{BASE_URL}/tech-media/artikel-2.html" style="color:#333; text-decoration:none;">Arsip Teknologi & Media</a></li>
                    <li><a href="{BASE_URL}/tools/saham/utility-2.html" style="color:#333; text-decoration:none;">Arsip Kalkulator Keuangan</a></li>
                    <li><a href="{BASE_URL}/business-news/artikel-2.html" style="color:#333; text-decoration:none;">Arsip Buletin Bisnis</a></li>
                    <li><a href="{BASE_URL}/international/artikel-2.html" style="color:#333; text-decoration:none;">Arsip Kebijakan Publik</a></li>
                    <li><a href="{BASE_URL}/tools/banklocator/utility-2.html" style="color:#333; text-decoration:none;">Arsip Pemetaan Perbankan</a></li>
                </ul>
            </div>
        </aside>
    </div>
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
    <footer>
        <div class="footer-links">
            <a href="{BASE_URL}/">Home</a>
            <a href="{BASE_URL}/about.html">About Us</a>
            <a href="{BASE_URL}/contact.html">Contact Us</a>
            <a href="{BASE_URL}/privacy.html">Privacy Policy</a>
            <a href="{BASE_URL}/sitemap.html">Sitemap</a>
            <a href="{BASE_URL}/disclaimer.html">Disclaimer</a>
            <a href="{BASE_URL}/terms.html">Terms on Conditional License</a>
        </div>
        <p>&copy; 2026 Indoinves. All Rights Reserved. Global Intelligence Report & Explorer Tools.</p>
    </footer>

</body>
</html>
"""


# 2. Generate Kategori Artikel dan file index.html di setiap foldernya
for cat in categories:
    cat_dir = os.path.join(".", cat)
    os.makedirs(cat_dir, exist_ok=True)
    
    # Buat index.html di folder kategori agar tidak 404
    with open(os.path.join(cat_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(get_directory_index_template(f"Kategori {cat.replace('-', ' ').title()}", f"Arsip dan laporan eksklusif untuk topik dan kategori {cat}."))
    urls_for_sitemap.append(f"{BASE_URL}/{cat}/")

    # Generate artikel di dalam kategori tersebut (10 artikel per kategori)
    for i in range(10):
        file_name = f"artikel-{i+1}.html"
        file_path = os.path.join(cat_dir, file_name)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(get_html_template(f"Laporan Eksklusif {cat.replace('-', ' ').title()} - Edisi {i+1}", cat, i+1))
        urls_for_sitemap.append(f"{BASE_URL}/{cat}/{file_name}")


# 3. Generate Tools & Utilitas beserta file index.html di setiap sub-foldernya
for tool_cat in tool_categories:
    cat_dir = os.path.join(".", tool_cat)
    os.makedirs(cat_dir, exist_ok=True)
    
    # Buat index.html di sub-folder tools agar tidak 404
    sub_name = tool_cat.split('/')[-1]
    with open(os.path.join(cat_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(get_directory_index_template(f"Tools {sub_name.title()}", f"Kumpulan perangkat dan kalkulator utilitas untuk sektor {sub_name}."))
    urls_for_sitemap.append(f"{BASE_URL}/{tool_cat}/")

    # Generate utility files di dalam folder tools (10 file per tool category)
    for i in range(10):
        file_name = f"utility-{i+1}.html"
        file_path = os.path.join(cat_dir, file_name)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(get_html_template(f"Analisis Sistem {sub_name.title()} - Utility {i+1}", sub_name, i+1))
        urls_for_sitemap.append(f"{BASE_URL}/{tool_cat}/{file_name}")


# 4. Buat File sitemap.xml Otomatis mencakup seluruh direktori dan file
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

print("Sukses! Seluruh file index.html direktori, artikel masif, tools, store, dan sitemap.xml telah berhasil dibuat.")
    
