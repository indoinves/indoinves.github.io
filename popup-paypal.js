(function () {
    // 1. Inject Styling Tailwind CSS jika belum ada
    if (!document.querySelector('script[src*="tailwindcss.com"]')) {
        const twScript = document.createElement('script');
        twScript.src = "https://cdn.tailwindcss.com";
        document.head.appendChild(twScript);
    }

    // 2. Buat Template HTML Modal Popup
    const modalHTML = `
    <div id="paypalModal" class="fixed inset-0 bg-black/70 backdrop-blur-sm flex items-center justify-center z-50 hidden">
        <div class="bg-slate-800 border border-slate-700 rounded-2xl max-w-md w-full p-6 relative shadow-2xl text-white">
            <!-- Close Button -->
            <button onclick="window.closePayPalModal()" class="absolute top-4 right-4 text-slate-400 hover:text-white text-xl font-bold">&times;</button>
            
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

            <!-- Form Aksi (Mengarah ke backend Flask) -->
            <form action="/create-paypal-payment" method="POST">
                <div class="mb-4 text-left">
                    <label class="block text-xs uppercase tracking-wider text-slate-400 mb-2">Email Akun PayPal Tujuan</label>
                    <input type="email" name="paypal_email" required placeholder="nama@domain.com" class="w-full bg-slate-900 border border-slate-700 rounded-lg px-4 py-2.5 text-white focus:outline-none focus:border-blue-500">
                </div>
                <button type="submit" class="w-full bg-blue-600 hover:bg-blue-500 text-white font-semibold py-3 rounded-xl shadow transition">
                    Lanjutkan Pembayaran $100
                </button>
            </form>
        </div>
    </div>
    `;

    // 3. Sisipkan elemen modal ke dalam body halaman saat DOM siap
    document.addEventListener("DOMContentLoaded", function () {
        const div = document.createElement('div');
        div.innerHTML = modalHTML;
        document.body.appendChild(div);
    });

    // 4. Fungsi Global untuk Mengontrol Modal
    window.openPayPalModal = function () {
        const modal = document.getElementById('paypalModal');
        if (modal) modal.classList.remove('hidden');
    };

    window.closePayPalModal = function () {
        const modal = document.getElementById('paypalModal');
        if (modal) modal.classList.add('hidden');
    };
})();
