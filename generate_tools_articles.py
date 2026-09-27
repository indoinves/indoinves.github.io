import os

# Daftar kategori tools, software, dan utilitas digital (18 kategori utama)
tool_categories = [
    "tools/saham", "tools/kripto", "tools/investasi", "tools/banklocator", 
    "tools/website", "tools/kalkulator", "tools/analisis", "tools/portofolio", 
    "tools/pajak", "tools/budgeting", "tools/forex", "tools/komoditas", 
    "tools/properti", "tools/pensiun", "tools/akuntansi", "tools/emiten", 
    "tools/fintech", "tools/ekuitas"
]

# Menghasilkan 200 halaman per sub-kategori (18 * 200 = 3.600+ halaman total)
pages_per_tool_category = 200

def get_tool_page_title(category_name, index):
    clean_name = category_name.split('/')[-1].replace('-', ' ').title()
    topics = [
        "Software & Tools Terbaik untuk Analisis", 
        "Panduan Penggunaan dan Fitur Unggulan", 
        "Optimasi Kinerja dan Automasi Perangkat", 
        "Studi Kasus Implementasi Perangkat Digital",
        "Evaluasi Fungsionalitas dan Perbandingan Sistem"
    ]
    topic_suffix = topics[index % len(topics)]
    return f"{clean_name} Utility: {topic_suffix} v{index + 1}.0"

