# pc_per10

Edge Detection Analysis: Sobel vs Canny on Cancer Cell Imagery
Proyek ini bertujuan untuk menganalisis performa dua algoritma deteksi tepi populer, Sobel dan Canny, dalam mengidentifikasi struktur sel pada citra medis sel kanker ![foto](https://github.com/ramzi121006/pc_per10/blob/e7161dfded68dc7b88e0c0896446e00f4e4fff45/pc_per%2010/lungaca1002.jpeg).

1. Analisis Perbandingan Algoritma ![foto](https://github.com/ramzi121006/pc_per10/blob/1e8d441280619e986e85c5e5abdc6b1e630074a4/ss%20pc_per10/gambar%201.png)
Pada tahap ini, dilakukan perbandingan visual langsung antara metode Sobel dan Canny.

Metode Sobel: * Karakteristik: Menghasilkan garis tepi yang tebal (multi-pixel).

Analisis: Sobel bekerja dengan menghitung gradien intensitas secara horizontal dan vertikal. Karena tekstur sel kanker memiliki gradasi warna yang halus, Sobel menangkap banyak informasi "tengah" sehingga garisnya terlihat gemuk.

Kelemahan: Sangat sensitif terhadap noise di latar belakang, terlihat bintik-bintik putih yang mengganggu di sekitar objek utama.

Metode Canny:

Karakteristik: Menghasilkan garis yang sangat tipis (single-pixel) dan presisi.

Analisis: Canny menggunakan tahap Non-Maximum Suppression yang berfungsi membuang piksel-piksel tebal dan hanya menyisakan titik puncak gradien.

Kelebihan: Sangat bersih dari noise berkat bantuan filter Gaussian Blur di tahap awal algoritmanya.

2. Implementasi Aplikasi Interaktif ![foto](https://github.com/ramzi121006/pc_per10/blob/f207adbb430e30a7097641fe6f01db367e696473/ss%20pc_per10/gambar2.png)
Untuk mempermudah analisis, dibuat aplikasi berbasis web menggunakan Streamlit.

Fungsi Interaktif: Aplikasi ini memungkinkan pengguna untuk mengubah nilai Threshold secara real-time melalui slider.

Observasi: * Low Threshold: Jika diatur terlalu rendah, detail halus sel akan muncul namun noise akan meningkat pesat.

High Threshold: Jika diatur terlalu tinggi, beberapa garis tepi sel yang penting mungkin akan terputus atau hilang.

Tujuan: Fitur ini sangat berguna dalam dunia medis untuk menentukan konfigurasi terbaik guna memisahkan massa sel kanker dari jaringan sehat di sekitarnya.

3. Analisis Hasil Akhir & Performa ![foto](https://github.com/ramzi121006/pc_per10/blob/c45dd85d277eb743a205465f1728cf209ec65cfb/ss%20pc_per10/gambar%203.png)
Bagian ini menunjukkan hasil akhir yang telah dioptimasi.

Presisi Geometris: Algoritma Canny berhasil mempertahankan bentuk morfologi sel (bundar/lonjong) dengan sangat konsisten. Hal ini krusial jika sistem ini digunakan untuk menghitung luas area atau jumlah sel secara otomatis (segmentasi).

Efisiensi: Meskipun Canny lebih kompleks secara algoritma (melalui 5 tahap: Blur, Gradient, NMS, Double Threshold, Hysteresis), performanya pada aplikasi interaktif tetap responsif, memberikan keseimbangan yang baik antara akurasi dan kecepatan.
