import streamlit as st
import time

# 1. KONFIGURASI HALAMAN UTAMA STREAMLIT
st.set_page_config(
    page_title="Belajar Bahasa Arab - Ustazah Melisa", 
    page_icon="🕌", 
    layout="centered"
)

# ==========================================================
# FOLDER / PANEL PROFIL & API KEY (SIDEBAR SEBELAH KIRI)
# ==========================================================
with st.sidebar:
    st.header("👤 Folder Konfigurasi")
    st.write("Silakan lengkapi data profil dan API Key Anda di sini:")
    
    # Input Teks untuk Nama, Username, dan API Key
    user_nama = st.text_input("Nama Lengkap", value="Melisa")
    user_username = st.text_input("Username", value="@melisa_7a")
    api_key_input = st.text_input("API Key Jaringan", type="password", placeholder="Masukkan API Key Anda di sini...")
    
    st.markdown("---")
    # Menampilkan status ringkas di dalam folder/sidebar
    st.success(f"Aktif sebagai: {user_nama}")
    if api_key_input:
        st.caption("🔑 API Key terhubung")
    else:
        st.caption("⚠️ API Key belum diisi")

# ==========================================================
# HALAMAN UTAMA CHAT (TENGAH LAYAR)
# ==========================================================
st.title("🕌 Kelas Bahasa Arab: Ustazah Melisa")
st.write(f"Selamat datang **{user_nama}** ({user_username})! Mari mulai latihan percakapan kita.")
st.markdown("---")

# 2. INISIALISASI RIWAYAT CHAT (Menggunakan Bahasa Arab + Terjemahan)
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "**أَهْلًا وَسَهْلًا! أَنَا الأُسْتَاذَةُ مَلِيْسَا، صَدِيْقَتُكِ لِمُمَارَسَةِ المُحَادَثَةِ بِاللُّغَةِ العَرَبِيَّةِ لِتَكُوْنِيْ أَكْثَرَ طَلَاقَةً.**\n\n"
                "*Artinya: Selamat datang! Saya Ustazah Melisa, temanmu untuk melatih percakapan bahasa Arab agar kamu menjadi lebih lancar.*\n\n"
                "**اليَوْمَ، أَيْنَ نُرِيْدُ أَنْ نَتَدَرَّبَ عَلَى الكَلَامِ؟ اِخْتَرِ المَوْضُوْعَ بِكِتَابَةِ الرَّقْمِ أَوِ الكَلِمَةِ:**\n"
                "*Artinya: Hari ini, di mana kita ingin berlatih bicara? Pilih topiknya dengan mengetik angka atau katanya langsung (Keluarga / Teman / Alamat):*\n\n"
                "1. **التَّعَارُفُ فِي الأُسْرَةِ** *(Perkenalan Keluarga / ketik: keluarga)*\n"
                "2. **التَّعَارُفُ بَيْنَ الأَصْدِقَاءِ** *(Perkenalan Sesama Teman / ketik: teman)*\n"
                "3. **عَنِ العُنْوَانِ** *(Tentang Alamat / ketik: alamat)*"
            )
        }
    ]

