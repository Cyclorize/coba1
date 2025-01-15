import streamlit as st
import numpy as np

# Fungsi untuk menghitung warna larutan berdasarkan panjang gelombang (nm)
def hitung_warna(panjang_gelombang):
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

# Fungsi utama aplikasi
def main():
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

            # Menyembunyikan input setelah hasil dihitung
            st.session_state.show_input = False

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

            ### 2. Sifat Katalitik
            Berdasarkan ukuran nanopartikel **{ukuran_nanopartikel} nm**, sifat katalitik nanopartikel ini dijelaskan sebagai berikut:
            - **Nanopartikel dengan ukuran kurang dari 5 nm** memiliki sifat katalitik yang sangat tinggi karena efek kuantum yang kuat dan luas permukaan yang lebih besar, yang meningkatkan reaktivitas kimia.
            - **Nanopartikel dengan ukuran antara 5-20 nm** masih memiliki sifat katalitik yang baik, tetapi efek kuantum mulai berkurang seiring dengan bertambahnya ukuran partikel.
            - **Nanopartikel lebih besar dari 20 nm** cenderung memiliki sifat katalitik yang lebih mirip dengan material bulk, karena efek kuantum hampir hilang, dan sifat permukaannya tidak sebesar nanopartikel kecil.
            """)

            # Tombol kembali untuk input ulang
            if st.button('Kembali'):
                st.session_state.show_input = True
        else:
            st.warning("Masukkan panjang gelombang dan ukuran nanopartikel dengan benar.")

    # Menampilkan input jika diperlukan
    if 'show_input' not in st.session_state or st.session_state.show_input:
        st.warning("Masukkan data untuk mendapatkan hasil!")

# Menjalankan fungsi utama
if __name__ == "__main__":
    main()
