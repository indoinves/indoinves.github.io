from feedgen.feed import FeedGenerator

def generate_rss_atom():
    # 1. Inisialisasi Feed Generator
    fg = FeedGenerator()
    fg.id('https://indoinves.github.io/')
    fg.title('IndoInves Blog')
    fg.author({'name': 'Admin IndoInves', 'email': 'email@example.com'})
    fg.link(href='https://indoinves.github.io/', rel='alternate')
    fg.logo('https://indoinves.github.io/favicon.ico')
    fg.subtitle('Update artikel dan informasi terbaru seputar investasi.')
    fg.language('id')

    # 2. Contoh Data Artikel / Postingan Anda
    # (Bisa Anda sesuaikan dengan hasil scanning folder HTML atau database Anda)
    articles = [
        {
            "title": "Cara Memulai Investasi Saham untuk Pemula",
            _id: "https://indoinves.github.io/investasi-saham-pemula.html",
            "link": "https://indoinves.github.io/investasi-saham-pemula.html",
            "description": "Panduan lengkap langkah demi langkah mulai investasi saham dari nol.",
            "date": "2026-06-01T10:00:00+00:00" # Format ISO 8601
        },
        {
            "title": "Analisis Pasar Keuangan Tahun Ini",
            _id: "https://indoinves.github.io/analisis-pasar.html",
            "link": "https://indoinves.github.io/analisis-pasar.html",
            "description": "Ulasan mendalam mengenai tren pasar keuangan global dan domestik.",
            "date": "2026-06-05T14:30:00+00:00"
        }
    ]

    # 3. Masukkan item/artikel ke dalam Feed
    for item in articles:
        fe = fg.add_entry()
        fe.id(item["id"])
        fe.title(item["title"])
        fe.link(href=item["link"])
        fe.description(item["description"])
        fe.published(item["date"])

    # 4. Generate file RSS 2.0 (rss.xml)
    fg.rss_file('rss.xml', pretty=True)
    print("RSS feed berhasil dibuat: rss.xml")

    # 5. Generate file Atom 1.0 (atom.xml)
    fg.atom_file('atom.xml', pretty=True)
    print("Atom feed berhasil dibuat: atom.xml")

if __name__ == '__main__':
    generate_rss_atom()
