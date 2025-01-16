import streamlit as st
import pandas as pd

# Fungsi untuk menghitung warna larutan berdasarkan panjang gelombang (nm)
def hitung_warna(panjang_gelombang):
    if 400 <= panjang_gelombang < 430:
        warna_diserap = "Violet"
        warna_teramati = "Kuning terang"
        color_code = "#FFFF00"  # Kuning terang
    elif 430 <= panjang_gelombang < 480:
        warna_diserap = "Nila"
        warna_teramati = "Kuning"
        color_code = "#FFFF00"  # Kuning
    elif 480 <= panjang_gelombang < 500:
        warna_diserap = "Biru"
        warna_teramati = "Oranye"
        color_code = "#FFA500"  # Oranye
    elif 500 <= panjang_gelombang < 530:
        warna_diserap = "Biru kehijauan"
        warna_teramati = "Merah"
        color_code = "#FF0000"  # Merah
    elif 530 <= panjang_gelombang < 560:
        warna_diserap = "Hijau"
        warna_teramati = "Ungu"
        color_code = "#800080"  # Ungu
    elif 560 <= panjang_gelombang < 580:
        warna_diserap = "Kuning terang"
        warna_teramati = "Violet"
        color_code = "#8A2BE2"  # Violet
    elif 580 <= panjang_gelombang < 610:
        warna_diserap = "Kuning"
        warna_teramati = "Nila"
        color_code = "#4B0082"  # Nila
    elif 610 <= panjang_gelombang < 680:
        warna_diserap = "Oranye"
        warna_teramati = "Biru"
        color_code = "#0000FF"  # Biru
    elif 680 <= panjang_gelombang < 800:
        warna_diserap = "Merah"
        warna_teramati = "Biru kehijauan"
        color_code = "#20B2AA"  # Biru kehijauan
    else:
        warna_diserap = "Tidak Terlihat"
        warna_teramati = "Tidak Terlihat"
        color_code = "#D3D3D3"  # Abu-abu untuk panjang gelombang di luar rentang tampak
    return warna_diserap, warna_teramati, color_code

# Fungsi untuk menentukan sifat magnetis berdasarkan ukuran nanopartikel (nm)
def sifat_magnetis(ukuran_nanopartikel):
    if ukuran_nanopartikel < 10:
        return "Nanopartikel ini sangat magnetis (Efek Superparamagnetik)."
    elif 10 <= ukuran_nanopartikel < 50:
        return "Nanopartikel ini memiliki sifat magnetis sedang."
    else:
        return "Nanopartikel ini hampir tidak memiliki sifat magnetis."

# Fungsi untuk menghitung luas permukaan berdasarkan ukuran nanopartikel (nm)
def luas_permukaan(ukuran_nanopartikel):
    luas = 6 / ukuran_nanopartikel
    return f"{luas:.2f} nm²"

# Fungsi untuk menampilkan sifat fisik berdasarkan material yang dipilih
def sifat_material(material):
    material_sifat = {
        "Titanium": {
            "Konduktivitas": "Rendah (isolator)",
            "Warna": "Perak keabuan",
            "Sifat Katalitik": "Bagus dalam reaksi oksidasi",
            "Densitas": "4.5 g/cm³",
            "Titik Leleh": "1668°C",
            "color_code": "#C0C0C0"
        },
        "Silver": {
            "Konduktivitas": "Sangat tinggi (konduktor)",
            "Warna": "Perak",
            "Sifat Katalitik": "Sangat baik untuk reaksi oksidasi",
            "Densitas": "10.49 g/cm³",
            "Titik Leleh": "962°C",
            "color_code": "#C0C0C0"
        },
        "Gold": {
            "Konduktivitas": "Tinggi (konduktor)",
            "Warna": "Emas",
            "Sifat Katalitik": "Bagus untuk reaksi reduksi",
            "Densitas": "19.32 g/cm³",
            "Titik Leleh": "1064°C",
            "color_code": "#FFD700"
        },
        "Copper": {
            "Konduktivitas": "Tinggi (konduktor)",
            "Warna": "Coklat kemerahan",
            "Sifat Katalitik": "Sedang",
            "Densitas": "8.96 g/cm³",
            "Titik Leleh": "1085°C",
            "color_code": "#B87333"
        },
        "Iron": {
            "Konduktivitas": "Sedang",
            "Warna": "Abu-abu kebiruan",
            "Sifat Katalitik": "Sedang",
            "Densitas": "7.87 g/cm³",
            "Titik Leleh": "1538°C",
            "color_code": "#B0C4DE"
        }
    }
    return material_sifat.get(material, {"Konduktivitas": "Tidak diketahui", "Warna": "Tidak diketahui", "Sifat Katalitik": "Tidak diketahui", "Densitas": "Tidak diketahui", "Titik Leleh": "Tidak diketahui", "color_code": "#D3D3D3"})

