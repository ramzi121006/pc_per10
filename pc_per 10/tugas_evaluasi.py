import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Load Gambar
img = cv2.imread('lungaca1002.jpeg', 0) # Load langsung sebagai grayscale
img_blur = cv2.GaussianBlur(img, (3, 3), 0)

# 2. Hitung Sobel (Manual/OpenCV)
sobel_x = cv2.Sobel(img_blur, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(img_blur, cv2.CV_64F, 0, 1, ksize=3)
sobel_mag = np.sqrt(sobel_x**2 + sobel_y**2)
sobel_mag = np.uint8(np.clip(sobel_mag, 0, 255))

# 3. Hitung Canny
canny = cv2.Canny(img_blur, 100, 200)

# 4. Fungsi RMSE (Root Mean Square Error)
# Digunakan untuk membandingkan seberapa besar perbedaan hasil deteksi
def calculate_rmse(imageA, imageB):
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])
    return np.sqrt(err)

rmse_val = calculate_rmse(sobel_mag, canny)

# 5. Visualisasi Perbandingan
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(sobel_mag, cmap='gray')
plt.title(f'Hasil Sobel\n(Garis lebih tebal)')

plt.subplot(1, 2, 2)
plt.imshow(canny, cmap='gray')
plt.title(f'Hasil Canny\n(Garis lebih presisi)')

plt.suptitle(f'Analisis Komparatif\nNilai RMSE: {rmse_val:.2f}')
plt.show()

print(f"Nilai RMSE antara Sobel dan Canny: {rmse_val:.2f}")