from flask import Flask, redirect, render_template_string, request, url_for, jsonify
from supabase import Client, create_client
import paypalrestsdk

app = Flask(__name__)

# Kredensial Supabase Anda
SUPABASE_URL = "https://tdiubbgueasfhmcmmahq.supabase.co"
SUPABASE_ANON_KEY = "sb_publishable_73oZ-U6TFidIXEP5uYSpkw_v0OSvs8S"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)

# Konfigurasi PayPal SDK (Gunakan mode 'sandbox' untuk uji coba, 'live' untuk produksi)
paypalrestsdk.configure({
    "mode": "sandbox",  # ganti ke "live" jika sudah siap produksi
    "client_id": "BAAGkRZXLxjNS5S3NiNypJRoGTyWqcsiWxxJt_-JKD2XqsRpCKjH-0SriOw3clU96j7AIEymXQzYsPFVAU",
    "client_secret": "EBUPteGteGmnI1f2auq_zIQPc1MoqsvijbN3hqfYGm8Q-JpC2DZlvkUfO0rxM3y6NI3-fvpZHwd4N5jy"
})

# Template HTML Utama dengan Modal Popup PayPal $100 & Integrasi Indoinves
OPEN_INDEX_HTML = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IndoInves - Platform Pintar Investasi & Keuangan</title>
    <meta name="description" content="Platform digital untuk merencanakan investasi, mengelola keuangan, mengakses kalkulator finansial, serta memantau simulasi saham dan kripto.">
    <meta name="keywords" content="investasi, keuangan, saham, kripto, kalkulator investasi, simulator saham, indoinves">
    <meta name="author" content="IndoInves Team">
    
    <!-- Open Graph Meta Tags -->
    <meta property="og:title" content="IndoInves - Platform Pintar Investasi & Keuangan">
    <meta property="og:description" content="Akses berbagai tools finansial, simulator saham, kripto, dan kalkulator investasi gratis di sini.">
    <meta property="og:image" content="https://indoinves.github.io/img/indoinves.png">
    <meta property="og:url" content="https://indoinves.github.io/">
    <meta property="og:type" content="website">

    <!-- Favicon -->
    <link rel="icon" type="image/png" href="https://indoinves.github.io/img/indoinves.png">

    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-slate-900 text-white min-h-screen flex flex-col justify-between">

    <!-- Header / Navbar -->
    <header class="bg-slate-800 border-b border-slate-700 p-4 shadow-md">
        <div class="max-w-6xl mx-auto flex justify-between items-center">
            <h1 class="text-xl font-bold tracking-wider text-blue-400">Indoinves Portal</h1>
            <nav class="space-x-4">
                <a href="/" class="hover:text-blue-400 transition">Beranda</a>
                <a href="/tentang" class="hover:text-blue-400 transition">Tentang</a>
                <button onclick="openModal()" class="bg-blue-600 hover:bg-blue-500 px-4 py-2 rounded-lg text-sm font-semibold shadow transition">Top Up $100</button>
            </nav>
        </div>
    </header>

    <!-- Main Content -->
    <main class="max-w-4xl mx-auto p-6 text-center my-auto">
        <div class="bg-slate-800 border border-slate-700 rounded-2xl p-8 shadow-xl">
            <h2 class="text-3xl font-extrabold mb-4">Selamat Datang di Indoinves</h2>
            <p class="text-slate-400 mb-6">Platform investasi & transaksi terpercaya. Dapatkan kemudahan top up saldo instan.</p>
            <button onclick="openModal()" class="bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-500 hover:to-indigo-500 text-white font-bold px-8 py-3 rounded-xl shadow-lg transform hover:-translate-y-0.5 transition">
                Buka Promo Top Up PayPal $100
            </button>
        </div>
    </main>

    <!-- Modal Popup PayPal Top Up $100 -->
    <div id="paypalModal" class="fixed inset-0 bg-black/70 backdrop-blur-sm flex items-center justify-center z-50 hidden">
        <div class="bg-slate-800 border border-slate-700 rounded-2xl max-w-md w-full p-6 relative shadow-2xl animate-fade-in">
            <!-- Close Button -->
            <button onclick="closeModal()" class="absolute top-4 right-4 text-slate-400 hover:text-white text-xl font-bold">&times;</button>
            
            <!-- Image / Icon Header -->
            <div class="text-center mb-4">
                <img src="https://www.paypalobjects.com/webstatic/mktg/logo/pp_cc_mark_37x23.jpg" alt="PayPal Logo" class="mx-auto mb-2 h-10 object-contain rounded">
                <h3 class="text-2xl font-bold text-blue-400">Top Up PayPal $100.00</h3>
                <p class="text-xs text-slate-400 mt-1">Isi saldo instan aman & terpercaya via sistem Indoinves</p>
            </div>

            <!-- Detail Paket -->
            <div class="bg-slate-900/60 p-4 rounded-xl mb-5 border border-slate-700/50 flex items-center justify-between">
                <div>
                    <span class="text-sm text-slate-400 block">Nominal</span>
                    <span class="text-lg font-bold text-emerald-400">$100.00 USD</span>
                </div>
                <div class="text-right">
                    <span class="text-sm text-slate-400 block">Status Biaya</span>
                    <span class="text-xs bg-blue-500/20 text-blue-300 px-2 py-1 rounded">Bebas Admin</span>
                </div>
            </div>

            <!-- Form Aksi -->
            <form action="/create-paypal-payment" method="POST">
                <div class="mb-4">
                    <label class="block text-xs uppercase tracking-wider text-slate-400 mb-2">Email Akun PayPal Tujuan</label>
                    <input type="email" name="paypal_email" required placeholder="nama@domain.com" class="w-full bg-slate-900 border border-slate-700 rounded-lg px-4 py-2.5 text-white focus:outline-none focus:border-blue-500">
                </div>
                <button type="submit" class="w-full bg-blue-600 hover:bg-blue-500 text-white font-semibold py-3 rounded-xl shadow transition">
                    Lanjutkan Pembayaran $100
                </button>
            </form>
        </div>
    </div>

    <!-- Footer -->
    <footer class="bg-slate-800 border-t border-slate-700 text-center p-4 text-sm text-slate-400">
        &copy; 2026 <a href="https://indoinves.github.io/" class="text-blue-400 hover:underline">Indoinves</a>. All rights reserved.
    </footer>

    <!-- Script Kontrol Popup -->
    <script>
        function openModal() {
            document.getElementById('paypalModal').classList.remove('hidden');
        }
        function closeModal() {
            document.getElementById('paypalModal').classList.add('hidden');
        }
    </script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(OPEN_INDEX_HTML)