# Tampilan aplikasi Streamlit
st.set_page_config(page_title="Kalkulator Sifat Fisik Nanomaterial", layout="wide")

# Sidebar untuk navigasi
menu = st.sidebar.radio("Navigasi", ["Selamat Datang", "Penjelasan", "Kalkulator"])

if menu == "Selamat Datang":
    st.markdown("""
        <div style="text-align: center; font-size: 36px; font-weight: bold; color: #1e3a8a;">
            Selamat Datang di Aplikasi Kalkulator Sifat Fisik Nanomaterial
        </div>
        <p style="text-align: center; font-size: 18px;">Gunakan aplikasi ini untuk mempelajari sifat fisik nanomaterial Anda.</p>
    """, unsafe_allow_html=True)

elif menu == "Penjelasan":
    st.markdown("""
        ## Penjelasan Aplikasi
        Aplikasi ini dirancang untuk menghitung dan menampilkan sifat fisik nanomaterial berdasarkan:
        
        - **Material yang Dipilih:** Seperti Titanium, Silver, Gold, Copper, atau Iron.
        - **Panjang Gelombang (nm):** Untuk menentukan warna larutan.
        - **Ukuran Nanopartikel (nm):** Untuk menentukan sifat magnetis dan luas permukaan.
        
        ### Cara Kerja:
        - Masukkan panjang gelombang cahaya dan ukuran nanopartikel.
        - Pilih material logam yang diinginkan.
        - Klik tombol "Lihat Hasil" untuk melihat hasil perhitungan.
    """)

elif menu == "Kalkulator":
    st.markdown("""
        <div style="text-align: center; font-size: 36px; font-weight: bold; color: #1e3a8a;">
            Kalkulator Sifat Fisik Nanomaterial
        </div>
    """, unsafe_allow_html=True)

    # Input dari pengguna
    material = st.selectbox("Pilih Material Logam", ["Titanium", "Silver", "Gold", "Copper", "Iron"])
    panjang_gelombang = st.number_input("Masukkan Panjang Gelombang (nm):", min_value=100.0, max_value=1500.0, step=1.0)
    ukuran_nanopartikel = st.number_input("Masukkan Ukuran Nanopartikel (nm):", min_value=1.0, max_value=1000.0, step=0.1)

    # Tombol untuk menghitung hasil
    if st.button('Lihat Hasil'):
        if panjang_gelombang > 0 and ukuran_nanopartikel > 0:
            # Menghitung warna larutan berdasarkan panjang gelombang
            warna_diserap, warna_teramati, color_code_warna = hitung_warna(panjang_gelombang)

            # Menentukan sifat magnetis berdasarkan ukuran nanopartikel
            sifat_magnetis_result = sifat_magnetis(ukuran_nanopartikel)

            # Menghitung luas permukaan berdasarkan ukuran nanopartikel
            luas_permukaan_result = luas_permukaan(ukuran_nanopartikel)

            # Mengambil data material
            material_sifat = sifat_material(material)

            # Menampilkan hasil dalam bentuk tabel
            st.subheader("Hasil Sifat Fisik Nanomaterial:")

            data = {
                "Sifat": ["Konduktivitas", "Warna", "Sifat Katalitik", "Densitas", "Titik Leleh"],
                "Nilai": [material_sifat["Konduktivitas"], material_sifat["Warna"], material_sifat["Sifat Katalitik"], material_sifat["Densitas"], material_sifat["Titik Leleh"]]
            }
            df = pd.DataFrame(data)
            st.table(df)

            # Warna Larutan
            st.write(f"**Panjang Gelombang**: {panjang_gelombang} nm")
            st.write(f"**Warna Diserap**: {warna_diserap}")
            st.write(f"**Warna Teramati**: {warna_teramati}")

            st.markdown(f'<div style="background-color:{color_code_warna}; padding: 20px; color:white; text-align:center; font-size:24px; font-weight:bold;">{warna_teramati}</div>', unsafe_allow_html=True)

            # Ukuran Nanopartikel
            st.write(f"**Ukuran Nanopartikel**: {ukuran_nanopartikel} nm")

            st.write(f"**Sifat Magnetis**: {sifat_magnetis_result}")
            st.write(f"**Luas Permukaan**: {luas_permukaan_result}")
