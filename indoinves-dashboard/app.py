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
    "client_id": "YOUR_PAYPAL_CLIENT_ID",
    "client_secret": "YOUR_PAYPAL_CLIENT_SECRET"
})


@app.route("/")
def index():
    return render_template_string(OPEN_INDEX_HTML)


@app.route("/admin.html")
def admin_dashboard():
    return render_template_string(ADMIN_HTML_TEMPLATE)


@app.route("/member.html")
def member_dashboard():
    return render_template_string(MEMBER_HTML_TEMPLATE)


# ----------------------------------------------------
# ENDPOINT PAYPAL PAYMENT
# ----------------------------------------------------
@app.route("/create-paypal-payment", methods=["POST"])
def create_paypal_payment():
    data = request.get_json()
    amount = data.get("amount")  # Jumlah dalam USD

    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {"payment_method": "paypal"},
        "redirect_urls": {
            "return_url": url_for("paypal_execute", _external=True),
            "cancel_url": url_for("index", _external=True),
        },
        "transactions": [{
            "amount": {"total": str(amount), "currency": "USD"},
            "description": "Top-up Saldo Indoinves",
        }],
    })

    if payment.create():
        for link in payment.links:
            if link.rel == "approval_url":
                return jsonify({"approval_url": link.href})
        return jsonify({"error": "Approval URL tidak ditemukan"}), 400
    else:
        return jsonify({"error": payment.error}), 400


@app.route("/paypal-execute")
def paypal_execute():
    payment_id = request.args.get("paymentId")
    payer_id = request.args.get("PayerID")

    payment = paypalrestsdk.Payment.find(payment_id)

    if payment.execute({"payer_id": payer_id}):
        return redirect(url_for("member_dashboard"))
    else:
        return "Pembayaran Gagal", 400


# ----------------------------------------------------
# 1. LANDING PAGE & AUTH MODAL (RESPONSIVE)
# ----------------------------------------------------
OPEN_INDEX_HTML = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Indoinves - Platform Investasi & Securities Crowdfunding Terpercaya</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
    <link rel="icon" type="image/png" href="https://indoinves.github.io/img/indoinves.png">
