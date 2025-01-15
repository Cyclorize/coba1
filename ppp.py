import streamlit as st
import numpy as np

# Fungsi untuk menghitung energi band gap dari ukuran nanopartikel
def hitung_band_gap(ukuran_nanopartikel):
    # Formula kasar berdasarkan teori kuantum
    # Band Gap (eV) = C / (Ukuran Nanopartikel)^(1/2)
    C = 1.0  # Konstanta empiris, misalnya
    band_gap = C / np.sqrt(ukuran_nanopartikel)
    return band_gap

# Fungsi untuk menghitung absorbansi dari panjang gelombang
def hitung_absorbansi(panjang_gelombang):
    # Formula kasar untuk absorbansi, misalnya untuk nanopartikel logam
    absorbansi = np.exp(-panjang_gelombang / 500)  # Asumsi panjang gelombang dalam nm
    return absorbansi

# Fungsi untuk menghitung fenomena terkait ukuran nanopartikel
def fenomena_fisik(ukuran_nanopartikel):
    if ukuran_nanopartikel < 10:
        return "Nanopartikel ini berada dalam ukuran kuantum yang menunjukkan sifat optik yang kuat dan efek kuantum."
    elif ukuran_nanopartikel < 50:
        return "Nanopartikel ini menunjukkan efek kuantum tetapi juga beberapa sifat material bulk."
    else:
        return "Nanopartikel ini lebih dekat dengan material bulk dengan sedikit efek kuantum."

# Tampilan Streamlit
st.title("Nanopedia - Sifat Fisik Nanopartikel")
st.markdown("Masukkan ukuran nanopartikel (dalam nm) dan panjang gelombang untuk mengetahui sifat fisik dari nanopartikel.")

# Input dari pengguna
ukuran_nanopartikel = st.number_input("Masukkan Ukuran Nanopartikel (nm):", min_value=1.0, max_value=1000.0, step=0.1)
panjang_gelombang = st.number_input("Masukkan Panjang Gelombang (nm):", min_value=200.0, max_value=2000.0, step=1.0)

# Kalkulasi
if ukuran_nanopartikel > 0 and panjang_gelombang > 0:
    # Menghitung band gap
    band_gap = hitung_band_gap(ukuran_nanopartikel)
    # Menghitung absorbansi
    absorbansi = hitung_absorbansi(panjang_gelombang)
    # Menampilkan hasil
    st.subheader("Hasil Kalkulasi:")
    st.write(f"Band Gap (eV): {band_gap:.2f}")
    st.write(f"Absorbansi: {absorbansi:.4f}")
    st.write(f"Fenomena Fisik: {fenomena_fisik(ukuran_nanopartikel)}")
    
    # Menampilkan grafik hubungan ukuran nanopartikel dengan band gap
    fig, ax = plt.subplots()
    ukuran_range = np.linspace(1, 1000, 100)
    band_gap_values = [hitung_band_gap(u) for u in ukuran_range]
    ax.plot(ukuran_range, band_gap_values, label="Band Gap vs Ukuran Nanopartikel")
    ax.set_xlabel("Ukuran Nanopartikel (nm)")
    ax.set_ylabel("Band Gap (eV)")
    ax.set_title("Hubungan Ukuran Nanopartikel dengan Band Gap")
    ax.legend()
    st.pyplot(fig)

    # Menampilkan grafik absorbansi vs panjang gelombang
    fig2, ax2 = plt.subplots()
    panjang_gelombang_range = np.linspace(200, 2000, 100)
    absorbansi_values = [hitung_absorbansi(pg) for pg in panjang_gelombang_range]
    ax2.plot(panjang_gelombang_range, absorbansi_values, label="Absorbansi vs Panjang Gelombang", color="red")
    ax2.set_xlabel("Panjang Gelombang (nm)")
    ax2.set_ylabel("Absorbansi")
    ax2.set_title("Hubungan Absorbansi dengan Panjang Gelombang")
    ax2.legend()
    st.pyplot(fig2)

else:
    st.warning("Masukkan ukuran nanopartikel dan panjang gelombang dengan benar.")
