import os

BASE_URL = "https://indoinves.github.io"
PAYPAL_ME = "https://www.paypal.com/paypalme/wahyudi9kdl"

def generate_templates_store():
    items_html = []
    
    # Daftar kategori dan variasi harga agar tampak natural dan profesional
    categories = ["Landing Page", "E-Commerce", "Dashboard Admin", "Portfolio", "Blog Minimalis", "SaaS Startup", "Company Profile"]
    
    print("Sedang merakit 17.000+ templates...")
    
    # Loop untuk membuat 17.000+ daftar templates secara otomatis
    for i in range(1, 17001):
        # Menentukan kategori dan harga secara dinamis berdasarkan nomor index
        cat_name = categories[i % len(categories)]
        
        # Variasi harga berdasarkan jenis/kategori
        if "Dashboard" in cat_name:
            price = 29
        elif "E-Commerce" in cat_name:
            price = 25
        elif "SaaS" in cat_name:
            price = 35
        else:
            price = 15
            
        items_html.append(f"""
        <div style="background:#fff; border:1px solid #e1e4e8; padding:15px; margin-bottom:12px; border-radius:6px; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
            <div style="flex: 1; min-width: 260px;">
                <span style="background:#e1f5fe; color:#0288d1; padding:3px 8px; font-size:0.75rem; font-weight:bold; border-radius:4px;">{cat_name}</span>
                <h3 style="margin:8px 0 4px 0; color:#111; font-size:1.05rem;">Professional Template Pro #{i}</h3>
                <p style="margin:0; color:#666; font-size:0.85rem;">Full Responsive • Siap Pakai • Akses Instan Tanpa Member</p>
                <p style="margin:6px 0 0 0; font-weight:bold; color:#2e7d32; font-size:0.95rem;">Harga: ${price}.00 USD</p>
            </div>
            <div style="margin-top: 10px; display:flex; gap:8px;">
                <a href="{PAYPAL_ME}/{price}?note=Order+Template+Nomor+{i}" target="_blank" style="background:#0070ba; color:#fff; padding:8px 14px; text-decoration:none; border-radius:4px; font-size:0.85rem; font-weight:bold; display:inline-block;">Bayar via PayPal (${price})</a>
                <a href="{BASE_URL}/downloads/template-{i}.zip" style="background:#2e7d32; color:#fff; padding:8px 14px; text-decoration:none; border-radius:4px; font-size:0.85rem; font-weight:bold; display:inline-block;" onclick="alert('Silakan selesaikan pembayaran via PayPal. Setelah itu file akan otomatis terunduh!');">Download File</a>
            </div>
        </div>
        """)

    store_html = f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>17.000+ Ultimate Web Templates Store - Indoinves</title>
    <meta name="description" content="Koleksi 17.000+ templates profesional siap pakai. Bayar via PayPal dan download langsung tanpa perlu registrasi atau jadi member." />
    <link rel="icon" type="image/png" href="{BASE_URL}/img/indoinves.png">
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; margin: 0; padding: 0; background: #f8f9fa; }}
        header {{ background: #1a1a1a; color: #fff; padding: 30px 20px; text-align: center; }}
        .container {{ max-width: 1100px; margin: 30px auto; padding: 0 15px; }}
        h1 {{ margin: 0 0 10px 0; font-size: 1.8rem; color: #fff; }}
        p.subtitle {{ color: #bbb; font-size: 0.95rem; }}
        .notice {{ background: #fff3cd; border: 1px solid #ffeeba; color: #856404; padding: 12px; border-radius: 4px; margin-bottom: 20px; font-size: 0.9rem; }}
        footer {{ background: #1a1a1a; color: #fff; text-align: center; padding: 20px; margin-top: 40px; font-size: 0.9rem; }}
    </style>
</head>
<body>
    <header>
        <h1>Indoinves Templates Marketplace (17.000+ Koleksi)</h1>
        <p class="subtitle">Pilih template, bayar sesuai nominal via PayPal.Me, dan langsung unduh file ZIP-nya!</p>
    </header>
    
    <div class="container">
        <div class="notice">
            <strong>Informasi Pembelian:</strong> Anda tidak perlu mendaftar atau login (tanpa member). Cukup klik tombol <strong>Bayar via PayPal</strong> sesuai harga template, lalu klik tombol <strong>Download File</strong>.
        </div>
        
        <h2>Katalog 17.000+ Templates Profesional</h2>
        <hr style="margin: 15px 0 25px 0; border:0; border-top:1px solid #ddd;">
        
        {"".join(items_html)}
    </div>
    
    <footer>
        <p>&copy; 2026 Indoinves Templates Store. All Rights Reserved.</p>
    </footer>
</body>
</html>
"""

    # Menyimpan hasil ke dalam folder 'store/templates.html'
    store_dir = os.path.join(".", "store")
    os.makedirs(store_dir, exist_ok=True)
    
    file_path = os.path.join(store_dir, "templates.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(store_html)
        
    print(f"Berhasil merakit 17.000+ templates di: {file_path}")

if __name__ == "__main__":
    generate_templates_store()
