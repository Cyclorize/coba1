import streamlit as st

# Fungsi untuk menentukan warna larutan berdasarkan panjang gelombang (nm)
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
        warna_larutan = hitung_warna(panjang_gelombang)

        # Menentukan sifat magnetis berdasarkan ukuran nanopartikel
        sifat_magnetis_result = sifat_magnetis(ukuran_nanopartikel)

        # Menghitung luas permukaan berdasarkan ukuran nanopartikel
        luas_permukaan_result = luas_permukaan(ukuran_nanopartikel)

        # Menampilkan hasil dalam bentuk tabel
        st.subheader("Hasil Sifat Fisik Nanomaterial:")
        st.write(f"**Panjang Gelombang**: {panjang_gelombang} nm")
        st.write(f"**Warna Larutan**: {warna_larutan}")
        st.write(f"**Ukuran Nanopartikel**: {ukuran_nanopartikel} nm")
        
        # Menampilkan sifat fisik lainnya
        st.write(f"**Sifat Magnetis**: {sifat_magnetis_result}")
        st.write(f"**Luas Permukaan**: {luas_permukaan_result}")
        
    else:
        st.warning("Masukkan panjang gelombang dan ukuran nanopartikel dengan benar.")
