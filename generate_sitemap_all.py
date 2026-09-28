import os
import datetime
from xml.etree import ElementTree as ET
from xml.dom import minidom
from feedgen.feed import FeedGenerator

# --- Konfigurasi Website ---
BASE_URL = "https://indoinves.github.io"
DIRECTORY = "." 
VALID_EXTENSIONS = (".html", ".htm")
EXCLUDE_FILES = ["404.html"]

def generate_sitemap_all():
    urlset = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    
    # Inisialisasi Feed Generator untuk RSS & Atom
    fg = FeedGenerator()
    fg.id(f"{BASE_URL}/")
    fg.title('IndoInves Website')
    fg.author({'name': 'Admin IndoInves', 'email': 'admin@indoinves.github.io'})
    fg.link(href=f"{BASE_URL}/", rel='alternate')
    fg.subtitle('Kumpulan artikel dan informasi seputar investasi.')
    fg.language('id')

    # Scan file HTML secara otomatis
    for root, dirs, files in os.walk(DIRECTORY):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        for file in files:
            if file.endswith(VALID_EXTENSIONS) and file not in EXCLUDE_FILES:
                rel_path = os.path.relpath(os.path.join(root, file), DIRECTORY)
                rel_path = rel_path.replace(os.sep, "/")
                
                # Format URL halaman
                if rel_path == "index.html":
                    page_url = f"{BASE_URL}/"
                    page_title = "Home - IndoInves"
                elif rel_path.endswith("/index.html"):
                    folder_name = rel_path[:-10]
                    page_url = f"{BASE_URL}/{folder_name}"
                    page_title = folder_name.replace('-', ' ').title()
                else:
                    page_url = f"{BASE_URL}/{rel_path}"
                    page_title = file[:-5].replace('-', ' ').title()

                # 1. Tambahkan ke Sitemap XML
                url_elem = ET.SubElement(urlset, "url")
                loc_elem = ET.SubElement(url_elem, "loc")
                loc_elem.text = page_url

                # Ambil waktu modifikasi file terakhir sebagai tanggal
                file_path = os.path.join(root, file)
                mod_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path), datetime.timezone.utc)
                
                lastmod_elem = ET.SubElement(url_elem, "lastmod")
                lastmod_elem.text = mod_time.strftime('%Y-%m-%d')

                # 2. Tambahkan ke RSS & Atom Feed
                fe = fg.add_entry()
                fe.id(page_url)
                fe.title(page_title)
                fe.link(href=page_url)
                fe.description(f"Informasi lebih lanjut mengenai {page_title} di IndoInves.")
                fe.published(mod_time)

    # Simpan Sitemap.xml
    rough_string = ET.tostring(urlset, encoding="utf-8")
    reparsed = minidom.parseString(rough_string)
    pretty_xml = reparsed.toprettyxml(indent="  ")
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(pretty_xml)
    print("Berhasil membuat: sitemap.xml")

    # Simpan RSS & Atom Feed
    fg.rss_file('rss.xml', pretty=True)
    print("Berhasil membuat: rss.xml")
    
    fg.atom_file('atom.xml', pretty=True)
    print("Berhasil membuat: atom.xml")

if __name__ == "__main__":
    generate_sitemap_all()

    # Tambahkan baris ini di dalam fungsi utama generate_sitemap_all.py Anda
robots_content = """User-agent: *
Allow: /

Sitemap: https://indoinves.github.io/sitemap.xml
"""

with open("robots.txt", "w", encoding="utf-8") as f:
    f.write(robots_content)
print("Berhasil membuat: robots.txt")
