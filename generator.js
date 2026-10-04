const fs = require('fs');
const path = require('path');

const categories = [
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

console.log("Memulai pembuatan direktori dan file HTML dengan Node.js...");

categories.forEach(cat => {
    const dirPath = path.join('blog', cat);
    if (!fs.existsSync(dirPath)) {
        fs.mkdirSync(dirPath, { recursive: true });
    }
    console.log(`Membuat direktori: ${dirPath}/`);

    for (let i = 1; i <= 30; i++) {
        const capitalizedCat = cat.charAt(0).toUpperCase() + cat.slice(1);
        const titleSlug = `${capitalizedCat} Article ${i} - Global Market, Finance & Business News`;
        const filePath = path.join(dirPath, `artikel${i}.html`);

        const html = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>${titleSlug} | Indoinves</title>
</head>
<body>
    <h1>${titleSlug}</h1>
    <p>Insights on ${cat} article ${i}.</p>
</body>
</html>`;

        fs.writeFileSync(filePath, html, 'utf8');
    }
    console.log(`-> Berhasil membuat 30 artikel untuk kategori: ${cat}`);
});

console.log("\nSelesai! Seluruh file berhasil dibuat via Node.js.");
