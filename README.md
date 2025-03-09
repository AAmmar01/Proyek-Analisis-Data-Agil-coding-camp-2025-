# 🚴 Proyek Akhir: Dashboard Analisis Peminjaman Sepeda

Proyek ini merupakan bagian dari **Coding Camp 2025 by DBS Foundation**, yang berfokus pada analisis data menggunakan Python. Proyek ini membangun **dashboard interaktif** dengan **Streamlit** untuk menganalisis pola peminjaman sepeda berdasarkan berbagai faktor seperti waktu, cuaca, dan permintaan.

## 📂 Struktur Proyek
📦Projek_Akhir ┣ 📂dashboard ┃ ┣ 📜dashboard.py ┣ 📂data ┃ ┣ 📜day.csv ┃ ┗ 📜hour.csv ┣ 📜Proyek_Akhir_Analisis_Data.ipynb ┣ 📜README.md ┗ 📜requirements.txt


## 🚀 Instalasi dan Menjalankan Dashboard
1. **Buat Virtual Environment (Opsional)**
   ```sh
   python -m venv env

2. Aktifkan Virtual Environment
Windows:
env\Scripts\activate

3. Instal Dependensi
pip install -r requirements.txt

4. Menjalankan Dashboard
streamlit run dashboard/dashboard.py

📊 Dataset
Dataset yang digunakan adalah dataset peminjaman sepeda yang berisi data harian (day.csv) dan per jam (hour.csv), yang diambil dari sumber publik.

📌 Fitur Dashboard
- Tampilan Data: Menampilkan dataset mentah untuk eksplorasi awal.
- Statistik Deskriptif: Analisis ringkasan data.
- Pola Peminjaman Sepeda:
  Berdasarkan waktu dalam sehari.
  Berdasarkan hari dalam seminggu.
- Faktor Lingkungan: Visualisasi hubungan antara suhu, kelembaban, dan kecepatan angin dengan peminjaman sepeda.
- Clustering Permintaan Sepeda: Pengelompokan berdasarkan kategori waktu dan permintaan.

🔗 Sumber Data
Dataset Bike Sharing