# 3. TAMPILKAN RIWAYAT CHAT DI LAYAR
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. PROSES INPUT DARI USER (Mendukung Perintah Bahasa Indonesia)
if user_input := st.chat_input("Ketik di sini... (Contoh: halo, keluarga, teman, atau alamat)"):
    
    # Tampilkan pesan user ke layar
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Simpan ke riwayat session
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Normalisasi teks input user
    pesan_bersih = user_input.strip().lower()
    
    # Jalankan animasi loading mengetik
    with st.chat_message("assistant"):
        with st.spinner("Ustazah Melisa sedang mengetik..."):
            time.sleep(0.8) 
            
            # Logika Deteksi Multi-Bahasa & Kata Kunci Indonesia
            is_salam = any(x in pesan_bersih for x in ['assalamualaikum', "assalamu'alaikum", 'halo', 'hai', 'pagi', 'permisi'])
            is_topik1 = any(x in pesan_bersih for x in ['1', 'keluarga', 'family', 'orang tua', 'usrah'])
            is_topik2 = any(x in pesan_bersih for x in ['2', 'teman', 'kawan', 'sahabat', 'taaruf'])
            is_topik3 = any(x in pesan_bersih for x in ['3', 'alamat', 'rumah', 'tinggal', 'unwan'])

            if is_salam:
                reply = (
                    "**وَعَلَيْكُمُ السَّلَامُ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ! أَهْلًا وَسَهْلًا بِكَ.**\n\n"
                    f"*Artinya: Wa'alaikumussalam warahmatullah wabarakatuh! Selamat datang, Kak {user_nama}.*\n\n"
                    "**اِخْتَرِ المَوْضُوْعَ يَا بَارَكَ اللهُ فِيْكِ:**\n"
                    "*Artinya: Silakan pilih topik belajar kita hari ini (bisa ketik angkanya atau ketik langsung katanya):*\n\n"
                    "• Ketik **1** atau **Keluarga**\n"
                    "• Ketik **2** atau **Teman**\n"
                    "• Ketik **3** atau **Alamat**"
                )
            elif is_topik1:
                reply = (
                    "**مُمْتَاز! مَوْضُوْعُ الأُسْرَةِ (العَائِلَةُ). هَيَّا نَبْدَأْ.**\n\n"
                    "*Artinya: Luar biasa! Topik Keluarga. Mari kita mulai.*\n\n"
                    "**مَا مَعْنَى هَذِهِ الجُمْلَةِ بِاللُّغَةِ العَرَبِيَّةِ: 'Ini adalah ibuku'?**\n\n"
                    "*Artinya: Apa bahasa Arabnya dari kalimat: 'Ini adalah ibuku'? Coba ketik jawabanmu!*"
                )
            elif is_topik2:
                reply = (
                    "**جَيِّدٌ جِدًّا! مَوْضُوْعُ التَّعَارُفِ بَيْنَ الأَصْدِقَاءِ.**\n\n"
                    "*Artinya: Bagus sekali! Topik Perkenalan Sesama Teman.*\n\n"
                    "**كَيْفَ تُحَيِّيْنَ صَدِيْقَتَكِ الجَدِيْدَةَ عِنْدَمَا Tَلْتَقِيَانِ؟**\n\n"
                    "*Artinya: Bagaimana caramu menyapa teman perempuan barumu ketika kalian saling bertemu?*"
                )
            elif is_topik3:
                reply = (
                    "**رَائِع! مَوْضُوْعُ العُنْوَانِ مُشَوِّقٌ جِدًّا.**\n\n"
                    "*Artinya: Hebat! Topik Alamat ini sangat menarik.*\n\n"
                    "**أَجِبْ عَنْ هَذَا السُّؤَالِ: أَيْنَ تَسْكُنُ الآنَ؟**\n\n"
                    "*Artinya: Jawablah pertanyaan ini: Di mana kamu tinggal sekarang?*"
                )
            else:
                reply = (
                    "**أَنَا هُنَا لِمُسَاعَدَتِكَ.**\n\n"
                    "*Artinya: Saya di sini untuk membantumu.*\n\n"
                    "**عَلَيْكَ أَنْ تَكْتُبَ كَلِمَةً مِثْلَ 'keluarga', 'teman', 'alamat' أَوِ الأَرْقَامِ لِنَبْدَأَ الدَّرْسَ.**\n\n"
                    "*Artinya: Kamu bisa menulis kata dalam Bahasa Indonesia seperti 'keluarga', 'teman', 'alamat' atau cukup masukkan angka untuk memulai pelajaran kita.*"
                )
            
            st.markdown(reply)
    
    # Simpan balasan Ustazah ke session state
    st.session_state.messages.append({"role": "assistant", "content": reply})