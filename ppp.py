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
    elif 590 <= panjang_gombang < 620:
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

# Tombol untuk menampilkan hasil
if st.button('Lihat Hasil'):
    if panjang_gelombang > 0 and ukuran_nanopartikel > 0:
        # Menghitung warna larutan berdasarkan panjang gelombang
        warna_larutan = hitung_warna(panjang_gelombang)

        # Menentukan sifat katalitik berdasarkan ukuran nanopartikel
        sifat_katalitik_result = sifat_katalitik(ukuran_nanopartikel)

        # Menampilkan hasil dalam bentuk tabel
        st.subheader("Hasil Kalkulasi:")
        hasil_data = {
            "Panjang Gelombang (nm)": [panjang_gelombang],
            "Warna Larutan": [warna_larutan],
            "Ukuran Nanopartikel (nm)": [ukuran_nanopartikel],
            "Sifat Katalitik": [sifat_katalitik_result]
        }
        st.table(hasil_data)

        # Penjelasan panjang mengenai hasil perhitungan
        st.subheader("Penjelasan Hasil:")
        st.markdown(f"""
        ### 1. Warna Larutan
        Berdasarkan panjang gelombang **{panjang_gelombang} nm**, larutan nanopartikel ini cenderung berwarna **{warna_larutan}**. 
        - Panjang gelombang dalam kisaran 380-450 nm menghasilkan warna **Ungu**.
        - Panjang gelombang 450-495 nm menghasilkan warna **Biru**.
        - Panjang gelombang 495-570 nm menghasilkan warna **Hijau**.
        - Panjang gelombang 570-590 nm menghasilkan warna **Kuning**.
        - Panjang gelombang 590-620 nm menghasilkan warna **Jingga**.
        - Panjang gelombang 620-750 nm menghasilkan warna **Merah**.
        - Panjang gelombang di luar kisaran tersebut, seperti UV atau IR, menghasilkan warna yang tidak tampak oleh mata manusia.

        ### 2. Sifat Katalitik
        Berdasarkan ukuran nanopartikel **{ukuran_nanopartikel} nm**, sifat katalitik nanopartikel ini dijelaskan sebagai berikut:
        - **Nanopartikel dengan ukuran kurang dari 5 nm** memiliki sifat katalitik yang sangat tinggi karena efek kuantum yang kuat dan luas permukaan yang lebih besar, yang meningkatkan reaktivitas kimia.
        - **Nanopartikel dengan ukuran antara 5-20 nm** masih memiliki sifat katalitik yang baik, tetapi efek kuantum mulai berkurang seiring dengan bertambahnya ukuran partikel.
        - **Nanopartikel lebih besar dari 20 nm** cenderung memiliki sifat katalitik yang lebih mirip dengan material bulk, karena efek kuantum hampir hilang, dan sifat permukaannya tidak sebesar nanopartikel kecil.

        Semoga informasi ini membantu dalam memahami sifat-sifat fisik dari nanomaterial!
        """)
    else:
        st.warning("Masukkan panjang gelombang dan ukuran nanopartikel dengan benar.")
