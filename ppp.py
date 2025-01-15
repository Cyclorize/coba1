import streamlit as st
import numpy as np

# Fungsi untuk menghitung warna larutan berdasarkan panjang gelombang (nm)
def hitung_warna(panjang_gelombang):
    # Penentuan warna berdasarkan panjang gelombang (nm)
    if 380 <= panjang_gelombang < 450:
        return "Ungu"
    elif 450 <= panjang_gelombang < 495:
        return "Biru"
    elif 495 <= panjang_gelombang < 570:
        return "Hijau"
    elif 570 <= panjang_gelombang < 590:
        return "Kuning"
    elif 590 <= panjang_gelombang < 620:
        return "Jingga"
    elif 620 <= panjang_gelombang < 750:
        return "Merah"
    else:
        return "Tidak Terlihat (UV/IR)"

# Fungsi untuk menentukan sifat katalitik berdasarkan ukuran nanopartikel (nm)
def sifat_katalitik(ukuran_nanopartikel):
    if ukuran_nanopartikel < 5:
        return "Nanopartikel ini memiliki sifat katalitik yang sangat tinggi karena efek kuantum dan luas permukaan yang besar."
    elif ukuran_nanopartikel < 20:
        return "Nanopartikel ini memiliki sifat katalitik yang baik, namun efek kuantum mulai berkurang."
    else:
        return "Nanopartikel ini lebih mirip dengan material bulk, dengan sifat katalitik yang moderat."

# Tampilan Streamlit
st.title("Nanopedia - Sifat Fisik Nanomaterial")
st.markdown("""
Aplikasi ini memungkinkan Anda untuk menghitung sifat fisik dari nanomaterial, seperti warna larutan berdasarkan panjang gelombang dan sifat katalitik berdasarkan ukuran nanopartikel.
""")

# Input dari pengguna
panjang_gelombang = st.number_input("Masukkan Panjang Gelombang (nm):", min_value=100.0, max_value=1500.0, step=1.0)
ukuran_nanopartikel = st.number_input("Masukkan Ukuran Nanopartikel (nm):", min_value=1.0, max_value=1000.0, step=0.1)

# Kalkulasi
if panjang_gelombang > 0 and ukuran_nanopartikel > 0:
    # Menghitung warna larutan berdasarkan panjang gelombang
    warna_larutan = hitung_warna(panjang_gelombang)
    
    # Menentukan sifat katalitik berdasarkan ukuran nanopartikel
    sifat_katalitik_result = sifat_katalitik(ukuran_nanopartikel)
    
    # Menampilkan hasil
    st.subheader("Hasil Kalkulasi:")
    st.write(f"**Warna Larutan (sesuai panjang gelombang {panjang_gelombang} nm):** {warna_larutan}")
    st.write(f"**Sifat Katalitik Nanopartikel (Ukuran {ukuran_nanopartikel} nm):** {sifat_katalitik_result}")
    
    # Menampilkan informasi lebih lanjut dalam bentuk tabel
    st.subheader("Informasi Tambahan")
    data = {
        "Panjang Gelombang (nm)": [panjang_gelombang],
        "Warna Larutan": [warna_larutan],
        "Ukuran Nanopartikel (nm)": [ukuran_nanopartikel],
        "Sifat Katalitik": [sifat_katalitik_result]
    }
    st.write(data)

else:
    st.warning("Masukkan panjang gelombang dan ukuran nanopartikel dengan benar.")
