Berikut contoh **deskripsi proyek** untuk kode segmentasi kamu, dengan gaya yang sama seperti contoh “UTS Citra Digital – Pengolahan Citra dengan Filter” di atas 👇

---

# 🧠 UTS Citra Digital – Segmentasi Citra dengan Metode Thresholding & Watershed

Proyek ini merupakan tugas UTS mata kuliah **Citra Digital**, yang berfokus pada penerapan **metode segmentasi citra** menggunakan *thresholding Otsu* dan *algoritma Watershed* untuk memisahkan objek dari latar belakang dengan bantuan operasi morfologi dan transformasi jarak (*distance transform*).

---

## 📂 Struktur Proyek

* `citradgital.py` → Program utama untuk menjalankan seluruh proses segmentasi
* `gambar.jpg` → Citra uji yang digunakan untuk segmentasi

---

## ⚙️ Teknologi yang Digunakan

* **Python**
* **OpenCV (`cv2`)** – untuk operasi pengolahan citra dan segmentasi
* **NumPy** – untuk perhitungan matriks dan operasi numerik
* **Matplotlib** – untuk visualisasi hasil dalam bentuk subplot

---

## 📸 Hasil Output

Berikut visualisasi tahapan pemrosesan citra:

| Tahap Proses                   | Keterangan                                                             |
| ------------------------------ | ---------------------------------------------------------------------- |
| **Citra Asli (Grayscale)**     | Gambar uji dikonversi menjadi grayscale agar mudah diproses.           |
| **Threshold (Otsu)**           | Segmentasi awal berbasis ambang otomatis (Otsu’s method).              |
| **Distance Transform**         | Mengukur jarak setiap piksel terhadap tepi terdekat.                   |
| **Sure Foreground**            | Area yang paling mungkin menjadi objek utama.                          |
| **Sure Background**            | Area yang paling mungkin menjadi latar belakang.                       |
| **Hasil Segmentasi Watershed** | Batas objek akhir ditandai warna merah sebagai hasil akhir segmentasi. |

![Hasil Segmentasi](https://github.com/paldi2099/program-Python-metode-thresholding/blob/da5a6fc09c5214d252d35e8f2374fff23fc8bf71/hasil%20output.png)

---

## 🧩 Penjelasan Singkat

Tahapan utama dalam proses segmentasi ini meliputi:

1. **Preprocessing & Gaussian Blur**
   Mengurangi noise agar thresholding lebih akurat.

2. **Thresholding (Otsu’s Method)**
   Menentukan nilai ambang secara otomatis untuk membedakan objek dan latar belakang.

3. **Morfologi & Distance Transform**
   Digunakan untuk memperjelas area foreground dan background sebelum dilakukan segmentasi.

4. **Algoritma Watershed**
   Menganggap citra sebagai lanskap topografi — air “mengalir” dari titik minimum (seed) untuk membentuk batas antara region.
   Hasilnya berupa segmentasi yang menandai batas objek dengan warna merah.

---

## 📈 Analisis Hasil

Metode Watershed bekerja sangat baik pada citra dengan perbedaan kontras jelas antara objek dan latar.
Namun, jika citra memiliki **noise tinggi atau pencahayaan tidak merata**, maka perlu dilakukan preprocessing tambahan seperti:

* Penyesuaian histogram
* Filter bilateral
* Penambahan *markers manual*

Secara visual, hasil akhir menunjukkan bahwa **batas objek terdeteksi dengan baik** dan **struktur utama citra tetap terjaga**, menjadikan metode ini efektif untuk segmentasi berbasis area dan tepi.

---

## ✅ Kesimpulan

* **Otsu Thresholding** berguna untuk segmentasi awal otomatis.
* **Watershed Algorithm** menyempurnakan hasil dengan menandai batas antar objek secara presisi.
* Kombinasi keduanya menghasilkan segmentasi yang baik tanpa memerlukan parameter manual.

---

Apakah kamu ingin saya tambahkan versi markdown-nya yang bisa langsung ditempel ke README GitHub (pakai format `README.md`)?
