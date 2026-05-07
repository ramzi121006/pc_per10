import numpy as np
import cv2
import matplotlib.pyplot as plt
from PIL import Image

# 1. Fungsi Konvolusi Manual (Persyaratan 12) [cite: 658]
def convolve2d_manual(image, kernel):
    # Padding reflect untuk border handling [cite: 682]
    h, w = image.shape
    padded = np.pad(image, 1, mode='reflect')
    output = np.zeros_like(image, dtype=np.float64)
    
    for y in range(h):
        for x in range(w):
            # Ambil window 3x3
            window = padded[y:y+3, x:x+3]
            # Operasi perkalian elemen dan jumlahkan
            output[y, x] = np.sum(window * kernel)
    return output

def sobel_from_scratch(image_path):
    # 2. Load gambar dan konversi ke Grayscale (Persyaratan 11) 
    img_raw = Image.open(image_path).convert('L')
    img = np.array(img_raw, dtype=np.float64)
    
    # 3. Definisi Kernel Sobel Gx dan Gy (Persyaratan 13) 
    Kx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype=np.float64)
    Ky = np.array([[-1, -2, -1], [ 0,  0,  0], [ 1,  2,  1]], dtype=np.float64)
    
    # 4. Proses Konvolusi [cite: 695]
    Gx = convolve2d_manual(img, Kx)
    Gy = convolve2d_manual(img, Ky)
    
    # 5. Hitung Magnitude dan Arah (Persyaratan 14) 
    magnitude = np.sqrt(Gx**2 + Gy**2)
    # Normalisasi ke 0-255
    magnitude = (magnitude / magnitude.max()) * 255
    
    angle = np.arctan2(Gy, Gx) * (180 / np.pi) # Dalam derajat
    
    # 6. Thresholding (Persyaratan 15) [cite: 701]
    threshold_val = 50
    result = np.where(magnitude > threshold_val, 255, 0).astype(np.uint8)
    
    return img, Gx, Gy, magnitude, angle, result

# --- Main Program ---
IMAGE_PATH = 'lungaca1002.jpeg' # Pastikan file ini satu folder dengan script
img_gray, gx, gy, mag, ang, thresh = sobel_from_scratch(IMAGE_PATH)

# Visualisasi (Persyaratan 15) [cite: 661]
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
axes[0,0].imshow(img_gray, cmap='gray'); axes[0,0].set_title('Original Grayscale')
axes[0,1].imshow(np.abs(gx), cmap='gray'); axes[0,1].set_title('Sobel X (Gx)')
axes[0,2].imshow(np.abs(gy), cmap='gray'); axes[0,2].set_title('Sobel Y (Gy)')
axes[1,0].imshow(mag, cmap='gray'); axes[1,0].set_title('Sobel Magnitude')
axes[1,1].imshow(ang, cmap='hsv'); axes[1,1].set_title('Direction Map')
axes[1,2].imshow(thresh, cmap='gray'); axes[1,2].set_title('Thresholded (50)')

plt.tight_layout()
plt.show()