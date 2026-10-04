import 'dart:io';
import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';

void main() {
  runApp(const IndoinvesApp());
}

class IndoinvesApp extends StatelessWidget {
  const IndoinvesApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Indoinves - Global Market, Finance & Business News',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        primarySwatch: Colors.blue,
        scaffoldBackgroundColor: const Color(0xFFF9F9F9),
        fontFamily: 'Arial',
      ),
      home: const HomePage(),
    );
  }
}

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  bool _isGenerating = false;
  String _statusMessage = '';

  final List<String> categories = [
    "market", "finance", "macro", "micro", "economy", "explainers", "manufacturing", 
    "property", "health", "education", "lifestyle", "hospitality", "tech", "media", 
    "smes", "luxury", "whos-who", "international", "local-resources", "politics", 
    "culture", "science", "public-policy", "business", "news", "sports", "arts", 
    "celebrities", "automotive", "commentary", "interview", "money", "perbankan", 
    "belanja", "sharia", "football", "opinion", "video", "kisah", "index", "sejarah", 
    "entrepreneur", "research", "photo", "olahraga", "selebritis", "country", "dki", 
    "diy", "jabar", "jatim", "jateng", "aceh", "papua", "kalimantan", "sumatra", 
    "sulawesi", "bali", "asia", "afrika", "australia", "rusia", "eropa", "amerika", 
    "ai", "teknologi", "astronomi", "zodiak", "maps"
  ];

  // Fungsi otomatis pembuat folder & file HTML
  Future<void> _generateFiles() async {
    if (kIsWeb) {
      setState(() {
        _statusMessage = "Generasi file file-system tidak didukung langsung di Flutter Web. Jalankan di Desktop/CLI.";
      });
      return;
    }

    setState(() {
      _isGenerating = true;
      _statusMessage = "Memulai pembuatan direktori dan file artikel...";
    });

    try {
      for (String cat in categories) {
        String dirName = "blog/$cat";
        Directory dir = Directory(dirName);
        if (!await dir.exists()) {
          await dir.create(recursive: true);
        }

        for (int i = 1; i <= 30; i++) {
          String titleSlug = "${cat[0].toUpperCase()}${cat.substring(1)} Article $i - Global Insights & Analysis";
          String filePath = "blog/$cat/artikel$i.html";
          
          String htmlContent = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>$titleSlug | Indoinves</title>
    <meta name="description" content="Read comprehensive analysis on $cat artikel $i covering global market trends, expert commentary, and strategic insights." />
    <meta name="keywords" content="$cat, Indoinves, Global Market, Finance, Business News" />
    <link rel="manifest" href="https://indoinves.github.io/manifest.json" />
    <link rel="icon" href="https://indoinves.github.io/indoinves.png" type="image/png" />
    <link rel="apple-touch-icon" sizes="180x180" href="/indoinves.jpg">
<link rel="icon" type="image/png" sizes="32x32" href="/indoinves.jpg">
<link rel="icon" type="image/png" sizes="16x16" href="/indoinves.jpg">
<link rel="apple-touch-icon" sizes="180x180" href="/indoinves.png">
<link rel="icon" type="image/png" sizes="32x32" href="/indoinves.png">
<link rel="icon" type="image/png" sizes="16x16" href="/indoinves.png">
<link rel="apple-touch-icon" sizes="180x180" href="https://indoinves.github.io/indoinves.jpg">
<link rel="icon" type="image/png" sizes="32x32" href="https://indoinves.github.io/indoinves.jpg">
<link rel="icon" type="image/png" sizes="16x16" href="https://indoinves.github.io/indoinves.jpg">
<link rel="apple-touch-icon" sizes="180x180" href="https://indoinves.github.io/indoinves.png">
<link rel="icon" type="image/png" sizes="32x32" href="https://indoinves.github.io/indoinves.png">
<link rel="icon" type="image/png" sizes="16x16" href="https://indoinves.github.io/indoinves.png">
<link rel="manifest" href="/site.webmanifest">

    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8423475960451668" crossorigin="anonymous"></script>
    <meta name="google-adsense-account" content="ca-pub-8423475960451668">
    <meta name="google-site-verification" content="U1VAgdRlZJWlLXGlGnsAGbZA1TVBp2DG0c6XzQJNonY" />
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />


</head>
<body>
    <h1>$titleSlug</h1>
    <p>Category: $cat - Article Number: $i</p>
    <p>Indoinves is an authoritative digital publication delivering high-impact news and market intelligence.</p>

    <!-- Footer -->
    <footer>
        <div class="footer-container">
            <div class="footer-col">
                <img src="https://indoinves.github.io/indoinves.png" alt="Indoinves Logo" style="height: 35px; margin-bottom: 15px; filter: brightness(0) invert(1);">
                <p>Indoinves is an authoritative digital publication delivering high-impact news, macroeconomic analysis, financial market intelligence, and structural business insights to a worldwide readership.</p>
            </div>

            <div class="footer-col">
                <h4>Tools Free Indoinves</h4>
                <ul>
                    <li><a href="https://indoinves.github.io/tools/banklocator.html">Tools Peta & Direktori Bank Global</a></li>
                    <li><a href="https://indoinves.github.io/tools/contentblog.html">Tools Konten Blog</a></li>
                    <li><a href="https://indoinves.github.io/tools/investasi.html">Tools Kalkulator Investasi</a></li>
                    <li><a href="https://indoinves.github.io/tools/saham.html">Tools Saham</a></li>
                    <li><a href="https://indoinves.github.io/tools/simulatorkripto-pro.html">Tools Simulator Kripto Pro</a></li>
                    <li><a href="https://indoinves.github.io/tools/simulatorkripto.html">Tools Simulator Kripto</a></li>
                    <li><a href="https://indoinves.github.io/tools/simulatorsaham.html">Tools Simulator Saham</a></li>
                    <li><a href="https://indoinves.github.io/tools/website.html">Tools Website / SEO Checker</a></li>
                </ul>
                
                <!-- Unit Iklan Autorelaxed AdSense -->
                <div style="margin: 25px 0;">
                    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8423475960451668" crossorigin="anonymous"></script>
                    <ins class="adsbygoogle"
                    style="display:block"
                    data-ad-format="autorelaxed"
                    data-ad-client="ca-pub-8423475960451668"
                    data-ad-slot="7183276396"></ins>
                    <script>
                    (adsbygoogle = window.adsbygoogle || []).push({});
                    </script>
                </div>
            </div>

            <div class="footer-col">
                <h4>Quick Links</h4>
                <ul>
                    <li><a href="https://indoinves.github.io/">Home</a></li>
                    <li><a href="https://indoinves.github.io/about">About Us</a></li>
                    <li><a href="https://indoinves.github.io/contact">Contact Us</a></li>
                    <li><a href="https://indoinves.github.io/privacy">Privacy Policy</a></li>
                    <li><a href="https://indoinves.github.io/sitemap">Sitemap</a></li>
                </ul>
            </div>

            <div class="footer-col">
                <h4>Policies & Editorial</h4>
                <ul>
                    <li><a href="https://indoinves.github.io/disclaimer">Disclaimer</a></li>
                    <li><a href="https://indoinves.github.io/terms">Terms On Conditional License</a></li>
                    <li><a href="https://indoinves.github.io/editorial">Editorial Guidelines</a></li>
                    <li><a href="https://indoinves.github.io/advertise">Advertise With Us</a></li>
                </ul>
            </div>

            <div class="footer-col">
                <h4>Community & Careers</h4>
                <ul>
                    <li><a href="https://indoinves.github.io/join-team">Join the Team</a></li>
                    <li><a href="https://indoinves.github.io/contact-forum">Contact Forum</a></li>
                    <li><a href="https://indoinves.github.io/community">Komunitas Indoinves</a></li>
                </ul>
                
                <!-- Unit Iklan Banner AdSense -->
                <div style="margin: 25px 0;">
                    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8423475960451668" crossorigin="anonymous"></script>
                    <ins class="adsbygoogle"
                    style="display:block"
                    data-ad-client="ca-pub-8423475960451668"
                    data-ad-slot="6147545291"
                    data-ad-format="auto"
                    data-full-width-responsive="true"></ins>
                    <script>
                    (adsbygoogle = window.adsbygoogle || []).push({});
                    </script>
                </div>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2026 Indoinves - All Rights Reserved. Secured via HTTPS.</p>
        </div>
    </footer>

</body>
</html>""";

          File file = File(filePath);
          await file.writeAsString(htmlContent);
        }
      }
      setState(() {
        _statusMessage = "Berhasil! Seluruh ${categories.length * 30} file artikel berhasil dibuat.";
        _isGenerating = false;
      });
    } catch (e) {
      setState(() {
        _statusMessage = "Terjadi kesalahan: $e";
        _isGenerating = false;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: const Color(0xFF111111),
        title: Row(
          children: [
            const Text('Indoinves', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
            const SizedBox(width: 20),
            Expanded(
              child: Container(
                height: 35,
                decoration: BoxDecoration(
                  color: Colors.white,
                  borderRadius: BorderRadius.circular(4),
                ),
                child: const TextField(
                  decoration: InputDecoration(
                    hintText: 'Search news, markets...',
                    border: InputBorder.none,
                    contentPadding: EdgeInsets.symmetric(horizontal: 10, vertical: 8),
                    prefixIcon: Icon(Icons.search, size: 20),
                  ),
                ),
              ),
            ),
          ],
        ),
      ),
      body: SingleChildScrollView(
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // Navigasi Bar Kategori
            Container(
              color: const Color(0xFF222222),
              padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 10),
              child: SingleChildScrollView(
                scrollDirection: Axis.horizontal,
                child: Row(
                  children: categories.map((cat) {
                    return Padding(
                      padding: const EdgeInsets.symmetric(horizontal: 8.0),
                      child: InkWell(
                        onTap: () {},
                        child: Text(
                          cat.toUpperCase(),
                          style: const TextStyle(color: Colors.white, fontSize: 13, fontWeight: FontWeight.w500),
                        ),
                      ),
                    );
                  }).toList(),
                ),
              ),
            ),

            // Konten Utama Dashboard Generator
            Padding(
              padding: const EdgeInsets.all(24.0),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  const Text(
                    'Indoinves Flutter Automated Publishing Dashboard',
                    style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold, color: Colors.black87),
                  ),
                  const SizedBox(height: 10),
                  const Text(
                    'Kelola direktori kategori, buat 30 halaman per kategori secara otomatis, dan siapkan file repository GitHub Anda.',
                    style: TextStyle(fontSize: 14, color: Colors.black54),
                  ),
                  const SizedBox(height: 20),
                  
                  // Tombol Eksekusi Generator
                  ElevatedButton.icon(
                    onPressed: _isGenerating ? null : _generateFiles,
                    icon: const Icon(Icons.play_arrow),
                    label: Text(_isGenerating ? 'Sedang Memproses...' : 'Generate 30 Halaman Semua Kategori'),
                    style: ElevatedButton.styleFrom(
                      backgroundColor: const Color(0xFF0056b3),
                      foregroundColor: Colors.white,
                      padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 12),
                    ),
                  ),
                  const SizedBox(height: 15),
                  if (_statusMessage.isNotEmpty)
                    Container(
                      padding: const EdgeInsets.all(12),
                      decoration: BoxDecoration(
                        color: Colors.blue.shade50,
                        border: Border.all(color: Colors.blue.shade200),
                        borderRadius: BorderRadius.circular(4),
                      ),
                      child: Text(_statusMessage, style: const TextStyle(color: Colors.blueAccent)),
                    ),

                  const SizedBox(height: 30),
                  const Divider(),
                  const SizedBox(height: 20),

                  // Daftar Grid Kategori
                  const Text('Daftar Kategori Aktif (${categories.length} Kategori x 30 Artikel)',
                      style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
                  const SizedBox(height: 15),

                  GridView.builder(
                    shrinkWrap: true,
                    physics: const NeverScrollableScrollPhysics(),
                    gridDelegate: const SliverGridDelegateWithMaxCrossAxisExtent(
                      maxCrossAxisExtent: 200,
                      childAspectRatio: 3,
                      crossAxisSpacing: 10,
                      mainAxisSpacing: 10,
                    ),
                    itemCount: categories.length,
                    itemBuilder: (context, index) {
                      return Container(
                        alignment: Alignment.center,
                        decoration: BoxDecoration(
                          color: Colors.white,
                          border: Border.all(color: Colors.grey.shade300),
                          borderRadius: BorderRadius.circular(4),
                        ),
                        child: Text(
                          categories[index].toUpperCase(),
                          style: const TextStyle(fontWeight: FontWeight.w600, fontSize: 12),
                        ),
                      );
                    },
                  ),
                ],
              ),
            ),

            // Footer Identik
            Container(
              color: const Color(0xFF1A1A1A),
              padding: const EdgeInsets.all(30),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  const Text('Indoinves', style: TextStyle(color: Colors.white, fontSize: 18, fontWeight: FontWeight.bold)),
                  const SizedBox(height: 10),
                  const Text(
                    'Indoinves is an authoritative digital publication delivering high-impact news, macroeconomic analysis, financial market intelligence, and structural business insights to a worldwide readership.',
                    style: TextStyle(color: Colors.grey, fontSize: 13),
                  ),
                  const SizedBox(height: 20),
                  const Divider(color: Colors.grey),
                  const SizedBox(height: 10),
                  Center(
                    child: const Text(
                      '© 2026 Indoinves - All Rights Reserved. Secured via HTTPS.',
                      style: TextStyle(color: Colors.grey, fontSize: 12),
                    ),
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}