# Rute dinamis untuk mencakup semua sub-direktori / file path
@app.route("/<path:subpath>")
def dynamic_directory(subpath):
    return render_template_string(OPEN_INDEX_HTML)

# Endpoint Pemrosesan Pembayaran PayPal
@app.route("/create-paypal-payment", methods=["POST"])
def create_paypal_payment():
    paypal_email = request.form.get("paypal_email")
    
    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"
        },
        "redirect_urls": {
            "return_url": url_for("paypal_execute", _external=True),
            "cancel_url": url_for("index", _external=True)
        },
        "transactions": [{
            "amount": {
                "total": "100.00",
                "currency": "USD"
            },
            "description": f"Top Up Saldo PayPal $100 untuk akun {paypal_email}"
        }]
    })

    if payment.create():
        for link in payment.links:
            if link.rel == "approval_url":
                return redirect(link.href)
    else:
        return jsonify({"error": payment.error}), 400

@app.route("/paypal-execute")
def paypal_execute():
    payment_id = request.args.get("paymentId")
    payer_id = request.args.get("PayerID")
    
    payment = paypalrestsdk.Payment.find(payment_id)
    if payment.execute({"payer_id": payer_id}):
        return "<h3>Top Up PayPal $100 Berhasil! Transaksi telah dikonfirmasi.</h3><a href='/'>Kembali ke Beranda</a>"
    else:
        return "<h3>Pembayaran Gagal</h3><a href='/'>Coba Lagi</a>", 400

if __name__ == "__main__":
    app.run(debug=True, port=5000)
