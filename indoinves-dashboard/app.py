import streamlit as st
import pandas as pd

# Konfigurasi Halaman & Tema
st.set_page_config(
    page_title="Indoinves - Platform Investasi & Crowdfunding",
    page_icon="https://indoinves.github.io/img/indoinves.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS untuk mempercantik tampilan ala Indoinves
st.markdown("""
    <style>
    .main { background-color: #020617; color: #f8fafc; }
    .sidebar .sidebar-content { background-color: #0f172a; }
    .metric-card { background-color: #1e293b; padding: 20px; border-radius: 12px; border: 1px solid #334155; }
    </style>
""", unsafe_allow_html=True)

# Sesi Login Sederhana (Simulasi)
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.role = None
    st.session_state.username = ""

# --- HALAMAN LOGIN ---
if not st.session_state.logged_in:
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.image("https://indoinves.github.io/img/indoinves.png", width=100)
        st.title("Portal Indoinves")
        st.markdown("Silakan masuk untuk mengakses sistem investasi.")
        
        with st.form("login_form"):
            username = st.text_input("Username / Email", placeholder="admin atau member")
            password = st.text_input("Password", type="password", placeholder="admin123 / member123")
            submit = st.form_submit_button("Masuk Dashboard", use_container_width=True)
            
            if submit:
                if username == "admin" and password == "admin123":
                    st.session_state.logged_in = True
                    st.session_state.role = "admin"
                    st.session_state.username = "Administrator"
                    st.rerun()
                elif username == "member" and password == "member123":
                    st.session_state.logged_in = True
                    st.session_state.role = "member"
                    st.session_state.username = "Budi Santoso (Investor)"
                    st.rerun()
                else:
                    st.error("Username atau Password salah! (Gunakan admin/admin123 atau member/member123)")
        
        st.info("💡 **Demo Akun:**\n- Admin: `admin` / `admin123`\n- Member: `member` / `member123`")

# --- SETELAH LOGIN ---
else:
    # Sidebar Navigasi
    with st.sidebar:
        st.image("https://indoinves.github.io/img/indoinves.png", width=60)
        st.markdown(f"### INDOINVES\n*Login sebagai:* **{st.session_state.username}**")
        st.markdown("---")
        
        if st.session_state.role == "admin":
            menu = st.radio("Navigasi Admin", ["Overview", "Manajemen User (KYC)", "Validasi Transaksi", "Manajemen Proyek"])
        else:
            menu = st.radio("Navigasi Member", ["Dashboard Utama", "Portofolio Aktif", "Katalog Proyek", "Dompet & Top-Up"])
            
        st.markdown("---")
        if st.button("Keluar (Logout)", use_container_width=True):
            st.session_state.logged_in = False
            st.session_state.role = None
            st.rerun()

    # ================= DASBOR ADMIN =================
    if st.session_state.role == "admin":
        st.title("🛠️ Admin Dashboard - Pusat Kendali Operasional")
        
        if menu == "Overview":
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric(label="Total AUM (Asset Under Management)", value="Rp 482.5 Juta", delta="+12.4%")
            with col2:
                st.metric(label="Total Investor Aktif", value="1,245 Orang", delta="+45 bulan ini")
            with col3:
                st.metric(label="Transaksi Pending", value="12 Antrean", delta="-2")
            with col4:
                st.metric(label="Kesehatan Sistem", value="Normal", delta="100% Uptime")
                
            st.markdown("### 📈 Grafik Volume Transaksi Harian")
            chart_data = pd.DataFrame({'Hari': ['Sen', 'Sel', 'Rab', 'Kam', 'Jum', 'Sab', 'Min'], 'Volume (Juta Rp)': [15, 22, 45, 30, 60, 85, 50]})
            st.bar_chart(chart_data, x='Hari', y='Volume (Juta Rp)', color="#10b981")

        elif menu == "Manajemen User (KYC)":
            st.subheader("Pusat Verifikasi Identitas (KYC)")
            kyc_data = pd.DataFrame({
                "ID": [101, 102, 103],
                "Nama": ["Dewi Lestari", "Rian Hidayat", "Siti Aminah"],
                "Email": ["dewi@mail.com", "rian@mail.com", "siti@mail.com"],
                "Status KTP": ["Pending", "Verified", "Pending"],
                "Aksi": ["Setujui / Tolak", "Terverifikasi", "Setujui / Tolak"]
            })
            st.dataframe(kyc_data, use_container_width=True)

        elif menu == "Validasi Transaksi":
            st.subheader("Antrean Konfirmasi Deposit & Withdrawal")
            trx_data = pd.DataFrame({
                "Trx ID": ["TRX-901", "TRX-902"],
                "Member": ["Budi Santoso", "Andi Pratama"],
                "Tipe": ["Deposit", "Withdrawal"],
                "Jumlah": ["Rp 5.000.000", "Rp 2.500.000"],
                "Status": ["Menunggu Validasi", "Menunggu Validasi"]
            })
            st.dataframe(trx_data, use_container_width=True)
            if st.button("Proses Validasi Otomatis"):
                st.success("Semua transaksi terpilih berhasil direkonsiliasi!")

        elif menu == "Manajemen Proyek":
            st.subheader("Penerbitan Proyek Crowdfunding Baru")
            with st.form("project_form"):
                p_title = st.text_input("Nama Proyek / Bisnis")
                p_target = st.number_input("Target Pendanaan (Rp)", value=100000000)
                p_price = st.number_input("Harga Per Lembar Saham (Rp)", value=10000)
                submitted = st.form_submit_button("Terbitkan Proyek ke Katalog")
                if submitted:
                    st.success(f"Proyek '{p_title}' berhasil diterbitkan ke katalog member!")

    # ================= DASBOR MEMBER =================
    elif st.session_state.role == "member":
        st.title("👤 Member Dashboard - Portofolio Investor")
        
        if menu == "Dashboard Utama":
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric(label="Total Kekayaan Bersih", value="Rp 12.540.000", delta="+14.2% ROI")
            with col2:
                st.metric(label="Kas Tersedia (Wallet)", value="Rp 1.540.000")
            with col3:
                st.metric(label="Keuntungan Bulan Ini", value="Rp 340.000", delta="Aman")
                
            st.markdown("### 📊 Alokasi Aset Portofolio Anda")
            asset_data = pd.DataFrame({'Instrumen': ['Crowdfunding Properti', 'SBN Ritel', 'Reksadana Pasar Uang', 'Kas'], 'Persentase (%)': [50, 30, 15, 5]})
            st.bar_chart(asset_data, x='Instrumen', y='Persentase (%)', color="#3b82f6")

        elif menu == "Portofolio Aktif":
            st.subheader("Daftar Investasi Berjalan")
            portfolio = pd.DataFrame({
                "Proyek": ["Green Apartment BSD", "Kopi Nusantara Franchise"],
                "Lembar Saham": [500, 250],
                "Total Modal": ["Rp 5.000.000", "Rp 6.000.000"],
                "Estimasi Imbal Hasil": ["12% p.a", "15% p.a"],
                "Status": ["Berjalan", "Berjalan"]
            })
            st.dataframe(portfolio, use_container_width=True)

        elif menu == "Katalog Proyek":
            st.subheader("Peluang Investasi Terbaru (Securities Crowdfunding)")
            st.markdown("Pilih proyek berkualitas yang telah dikurasi oleh tim Indoinves.")
            
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("#### 🏢 Pabrik Kakao Sulawesi")
                st.write("Target: Rp 500.000.000 | Minimal: Rp 100.000")
                if st.button("Beli Saham Proyek 1"):
                    st.success("Berhasil memesan saham Pabrik Kakao Sulawesi!")
            with col2:
                st.markdown("#### ⚡ PLTS Atap Industri")
                st.write("Target: Rp 250.000.000 | Minimal: Rp 50.000")
                if st.button("Beli Saham Proyek 2"):
                    st.success("Berhasil memesan saham PLTS Atap Industri!")

        elif menu == "Dompet & Top-Up":
            st.subheader("Manajemen Saldo & Tarik Dana")
            st.write("Saldo Dompet Saat Ini: **Rp 1.540.000**")
            
            tab1, tab2 = st.tabs(["Top Up (Deposit)", "Tarik Dana (Withdrawal)"])
            with tab1:
                topup_amount = st.number_input("Nominal Top Up", value=100000, step=50000)
                if st.button("Generate QRIS / VA"):
                    st.info(f"Silakan scan QRIS atau transfer ke VA BCA untuk nominal Rp {topup_amount:,}")
            with tab2:
                wd_amount = st.number_input("Nominal Penarikan", value=500000, step=50000)
                st.text("Rekening Terdaftar: BCA - 1234567890 (Budi Santoso)")
                if st.button("Ajukan Penarikan"):
                    st.success("Pengajuan penarikan dana berhasil dikirim ke Admin.")