</head>
<body class="bg-slate-950 text-slate-100 font-sans antialiased min-h-screen flex flex-col justify-between">
    <header class="border-b border-slate-800 bg-slate-900/90 backdrop-blur sticky top-0 z-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
            <div class="flex items-center space-x-3">
                <img src="https://indoinves.github.io/img/indoinves.png" alt="Indoinves Logo" class="w-8 h-8 sm:w-10 sm:h-10 object-contain">
                <span class="font-bold text-lg sm:text-xl text-emerald-400 tracking-wide">INDOINVES</span>
            </div>
            <div>
                <button onclick="openAuthModal()" class="bg-emerald-500 hover:bg-emerald-600 text-slate-950 px-3.5 py-2 sm:px-4 rounded-lg font-semibold text-xs sm:text-sm transition shadow">
                    Masuk / Daftar
                </button>
            </div>
        </div>
    </header>

    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 sm:py-20 flex-1 flex flex-col items-center justify-center text-center">
        <h1 class="text-3xl sm:text-5xl font-extrabold tracking-tight max-w-3xl mb-4 sm:mb-6 leading-tight">
            Kembangkan Portofolio Masa Depan Bersama <span class="text-emerald-400">Indoinves</span>
        </h1>
        <p class="text-slate-400 max-w-xl mb-6 sm:mb-8 text-base sm:text-lg px-2">
            Platform investasi dan securities crowdfunding aman, transparan, dan terkurasi untuk pertumbuhan aset finansial Anda.
        </p>
        <button onclick="openAuthModal()" class="bg-emerald-500 hover:bg-emerald-600 text-slate-950 font-bold py-3 px-6 sm:px-8 rounded-xl transition shadow-lg shadow-emerald-500/20 text-sm sm:text-base">
            Mulai Akses Dashboard
        </button>
    </main>

    <!-- Modal Auth Responsif -->
    <div id="authModal" class="fixed inset-0 bg-black/75 backdrop-blur-sm z-50 flex items-center justify-center hidden p-4">
        <div class="bg-slate-900 border border-slate-800 p-6 sm:p-8 rounded-2xl w-full max-w-md relative shadow-2xl">
            <button onclick="closeAuthModal()" class="absolute top-4 right-4 text-slate-400 hover:text-slate-100 text-2xl font-bold">&times;</button>
            <h2 class="text-xl font-bold text-emerald-400 mb-6 text-center">Portal Akun Indoinves</h2>
            <div class="space-y-4">
                <div>
                    <label class="block text-xs text-slate-400 mb-1">Email</label>
                    <input type="email" id="emailInput" placeholder="nama@email.com" class="w-full bg-slate-950 border border-slate-800 rounded-lg px-4 py-2.5 text-sm text-white focus:border-emerald-500 outline-none">
                </div>
                <div>
                    <label class="block text-xs text-slate-400 mb-1">Password</label>
                    <input type="password" id="passwordInput" placeholder="••••••••" class="w-full bg-slate-950 border border-slate-800 rounded-lg px-4 py-2.5 text-sm text-white focus:border-emerald-500 outline-none">
                </div>
                <div class="flex flex-col sm:flex-row gap-3 pt-2">
                    <button onclick="handleLogin()" class="w-full sm:flex-1 bg-emerald-500 hover:bg-emerald-600 text-slate-950 font-bold py-2.5 rounded-lg text-sm transition">Masuk</button>
                    <button onclick="handleRegister()" class="w-full sm:flex-1 bg-slate-800 hover:bg-slate-700 text-slate-200 py-2.5 rounded-lg text-sm border border-slate-700 transition">Daftar</button>
                </div>
            </div>
        </div>
    </div>

    <footer class="border-t border-slate-900 py-6 text-center text-xs text-slate-500">
        &copy; 2026 Indoinves. All rights reserved.
    </footer>

    <script>
        const supabaseClient = supabase.createClient('https://tdiubbgueasfhmcmmahq.supabase.co', 'sb_publishable_73oZ-U6TFidIXEP5uYSpkw_v0OSvs8S');
        function openAuthModal() { document.getElementById('authModal').classList.remove('hidden'); }
        function closeAuthModal() { document.getElementById('authModal').classList.add('hidden'); }

        async function handleLogin() {
            const email = document.getElementById('emailInput').value;
            const password = document.getElementById('passwordInput').value;
            const { data, error } = await supabaseClient.auth.signInWithPassword({ email, password });
            if (error) { alert('Login Gagal: ' + error.message); return; }
            
            const { data: profile } = await supabaseClient.from('profiles').select('role').eq('id', data.user.id).single();
            if (profile && profile.role === 'admin') {
                window.location.href = '/admin.html';
            } else {
                window.location.href = '/member.html';
            }
        }

        async function handleRegister() {
            const email = document.getElementById('emailInput').value;
            const password = document.getElementById('passwordInput').value;
            const { data, error } = await supabaseClient.auth.signUp({ email, password });
            if (error) { alert('Gagal: ' + error.message); return; }
            if (data.user) {
                await supabaseClient.from('profiles').insert([{ id: data.user.id, email: email, role: 'member', saldo: 0 }]);
            }
            alert('Pendaftaran Berhasil! Silakan Masuk.');
        }
    </script>
