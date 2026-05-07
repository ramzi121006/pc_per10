import streamlit as st
import cv2
import numpy as np
from PIL import Image

# 1. Konfigurasi Halaman
st.set_page_config(page_title="Aplikasi Deteksi Tepi - Tugas 3", layout="wide")

st.title("🔬 Aplikasi Deteksi Tepi: Citra Sel Kanker")
st.write("Gunakan slider di samping kiri untuk mengatur parameter deteksi.")

# 2. Sidebar Kontrol
st.sidebar.header("Parameter Kontrol")
metode = st.sidebar.selectbox("Pilih Metode", ["Sobel", "Canny", "Bandingkan Keduanya"])

# Inisialisasi variabel gambar
img_original = None

# 3. Penanganan Input Gambar
uploaded_file = st.file_uploader("Upload foto lungaca1002.jpeg", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    # Jika user upload file
    img_raw = Image.open(uploaded_file)
    img_original = np.array(img_raw)
else:
    # Jika belum upload, coba cari file default di folder
    try:
        img_raw = Image.open('lungaca1002.jpeg')
        img_original = np.array(img_raw)
        st.info("ℹ️ Menggunakan file default: lungaca1002.jpeg")
    except FileNotFoundError:
        st.warning("⚠️ File 'lungaca1002.jpeg' tidak ditemukan. Silakan upload gambar secara manual di atas.")

# 4. Proses Pengolahan Citra (Jika gambar ada)
if img_original is not None:
    # Konversi ke Grayscale dengan aman
    if len(img_original.shape) == 3:
        gray = cv2.cvtColor(img_original, cv2.COLOR_RGB2GRAY)
    else:
        gray = img_original

    # Layout Kolom
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🖼️ Gambar Grayscale")
        st.image(gray, use_container_width=True)

    with col2:
        # LOGIKA SOBEL
        if metode in ["Sobel", "Bandingkan Keduanya"]:
            st.subheader("⚡ Hasil Deteksi Sobel")
            s_thresh = st.sidebar.slider("Sobel Threshold", 0, 255, 50)
            
            blur_s = cv2.GaussianBlur(gray, (3, 3), 0)
            gx = cv2.Sobel(blur_s, cv2.CV_64F, 1, 0, ksize=3)
            gy = cv2.Sobel(blur_s, cv2.CV_64F, 0, 1, ksize=3)
            mag = np.sqrt(gx**2 + gy**2)
            mag = np.uint8(np.clip(mag, 0, 255))
            _, sobel_final = cv2.threshold(mag, s_thresh, 255, cv2.THRESH_BINARY)
            st.image(sobel_final, use_container_width=True)

        # LOGIKA CANNY
        if metode in ["Canny", "Bandingkan Keduanya"]:
            st.subheader("🎯 Hasil Deteksi Canny")
            low_t = st.sidebar.slider("Canny Low Threshold", 0, 255, 50)
            high_t = st.sidebar.slider("Canny High Threshold", 0, 255, 150)
            
            blur_c = cv2.GaussianBlur(gray, (5, 5), 1.4)
            canny_final = cv2.Canny(blur_c, low_t, high_t)
            st.image(canny_final, use_container_width=True)

    st.success("Proses Berhasil! Sesuaikan slider di sidebar untuk melihat perubahan.")