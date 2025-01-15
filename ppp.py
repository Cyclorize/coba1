import streamlit as st
import pandas as pd

# Fungsi untuk menghitung warna larutan berdasarkan panjang gelombang (nm)
def hitung_warna(panjang_gelombang):
    # Data spektrum panjang gelombang dan warna yang diserap/teramati
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
        color_code = "#D3D3D3"  # Kode warna abu-abu untuk panjang gelombang di luar rentang tampak
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
    # Menggunakan rumus luas permukaan untuk bola (A = 6 / D)
    luas = 6 / ukuran_nanopartikel
    return f"{luas:.2f} nm²"

# Fungsi untuk menampilkan sifat fisik berdasarkan material yang dipilih
def sifat_material(material):
    # Sifat fisik dari beberapa material logam
    material_sifat = {
        "Titanium": {
            "Konduktivitas": "Rendah (isolator)",
            "Warna": "Perak keabuan",
            "Sifat Katalitik": "Bagus dalam reaksi oksidasi",
            "Densitas": "4.5 g/cm³",
            "color_code": "#C0C0C0",  # Perak
            "gambar": "images/titanium.jpg"  # Pastikan gambar ada di folder 'images'
        },
        "Silver": {
            "Konduktivitas": "Sangat tinggi (konduktor)",
            "Warna": "Perak",
            "Sifat Katalitik": "Sangat baik untuk reaksi oksidasi",
            "Densitas": "10.49 g/cm³",
            "color_code": "#C0C0C0",  # Perak
            "gambar": "images/silver.jpg"  # Pastikan gambar ada di folder 'images'
        },
        "Gold": {
            "Konduktivitas": "Tinggi (konduktor)",
            "Warna": "Emas",
            "Sifat Katalitik": "Bagus untuk reaksi reduksi",
            "Densitas": "19.32 g/cm³",
            "color_code": "#FFD700",  # Emas
            "gambar": "images/gold.jpg"  # Pastikan gambar ada di folder 'images'
        },
        "Copper": {
            "Konduktivitas": "Tinggi (konduktor)",
            "Warna": "Coklat kemerahan",
            "Sifat Katalitik": "Sedang",
            "Densitas": "8.96 g/cm³",
            "color_code": "#B87333",  # Coklat kemerahan
            "gambar": "images/copper.jpg"  # Pastikan gambar ada di folder 'images'
        },
        "Iron": {
            "Konduktivitas": "Sedang",
            "Warna": "Abu-abu kebiruan",
            "Sifat Katalitik": "Sedang",
            "Densitas": "7.87 g/cm³",
            "color_code": "#B0C4DE",  # Abu-abu kebiruan
            "gambar": "images/iron.jpg"  # Pastikan gambar ada di folder 'images'
        }
    }
    
    # Mengembalikan sifat material yang dipilih, jika material tidak ada di daftar, tampilkan pesan error.
    return material_sifat.get(material, {"Konduktivitas": "Tidak diketahui", "Warna": "Tidak diketahui", "Sifat Katalitik": "Tidak diketahui", "Densitas": "Tidak diketahui", "color_code": "#D3D3D3", "gambar": ""})  # Warna default jika tidak ada material yang cocok

# Tampilan aplikasi Streamlit
st.title("Kalkulator Sifat Fisik Nanomaterial")
st.markdown("""
Aplikasi ini menghitung sifat fisik dari nanomaterial berdasarkan panjang gelombang larutan, ukuran nanopartikel, dan material yang dipilih.
""")

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
        
        # Tampilkan gambar material
        if material_sifat['gambar']:
            st.image(material_sifat['gambar'], caption=material, use_column_width=True)

        # Menampilkan tabel sifat material
        data = {
            "Sifat": ["Konduktivitas", "Warna", "Sifat Katalitik", "Densitas"],
            "Nilai": [material_sifat["Konduktivitas"], material_sifat["Warna"], material_sifat["Sifat Katalitik"], material_sifat["Densitas"]]
        }
        df = pd.DataFrame(data)
        st.table(df)

        # Warna Larutan
        st.write(f"**Panjang Gelombang**: {panjang_gelombang} nm")
        st.write(f"**Warna Diserap**: {warna_diserap}")
        st.write(f"**Warna Teramati**: {warna_teramati}")
        
        # Menampilkan warna larutan yang sesuai
        st.markdown(f'<div style="background-color:{color_code_warna}; padding: 20px; color:white; text-align:center; font-size:24px; font-weight:bold;">{warna_teramati}</div>', unsafe_allow_html=True)

        # Ukuran Nanopartikel
        st.write(f"**Ukuran Nanopartikel**: {ukuran_nanopartikel} nm")
        
        # Menampilkan sifat fisik lainnya
        st.write(f"**Sifat Magnetis**: {sifat_magnetis_result}")
        st.write(f"**Luas Permukaan**: {luas_permukaan_result}")
        
    else:
        st.warning("Masukkan panjang gelombang dan ukuran nanopartikel dengan benar.")