</body>
</html>
"""

# ----------------------------------------------------
# 2. ADMIN DASHBOARD LENGKAP (RESPONSIVE DENGAN MOBILE SIDEBAR TOGGLE)
# ----------------------------------------------------
ADMIN_HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Dashboard - Indoinves</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
</head>
<body class="bg-slate-950 text-slate-100 font-sans antialiased min-h-screen flex flex-col md:flex-row">

    <!-- Mobile Sidebar Overlay & Sidebar -->
    <aside id="sidebar" class="fixed inset-y-0 left-0 z-50 w-64 bg-slate-900 border-r border-slate-800 flex flex-col justify-between transform -translate-x-full md:translate-x-0 transition-transform duration-300">
        <div class="p-6">
            <div class="flex items-center justify-between mb-8">
                <div class="flex items-center space-x-3">
                    <img src="https://indoinves.github.io/img/indoinves.png" alt="Logo" class="w-8 h-8 object-contain">
                    <span class="font-bold text-lg text-emerald-400">Admin Panel</span>
                </div>
                <!-- Tombol Tutup Sidebar khusus HP -->
                <button onclick="toggleSidebar()" class="md:hidden text-slate-400 hover:text-white text-xl font-bold">&times;</button>
            </div>
            <nav class="space-y-1">
                <button onclick="switchTab('overview'); toggleSidebar();" id="nav-overview" class="w-full flex items-center space-x-3 px-4 py-2.5 rounded-lg text-sm font-medium bg-emerald-500/10 text-emerald-400">📊 <span>Overview</span></button>
                <button onclick="switchTab('users'); toggleSidebar();" id="nav-users" class="w-full flex items-center space-x-3 px-4 py-2.5 rounded-lg text-sm font-medium text-slate-400 hover:bg-slate-800 hover:text-white">👥 <span>Manajemen Member</span></button>
                <button onclick="switchTab('transactions'); toggleSidebar();" id="nav-transactions" class="w-full flex items-center space-x-3 px-4 py-2.5 rounded-lg text-sm font-medium text-slate-400 hover:bg-slate-800 hover:text-white">💳 <span>Persetujuan Top-up</span></button>
                <button onclick="switchTab('projects'); toggleSidebar();" id="nav-projects" class="w-full flex items-center space-x-3 px-4 py-2.5 rounded-lg text-sm font-medium text-slate-400 hover:bg-slate-800 hover:text-white">📈 <span>Proyek Investasi</span></button>
            </nav>
        </div>
        <div class="p-6 border-t border-slate-800">
            <button onclick="logoutAdmin()" class="w-full bg-red-500/10 hover:bg-red-500/20 text-red-400 py-2 rounded-lg text-sm font-semibold transition">Keluar</button>
        </div>
    </aside>

    <!-- Main Content Area -->
    <main class="flex-1 flex flex-col min-w-0 md:ml-64">
        <!-- Topbar Responsif -->
        <header class="bg-slate-900 border-b border-slate-800 h-16 flex items-center justify-between px-4 sm:px-8 sticky top-0 z-30">
            <div class="flex items-center space-x-3">
                <button onclick="toggleSidebar()" class="md:hidden text-slate-300 hover:text-emerald-400 text-xl font-bold focus:outline-none">&#9776;</button>
                <h1 class="text-base sm:text-lg font-bold text-emerald-400 uppercase tracking-wider truncate" id="pageTitle">Overview Statistik</h1>
            </div>
            <a href="/" class="text-xs text-slate-400 hover:text-white underline whitespace-nowrap">Beranda Utama</a>
        </header>

        <div class="p-4 sm:p-8 space-y-6">
            
            <!-- TAB 1: OVERVIEW -->
            <section id="tab-overview" class="space-y-6">
                <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 sm:gap-6">
                    <div class="bg-slate-900 border border-slate-800 p-5 sm:p-6 rounded-xl">
                        <p class="text-sm text-slate-400">Total Member Terdaftar</p>
                        <h3 class="text-2xl sm:text-3xl font-extrabold text-emerald-400 mt-2" id="statTotalUsers">0</h3>
                    </div>
                    <div class="bg-slate-900 border border-slate-800 p-5 sm:p-6 rounded-xl">
                        <p class="text-sm text-slate-400">Total Saldo Member</p>
                        <h3 class="text-2xl sm:text-3xl font-extrabold text-emerald-400 mt-2" id="statTotalSaldo">Rp 0</h3>
                    </div>
                    <div class="bg-slate-900 border border-slate-800 p-5 sm:p-6 rounded-xl">
                        <p class="text-sm text-slate-400">Proyek Aktif</p>
                        <h3 class="text-2xl sm:text-3xl font-extrabold text-emerald-400 mt-2" id="statTotalProjects">0</h3>
                    </div>
                </div>
            </section>

            <!-- TAB 2: USERS MANAGEMENT -->
            <section id="tab-users" class="space-y-4 hidden">
                <div class="bg-slate-900 border border-slate-800 rounded-xl overflow-hidden">
                    <div class="p-4 sm:p-6 border-b border-slate-800"><h3 class="font-bold text-base sm:text-lg">Daftar Akun Member</h3></div>
                    <div class="overflow-x-auto">
                        <table class="w-full text-left text-sm text-slate-300 min-w-[600px]">
                            <thead class="bg-slate-950 text-slate-400 uppercase text-xs">
                                <tr>
                                    <th class="px-6 py-3">Email</th>
                                    <th class="px-6 py-3">Role</th>
                                    <th class="px-6 py-3">Saldo (Rp)</th>
                                    <th class="px-6 py-3">Aksi</th>
                                </tr>
                            </thead>
                            <tbody id="userTableBody" class="divide-y divide-slate-800"></tbody>
                        </table>
                    </div>
                </div>
            </section>

            <!-- TAB 3: TRANSACTIONS MANAGEMENT -->
            <section id="tab-transactions" class="space-y-4 hidden">
                <div class="bg-slate-900 border border-slate-800 rounded-xl overflow-hidden">
                    <div class="p-4 sm:p-6 border-b border-slate-800"><h3 class="font-bold text-base sm:text-lg">Persetujuan Transaksi / Top-Up Pending</h3></div>
                    <div class="overflow-x-auto">
                        <table class="w-full text-left text-sm text-slate-300 min-w-[700px]">
                            <thead class="bg-slate-950 text-slate-400 uppercase text-xs">
                                <tr>
                                    <th class="px-6 py-3">ID Transaksi</th>
                                    <th class="px-6 py-3">User ID</th>
                                    <th class="px-6 py-3">Jumlah</th>
                                    <th class="px-6 py-3">Status</th>
                                    <th class="px-6 py-3">Aksi</th>
                                </tr>
                            </thead>
                            <tbody id="transactionTableBody" class="divide-y divide-slate-800"></tbody>
                        </table>
                    </div>
                </div>
            </section>

            <!-- TAB 4: PROJECTS MANAGEMENT -->
            <section id="tab-projects" class="space-y-6 hidden">
                <div class="bg-slate-900 border border-slate-800 p-5 sm:p-6 rounded-xl space-y-4">
                    <h3 class="font-bold text-base sm:text-lg text-emerald-400">Tambah Proyek Crowdfunding Baru</h3>
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                        <input type="text" id="projTitle" placeholder="Nama Proyek Bisnis" class="bg-slate-950 border border-slate-800 rounded-lg px-4 py-2.5 text-sm text-white outline-none focus:border-emerald-500">
                        <input type="number" id="projTarget" placeholder="Target Dana (Rp)" class="bg-slate-950 border border-slate-800 rounded-lg px-4 py-2.5 text-sm text-white outline-none focus:border-emerald-500">
                        <input type="number" id="projRoi" placeholder="Estimasi ROI (%)" class="bg-slate-950 border border-slate-800 rounded-lg px-4 py-2.5 text-sm text-white outline-none focus:border-emerald-500">
                        <input type="text" id="projDuration" placeholder="Durasi (Contoh: 12 Bulan)" class="bg-slate-950 border border-slate-800 rounded-lg px-4 py-2.5 text-sm text-white outline-none focus:border-emerald-500">
                    </div>
                    <button onclick="createProject()" class="w-full sm:w-auto bg-emerald-500 hover:bg-emerald-600 text-slate-950 font-bold px-6 py-2.5 rounded-lg text-sm transition">Terbitkan Proyek</button>
                </div>

                <div class="bg-slate-900 border border-slate-800 rounded-xl overflow-hidden">
                    <div class="p-4 sm:p-6 border-b border-slate-800"><h3 class="font-bold text-base sm:text-lg">Daftar Proyek Aktif</h3></div>
                    <div class="overflow-x-auto">
                        <table class="w-full text-left text-sm text-slate-300 min-w-[600px]">
                            <thead class="bg-slate-950 text-slate-400 uppercase text-xs">
                                <tr>
                                    <th class="px-6 py-3">Proyek</th>
                                    <th class="px-6 py-3">Target</th>
                                    <th class="px-6 py-3">ROI</th>
                                    <th class="px-6 py-3">Durasi</th>
                                </tr>
                            </thead>
                            <tbody id="projectTableBody" class="divide-y divide-slate-800"></tbody>
                        </table>
                    </div>
                </div>
            </section>

        </div>
    </main>

    <script>
        const supabaseClient = supabase.createClient('https://tdiubbgueasfhmcmmahq.supabase.co', 'sb_publishable_73oZ-U6TFidIXEP5uYSpkw_v0OSvs8S');

        function toggleSidebar() {
            const sidebar = document.getElementById('sidebar');
            sidebar.classList.toggle('-translate-x-full');
        }

        function switchTab(tabName) {
            ['overview', 'users', 'transactions', 'projects'].forEach(t => {
                document.getElementById('tab-' + t).classList.add('hidden');
                document.getElementById('nav-' + t).className = "w-full flex items-center space-x-3 px-4 py-2.5 rounded-lg text-sm font-medium text-slate-400 hover:bg-slate-800 hover:text-white";
            });
            document.getElementById('tab-' + tabName).classList.remove('hidden');
            document.getElementById('nav-' + tabName).className = "w-full flex items-center space-x-3 px-4 py-2.5 rounded-lg text-sm font-medium bg-emerald-500/10 text-emerald-400";
            document.getElementById('pageTitle').innerText = tabName.toUpperCase();
            
            if(tabName === 'overview') loadOverview();
            if(tabName === 'users') loadUsers();
            if(tabName === 'transactions') loadTransactions();
            if(tabName === 'projects') loadProjects();
        }

        async function loadOverview() {
            const { data: users } = await supabaseClient.from('profiles').select('saldo');
            const { data: projects } = await supabaseClient.from('projects').select('id');
            
            if (users) {
                document.getElementById('statTotalUsers').innerText = users.length;
                const totalSaldo = users.reduce((acc, curr) => acc + (curr.saldo || 0), 0);
                document.getElementById('statTotalSaldo').innerText = 'Rp ' + totalSaldo.toLocaleString('id-ID');
            }
            if (projects) {
                document.getElementById('statTotalProjects').innerText = projects.length;
            }
        }

        async function loadUsers() {
            const { data: users } = await supabaseClient.from('profiles').select('*');
            const tbody = document.getElementById('userTableBody');
            tbody.innerHTML = '';
            if (users) {
                users.forEach(u => {
                    tbody.innerHTML += `<tr>
                        <td class="px-6 py-4">${u.email}</td>
                        <td class="px-6 py-4"><span class="px-2.5 py-1 text-xs rounded-full bg-emerald-500/10 text-emerald-400">${u.role}</span></td>
                        <td class="px-6 py-4">Rp ${(u.saldo || 0).toLocaleString('id-ID')}</td>
                        <td class="px-6 py-4"><button onclick="deleteUser('${u.id}')" class="text-red-400 hover:underline text-xs">Hapus</button></td>
                    </tr>`;
                });
            }
        }

        async function loadTransactions() {
            const { data: txs } = await supabaseClient.from('transactions').select('*');
            const tbody = document.getElementById('transactionTableBody');
            tbody.innerHTML = '';
            if (txs) {
                txs.forEach(t => {
                    tbody.innerHTML += `<tr>
                        <td class="px-6 py-4">${t.id}</td>
                        <td class="px-6 py-4">${t.user_id}</td>
                        <td class="px-6 py-4">Rp ${(t.amount || 0).toLocaleString('id-ID')}</td>
                        <td class="px-6 py-4"><span class="px-2 py-0.5 text-xs rounded bg-yellow-500/10 text-yellow-400">${t.status}</span></td>
                        <td class="px-6 py-4"><button onclick="approveTx('${t.id}', ${t.amount}, '${t.user_id}')" class="bg-emerald-500 text-slate-950 px-3 py-1 rounded text-xs font-bold">Setujui</button></td>
                    </tr>`;
                });
            }
        }

        async function loadProjects() {
            const { data: projs } = await supabaseClient.from('projects').select('*');
            const tbody = document.getElementById('projectTableBody');
            tbody.innerHTML = '';
            if (projs) {
                projs.forEach(p => {
                    tbody.innerHTML += `<tr>
                        <td class="px-6 py-4 font-semibold text-white">${p.title}</td>
                        <td class="px-6 py-4">Rp ${(p.target || 0).toLocaleString('id-ID')}</td>
                        <td class="px-6 py-4">${p.roi}%</td>
                        <td class="px-6 py-4">${p.duration}</td>
                    </tr>`;
                });
            }
        }

        async function createProject() {
            const title = document.getElementById('projTitle').value;
            const target = parseFloat(document.getElementById('projTarget').value);
            const roi = parseFloat(document.getElementById('projRoi').value);
            const duration = document.getElementById('projDuration').value;

            const { error } = await supabaseClient.from('projects').insert([{ title, target, roi, duration }]);
            if(error) { alert('Gagal: ' + error.message); return; }
            alert('Proyek berhasil diterbitkan!');
            loadProjects();
        }

        async function approveTx(id, amount, userId) {
            await supabaseClient.from('transactions').update({ status: 'approved' }).eq('id', id);
            const { data: profile } = await supabaseClient.from('profiles').select('saldo').eq('id', userId).single();
            const newSaldo = (profile.saldo || 0) + amount;
            await supabaseClient.from('profiles').update({ saldo: newSaldo }).eq('id', userId);
            alert('Transaksi disetujui dan saldo member bertambah.');
            loadTransactions();
        }

        async function deleteUser(id) {
            if(confirm('Hapus user ini?')) {
                await supabaseClient.from('profiles').delete().eq('id', id);
                loadUsers();
            }
        }

        async function logoutAdmin() {
            await supabaseClient.auth.signOut();
            window.location.href = '/';
        }

        loadOverview();
    </script>
</body>
</html>
"""

