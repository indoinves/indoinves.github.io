/**
 * IndoInves - CLI Input/Output Manager (Node.js)
 * Mengelola interaksi pembacaan dan penyimpanan data konfigurasi JSON via terminal.
 */

const fs = require('fs');
const readline = require('readline');

const CONFIG_FILE = 'config.json';

// Inisialisasi antarmuka input/output terminal
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function displayMenu() {
    console.log("\n==========================================");
    console.log("       INDOINVES - I/O MANAGER CLI        ");
    console.log("==========================================");
    console.log("1. Lihat Info Platform (dari config.json)");
    console.log("2. Tampilkan Daftar Tools Finansial");
    console.log("3. Tambah Tool Baru ke Konfigurasi");
    console.log("4. Keluar");
    console.log("==========================================");
    
    rl.question("Pilih menu (1-4): ", handleMenu);
}

function handleMenu(choice) {
    switch (choice.trim()) {
        case '1':
            showPlatformInfo();
            break;
        case '2':
            showToolsList();
            break;
        case '3':
            addNewToolPrompt();
            break;
        case '4':
            console.log("Terima kasih telah menggunakan IndoInves I/O Manager!");
            rl.close();
            break;
        default:
            console.log("Pilihan tidak valid. Silakan coba lagi.");
            displayMenu();
            break;
    }
}

function loadConfig() {
    if (!fs.existsSync(CONFIG_FILE)) {
        console.log("File config.json tidak ditemukan!");
        return null;
    }
    const data = fs.readFileSync(CONFIG_FILE, 'utf8');
    return JSON.parse(data);
}

function showPlatformInfo() {
    const config = loadConfig();
    if (!config) return displayMenu();

    console.log("\n--- INFORMASI PLATFORM ---");
    console.log(`Nama      : ${config.platform.name}`);
    console.log(`Tagline   : ${config.platform.tagline}`);
    console.log(`URL Utama : ${config.platform.baseUrl}`);
    console.log(`Pembuat   : ${config.platform.author}`);
    displayMenu();
}

function showToolsList() {
    const config = loadConfig();
    if (!config) return displayMenu();

    console.log("\n--- DAFTAR TOOLS FINANSIAL ---");
    config.tools.forEach((tool, index) => {
        console.log(`${index + 1}. [${tool.category}] ${tool.name} -> ${tool.url}`);
    });
    displayMenu();
}

function addNewToolPrompt() {
    rl.question("\nMasukkan nama tool baru: ", (name) => {
        rl.question("Masukkan URL tool baru: ", (url) => {
            rl.question("Masukkan kategori tool: ", (category) => {
                const config = loadConfig();
                if (config) {
                    const newId = name.toLowerCase().replace(/\s+/g, '-');
                    config.tools.push({
                        id: newId,
                        name: name,
                        url: url,
                        category: category
                    });

                    fs.writeFileSync(CONFIG_FILE, JSON.stringify(config, null, 2), 'utf8');
                    console.log(`\nBerhasil! Tool "${name}" berhasil ditambahkan ke config.json.`);
                }
                displayMenu();
            });
        });
    });
}

// Menjalankan program utama
console.log("Memulai IndoInves I/O Interface...");
displayMenu();
