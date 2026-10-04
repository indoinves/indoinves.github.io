<?php
// index.php - Halaman Utama Indoinves
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Indoinves - Global Market, Finance & Business News</title>
    <meta name="description" content="Indoinves delivers authoritative insights on global markets, finance, macro economy, business news, and structural financial analysis." />
    <meta name="keywords" content="Indoinves, Business News, Macro Economy, Market & Finance, Tech, Investment Tools" />
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8423475960451668" crossorigin="anonymous"></script>
    <meta name="google-adsense-account" content="ca-pub-8423475960451668">
    <meta name="google-site-verification" content="U1VAgdRlZJWlLXGlGnsAGbZA1TVBp2DG0c6XzQJNonY" />
    
    <!-- Open Graph Meta Tags -->
    <meta property="og:title" content="Indoinves - Global Market, Finance & Business News" />
    <meta property="og:description" content="Authoritative digital publication delivering high-impact news and financial market intelligence." />
    <meta property="og:image" content="https://indoinves.github.io/indoinves.jpg" />
    <meta property="og:url" content="https://indoinves.github.io/" />
    <meta property="og:type" content="website" />

    <!-- Manifest & Favicon -->
    <link rel="manifest" href="https://indoinves.github.io/manifest.json" />
    <link rel="icon" href="https://indoinves.github.io/indoinves.png" type="image/png" />

    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f9f9f9; color: #333; line-height: 1.6; }
        header { background: #111; color: #fff; padding: 15px 0; }
        .header-container { width: 90%; max-width: 1200px; margin: auto; display: flex; justify-content: space-between; align-items: center; }
        .logo-container img { height: 40px; }
        .search-box input { padding: 8px; width: 200px; border-radius: 4px; border: none; }
        nav { background: #222; color: #fff; }
        .nav-wrap { width: 90%; max-width: 1200px; margin: auto; display: flex; }
        .nav-container { list-style: none; padding: 0; margin: 0; display: flex; flex-wrap: wrap; }
        .nav-container li a { color: #fff; text-decoration: none; padding: 15px; display: block; font-size: 14px; }
        .nav-container li a:hover { background: #444; }
        
        .main-container { width: 90%; max-width: 1200px; margin: 30px auto; display: flex; gap: 30px; }
        .content-area { flex: 3; background: #fff; padding: 30px; box-shadow: 0 2px 5px rgba(0,0,0,0.05); }
        .sidebar { flex: 1; display: flex; flex-direction: column; gap: 20px; }
        
        .hero { background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url('https://indoinves.github.io/indoinves.jpg') center/cover; color: #fff; padding: 60px 30px; border-radius: 6px; margin-bottom: 30px; }
        .hero h1 { font-size: 36px; margin-top: 0; }
        .hero p { font-size: 18px; }

        .categories-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); gap: 10px; margin-top: 20px; }
        .categories-grid a { background: #f1f1f1; padding: 10px 15px; text-align: center; color: #0056b3; text-decoration: none; border-radius: 4px; font-size: 14px; transition: background 0.2s; }
        .categories-grid a:hover { background: #0056b3; color: #fff; }

        .widget { background: #fff; padding: 20px; box-shadow: 0 2px 5px rgba(0,0,0,0.05); }
        .widget h3 { border-bottom: 2px solid #0056b3; padding-bottom: 8px; margin-top: 0; color: #111; font-size: 18px; }
        .widget ul { padding-left: 20px; margin: 0; }
        .widget li { margin-bottom: 8px; font-size: 14px; }
        .widget a { color: #0056b3; text-decoration: none; }
        .widget a:hover { text-decoration: underline; }

        footer { background: #1a1a1a; color: #fff; padding: 40px 0 20px 0; margin-top: 50px; }
        .footer-container { width: 90%; max-width: 1200px; margin: auto; display: flex; flex-wrap: wrap; justify-content: space-between; gap: 20px; }
        .footer-col { flex: 1; min-width: 200px; }
        .footer-col h4 { color: #fff; margin-bottom: 15px; font-size: 16px; }
        .footer-col ul { list-style: none; padding: 0; margin: 0; }
        .footer-col li { margin-bottom: 8px; }
        .footer-col a { color: #ccc; text-decoration: none; font-size: 13px; }
        .footer-col a:hover { color: #fff; }
        .footer-bottom { text-align: center; border-top: 1px solid #333; margin-top: 30px; padding-top: 15px; font-size: 13px; color: #aaa; }
    </style>
</head>
<body>

    <!-- Header -->
    <header>
        <div class="header-container">
            <div class="logo-container">
                <a href="https://indoinves.github.io/">
                    <img src="https://indoinves.github.io/indoinves.png" alt="Indoinves Logo">
                </a>
            </div>
            <div class="search-box">
                <form action="https://indoinves.github.io/" method="GET">
                    <input type="text" placeholder="Search news, markets..." />
                </form>
            </div>
        </div>
    </header>

    <!-- Navigasi Utama -->
    <nav>
        <div class="nav-wrap">
            <ul class="nav-container">
                <li><a href="https://indoinves.github.io/">Home</a></li>
                <li><a href="https://indoinves.github.io/blog/market/">Market</a></li>
                <li><a href="https://indoinves.github.io/blog/finance/">Finance</a></li>
                <li><a href="https://indoinves.github.io/blog/macro/">Macro</a></li>
                <li><a href="https://indoinves.github.io/blog/economy/">Economy</a></li>
                <li><a href="https://indoinves.github.io/blog/tech/">Tech</a></li>
                <li><a href="https://indoinves.github.io/blog/property/">Property</a></li>
            </ul>
        </div>
    </nav>

    <div class="main-container">
        <!-- Main Content Area -->
        <main class="content-area">
            <div class="hero">
                <h1>Welcome to Indoinves</h1>
                <p>Delivering high-impact news, macroeconomic analysis, financial market intelligence, and structural business insights.</p>
            </div>

            <h2>Featured Articles</h2>
            <ul>
                <li><a href="blog/market/artikel1.html">Market Article 1 - Global Market, Finance & Business News</a></li>
                <li><a href="blog/finance/artikel1.html">Finance Article 1 - Global Market, Finance & Business News</a></li>
                <li><a href="blog/macro/artikel1.html">Macro Article 1 - Global Market, Finance & Business News</a></li>
                <li><a href="blog/economy/artikel1.html">Economy Article 1 - Global Market, Finance & Business News</a></li>
                <li><a href="blog/tech/artikel1.html">Tech Article 1 - Global Market, Finance & Business News</a></li>
            </ul>

            <h2>Explore All Categories</h2>
            <div class="categories-grid">
                <?php
                $categories = [
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

                foreach ($categories as $cat) {
                    $displayName = ucwords(str_replace('-', ' ', $cat));
                    echo '<a href="blog/' . $cat . '/artikel1.html">' . htmlspecialchars($displayName) . '</a>';
                }
                ?>
            </div>
        </main>

        <!-- Sidebar -->
        <aside class="sidebar">
            <div class="widget">
                <h3>Free Financial Tools</h3>
                <ul>
                    <li><a href="https://indoinves.github.io/tools/investasi.html">Tools Kalkulator Investasi</a></li>
                    <li><a href="https://indoinves.github.io/tools/saham.html">Tools Saham</a></li>
                    <li><a href="https://indoinves.github.io/tools/simulatorkripto-pro.html">Tools Simulator Kripto Pro</a></li>
                    <li><a href="https://indoinves.github.io/tools/banklocator.html">Tools Peta & Direktori Bank Global</a></li>
                </ul>
            </div>

            <div class="widget">
                <h3>Quick Links</h3>
                <ul>
                    <li><a href="https://indoinves.github.io/about">About Us</a></li>
                    <li><a href="https://indoinves.github.io/contact">Contact Us</a></li>
                    <li><a href="https://indoinves.github.io/privacy">Privacy Policy</a></li>
                    <li><a href="https://indoinves.github.io/sitemap">Sitemap</a></li>
                </ul>
            </div>
        </aside>
    </div>

    <!-- Footer Lengkap Sesuai Permintaan -->
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
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2026 Indoinves - All Rights Reserved. Secured via HTTPS.</p>
        </div>
    </footer>

</body>
</html>
