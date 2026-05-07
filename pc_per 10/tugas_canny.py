import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Load gambar sel kanker
img = cv2.imread('lungaca1002.jpeg')
# Konversi ke Grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 2. Pre-processing: Gaussian Blur (Sangat penting untuk Canny agar tidak noise)
# Sesuai langkah di halaman 1 modul
blur = cv2.GaussianBlur(gray, (5, 5), 1.4)

# 3. Implementasi Canny Edge Detection
# Kita akan mencoba 3 variasi threshold untuk melihat perbedaannya
# cv2.Canny(image, low_threshold, high_threshold)
canny_low = cv2.Canny(blur, 50, 100)
canny_mid = cv2.Canny(blur, 100, 200)
canny_high = cv2.Canny(blur, 150, 250)

# 4. Visualisasi Hasil Perbandingan
titles = ['Original Grayscale', 'Canny (50, 100)', 
          'Canny (100, 200)', 'Canny (150, 250)']
images = [gray, canny_low, canny_mid, canny_high]

plt.figure(figsize=(16, 8))
for i in range(4):
    plt.subplot(1, 4, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.show()

# 5. Menampilkan hasil perbandingan Sobel vs Canny (Opsional untuk laporan)
sobel_x = cv2.Sobel(blur, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(blur, cv2.CV_64F, 0, 1, ksize=3)
sobel_mag = np.sqrt(sobel_x**2 + sobel_y**2)
sobel_mag = np.uint8(np.clip(sobel_mag, 0, 255))

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(sobel_mag, cmap='gray')
plt.title('Hasil Sobel')
plt.subplot(1, 2, 2)
plt.imshow(canny_mid, cmap='gray')
plt.title('Hasil Canny (Lebih Bersih)')
plt.show()