import os

BASE_URL = "https://indoinves.github.io"
PAYPAL_ME = "https://www.paypal.com/paypalme/wahyudi9kdl"

def generate_plugin_store():
    items_html = []
    
    # Loop untuk membuat 1000 daftar produk plugin & templates secara otomatis
    for i in range(1, 1001):
        items_html.append(f"""
        <div style="background:#fff; border:1px solid #ddd; padding:15px; margin-bottom:15px; border-radius:5px; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap;">
            <div style="flex: 1; min-width: 250px;">
                <h3 style="margin:0 0 5px 0; color:#0056b3;">Pro Plugin / Template # {i}</h3>
                <p style="margin:0; color:#666; font-size:0.9rem;">Lisensi Resmi • Siap Pakai • Update Otomatis</p>
                <p style="margin:5px 0 0 0; font-weight:bold; color:#28a745;">Harga: $15.00 USD</p>
            </div>
            <div style="margin-top: 10px;">
                <a href="{PAYPAL_ME}/15?note=Order+Plugin+Nomor+{i}" target="_blank" style="background:#0070ba; color:#fff; padding:10px 15px; text-decoration:none; border-radius:4px; font-weight:bold; display:inline-block; margin-right:5px;">Bayar via PayPal</a>
                <a href="{BASE_URL}/downloads/file-{i}.zip" style="background:#28a745; color:#fff; padding:10px 15px; text-decoration:none; border-radius:4px; font-weight:bold; display:inline-block;" onclick="alert('Pastikan sudah melakukan pembayaran via PayPal, setelah itu file akan otomatis terunduh!');">Download File</a>
            </div>
        </div>
        """)

    store_html = f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>1.000+ Premium Plugins & Templates Store - Indoinves</title>
    <meta name="description" content="Download 1000+ plugin dan templates profesional berkualitas tinggi untuk kebutuhan website dan bisnis Anda." />
    <link rel="icon" type="image/png" href="{BASE_URL}/img/indoinves.png">
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; margin: 0; padding: 0; background: #f4f7f6; }}
        header {{ background: #111; color: #fff; padding: 20px; text-align: center; }}
        .container {{ max-width: 1000px; margin: 30px auto; padding: 0 15px; }}
        h1 {{ color: #111; }}
        footer {{ background: #111; color: #fff; text-align: center; padding: 20px; margin-top: 40px; }}
    </style>
</head>
<body>
    <header>
        <h1>Indoinves Marketplace - 1.000+ Plugins & Templates</h1>
        <p>Bayar via PayPal.Me/wahyudi9kdl, lalu unduh file yang Anda inginkan secara instan!</p>
    </header>
    <div class="container">
        <h2>Daftar Koleksi Digital Eksklusif</h2>
        <p>Silakan pilih produk di bawah ini. Klik <strong>Bayar via PayPal</strong> (sesuai nominal harga), lalu klik tombol <strong>Download File</strong>.</p>
        <hr style="margin: 20px 0;">
        {"".join(items_html)}
    </div>
    <footer>
        <p>&copy; 2026 Indoinves Store. All Rights Reserved.</p>
    </footer>
</body>
</html>
"""

    # Buat folder 'store' dan simpan file 'plugins.html' di dalamnya
    store_dir = os.path.join(".", "store")
    os.makedirs(store_dir, exist_ok=True)
    
    file_path = os.path.join(store_dir, "plugins.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(store_html)
        
    print(f"Berhasil merakit halaman store 1.000+ plugin di: {file_path}")

if __name__ == "__main__":
    generate_plugin_store()
