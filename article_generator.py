import os
import datetime

# Konfigurasi Direktori Dasar (Sesuaikan dengan struktur lokal project Anda)
BASE_DIR = "relmusic_site"  # Ganti dengan path folder project lokal Anda jika perlu
BLOG_DIR = os.path.join(BASE_DIR, "blog")

# Pastikan direktori ada
os.makedirs(BLOG_DIR, exist_ok=True)

# Template HTML untuk Artikel Blog
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - RelMusic Blog</title>
    <meta name="description" content="{description}">
    <link rel="stylesheet" href="../style.css"> <!-- Sesuaikan path CSS Anda -->
</head>
<body>
    <header>
        <nav>
            <a href="../index.html">Home</a> | 
            <a href="index.html">Blog</a> | 
            <a href="../about.html">About</a> | 
            <a href="../contact.html">Contact</a>
        </nav>
    </header>

    <main>
        <article>
            <h1>{title}</h1>
            <p><small>Dipublikasikan pada: {date}</small></p>
            
            <div class="content">
                {content}
            </div>
        </article>
    </main>

    <footer>
        <p>&copy; {year} RelMusic. All rights reserved. | <a href="../sitemap.html">Sitemap</a></p>
    </footer>
</body>
</html>
"""

def slugify(text):
    """Mengubah judul artikel menjadi format URL slug yang ramah SEO."""
    return "".join(c.lower() if c.isalnum() else "-" for c in text).strip("-").replace("--", "-")

def create_article(title, description, content_html):
    """Fungsi untuk membuat file HTML artikel baru."""
    slug = slugify(title)
    filename = f"{slug}.html"
    filepath = os.path.join(BLOG_DIR, filename)
    
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    current_year = datetime.datetime.now().strftime("%Y")
    
    # Render isi template
    html_content = HTML_TEMPLATE.format(
        title=title,
        description=description,
        content=content_html,
        date=current_date,
        year=current_year
    )
    
    # Tulis ke file
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html_content)
        
    print(f"[SUCCESS] Artikel berhasil dibuat: /blog/{filename}")
    update_sitemap()

def update_sitemap():
    """Memperbarui halaman sitemap.html secara otomatis berdasarkan file yang ada di direktori."""
    sitemap_path = os.path.join(BASE_DIR, "sitemap.html")
    
    # Kumpulkan semua file html di blog
    blog_files = [f for f in os.listdir(BLOG_DIR) if f.endswith(".html")]
    
    sitemap_content = """<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>Sitemap - RelMusic</title>
</head>
<body>
    <h1>Sitemap RelMusic</h1>
    <h2>Halaman Utama</h2>
    <ul>
        <li><a href="index.html">Home</a></li>
        <li><a href="about.html">About</a></li>
        <li><a href="contact.html">Contact</a></li>
        <li><a href="privacy.html">Privacy Policy</a></li>
        <li><a href="disclaimers.html">Disclaimer</a></li>
    </ul>
    
    <h2>Blog Artikel</h2>
    <ul>
"""
    for file in sorted(blog_files):
        title_display = file.replace(".html", "").replace("-", " ").title()
        sitemap_content += f'        <li><a href="blog/{file}">{title_display}</a></li>\n'
        
    sitemap_content += """    </ul>
</body>
</html>
"""

    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(sitemap_content)
    print("[INFO] Sitemap berhasil diperbarui secara otomatis!")

# ==========================================
# CONTOH CARA PENGGUNAAN (GENERATOR)
# ==========================================
if __name__ == "__main__":
    print("=== RELMUSIC ARTICLE GENERATOR ===")
    
    # Contoh input data artikel baru yang ingin digenerate
    sample_title = "Panduan Belajar Musik dan Teknologi AI Terbaru 2026"
    sample_desc = "Pelajari bagaimana kecerdasan buatan (AI) merevolusi industri musik modern dan produksi audio di tahun 2026."
    sample_body = """
        <p>Industri musik saat ini mengalami transformasi besar berkat adopsi teknologi kecerdasan buatan (Artificial Intelligence).</p>
        <h2>1. Peran AI dalam Produksi Musik</h2>
        <p>Produser kini dapat menggunakan tools berbasis AI untuk melakukan mixing, mastering, hingga menghasilkan instrumen unik secara instan.</p>
        <h2>2. Tren Musik Digital</h2>
        <p>Platform streaming dan integrasi web3 membuka peluang royalti baru bagi para musisi independen.</p>
    """
    
    # Jalankan fungsi generator
    create_article(
        title=sample_title,
        description=sample_desc,
        content_html=sample_body
    )