def generate_tool_html(category, title_slug, page_title):
    return f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{page_title} - Indoinves Tools</title>
    <meta name="description" content="Indoinves provides advanced software utilities, financial calculators, and professional digital tools for {category}." />
    <meta name="keywords" content="Indoinves, Tools, Software, Financial Calculator, {category}, Digital Utility" />
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
    
    <!-- Open Graph Meta Tags -->
    <meta property="og:title" content="{page_title} - Indoinves" />
    <meta property="og:description" content="Explore authoritative software tools and modern digital utilities for financial planning and market analysis." />
    <meta property="og:image" content="https://indoinves.github.io/indoinves.jpg" />
    <meta property="og:url" content="https://indoinves.github.io/{category}/{title_slug}.html" />
    <meta property="og:type" content="article" />
    
    <!-- Manifest JSON Link -->
    <link rel="manifest" href="https://indoinves.github.io/manifest.json" />
    
    <!-- Favicon -->
    <link rel="icon" href="https://indoinves.github.io/indoinves.png" type="image/png" />
    
    <!-- Schema JSON-LD -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "NewsMediaOrganization",
      "name": "Indoinves",
      "url": "https://indoinves.github.io/",
      "logo": {{
        "@type": "ImageObject",
        "url": "https://indoinves.github.io/indoinves.png"
      }},
      "sameAs": [
        "https://facebook.com/indoinves",
        "https://twitter.com/indoinves",
        "https://linkedin.com/company/indoinves"
      ]
    }}
    </script>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; margin: 0; padding: 0; background: #fdfdfd; }}
        header, footer {{ background: #111; color: #fff; padding: 20px; text-align: center; }}
        nav a, footer a {{ color: #4da6ff; text-decoration: none; margin: 0 10px; }}
        main {{ max-width: 900px; margin: 20px auto; background: #fff; padding: 40px; box-shadow: 0 0 10px rgba(0,0,0,0.05); }}
        h1, h2, h3 {{ color: #111; }}
        .table-of-contents {{ background: #f0f0f0; padding: 15px; margin-bottom: 20px; border-left: 4px solid #0056b3; }}
        table {{ width: 100%; border-collapse: collapse; margin: 20px 0; }}
        table, th, td {{ border: 1px solid #ddd; padding: 10px; text-align: left; }}
        th {{ background: #f4f4f4; }}
        .contact-form {{ background: #f9f9f9; padding: 20px; margin-top: 30px; border: 1px solid #ddd; }}
        .contact-form input, .contact-form textarea {{ width: 100%; padding: 10px; margin: 10px 0; border: 1px solid #ccc; }}
        .social-share {{ margin: 20px 0; font-weight: bold; }}
    </style>
</head>
<body>

    <!-- Header & Navigasi -->
    <header>
        <img src="https://indoinves.github.io/indoinves.png" alt="Indoinves Logo" width="80" height="80">
        <h1>IndoInves Platform</h1>
        <p>Platform Pintar Investasi, Keuangan, dan Kumpulan Tools Finansial Modern</p>
        <nav>
            <a href="https://indoinves.github.io/">Home</a> | 
            <a href="https://indoinves.github.io/tools/investasi.html">Investasi</a> | 
            <a href="https://indoinves.github.io/komunitas.html">Komunitas</a> | 
            <a href="https://indoinves.github.io/forum.html">Forum</a> | 
            <a href="https://indoinves.github.io/contact.html">Kontak</a>
        </nav>
    </header>

    <!-- Konten Utama Artikel -->
    <main>
        <article>
            <h1>{page_title}</h1>
            <p><em>Dokumentasi Teknis & Perangkat Utilitas Digital Indoinves | Diperbarui pada 2026</em></p>
            
            <img src="https://indoinves.github.io/img/indoinves.jpg" alt="Ilustrasi Software Tools {page_title}" width="800" height="450" style="width:100%; height:auto; border-radius:8px;">

            <!-- Daftar Isi (Table of Contents) -->
            <div class="table-of-contents">
                <h3>Daftar Isi Utilitas</h3>
                <ul>
                    <li><a href="#pengantar">1. Pengantar Perangkat & Software</a></li>
                    <li><a href="#fitur">2. Arsitektur dan Fitur Utama Sistem</a></li>
                    <li><a href="#tabel-data">3. Parameter Komparasi Kinerja Software</a></li>
                    <li><a href="#implementasi">4. Panduan Implementasi dan Penggunaan</a></li>
                    <li><a href="#keamanan">5. Standar Keamanan dan Privasi Data</a></li>
                    <li><a href="#faq">6. Pertanyaan yang Sering Diajukan (FAQ)</a></li>
                    <li><a href="#kesimpulan">7. Kesimpulan dan Rekomendasi</a></li>
                </ul>
            </div>

            <h2 id="pengantar">1. Pengantar Perangkat & Software</h2>
            <p>Dalam era digital yang serba cepat, ketersediaan perangkat lunak (*software*) dan utilitas berbasis web yang handal menjadi fondasi utama bagi efisiensi operasional. Kategori <strong>{category}</strong> merangkum berbagai perangkat mutakhir yang dirancang khusus untuk mempermudah kalkulasi finansial, pemantauan aset, serta pengelolaan data secara real-time.</p>
            <p>Penggunaan sistem otomasi ini terbukti mampu memangkas waktu pengerjaan manual sekaligus meminimalkan potensi kesalahan hitung manusia (*human error*) dalam analisis investasi maupun manajemen bisnis.</p>

            <h2 id="fitur">2. Arsitektur dan Fitur Utama Sistem</h2>
            <p>Sistem ini dibangun dengan mengintegrasikan teknologi web standar berkinerja tinggi, memastikan kompatibilitas penuh di berbagai perangkat tanpa memerlukan instalasi tambahan yang rumit. Pengguna dapat langsung mengakses fitur kalkulasi lanjutan, visualisasi grafik interaktif, serta laporan analitik mendalam.</p>
            <p>Fleksibilitas antarmuka memungkinkan penyesuaian parameter sesuai dengan kebutuhan spesifik pengguna, baik untuk investor ritel maupun institusi profesional.</p>

            <h2 id="tabel-data">3. Parameter Komparasi Kinerja Software</h2>
            <p>Tabel di bawah ini menyajikan perbandingan spesifikasi fungsional dan performa utilitas sistem:</p>
            <table>
                <thead>
                    <tr>
                        <th>Fitur Modul</th>
                        <th>Versi Standar</th>
                        <th>Versi Pro / Enterprise</th>
                        <th>Tingkat Efisiensi</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Kecepatan Eksekusi</td>
                        <td>Optimal (&lt; 1.2s)</td>
                        <td>Super Cepat (&lt; 0.4s)</td>
                        <td>Sangat Tinggi</td>
                    </tr>
                    <tr>
                        <td>Kustomisasi Parameter</td>
                        <td>Terbatas</td>
                        <td>Tanpa Batas (Full Access)</td>
                        <td>Tinggi</td>
                    </tr>
                    <tr>
                        <td>Dukungan Integrasi API</td>
                        <td>Tidak Tersedia</td>
                        <td>Tersedia Penuh</td>
                        <td>Maksimal</td>
                    </tr>
                </tbody>
            </table>

            <h2 id="implementasi">4. Panduan Implementasi dan Penggunaan</h2>
            <p>Untuk memaksimalkan fungsi dari perangkat ini, pengguna disarankan untuk mengikuti panduan operasional standar. Integrasikan perangkat ini dengan perangkat utilitas lain seperti yang tersedia di <a href="https://indoinves.github.io/tools/website.html">Tech Tools Indoinves</a> untuk mendapatkan hasil analisis yang komprehensif.</p>
            <p>Pastikan juga untuk selalu memperbarui *cache* browser guna mendapatkan versi antarmuka paling mutakhir.</p>

            <h2 id="keamanan">5. Standar Keamanan dan Privasi Data</h2>
            <p>Indoinves menjunjung tinggi kerahasiaan data pengguna. Seluruh pemrosesan kalkulasi dilakukan secara lokal pada peramban (*client-side processing*) atau melalui jalur terenkripsi yang aman, sehingga meminimalisasi risiko kebocoran informasi sensitif.</p>

            <!-- Internal & External Links Section -->
            <h3>Referensi & Tautan Terkait</h3>
            <ul>
                <li>Internal: <a href="https://indoinves.github.io/">Halaman Utama Indoinves</a></li>
                <li>Internal: <a href="https://indoinves.github.io/tools/investasi.html">Kalkulator Investasi Modern</a></li>
                <li>Internal: <a href="https://indoinves.github.io/tools/simulatorsaham.html">Simulator Saham Interaktif</a></li>
                <li>Internal: <a href="https://indoinves.github.io/tools/simulatorkripto.html">Analisis Pasar Kripto</a></li>
                <li>Internal: <a href="https://indoinves.github.io/forum.html">Forum Diskusi Komunitas</a></li>
                <li>Internal: <a href="https://indoinves.github.io/komunitas.html">Pusat Informasi Komunitas</a></li>
                <li>Internal: <a href="https://indoinves.github.io/about.html">Tentang Profil Indoinves</a></li>
                <li>Eksternal: <a href="https://github.com" target="_blank" rel="noopener">GitHub Developer Platform</a></li>
                <li>Eksternal: <a href="https://stackoverflow.com" target="_blank" rel="noopener">Stack Overflow Community</a></li>
                <li>Eksternal: <a href="https://developer.mozilla.org" target="_blank" rel="noopener">MDN Web Docs</a></li>
                <li>Eksternal: <a href="https://www.w3schools.com" target="_blank" rel="noopener">W3Schools Web Standards</a></li>
                <li>Eksternal: <a href="https://nodejs.org" target="_blank" rel="noopener">Node.js Runtime Environment</a></li>
                <li>Eksternal: <a href="https://www.python.org" target="_blank" rel="noopener">Python Software Foundation</a></li>
                <li>Eksternal: <a href="https://www.docker.com" target="_blank" rel="noopener">Docker Containerization</a></li>
            </ul>

            <h2 id="faq">6. Pertanyaan yang Sering Diajukan (FAQ)</h2>
            <p><strong>Q: Apakah perangkat lunak ini memerlukan instalasi aplikasi tambahan?</strong><br>A: Tidak, seluruh tools dapat diakses langsung melalui browser web standar secara instan.</p>
            <p><strong>Q: Apakah hasil kalkulasi dijamin akurat 100%?</strong><br>A: Perangkat ini dirancang berdasarkan formula matematis dan finansial standar industri sebagai referensi analisis awal.</p>
            <p><strong>Q: Bagaimana cara melaporkan kendala teknis pada sistem?</strong><br>A: Anda dapat menghubungi tim support melalui <a href="https://indoinves.github.io/contact.html">Halaman Kontak</a>.</p>

            <h2 id="kesimpulan">7. Kesimpulan dan Rekomendasi</h2>
            <p>Pemanfaatan perangkat digital dan software utilitas yang tepat akan memberikan keunggulan strategis dalam pengelolaan keuangan maupun pengembangan proyek digital. Jelajahi terus berbagai varian tools di Indoinves untuk mendukung produktivitas harian Anda.</p>

            <!-- Social Share Simulation -->
            <div class="social-share">
                <span>Bagikan Perangkat Ini:</span>
                <a href="https://facebook.com/indoinves" target="_blank">Facebook</a> | 
                <a href="https://twitter.com/indoinves" target="_blank">Twitter</a> | 
                <a href="https://linkedin.com/company/indoinves" target="_blank">LinkedIn</a> | 
                <a href="https://api.whatsapp.com/send?text=Cek%20perangkat%20bermanfaat%20di%20Indoinves" target="_blank">WhatsApp</a>
            </div>

            <!-- Contact Form Section -->
            <div class="contact-form">
                <h3>Hubungi Tim Pengembang Tools</h3>
                <p>Punya ide pengembangan fitur atau software baru? Kirimkan masukan Anda:</p>
                <form action="https://indoinves.github.io/contact.html" method="GET">
                    <input type="text" name="name" placeholder="Nama Lengkap Anda" required>
                    <input type="email" name="email" placeholder="Alamat Email Aktif" required>
                    <textarea name="message" rows="4" placeholder="Tuliskan saran atau kendala teknis di sini..." required></textarea>
                    <button type="submit" style="background:#0056b3; color:#fff; padding:10px 20px; border:none; cursor:pointer;">Kirim Pesan</button>
                </form>
            </div>
        </article>
    </main>

    <!-- Footer Sama Persis dengan Halaman Utama -->
    <footer>
        <p>&copy; 2026 IndoInves. Seluruh Hak Cipta Dilindungi Undang-Undang.</p>
        <p>
            <a href="https://indoinves.github.io/privacy.html">Kebijakan Privasi</a> | 
            <a href="https://indoinves.github.io/terms.html">Syarat & Ketentuan</a> | 
            <a href="https://indoinves.github.io/disclaimer.html">Disclaimer</a> | 
            <a href="https://indoinves.github.io/contact.html">Kontak</a>
        </p>
    </footer>

</body>
</html>
"""

# Eksekusi pembuatan file secara masif untuk 3600+ halaman tools
total_tools_files = 0
for tool_cat in tool_categories:
    cat_dir = os.path.join(".", tool_cat)
    os.makedirs(cat_dir, exist_ok=True)
    for i in range(pages_per_tool_category):
        slugs = ["utility", "software", "generator", "kalkulator", "analyzer", "manager", "optimizer", "simulator"]
        title_slug = f"{slugs[i % len(slugs)]}-{i + 1}"
        page_title = get_tool_page_title(tool_cat, i)
        
        file_path = os.path.join(cat_dir, f"{title_slug}.html")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(generate_tool_html(tool_cat, title_slug, page_title))
        total_tools_files += 1

print(f"Sukses! Total {total_tools_files} file direktori tools dan software berhasil dibuat.")
