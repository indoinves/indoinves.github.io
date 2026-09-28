import os
from xml.etree import ElementTree as ET
from xml.dom import minidom

# Konfigurasi Domain Website Anda
BASE_URL = "https://indoinves.github.io"
# Direktori lokal tempat file HTML Anda berada (gunakan '.' jika di root folder)
DIRECTORY = "." 

# Ekstensi file yang ingin dimasukkan ke sitemap
VALID_EXTENSIONS = (".html", ".htm")
# File yang ingin diabaikan (opsional)
EXCLUDE_FILES = ["404.html"]

def generate_sitemap():
    urlset = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")

    for root, dirs, files in os.walk(DIRECTORY):
        # Abaikan folder tersembunyi seperti .git, .github, dll.
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        for file in files:
            if file.endswith(VALID_EXTENSIONS) and file not in EXCLUDE_FILES:
                # Dapatkan path relatif dari root folder
                rel_path = os.path.relpath(os.path.join(root, file), DIRECTORY)
                
                # Ubah path Windows (\) ke slash URL (/) jika berjalan di Windows
                rel_path = rel_path.replace(os.sep, "/")
                
                # Tangani file index.html agar menjadi root directory (misal: /about/index.html -> /about/)
                if rel_path == "index.html":
                    page_url = f"{BASE_URL}/"
                elif rel_path.endswith("/index.html"):
                    page_url = f"{BASE_URL}/{rel_path[:-10]}"
                else:
                    page_url = f"{BASE_URL}/{rel_path}"

                # Buat elemen XML <url>
                url_elem = ET.SubElement(urlset, "url")
                
                loc_elem = ET.SubElement(url_elem, "loc")
                loc_elem.text = page_url

    # Format XML agar rapi (pretty print)
    rough_string = ET.tostring(urlset, encoding="utf-8")
    reparsed = minidom.parseString(rough_string)
    pretty_xml = reparsed.toprettyxml(indent="  ")

    # Simpan ke file sitemap.xml
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(pretty_xml)

    print("Sitemap berhasil dibuat: sitemap.xml")

if __name__ == "__main__":
    generate_sitemap()
