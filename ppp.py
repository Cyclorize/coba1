import streamlit as st
import pandas as pd
from PIL import Image
import plotly.graph_objects as go

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
    elif 680 <= panjang_gelombang < 800:
        warna_diserap = "Merah"
        warna_teramati = "Biru kehijauan"
        color_code = "#20B2AA"
    else:
        warna_diserap = "Tidak Terlihat"
        warna_teramati = "Tidak Terlihat"
        color_code = "#D3D3D3"
    return warna_diserap, warna_teramati, color_code

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

# Fungsi untuk menampilkan animasi larutan dalam erlenmeyer
def plot_larutan_animasi(color_code):
    fig = go.Figure()

    # Membuat bentuk Erlenmeyer
    erlenmeyer = go.Scatter(
        x=[0, 1, 0.5, 0],
        y=[0, 0, 3, 3],
        fill='toself',
        fillcolor="gray",
        line=dict(color='black'),
        mode='lines',
        name="Erlenmeyer"
    )
    fig.add_trace(erlenmeyer)

    # Larutan dengan warna yang dipilih
    fig.add_trace(go.Scatter(
        x=[0, 1, 0.5, 0],
        y=[0, 0, 2.5, 2.5],
        fill='toself',
        fillcolor=color_code,
        line=dict(color='black'),
        mode='lines',
        name="Larutan"
    ))

    # Set layout
    fig.update_layout(
        title="Larutan dalam Erlenmeyer",
        xaxis=dict(range=[-1, 2], showgrid=False, zeroline=False),
        yaxis=dict(range=[-1, 4], showgrid=False, zeroline=False),
        showlegend=False
    )

    return fig

# Tampilan aplikasi Streamlit
st.set_page_config(page_title="Kalkulator Sifat Fisik Nanomaterial", layout="wide")

# Sidebar
st.sidebar.title("Navigasi")
menu = st.sidebar.radio("Pilih Halaman", ["Selamat Datang", "Penjelasan", "Kalkulator", "Identitas Pembuat"])

if menu == "Selamat Datang":
    st.title("Selamat Datang di Kalkulator Sifat Fisik Nanomaterial")
    st.write("""
        Aplikasi ini dirancang untuk membantu Anda menganalisis sifat fisik dari nanomaterial berdasarkan panjang gelombang, 
        ukuran nanopartikel, dan material yang dipilih.
    
        Gunakan navigasi di sidebar untuk mengakses halaman lainnya.
    
    
    """)

elif menu == "Penjelasan":
    st.title("Penjelasan Aplikasi")
    st.write("""
        - **Warna Larutan:** Ditentukan berdasarkan panjang gelombang cahaya tampak yang diserap oleh material.
        - **Sifat Magnetis:** Ditentukan berdasarkan ukuran nanopartikel.
        - **Luas Permukaan:** Menghitung luas permukaan nanopartikel berdasarkan ukurannya.
    """)

elif menu == "Kalkulator":
    st.title("Kalkulator Sifat Fisik Nanomaterial")

    material = st.selectbox("Pilih Material Logam", ["Titanium", "Silver", "Gold", "Copper", "Iron"])
    panjang_gelombang = st.number_input("Masukkan Panjang Gelombang (nm):", min_value=100.0, max_value=1500.0, step=1.0)

    if st.button("Lihat Hasil"):
        if panjang_gelombang > 0:
            warna_diserap, warna_teramati, color_code_warna = hitung_warna(panjang_gelombang)
            material_sifat = sifat_material(material)

            st.subheader("Hasil Sifat Fisik Nanomaterial:")

            data = {
                "Sifat": ["Konduktivitas", "Warna", "Sifat Katalitik", "Densitas", "Titik Leleh"],
                "Nilai": [
                    material_sifat["Konduktivitas"],
                    material_sifat["Warna"],
                    material_sifat["Sifat Katalitik"],
                    material_sifat["Densitas"],
                    material_sifat["Titik Leleh"]
                ]
            }
            df = pd.DataFrame(data)
            st.table(df)

            st.write(f"**Warna Diserap**: {warna_diserap}")
            st.write(f"**Warna Teramati**: {warna_teramati}")
            st.plotly_chart(plot_larutan_animasi(color_code_warna))

elif menu == "Identitas Pembuat":
    st.title("Identitas Pembuat")
    st.write("""
    **MAHASISWA POLITEKNIK AKA BOGOR**  
    **PROGRAM STUDI D4 NANOTEKNOLOGI PANGAN**

    1. Alifa Nadia Utami (2350072)  
    2. Nayla Haliza Rahma (2350123)  
    3. Larissa Febriyanti (2350104)  
    4. Aulia Salwa Sahputri Malau (2350078)  
    5. Muhammad Thoriq Syafaat (2350111)
    """)
