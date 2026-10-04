require 'fileutils'

categories = [
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
]

footer_html = <<-FOOTER
<footer>
    <div class="footer-container">
        <div class="footer-col">
            <img src="https://indoinves.github.io/indoinves.png" alt="Indoinves Logo" style="height: 35px; margin-bottom: 15px; filter: brightness(0) invert(1);">
            <p>Indoinves is an authoritative digital publication delivering high-impact news, macroeconomic analysis, financial market intelligence, and structural business insights to a worldwide readership.</p>
        </div>
        <div class="footer-col">
            <h4>Quick Links</h4>
            <ul>
                <li><a href="https://indoinves.github.io/">Home</a></li>
                <li><a href="https://indoinves.github.io/about">About Us</a></li>
                <li><a href="https://indoinves.github.io/contact">Contact Us</a></li>
            </ul>
        </div>
    </div>
    <div class="footer-bottom">
        <p>&copy; 2026 Indoinves - All Rights Reserved.</p>
    </div>
</footer>
FOOTER

puts "Memulai pembuatan direktori dan file HTML dengan Ruby..."

categories.each do |cat|
  dir_path = "blog/#{cat}"
  FileUtils.mkdir_p(dir_path)
  puts "Membuat direktori: #{dir_path}/"

  (1..30).each do |i|
    capitalized_cat = cat.capitalize
    title_slug = "#{capitalized_cat} Article #{i} - Global Market, Finance & Business News"
    file_path = "#{dir_path}/artikel#{i}.html"

    html_content = <<-HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>#{titleSlug} | Indoinves</title>
</head>
<body>
    <header><h1>#{titleSlug}</h1></header>
    <main>
        <p>Comprehensive publication focusing on <strong>#{cat}</strong>.</p>
    </main>
    #{footer_html}
</body>
</html>
    HTML

    File.write(file_path, html_content)
  end
  puts "-> Berhasil membuat 30 artikel untuk kategori: #{cat}"
end

puts "\nSelesai! Seluruh file berhasil dibuat via Ruby."
