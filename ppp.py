import streamlit as st
import pandas as pd
from PIL import Image
import time

# Fungsi untuk menghitung warna larutan berdasarkan panjang gelombang (nm)
def hitung_warna(panjang_gelombang):
    if 400 <= panjang_gelombang < 430:
        warna_diserap = "Violet"
        warna_teramati = "Kuning terang"
        color_code = "#FFFF00"
    elif 430 <= panjang_gelombang < 480:
        warna_diserap = "Nila"
        warna_teramati = "Kuning"
        color_code = "#FFFF00"
    elif 480 <= panjang_gelombang < 500:
        warna_diserap = "Biru"
        warna_teramati = "Oranye"
        color_code = "#FFA500"
    elif 500 <= panjang_gelombang < 530:
        warna_diserap = "Biru kehijauan"
        warna_teramati = "Merah"
        color_code = "#FF0000"
    elif 530 <= panjang_gelombang < 560:
        warna_diserap = "Hijau"
        warna_teramati = "Ungu"
        color_code = "#800080"
    elif 560 <= panjang_gelombang < 580:
        warna_diserap = "Kuning terang"
        warna_teramati = "Violet"
        color_code = "#8A2BE2"
    elif 580 <= panjang_gelombang < 610:
        warna_diserap = "Kuning"
        warna_teramati = "Nila"
        color_code = "#4B0082"
    elif 610 <= panjang_gelombang < 680:
        warna_diserap = "Oranye"
        warna_teramati = "Biru"
        color_code = "#0000FF"
    elif 680 <= panjang_gelombang <= 800:
        warna_diserap = "Merah"
        warna_teramati = "Biru kehijauan"
        color_code = "#20B2AA"
    else:
        warna_diserap = "Tidak Terlihat"
        warna_teramati = "Tidak Terlihat"
        color_code = "#D3D3D3"
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
    return material_sifat.get(material, {
        "Konduktivitas": "Tidak diketahui", 
        "Warna": "Tidak diketahui", 
        "Sifat Katalitik": "Tidak diketahui", 
        "Densitas": "Tidak diketahui", 
        "Titik Leleh": "Tidak diketahui", 
        "color_code": "#D3D3D3"
    })

# Fungsi untuk memperkenalkan aplikasi dengan animasi teks sederhana
def animasi_berjalan(text, delay=0.1):
    for i in range(len(text)+1):
        st.markdown(text[:i], unsafe_allow_html=True)
        time.sleep(delay)

# Tampilan aplikasi Streamlit
st.set_page_config(page_title="Sifat Fisik Nanologam", layout="wide")

# Sidebar dengan gambar
image = Image.open("AKA.jpg")
st.sidebar.image(image, use_container_width=True)
st.sidebar.title("Navigasi")

# Halaman awal
menu = st.sidebar.radio("Pilih Halaman", ["Selamat Datang", "Penjelasan", "Kalkulator", "Identitas Pembuat"])

if menu == "Selamat Datang":
    st.markdown(
        "<h1 style='text-align: center; color: #4B0082;'>Sifat Fisik Nanologam</h1>", 
        unsafe_allow_html=True
    )
    st.markdown(
        "<p style='text-align: center; font-size: 20px; color: #555;'>Aplikasi ini dirancang untuk membantu Anda menganalisis sifat fisik dari nanomaterial berdasarkan panjang gelombang, ukuran nanopartikel, dan material yang dipilih.</p>", 
        unsafe_allow_html=True
    )

elif menu == "Penjelasan":
    st.title("Penjelasan Aplikasi")
    st.write("""
        Pada halaman ini, Anda akan mempelajari lebih lanjut tentang fitur dan fungsi aplikasi ini:

        - **Warna Larutan:** Ditentukan berdasarkan panjang gelombang cahaya tampak yang diserap oleh material.
        - **Sifat Magnetis:** Ditentukan berdasarkan ukuran nanopartikel, dengan rentang efek superparamagnetik.
        - **Luas Permukaan:** Menghitung luas permukaan nanopartikel berdasarkan ukurannya.
    """)

elif menu == "Kalkulator":
    st.title("Kalkulator Sifat Fisik Nanomaterial")
    material = st.selectbox("Pilih Material Logam", ["Titanium", "Silver", "Gold", "Copper", "Iron"])
    panjang_gelombang = st.number_input("Masukkan Panjang Gelombang (nm):", min_value=100.0, max_value=800.0, step=1.0)
    ukuran_nanopartikel = st.number_input("Masukkan Ukuran Nanopartikel (nm):", min_value=1.0, max_value=1000.0, step=0.1)

    if st.button("Lihat Hasil"):
        if panjang_gelombang > 0 and ukuran_nanopartikel > 0:
            # Menghitung warna dan sifat lainnya
            warna_diserap, warna_teramati, color_code_warna = hitung_warna(panjang_gelombang)
            # Menampilkan warna teramati tanpa informasi panjang gelombang atau ukuran nanopartikel
            st.markdown(
                f'<div style="background-color:{color_code_warna}; padding: 20px; color:white; text-align:center; font-size:24px; font-weight:bold;">{warna_teramati}</div>', 
                unsafe_allow_html=True
            )
            st.write(f"**Warna Diserap**: {warna_diserap}")
            st.write(f"**Warna Teramati**: {warna_teramati}")
            st.write(f"**Sifat Magnetis**: {sifat_magnetis(ukuran_nanopartikel)}")
            st.write(f"**Luas Permukaan**: {luas_permukaan(ukuran_nanopartikel)}")

            sifat = sifat_material(material)
            data = {
                "Properti": ["Konduktivitas", "Warna Material", "Sifat Katalitik", "Densitas", "Titik Leleh"],
                "Nilai": [sifat["Konduktivitas"], sifat["Warna"], sifat["Sifat Katalitik"], sifat["Densitas"], sifat["Titik Leleh"]]
            }
            df = pd.DataFrame(data)
            st.markdown(f"<h3 style='text-align: center; color: {sifat['color_code']};'>Informasi Material: {material}</h3>", unsafe_allow_html=True)
            st.table(df)

elif menu == "Identitas Pembuat":
    st.title("Identitas Pembuat")
    st.write("""
        Aplikasi ini dikembangkan oleh mahasiswa Program Studi D4 Nanoteknologi Pangan Politeknik AKA Bogor.
        
        **Anggota Kelompok:**
        1. Alifa Nadia Utami (2350072)
        2. Nayla Haliza Rahma (2350123)
        3. Larissa Febriyanti (2350104)
        4. Aulia Salwa Sahputri Malau (2350078)
        5. Muhammad Thoriq Syafaat (2350111)
    """)
