import os

# Daftar 25 Kategori Direktori sesuai permintaan
categories = [
    "macro-economy", "explainers", "manufacturing", "property", "health", 
    "education", "lifestyle", "hospitality", "tech-media", "smes", "luxury", 
    "whos-who", "international", "local-resources", "politics", "culture", 
    "science", "public-policy", "business-news", "sports", "arts", 
    "celebrities", "automotive", "commentary", "interview"
]

# Membuat 40 halaman per kategori (25 * 40 = 1000 halaman total)
pages_per_category = 40

def get_page_title(category, index):
    readable_cat = category.replace('-', ' ').title()
    topics = [
        "Strategi dan Analisis Tren Terbaru", 
        "Panduan Komprehensif dan Riset Mendalam", 
        "Dampak Jangka Panjang dan Proyeksi Masa Depan", 
        "Studi Kasus dan Implementasi Praktis",
        "Tinjauan Kritis dan Perspektif Global"
    ]
    topic_suffix = topics[index % len(topics)]
    return f"Eksklusif {readable_cat}: {topic_suffix} Bagian {index + 1}"

def generate_html(category, title_slug, page_title):
    return f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{page_title} - Indoinves</title>
    <meta name="description" content="Indoinves delivers authoritative insights on Market & Finance, Macro Economy, Business News, Technology, Real Estate, and Global Politics regarding {category}." />
    <meta name="keywords" content="Indoinves, Business News, Macro Economy, Market & Finance, {category}, Global Economy" />
    
    <!-- Open Graph Meta Tags -->
    <meta property="og:title" content="{page_title} - Indoinves" />
    <meta property="og:description" content="Get the latest updates on Macro Economy, Financial Markets, Technology, and Business News worldwide in {category}." />
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
        body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; margin: 0; padding: 0; background: #f9f9f9; }}
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
            <p><em>Dipublikasikan oleh Tim Riset Global Indoinves | Diperbarui pada 2026</em></p>
            
            <img src="https://indoinves.github.io/img/indoinves.jpg" alt="Ilustrasi Eksklusif {page_title}" width="800" height="450" style="width:100%; height:auto; border-radius:8px;">

            <!-- Daftar Isi (Table of Contents) -->
            <div class="table-of-contents">
                <h3>Daftar Isi</h3>
                <ul>
                    <li><a href="#pengantar">1. Pengantar dan Latar Belakang</a></li>
                    <li><a href="#analisis">2. Analisis Mendalam Sektor Terkait</a></li>
                    <li><a href="#tabel-data">3. Ringkasan Metrik dan Proyeksi Data</a></li>
                    <li><a href="#strategi">4. Strategi Pengelolaan dan Implementasi</a></li>
                    <li><a href="#tantangan">5. Tantangan dan Mitigasi Risiko Global</a></li>
                    <li><a href="#faq">6. Pertanyaan yang Sering Diajukan (FAQ)</a></li>
                    <li><a href="#kesimpulan">7. Kesimpulan</a></li>
                </ul>
            </div>

            <h2 id="pengantar">1. Pengantar dan Latar Belakang</h2>
            <p>Dinamika ekonomi global saat ini menuntut pendekatan yang lebih taktis dan berbasis data. Dalam kategori <strong>{category}</strong>, perubahan struktural terjadi secara masif seiring dengan inovasi teknologi dan pergeseran kebijakan makro. Artikel komprehensif ini mengkaji berbagai sudut pandang penting yang relevan dengan kebutuhan para investor, pelaku bisnis, serta pengamat pasar profesional.</p>
            <p>Melalui riset mendalam, kita dapat melihat bagaimana pasar merespons berbagai sentimen domestik maupun internasional. Keterbukaan informasi menjadi kunci utama dalam merumuskan keputusan finansial yang akurat dan terukur dalam jangka panjang.</p>

            <h2 id="analisis">2. Analisis Mendalam Sektor Terkait</h2>
            <p>Pertumbuhan sektor ini tidak terlepas dari dukungan ekosistem digital dan kebijakan fiskal yang adaptif. Berbagai indikator menunjukkan adanya tren positif yang berkelanjutan, meskipun volatilitas pasar tetap harus diwaspadai oleh setiap pelaku ekonomi.</p>
            <p>Pentingnya literasi keuangan dan pemahaman mendalam terhadap instrumen terkait memberikan keunggulan kompetitif bagi para pemangku kepentingan. Kolaborasi lintas sektor juga menjadi motor penggerak utama dalam menciptakan stabilitas ekonomi yang inklusif.</p>

            <h2 id="tabel-data">3. Ringkasan Metrik dan Proyeksi Data</h2>
            <p>Berikut adalah tabel ringkasan komparatif yang merangkum parameter penting berdasarkan tren riset pasar global terkini:</p>
            <table>
                <thead>
                    <tr>
                        <th>Parameter Analisis</th>
                        <th>Kondisi Saat Ini</th>
                        <th>Proyeksi Tren</th>
                        <th>Tingkat Pengaruh</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Indikator Likuiditas</td>
                        <td>Stabil & Terkendali</td>
                        <td>Tumbuh Positif</td>
                        <td>Tinggi</td>
                    </tr>
                    <tr>
                        <td>Adopsi Teknologi Modern</td>
                        <td>Akselerasi Cepat</td>
                        <td>Dominan</td>
                        <td>Sangat Tinggi</td>
                    </tr>
                    <tr>
                        <td>Mitigasi Risiko Makro</td>
                        <td>Standar Ketat</td>
                        <td>Adaptif</td>
                        <td>Menengah</td>
                    </tr>
                </tbody>
            </table>

            <h2 id="strategi">4. Strategi Pengelolaan dan Implementasi</h2>
            <p>Penerapan strategi yang tepat sasaran memerlukan kerangka kerja operasional yang solid. Pelaku industri dianjurkan untuk terus memantau pembaruan regulasi serta mengoptimalkan perangkat digital modern yang tersedia pada platform seperti <a href="https://indoinves.github.io/tools/website.html">Tech Tools Indoinves</a> guna meningkatkan efisiensi kerja.</p>
            <p>Selain itu, pengelolaan portofolio yang terdiversifikasi dengan baik akan meminimalkan eksposur terhadap guncangan pasar yang tidak terduga.</p>

            <h2 id="tantangan">5. Tantangan dan Mitigasi Risiko Global</h2>
            <p>Setiap peluang investasi atau ekspansi bisnis selalu berdampingan dengan risiko inheren. Faktor geopolitik, perubahan suku bunga acuan bank sentral, serta dinamika rantai pasok global merupakan beberapa variabel utama yang memerlukan perhatian khusus.</p>
            <p>Dengan menerapkan prinsip manajemen risiko yang disiplin, para pengambil keputusan dapat mengamankan aset sekaligus memaksimalkan potensi imbal hasil (return) di masa depan.</p>

            <!-- Internal & External Links Section -->
            <h3>Referensi & Tautan Terkait</h3>
            <p>Untuk memperdalam wawasan Anda, silakan kunjungi sumber-sumber tepercaya berikut:</p>
            <ul>
                <li>Internal: <a href="https://indoinves.github.io/">Halaman Utama Indoinves</a></li>
                <li>Internal: <a href="https://indoinves.github.io/tools/investasi.html">Kalkulator Investasi Modern</a></li>
                <li>Internal: <a href="https://indoinves.github.io/tools/simulatorsaham.html">Simulator Saham Interaktif</a></li>
                <li>Internal: <a href="https://indoinves.github.io/tools/simulatorkripto.html">Analisis Pasar Kripto</a></li>
                <li>Internal: <a href="https://indoinves.github.io/forum.html">Forum Diskusi Komunitas</a></li>
                <li>Internal: <a href="https://indoinves.github.io/komunitas.html">Pusat Informasi Komunitas</a></li>
                <li>Internal: <a href="https://indoinves.github.io/about.html">Tentang Profil Indoinves</a></li>
                <li>Eksternal: <a href="https://www.reuters.com" target="_blank" rel="noopener">Reuters Global Finance</a></li>
                <li>Eksternal: <a href="https://www.bloomberg.com" target="_blank" rel="noopener">Bloomberg Markets</a></li>
                <li>Eksternal: <a href="https://www.wsj.com" target="_blank" rel="noopener">Wall Street Journal</a></li>
                <li>Eksternal: <a href="https://www.ft.com" target="_blank" rel="noopener">Financial Times</a></li>
                <li>Eksternal: <a href="https://www.cnbc.com" target="_blank" rel="noopener">CNBC International</a></li>
                <li>Eksternal: <a href="https://www.imf.org" target="_blank" rel="noopener">International Monetary Fund (IMF)</a></li>
                <li>Eksternal: <a href="https://www.worldbank.org" target="_blank" rel="noopener">World Bank Group</a></li>
            </ul>

            <h2 id="faq">6. Pertanyaan yang Sering Diajukan (FAQ)</h2>
            <p><strong>Q: Apakah informasi dalam artikel ini diperbarui secara berkala?</strong><br>A: Ya, tim redaksi Indoinves selalu meninjau ulang konten secara berkala sesuai dengan dinamika pasar terbaru.</p>
            <p><strong>Q: Bagaimana cara berpartisipasi dalam diskusi komunitas?</strong><br>A: Anda dapat langsung bergabung melalui tautan <a href="https://indoinves.github.io/komunitas.html">Komunitas Resmi</a>.</p>
            <p><strong>Q: Apakah layanan analisis ini memerlukan biaya berlangganan?</strong><br>A: Tidak, seluruh fasilitas dan artikel riset di platform ini dapat diakses secara gratis.</p>

            <h2 id="kesimpulan">7. Kesimpulan</h2>
            <p>Pemahaman yang komprehensif mengenai dinamika sektor <strong>{category}</strong> memberikan landasan kokoh dalam mengambil keputusan strategis. Dengan memanfaatkan perangkat analitis dan informasi tepercaya dari Indoinves, diharapkan para pembaca dapat mengoptimalkan pencapaian finansial dan profesional mereka secara berkelanjutan.</p>

            <!-- Social Share Simulation -->
            <div class="social-share">
                <span>Bagikan Artikel Ini:</span>
                <a href="https://facebook.com/indoinves" target="_blank">Facebook</a> | 
                <a href="https://twitter.com/indoinves" target="_blank">Twitter</a> | 
                <a href="https://linkedin.com/company/indoinves" target="_blank">LinkedIn</a> | 
                <a href="https://api.whatsapp.com/send?text=Baca%20artikel%20menarik%20di%20Indoinves" target="_blank">WhatsApp</a>
            </div>

            <!-- Contact Form Section -->
            <div class="contact-form">
                <h3>Hubungi Redaksi & Tim Dukungan</h3>
                <p>Punya pertanyaan atau ingin berkolaborasi? Kirimkan pesan Anda melalui formulir di bawah ini:</p>
                <form action="https://indoinves.github.io/contact.html" method="GET">
                    <input type="text" name="name" placeholder="Nama Lengkap Anda" required>
                    <input type="email" name="email" placeholder="Alamat Email Aktif" required>
                    <textarea name="message" rows="4" placeholder="Tuliskan pesan atau pertanyaan Anda di sini..." required></textarea>
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

# Eksekusi pembuatan direktori dan file secara masif
total_files = 0
for cat in categories:
    cat_dir = os.path.join(".", cat)
    os.makedirs(cat_dir, exist_ok=True)
    for i in range(pages_per_category):
        # Membuat slug file yang bervariasi
        slugs = ["analisis", "panduan", "strategi", "tren", "prospek", "tips", "laporan", "tinjauan"]
        title_slug = f"{slugs[i % len(slugs)]}-{i + 1}"
        page_title = get_page_title(cat, i)
        
        file_path = os.path.join(cat_dir, f"{title_slug}.html")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(generate_html(cat, title_slug, page_title))
        total_files += 1

print(f"Sukses! Total {total_files} file artikel di 25 direktori kategori berhasil dibuat dan siap dipublikasikan.")
