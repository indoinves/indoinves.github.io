import { readFileSync, writeFileSync, readdirSync, statSync } from "fs";
import { join } from "path";

// Fungsi rekursif untuk mendapatkan semua file HTML di dalam folder (pengganti cup.getAllFilePaths)
function getAllHtmlFiles(dir, fileList = []) {
    const files = readdirSync(dir);
    for (const file of files) {
        const filePath = join(dir, file);
        if (statSync(filePath).isDirectory()) {
            getAllHtmlFiles(filePath, fileList);
        } else if (filePath.endsWith(".html")) {
            fileList.push(filePath);
        }
    }
    return fileList;
}

try {
    console.log("Memulai penyisipan kode AdSense untuk indoinves.github.io...");
    
    const data = getAllHtmlFiles("dist");
    const adsenseScript = `<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8423475960451668" crossorigin="anonymous"></script>`;

    let count = 0;
    for (let x of data) {
        let isi = readFileSync(x, "utf-8");

        // Cek apakah kode AdSense sudah ada agar tidak terpasang dua kali
        if (!isi.includes("ca-pub-8423475960451668")) {
            // Sisipkan sebelum tag </head> agar lebih valid secara HTML, atau setelah <head>
            if (isi.includes("</head>")) {
                isi = isi.replace("</head>", `  ${adsenseScript}\n</head>`);
            } else if (isi.includes("<head>")) {
                isi = isi.replace("<head>", `<head>\n  ${adsenseScript}`);
            }
            
            writeFileSync(x, isi, "utf-8");
            count++;
        }
    }

    console.log(`Berhasil! Kode AdSense telah disisipkan ke dalam ${count} file HTML.`);
} catch (error) {
    console.error("Terjadi kesalahan saat menyisipkan AdSense:", error);
}
