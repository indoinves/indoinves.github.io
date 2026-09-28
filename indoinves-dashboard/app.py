from flask import Flask, redirect, render_template_string, request, url_for
from supabase import Client, create_client

app = Flask(__name__)

# Kredensial Supabase Anda
SUPABASE_URL = "https://tdiubbgueasfhmcmmahq.supabase.co"
SUPABASE_ANON_KEY = "sb_publishable_73oZ-U6TFidIXEP5uYSpkw_v0OSvs8S"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)


@app.route("/")
def index():
  # Menggunakan template index.html yang Anda miliki
  # (Pastikan file index.html ditaruh di dalam folder 'templates' jika ingin dipisah,
  # atau dirender langsung lewat string seperti di bawah ini jika digabung)
  return render_template_string(OPEN_INDEX_HTML)


@app.route("/admin.html")
def admin_dashboard():
  return render_template_string(ADMIN_HTML_TEMPLATE)


@app.route("/member.html")
def member_dashboard():
  return render_template_string(MEMBER_HTML_TEMPLATE)


# Template HTML disimpan langsung agar mudah dijalankan dalam satu file app.py
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
    <header class="border-b border-slate-800 bg-slate-900/80 backdrop-blur sticky top-0 z-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
            <div class="flex items-center space-x-3">
                <img src="https://indoinves.github.io/img/indoinves.png" alt="Indoinves Logo" class="w-10 h-10 object-contain">
                <span class="font-bold text-xl text-emerald-400 tracking-wide">INDOINVES (Python Backend)</span>
            </div>
            <div>
                <button onclick="openAuthModal()" class="bg-emerald-500 hover:bg-emerald-600 text-slate-950 px-4 py-2 rounded-lg font-semibold text-sm transition">
                    Masuk / Daftar
                </button>
            </div>
        </div>
    </header>

    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20 flex-1 flex flex-col items-center justify-center text-center">
        <h1 class="text-4xl sm:text-5xl font-extrabold tracking-tight max-w-3xl mb-6">
            Kembangkan Portofolio Masa Depan Bersama <span class="text-emerald-400">Indoinves</span>
        </h1>
        <button onclick="openAuthModal()" class="bg-emerald-500 hover:bg-emerald-600 text-slate-950 font-bold py-3 px-6 rounded-xl transition">
            Mulai Akses Dashboard
        </button>
    </main>

    <div id="authModal" class="fixed inset-0 bg-black/70 backdrop-blur-sm z-50 flex items-center justify-center hidden px-4">
        <div class="bg-slate-900 border border-slate-800 p-8 rounded-2xl w-full max-w-md relative shadow-2xl">
            <button onclick="closeAuthModal()" class="absolute top-4 right-4 text-slate-400 hover:text-slate-100 text-xl font-bold">&times;</button>
            <h2 class="text-xl font-bold text-emerald-400 mb-4 text-center">Portal Akun Indoinves</h2>
            <div class="space-y-4">
                <input type="email" id="emailInput" placeholder="nama@email.com" class="w-full bg-slate-950 border border-slate-800 rounded-lg px-4 py-2.5 text-sm text-white">
                <input type="password" id="passwordInput" placeholder="••••••••" class="w-full bg-slate-950 border border-slate-800 rounded-lg px-4 py-2.5 text-sm text-white">
                <div class="flex gap-3 pt-2">
                    <button onclick="handleLogin()" class="flex-1 bg-emerald-500 text-slate-950 font-bold py-2.5 rounded-lg text-sm">Masuk</button>
                    <button onclick="handleRegister()" class="flex-1 bg-slate-800 text-slate-200 py-2.5 rounded-lg text-sm border border-slate-700">Daftar</button>
                </div>
            </div>
        </div>
    </div>

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

ADMIN_HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8"><title>Admin Dashboard - Indoinves</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
</head>
<body class="bg-slate-950 text-slate-100 p-8">
    <h1 class="text-2xl font-bold text-emerald-400 mb-6">Panel Administrator</h1>
    <div class="bg-slate-900 p-6 rounded-xl border border-slate-800">
        <p class="text-sm text-slate-300">Selamat datang di Admin Dashboard. (Kelola transaksi & member di sini).</p>
        <a href="/" class="inline-block mt-4 text-emerald-400 underline text-sm">Kembali ke Beranda</a>
    </div>
</body>
</html>
"""

MEMBER_HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8"><title>Member Dashboard - Indoinves</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
</head>
<body class="bg-slate-950 text-slate-100 p-8">
    <h1 class="text-2xl font-bold text-emerald-400 mb-6">Dashboard Investor</h1>
    <div class="bg-slate-900 p-6 rounded-xl border border-slate-800">
        <p class="text-sm text-slate-300">Selamat datang di Portofolio Member Anda.</p>
        <a href="/" class="inline-block mt-4 text-emerald-400 underline text-sm">Kembali ke Beranda</a>
    </div>
</body>
</html>
"""

if __name__ == "__main__":
  app.run(debug=True, port=5000)
