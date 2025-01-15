import streamlit as st

# Fungsi untuk menghitung warna larutan berdasarkan panjang gelombang (nm)
def hitung_warna(panjang_gelombang):
    if 380 <= panjang_gelombang < 450:
        warna = "Ungu"
        color_code = "#8B00FF"  # Kode warna ungu
    elif 450 <= panjang_gelombang < 495:
        warna = "Biru"
        color_code = "#0000FF"  # Kode warna biru
    elif 495 <= panjang_gelombang < 570:
        warna = "Hijau"
        color_code = "#00FF00"  # Kode warna hijau
    elif 570 <= panjang_gelombang < 590:
        warna = "Kuning"
        color_code = "#FFFF00"  # Kode warna kuning
    elif 590 <= panjang_gelombang < 620:
        warna = "Jingga"
        color_code = "#FFA500"  # Kode warna jingga
    elif 620 <= panjang_gelombang < 750:
        warna = "Merah"
        color_code = "#FF0000"  # Kode warna merah
    else:
        warna = "Tidak Terlihat (UV/IR)"
        color_code = "#D3D3D3"  # Kode warna abu-abu untuk UV/IR
    return warna, color_code

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

# Tampilan aplikasi Streamlit
st.title("Kalkulator Sifat Fisik Nanomaterial")
st.markdown("""
Aplikasi ini menghitung sifat fisik dari nanomaterial berdasarkan panjang gelombang larutan dan ukuran nanopartikel yang dimasukkan.
""")

# Input dari pengguna
panjang_gelombang = st.number_input("Masukkan Panjang Gelombang (nm):", min_value=100.0, max_value=1500.0, step=1.0)
ukuran_nanopartikel = st.number_input("Masukkan Ukuran Nanopartikel (nm):", min_value=1.0, max_value=1000.0, step=0.1)

# Tombol untuk menghitung hasil
if st.button('Lihat Hasil'):
    if panjang_gelombang > 0 and ukuran_nanopartikel > 0:
        # Menghitung warna larutan berdasarkan panjang gelombang
        warna_larutan, color_code = hitung_warna(panjang_gelombang)

        # Menentukan sifat magnetis berdasarkan ukuran nanopartikel
        sifat_magnetis_result = sifat_magnetis(ukuran_nanopartikel)

        # Menghitung luas permukaan berdasarkan ukuran nanopartikel
        luas_permukaan_result = luas_permukaan(ukuran_nanopartikel)

        # Menampilkan hasil dalam bentuk tabel
        st.subheader("Hasil Sifat Fisik Nanomaterial:")
        st.write(f"**Panjang Gelombang**: {panjang_gelombang} nm")
        st.write(f"**Warna Larutan**: {warna_larutan}")
        
        # Menampilkan warna larutan yang sesuai
        st.markdown(f'<div style="background-color:{color_code}; padding: 20px; color:white; text-align:center;">{warna_larutan}</div>', unsafe_allow_html=True)
        
        st.write(f"**Ukuran Nanopartikel**: {ukuran_nanopartikel} nm")
        
        # Menampilkan sifat fisik lainnya
        st.write(f"**Sifat Magnetis**: {sifat_magnetis_result}")
        st.write(f"**Luas Permukaan**: {luas_permukaan_result}")
        
    else:
        st.warning("Masukkan panjang gelombang dan ukuran nanopartikel dengan benar.")
