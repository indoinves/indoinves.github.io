using System;
using System.IO;

class Program
{
    static void Main(string[] args)
    {
        string[] categories = {
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
        };

        Console.WriteLine("Memulai pembuatan direktori dan file HTML dengan C# .NET...");

        foreach (var cat in categories)
        {
            string dirPath = Path.Combine("blog", cat);
            Directory.CreateDirectory(dirPath);
            Console.WriteLine($"Membuat direktori: {dirPath}/");

            for (int i = 1; i <= 30; i++)
            {
                string capitalizedCat = char.ToUpper(cat[0]) + cat.Substring(1);
                string titleSlug = $"{capitalizedCat} Article {i} - Global Market, Finance & Business News";
                string filePath = Path.Combine(dirPath, $"artikel{i}.html");

                string html = $@"<!DOCTYPE html>
<html lang=""en"">
<head>
    <meta charset=""UTF-8"">
    <title>{titleSlug} | Indoinves</title>
</head>
<body>
    <h1>{titleSlug}</h1>
    <p>Insights on {cat} article {i}.</p>
</body>
</html>";

                File.WriteAllText(filePath, html);
            }
            Console.WriteLine($"-> Berhasil membuat 30 artikel untuk kategori: {cat}");
        }

        Console.WriteLine("\nSelesai! Seluruh file berhasil dibuat via .NET NuGet ecosystem.");
    }
}
