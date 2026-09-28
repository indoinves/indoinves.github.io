import os

# Daftar kategori direktori yang sesuai dengan menu navbar Indoinves
DIRECTORIES = [
    "market/stocks",
    "market/crypto",
    "market/forex",
    "macro-economy",
    "explainers",
    "manufacturing",
    "property",
    "health",
    "education",
    "lifestyle",
    "hospitality",
    "tech-media",
    "smes",
    "luxury",
    "whos-who",
    "intl/americas",
    "intl/europe",
    "intl/asia",
    "local-resources",
    "politics",
    "culture",
    "science",
    "public-policy",
    "business-news",
    "sports",
    "arts",
    "celebrities",
    "automotive",
    "commentary",
    "interview"
]

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="id">
<head>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8423475960451668" crossorigin="anonymous"></script>
    <meta name="google-adsense-account" content="ca-pub-8423475960451668">
    <meta name="google-site-verification" content="U1VAgdRlZJWlLXGlGnsAGbZA1TVBp2DG0c6XzQJNonY" />
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{title} - Indoinves</title>
    <meta name="description" content="{description}" />
    <meta name="keywords" content="Indoinves, {category_name}, Business News, Macro Economy, Market & Finance" />
    
    <!-- Open Graph Meta Tags -->
    <meta property="og:title" content="{title} - Indoinves" />
    <meta property="og:description" content="{description}" />
    <meta property="og:image" content="https://indoinves.github.io/indoinves.jpg" />
    <meta property="og:url" content="https://indoinves.github.io/{file_url}" />
    <meta property="og:type" content="article" />

    <!-- Favicon -->
    <link rel="icon" href="https://indoinves.github.io/indoinves.png" type="image/png" />

    <!-- Schema JSON-LD -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "NewsArticle",
      "headline": "{title}",
      "image": ["https://indoinves.github.io/indoinves.jpg"],
      "datePublished": "2026-06-01T08:00:00+07:00",
      "author": {{
        "@type": "Organization",
        "name": "Indoinves Editorial Team"
      }},
      "publisher": {{
        "@type": "Organization",
        "name": "Indoinves",
        "logo": {{
          "@type": "ImageObject",
          "url": "https://indoinves.github.io/indoinves.png"
        }}
      }}
    }}
    </script>

    <style>
        :root {{
            --primary-color: #0b1f33;
            --secondary-color: #16324f;
            --accent-color: #1e824c;
            --header-bg: #ffffff;
            --text-color: #2b2b2b;
            --bg-light: #f4f6f8;
            --border-color: #e2e8f0;
            --white: #ffffff;
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }}
        body {{ color: var(--text-color); background-color: var(--bg-light); line-height: 1.6; }}
        
        /* Header */
        header {{ background: var(--header-bg); border-bottom: 1px solid var(--border-color); position: sticky; top: 0; z-index: 1000; box-shadow: 0 1px 3px rgba(0,0,0,0.05); }}
        .header-container {{ max-width: 1200px; margin: 0 auto; padding: 15px 20px; display: flex; justify-content: space-between; align-items: center; }}
        .logo-container img {{ height: 42px; display: block; }}
        .search-box form input {{ padding: 9px 14px; border: 1px solid var(--border-color); border-radius: 6px; font-size: 13px; width: 240px; outline: none; transition: border 0.2s; }}
        .search-box form input:focus {{ border-color: var(--accent-color); }}

        /* Responsive Navigation & Dropdown Styling */
        nav {{ background: var(--primary-color); color: var(--white); position: relative; box-shadow: inset 0 -2px 0 rgba(0,0,0,0.15); }}
        .nav-wrap {{ max-width: 1200px; margin: 0 auto; display: flex; justify-content: space-between; align-items: center; padding: 0 15px; }}
        
        .nav-container {{ display: flex; flex-wrap: wrap; list-style: none; margin: 0; padding: 0; }}
        .nav-container li {{ position: relative; }}
        .nav-container li a {{ display: block; color: #e2e8f0; padding: 12px 14px; text-decoration: none; font-size: 13.5px; font-weight: 500; transition: background 0.2s, color 0.2s; white-space: nowrap; }}
        .nav-container li a:hover, .dropdown:hover > a {{ background: var(--secondary-color); color: var(--white); }}
        
        /* Dropdown content */
        .dropdown-content {{ display: none; position: absolute; background: var(--white); min-width: 200px; box-shadow: 0px 10px 25px rgba(0,0,0,0.15); z-index: 999; top: 100%; left: 0; border-radius: 0 0 6px 6px; overflow: hidden; border-top: 3px solid var(--accent-color); }}
        .dropdown-content a {{ color: var(--text-color) !important; padding: 11px 16px; border-bottom: 1px solid #f1f5f9; font-size: 13px; }}
        .dropdown-content a:hover {{ background: #f8fafc; color: var(--accent-color) !important; padding-left: 20px; }}
        .dropdown:hover .dropdown-content {{ display: block; }}

        /* Mobile Menu Toggle Button */
        .menu-toggle {{ display: none; background: none; border: none; color: var(--white); font-size: 24px; cursor: pointer; padding: 8px; }}

        @media(max-width: 1024px) {{
            .menu-toggle {{ display: block; }}
            .nav-wrap {{ flex-direction: column; align-items: flex-start; padding: 10px 15px; }}
            .nav-container {{ display: none; width: 100%; flex-direction: column; padding-bottom: 10px; }}
            .nav-container.active {{ display: flex; }}
            .nav-container li {{ width: 100%; border-top: 1px solid rgba(255,255,255,0.08); }}
            .dropdown-content {{ position: static; box-shadow: none; background: rgba(0,0,0,0.15); border-top: none; }}
            .dropdown-content a {{ color: #cbd5e1 !important; padding-left: 25px; }}
            .dropdown-content a:hover {{ background: rgba(0,0,0,0.25); color: #fff !important; }}
        }}

        /* Layout Grid */
        .main-layout {{ max-width: 1200px; margin: 25px auto; display: grid; grid-template-columns: 2.5fr 1fr; gap: 30px; padding: 0 20px; }}
        @media(max-width: 900px) {{ .main-layout {{ grid-template-columns: 1fr; }} }}

        /* Content Styles */
        .content-area {{ background: var(--white); padding: 30px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.05); }}
        h1 {{ font-size: 28px; color: var(--primary-color); margin-bottom: 15px; line-height: 1.3; }}
        .lead-text {{ font-size: 16px; font-weight: 600; color: #555; margin-bottom: 20px; }}
        
        /* Table of Contents */
        .toc {{ background: #f0f4f8; padding: 15px 20px; border-left: 4px solid var(--accent-color); margin: 20px 0; border-radius: 4px; }}
        .toc h3 {{ font-size: 18px; margin-bottom: 10px; color: var(--primary-color); }}
        .toc ul {{ padding-left: 20px; font-size: 14px; }}
        .toc li {{ margin-bottom: 5px; }}
        .toc a {{ color: var(--secondary-color); text-decoration: none; }}
        .toc a:hover {{ text-decoration: underline; }}

        h2 {{ font-size: 22px; color: var(--primary-color); margin: 25px 0 10px; }}
        h3 {{ font-size: 18px; color: var(--secondary-color); margin: 20px 0 8px; }}
        h4 {{ font-size: 16px; margin: 15px 0 5px; }}
        h5 {{ font-size: 14px; margin: 12px 0 5px; }}
        h6 {{ font-size: 13px; margin: 10px 0 5px; color: #666; }}
        p {{ margin-bottom: 15px; font-size: 15px; }}

        /* Sidebar Styles */
        .sidebar {{ display: flex; flex-direction: column; gap: 25px; }}
        .widget {{ background: var(--white); padding: 20px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.05); }}
        .widget h3 {{ font-size: 16px; border-bottom: 2px solid var(--accent-color); padding-bottom: 8px; margin-bottom: 15px; color: var(--primary-color); }}
        .widget ul {{ list-style: none; }}
        .widget ul li {{ margin-bottom: 10px; font-size: 14px; }}
        .widget ul li a {{ color: var(--secondary-color); text-decoration: none; }}
        .widget ul li a:hover {{ text-decoration: underline; }}

        /* FAQ & Form */
        .faq-box {{ background: #fafafa; border: 1px solid var(--border-color); padding: 15px; border-radius: 6px; margin-bottom: 15px; }}
        .faq-box h4 {{ margin-top: 0; color: var(--primary-color); }}
        .contact-form {{ background: #f8fafc; padding: 20px; border-radius: 6px; border: 1px solid var(--border-color); margin-top: 30px; }}
        .contact-form input, .contact-form textarea {{ width: 100%; padding: 10px; margin-bottom: 12px; border: 1px solid var(--border-color); border-radius: 4px; }}
        .contact-form button {{ background: var(--accent-color); color: #fff; border: none; padding: 10px 20px; border-radius: 4px; cursor: pointer; font-weight: bold; }}

        /* Cookie Banner */
        #cookie-banner {{ position: fixed; bottom: 0; left: 0; width: 100%; background: #111827; color: #fff; padding: 15px 20px; display: flex; justify-content: space-between; align-items: center; z-index: 2000; box-shadow: 0 -2px 10px rgba(0,0,0,0.3); font-size: 14px; }}
        #cookie-banner button {{ background: var(--accent-color); color: #fff; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer; font-weight: bold; }}

        /* Footer */
        footer {{ background: var(--primary-color); color: var(--white); padding: 40px 20px 20px; margin-top: 40px; }}
        .footer-container {{ max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 30px; margin-bottom: 30px; }}
        .footer-col h4 {{ font-size: 16px; margin-bottom: 15px; border-bottom: 1px solid rgba(255,255,255,0.2); padding-bottom: 5px; }}
        .footer-col ul {{ list-style: none; }}
        .footer-col ul li {{ margin-bottom: 8px; font-size: 14px; }}
        .footer-col ul li a {{ color: #cbd5e1; text-decoration: none; }}
        .footer-col ul li a:hover {{ color: #fff; text-decoration: underline; }}
        .footer-col p {{ font-size: 13px; color: #cbd5e1; line-height: 1.5; }}
        .footer-bottom {{ text-align: center; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 15px; font-size: 13px; color: #94a3b8; }}
    </style>
</head>
<body>

    <!-- Header -->
    <header>
        <div class="header-container">
            <div class="logo-container">
                <a href="https://indoinves.github.io/">
                    <img src="https://indoinves.github.io/indoinves.png" alt="Indoinves Logo">
                </a>
            </div>
            <div class="search-box">
                <form action="https://indoinves.github.io/" method="GET">
                    <input type="text" placeholder="Search news, markets..." />
                </form>
            </div>
        </div>
    </header>

    <!-- Navigasi -->
    <nav>
        <div class="nav-wrap">
            <button class="menu-toggle" id="menu-toggle-btn" aria-label="Toggle Navigation">☰ Menu</button>
            <ul class="nav-container" id="main-nav-list">
                <li><a href="https://indoinves.github.io/">Home</a></li>
                <li class="dropdown">
                    <a href="#">Market & Finance ▾</a>
                    <div class="dropdown-content">
                        <a href="https://indoinves.github.io/market/stocks">Stocks & Equities</a>
                        <a href="https://indoinves.github.io/market/crypto">Cryptocurrency</a>
                        <a href="https://indoinves.github.io/market/forex">Forex Trading</a>
                    </div>
                </li>
                <li><a href="https://indoinves.github.io/macro-economy">Macro Economy</a></li>
                <li><a href="https://indoinves.github.io/explainers">Explainers</a></li>
                <li><a href="https://indoinves.github.io/manufacturing">Manufacturing</a></li>
                <li><a href="https://indoinves.github.io/property">Property</a></li>
                <li><a href="https://indoinves.github.io/health">Health</a></li>
                <li><a href="https://indoinves.github.io/education">Education</a></li>
                <li><a href="https://indoinves.github.io/lifestyle">Lifestyle</a></li>
                <li><a href="https://indoinves.github.io/hospitality">Hospitality</a></li>
                <li><a href="https://indoinves.github.io/tech-media">Tech & Media</a></li>
                <li><a href="https://indoinves.github.io/smes">Smes</a></li>
                <li><a href="https://indoinves.github.io/luxury">Luxury</a></li>
                <li><a href="https://indoinves.github.io/whos-who">Who's Who</a></li>
                <li class="dropdown">
                    <a href="#">International ▾</a>
                    <div class="dropdown-content">
                        <a href="https://indoinves.github.io/intl/americas">Americas</a>
                        <a href="https://indoinves.github.io/intl/europe">Europe</a>
                        <a href="https://indoinves.github.io/intl/asia">Asia Pacific</a>
                    </div>
                </li>
                <li><a href="https://indoinves.github.io/local-resources">Local Resources</a></li>
                <li><a href="https://indoinves.github.io/politics">Politics</a></li>
                <li><a href="https://indoinves.github.io/culture">Culture</a></li>
                <li><a href="https://indoinves.github.io/science">Science</a></li>
                <li><a href="https://indoinves.github.io/public-policy">Public Policy</a></li>
                <li><a href="https://indoinves.github.io/business-news">Business News</a></li>
                <li><a href="https://indoinves.github.io/sports">Sports</a></li>
                <li><a href="https://indoinves.github.io/arts">Arts</a></li>
                <li><a href="https://indoinves.github.io/celebrities">Celebrities</a></li>
                <li><a href="https://indoinves.github.io/automotive">Automotive</a></li>
                <li><a href="https://indoinves.github.io/commentary">Commentary</a></li>
                <li><a href="https://indoinves.github.io/interview">Interview</a></li>
            </ul>
        </div>
    </nav>

    <!-- Main Content & Sidebar -->
    <div class="main-layout">
        <main class="content-area">
            <h1>{title}</h1>
            <p class="lead-text">{description}</p>
            
            <!-- Table of Contents -->
            <div class="toc">
                <h3>Daftar Isi</h3>
                <ul>
                    <li><a href="#pendahuluan">1. Pendahuluan & Tinjauan Umum</a></li>
                    <li><a href="#analisis">2. Analisis Komprehensif & Strategi</a></li>
                    <li><a href="#implementasi">3. Langkah Implementasi & Evaluasi</a></li>
                    <li><a href="#faq">4. Pertanyaan yang Sering Diajukan (FAQ)</a></li>
                    <li><a href="#kesimpulan">5. Kesimpulan</a></li>
                </ul>
            </div>

            <h2 id="pendahuluan">1. Pendahuluan & Tinjauan Umum</h2>
            <p>Perkembangan sektor {category_name} di era modern menuntut ketepatan analisis serta pemahaman mendalam terhadap tren global. Untuk referensi global, Anda dapat meninjau data dari <a href="https://www.reuters.com" target="_blank" rel="noopener">Reuters</a>, <a href="https://www.bloomberg.com" target="_blank" rel="noopener">Bloomberg</a>, serta laporan riset dari <a href="https://www.imf.org" target="_blank" rel="noopener">IMF</a> dan <a href="https://www.worldbank.org" target="_blank" rel="noopener">World Bank</a>.</p>

            <h3>1.1 Ruang Lingkup & Parameter Utama</h3>
            <p>Parameter pengukuran kinerja sektor ini berfokus pada efisiensi operasional, manajemen risiko, serta adaptasi terhadap regulasi internasional.</p>

            <h2 id="analisis">2. Analisis Komprehensif & Strategi</h2>
            <p>Analisis mendalam menunjukkan bahwa transformasi digital dan otomatisasi memberikan dampak positif yang signifikan terhadap pertumbuhan ekonomi jangka panjang.</p>

            <h4>2.1 Pengaruh Terhadap Ekosistem Industri</h4>
            <p>Kolaborasi antar sektor menjadi kunci utama dalam menghadapi ketidakpastian ekonomi global yang dinamis.</p>

            <h5>2.1.1 Optimalisasi Sumber Daya</h5>
            <p>Pengelolaan aset yang efisien dapat meningkatkan margin keuntungan secara berkelanjutan.</p>

            <h6>2.1.1.1 Mitigasi Risiko Finansial</h6>
            <p>Penerapan manajemen risiko yang ketat melindungi portofolio dari volatilitas pasar yang ekstrem. Anda dapat mengecek standar keamanan global di <a href="https://www.iso.org" target="_blank" rel="noopener">ISO Standards</a> serta tren teknologi melalui <a href="https://techcrunch.com" target="_blank" rel="noopener">TechCrunch</a> dan <a href="https://www.wired.com" target="_blank" rel="noopener">Wired</a>.</p>

            <h2 id="implementasi">3. Langkah Implementasi & Evaluasi</h2>
            <p>Langkah taktis perlu dirumuskan secara terstruktur agar target strategis perusahaan atau pelaku usaha dapat tercapai secara optimal.</p>

            <!-- Internal Links (10 Links) -->
            <h3 style="margin-top: 30px;">Artikel & Tools Terkait di Indoinves:</h3>
            <ul style="margin-bottom: 25px; padding-left: 20px;">
                <li><a href="https://indoinves.github.io/tools/banklocator.html">Peta & Direktori Bank Global</a></li>
                <li><a href="https://indoinves.github.io/tools/investasi.html">Kalkulator Investasi Finansial</a></li>
                <li><a href="https://indoinves.github.io/tools/saham.html">Analisis Pasar Saham Harian</a></li>
                <li><a href="https://indoinves.github.io/tools/simulatorkripto-pro.html">Simulator Kripto Versi Pro</a></li>
                <li><a href="https://indoinves.github.io/tools/simulatorsaham.html">Simulator Trading Saham Pemula</a></li>
                <li><a href="https://indoinves.github.io/tools/website.html">Website & SEO Checker Tools</a></li>
                <li><a href="https://indoinves.github.io/macro-economy">Analisis Makroekonomi Terkini</a></li>
                <li><a href="https://indoinves.github.io/market/stocks">Update Saham & Ekuitas Global</a></li>
                <li><a href="https://indoinves.github.io/editorial">Pedoman & Kebijakan Editorial Indoinves</a></li>
                <li><a href="https://indoinves.github.io/">Kembali ke Beranda Utama Indoinves</a></li>
            </ul>

            <h2 id="faq">4. Pertanyaan yang Sering Diajukan (FAQ)</h2>
            <div class="faq-box">
                <h4>Apa fokus utama dari pembahasan topik ini?</h4>
                <p>Topik ini berfokus pada analisis mendalam, tren industri terkini, serta strategi praktis bagi para profesional dan pelaku bisnis.</p>
            </div>
            <div class="faq-box">
                <h4>Bagaimana cara memanfaatkan informasi ini untuk strategi bisnis?</h4>
                <p>Informasi dan data yang disajikan dapat dijadikan sebagai acuan awal dalam menyusun perencanaan strategis serta manajemen risiko.</p>
            </div>
            <div class="faq-box">
                <h4>Apakah Indoinves menyediakan layanan konsultasi khusus?</h4>
                <p>Anda dapat menghubungi tim kami melalui formulir kontak yang tersedia di bawah halaman untuk kerja sama atau informasi lebih lanjut.</p>
            </div>

            <h2 id="kesimpulan">5. Kesimpulan</h2>
            <p>Dengan pemahaman yang komprehensif mengenai {category_name}, para pemangku kepentingan dapat mengambil keputusan yang lebih tepat, terukur, dan berkelanjutan di masa depan.</p>

            <!-- Social Share & Contact Form -->
            <div style="margin: 30px 0; padding: 15px; background: #f1f5f9; border-radius: 6px;">
                <strong>Bagikan Artikel Ini:</strong>
                <div style="margin-top: 8px; display: flex; gap: 10px;">
                    <a href="https://facebook.com/sharer/sharer.php?u=https://indoinves.github.io/{file_url}" target="_blank" style="background: #1877f2; color: #fff; padding: 6px 12px; border-radius: 4px; text-decoration: none; font-size: 13px;">Facebook</a>
                    <a href="https://twitter.com/intent/tweet?url=https://indoinves.github.io/{file_url}&text={title}" target="_blank" style="background: #1da1f2; color: #fff; padding: 6px 12px; border-radius: 4px; text-decoration: none; font-size: 13px;">Twitter / X</a>
                    <a href="https://www.linkedin.com/shareArticle?mini=true&url=https://indoinves.github.io/{file_url}&title={title}" target="_blank" style="background: #0a66c2; color: #fff; padding: 6px 12px; border-radius: 4px; text-decoration: none; font-size: 13px;">LinkedIn</a>
                </div>
            </div>

            <div class="contact-form">
                <h3>Hubungi Redaksi Indoinves</h3>
                <p style="font-size: 13px; margin-bottom: 15px;">Punya pertanyaan atau masukan seputar artikel ini? Kirimkan pesan kepada kami.</p>
                <form action="#" method="POST">
                    <input type="text" placeholder="Nama Lengkap" required />
                    <input type="email" placeholder="Alamat Email" required />
                    <textarea rows="4" placeholder="Tuliskan pesan atau pertanyaan Anda..." required></textarea>
                    <button type="submit">Kirim Pesan</button>
                </form>
            </div>
        </main>

        <!-- Sidebar -->
        <aside class="sidebar">
            <div class="widget">
                <h3>Related Articles</h3>
                <ul>
                    <li><a href="https://indoinves.github.io/{dir}/artikel-1.html">Strategi Sukses di Sektor {category_name} Tahun 2026</a></li>
                    <li><a href="https://indoinves.github.io/{dir}/artikel-2.html">Analisis Tren & Peluang Bisnis Global</a></li>
                    <li><a href="https://indoinves.github.io/{dir}/artikel-3.html">Panduan Lengkap Manajemen Risiko Modern</a></li>
                </ul>
            </div>
            <div class="widget">
                <h3>Most Popular</h3>
                <ul>
                    <li><a href="https://indoinves.github.io/market/stocks">1. Top 10 Saham Pilihan Bulan Ini</a></li>
                    <li><a href="https://indoinves.github.io/macro-economy">2. Prospek Makroekonomi Global 2026</a></li>
                    <li><a href="https://indoinves.github.io/tools/investasi.html">3. Kalkulator Finansial & Investasi</a></li>
                </ul>
            </div>
            <div class="widget">
                <h3>AdSense Widget</h3>
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
        </aside>
    </div>

    <!-- Cookie Consent -->
    <div id="cookie-banner">
        <span>Kami menggunakan cookie untuk meningkatkan pengalaman pengguna dan analitik trafik.</span>
        <button onclick="document.getElementById('cookie-banner').style.display='none'">Setuju</button>
    </div>
    
    <!-- Footer -->
    <footer>
        <div class="footer-container">
            <div class="footer-col">
                <img src="https://indoinves.github.io/indoinves.png" alt="Indoinves Logo" style="height: 35px; margin-bottom: 15px; filter: brightness(0) invert(1);">
                <p>Indoinves adalah publikasi digital otoritatif yang menyajikan berita bisnis, analisis makroekonomi, dan intelijen pasar keuangan global.</p>
            </div>
            <div class="footer-col">
                <h4>Tools Free Indoinves</h4>
                <ul>
                    <li><a href="https://indoinves.github.io/tools/banklocator.html">Peta & Direktori Bank Global</a></li>
                    <li><a href="https://indoinves.github.io/tools/investasi.html">Kalkulator Investasi</a></li>
                    <li><a href="https://indoinves.github.io/tools/saham.html">Tools Saham</a></li>
                    <li><a href="https://indoinves.github.io/tools/website.html">SEO Checker</a></li>
                </ul>
            </div>
            <div class="footer-col">
                <h4>Quick Links</h4>
                <ul>
                    <li><a href="https://indoinves.github.io/">Home</a></li>
                    <li><a href="https://indoinves.github.io/about">About Us</a></li>
                    <li><a href="https://indoinves.github.io/contact">Contact Us</a></li>
                    <li><a href="https://indoinves.github.io/privacy">Privacy Policy</a></li>
                </ul>
            </div>
            <div class="footer-col">
                <h4>Policies</h4>
                <ul>
                    <li><a href="https://indoinves.github.io/disclaimer">Disclaimer</a></li>
                    <li><a href="https://indoinves.github.io/terms">Terms & Conditions</a></li>
                    <li><a href="https://indoinves.github.io/editorial">Editorial Guidelines</a></li>
                </ul>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2026 Indoinves - All Rights Reserved.</p>
        </div>
    </footer>

    <script>
        const menuToggleBtn = document.getElementById('menu-toggle-btn');
        const mainNavList = document.getElementById('main-nav-list');
        menuToggleBtn.addEventListener('click', () => {{
            mainNavList.classList.toggle('active');
        }});
    </script>
</body>
</html>
"""

def generate_articles():
    total_files = 0
    for directory in DIRECTORIES:
        os.makedirs(directory, exist_ok=True)
        cat_name = directory.replace("/", " - ").replace("-", " ").title()
        
        for i in range(1, 31):
            filename = f"artikel-{i}.html"
            filepath = os.path.join(directory, filename)
            file_url = f"{directory}/{filename}"
            
            title = f"Panduan Lengkap & Analisis Sektor {cat_name} Edisi #{i}"
            description = f"Pelajari wawasan mendalam, tren terbaru, dan strategi komprehensif seputar {cat_name} di Indoinves."
            
            content = HTML_TEMPLATE.format(
                title=title,
                description=description,
                category_name=cat_name,
                file_url=file_url,
                dir=directory
            )
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            total_files += 1
            
    print(f"Berhasil menghasilkan total {total_files} file artikel di {len(DIRECTORIES)} direktori!")

if __name__ == "__main__":
    generate_articles()