# ----------------------------------------------------
# 3. MEMBER DASHBOARD LENGKAP (RESPONSIVE)
# ----------------------------------------------------
MEMBER_HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Member Dashboard - Indoinves</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen p-4 sm:p-8">
    <div class="max-w-4xl mx-auto space-y-6 sm:space-y-8">
        <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-2">
            <div>
                <h1 class="text-2xl font-bold text-emerald-400">Dashboard Investor</h1>
                <p class="text-sm text-slate-300">Selamat datang di Portofolio Member Anda.</p>
            </div>
            <a href="/" class="text-emerald-400 underline text-sm w-fit">Kembali ke Beranda</a>
        </div>

        <!-- Top-Up Saldo via PayPal -->
        <div class="bg-slate-900 p-5 sm:p-6 rounded-xl border border-slate-800 space-y-4 shadow-lg">
            <h3 class="font-bold text-emerald-400">Top-Up Saldo via PayPal</h3>
            <div class="flex flex-col sm:flex-row gap-3 items-stretch sm:items-center">
                <input type="number" id="depositAmount" placeholder="Jumlah dalam USD" class="bg-slate-950 border border-slate-800 rounded-lg px-4 py-2.5 text-sm text-white outline-none focus:border-emerald-500 w-full sm:w-64">
                <button onclick="payWithPayPal()" class="bg-blue-600 hover:bg-blue-700 text-white font-bold px-5 py-2.5 rounded-lg text-sm transition">
                    Bayar dengan PayPal
                </button>
            </div>
        </div>

        <!-- Pilih Paket Investasi / Langganan -->
        <div class="space-y-4">
            <h3 class="text-xl font-bold text-emerald-400">Pilih Paket Investasi / Langganan</h3>
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
                
                <!-- Paket 1 -->
                <div class="bg-slate-900 border border-slate-800 p-5 sm:p-6 rounded-xl flex flex-col justify-between shadow-lg">
                    <div>
                        <h4 class="font-bold text-lg text-white">Paket Reguler</h4>
                        <p class="text-slate-400 text-sm mt-1">Langganan bulanan platform.</p>
                    </div>
                    <a href="https://www.paypal.com/webapps/billing/plans/subscribe?plan_id=P-8MU20167P66356111MYMSC5Q" 
                       target="_blank" 
                       class="mt-6 block text-center bg-blue-600 hover:bg-blue-700 text-white font-bold py-2.5 rounded-lg text-sm transition">
                        Berlangganan Sekarang
                    </a>
                </div>
                
                <!-- Paket 2 -->
                <div class="bg-slate-900 border border-slate-800 p-5 sm:p-6 rounded-xl flex flex-col justify-between shadow-lg">
                    <div>
                        <h4 class="font-bold text-lg text-white">Paket Premium</h4>
                        <p class="text-slate-400 text-sm mt-1">Akses eksklusif proyek pilihan.</p>
                    </div>
                    <a href="https://www.paypal.com/webapps/billing/plans/subscribe?plan_id=P-0KC8311077154863SMZQ3EDA" 
                       target="_blank" 
                       class="mt-6 block text-center bg-blue-600 hover:bg-blue-700 text-white font-bold py-2.5 rounded-lg text-sm transition">
                        Berlangganan Sekarang
                    </a>
                </div>
                
                <!-- Paket 3 -->
                <div class="bg-slate-900 border border-slate-800 p-5 sm:p-6 rounded-xl flex flex-col justify-between shadow-lg sm:col-span-2 lg:col-span-1">
                    <div>
                        <h4 class="font-bold text-lg text-white">Paket Bisnis</h4>
                        <p class="text-slate-400 text-sm mt-1">Fitur lengkap dan dukungan prioritas.</p>
                    </div>
                    <a href="https://www.paypal.com/webapps/billing/plans/subscribe?plan_id=P-4WF80797503132036MIXUZVI" 
                       target="_blank" 
                       class="mt-6 block text-center bg-blue-600 hover:bg-blue-700 text-white font-bold py-2.5 rounded-lg text-sm transition">
                        Berlangganan Sekarang
                    </a>
                </div>
                
            </div>
        </div>
    </div>

    <script>
        async function payWithPayPal() {
            const amount = document.getElementById('depositAmount').value;
            if(!amount || amount <= 0) {
                alert('Masukkan jumlah top-up yang valid!');
                return;
            }
            const response = await fetch('/create-paypal-payment', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ amount: amount })
            });
            const data = await response.json();
            if (data.approval_url) {
                window.location.href = data.approval_url;
            } else {
                alert('Gagal memproses pembayaran PayPal: ' + (data.error || 'Kesalahan tidak dikenal'));
            }
        }
    </script>
</body>
</html>
"""

if __name__ == "__main__":
    app.run(debug=True, port=5000)
