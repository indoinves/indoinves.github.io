import webbrowser
import time

# Daftar URL yang ingin dibuka
urls = [
    "https://sfile.co/nXxrXVGMKbo",
    "https://sfile.co/QTqz1iLsTSr",
    "https://sfile.co/M0EsqRLwjcx",
    "https://sfile.co/5AEhkcRbK3f",
    "https://sfile.co/GHah9oDZJ1r",
    "https://sfile.co/GHah9oDZJ1r",
    "https://sfile.co/jAPeNa8EtqV",
    "https://sfile.co/ZoGUL7dUUMd",
    "https://sfile.co/GGbWLAKRuXa",
    "https://sfile.co/XIn40kty9GP",
    "https://sfile.co/pFDKObQYmG8",
    "https://sfile.co/nxDxP7LGcYf",
    "https://sfile.co/RWUPnUu5890",
    "https://sfile.co/riVh5PhVPOd",
    "https://sfile.co/i8OxwXgjvFW",
    "https://sfile.co/t7gxCmnaJa9",
    "https://sfile.co/Kz4E1keJwr5",
    "https://sfile.co/m659lxp2PhN",
    "https://sfile.co/B2oecuNVtTx",
    "https://sfile.co/M1qwIlpT7uZ",
    "https://sfile.co/j9SiJdhjh7G",
    "https://sfile.co/zfBFExsqmww",
    "https://sfile.co/ZnZX8ClSDid",
    "https://sfile.co/4udVSmTXKTm",
    "https://sfile.co/fYk5h1ZdhIh",
    "https://sfile.co/6IIsJm7gXiS",
    "https://sfile.co/aD1M4p4iHYd",
    "https://sfile.co/3f1HZnAP8AG",
    "https://sfile.co/aNQRGYA17aW",
    "https://sfile.co/4ujauwjm6sZ",
    "https://sfile.co/invite/358103"
]

print(f"Mempersiapkan membuka {len(urls)} URL...")

for i, url in enumerate(urls, 1):
    print(f"Membuka ({i}/{len(urls)}): {url}")
    webbrowser.open(url)
    # Jeda 0.5 detik antar tab agar browser tidak "lag" atau kewalahan
    time.sleep(0.5)

print("Selesai! Semua URL telah dibuka di browser.")
