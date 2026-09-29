import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# Daftar URL yang ingin dibuka dan didownload
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
    "https://sfile.co/invite/358103",
]

# Tentukan folder download (ubah path jika diperlukan)
download_dir = os.path.join(os.getcwd(), "downloads")
os.makedirs(download_dir, exist_ok=True)

# Konfigurasi Chrome agar otomatis mendownload ke folder tertentu tanpa popup
options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True,
}
options.add_experimental_option("prefs", prefs)
# Hapus tanda pagar '#' di bawah jika ingin berjalan di latar belakang (tanpa membuka jendela browser secara fisik)
# options.add_argument("--headless")

print(f"Mempersiapkan browser untuk mendownload {len(urls)} URL...")
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options
)

try:
  for i, url in enumerate(urls, 1):
    print(f"\nMemproses ({i}/{len(urls)}): {url}")
    try:
      driver.get(url)

      # Berikan waktu jeda untuk halaman termuat (menyesuaikan jika ada countdown/iklan)
      wait = WebDriverWait(driver, 10)

      # Mencari tombol download (biasanya memiliki teks 'Download' atau ID/Class tertentu)
      # Anda bisa menyesuaikan selector di bawah jika struktur tombol sfile.co berubah
      try:
        download_button = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//a[contains(@class, 'download') or contains(text(),"
                    " 'Download') or contains(text(), 'Unduh')]",
                )
            )
        )
        download_button.click()
        print("Berhasil mengklik tombol download.")

        # Jeda sejenak agar file mulai terunduh sebelum lanjut ke URL berikutnya
        time.sleep(3)
      except Exception:
        print(
            "Tombol download otomatis tidak ditemukan/perlu klik manual pada"
            " halaman ini."
        )

    except Exception as e:
      print(f"Gagal memproses URL {url}: {e}")

    # Jeda antar URL agar browser tidak lag
    time.sleep(1)

  print("\nSelesai! Semua URL telah diproses. Cek folder 'downloads'.")

finally:
  # Tutup browser setelah selesai
  time.sleep(5)
  driver.quit()
