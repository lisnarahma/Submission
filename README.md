# Dashboard Penyewaan Sepeda 🚲

Dokumen ini berisi panduan untuk menjalankan dashboard yang telah dibuat untuk projek akhir dalam course analisis data menggunakan python. Analisis ini bertujuan untuk memahami pola penyewaan sepeda berdasarkan faktor waktu dan jenis hari (hari kerja vs akhir pekan). Data yang digunakan mencakup variabel-variabel seperti tanggal, musim, kondisi cuaca, dan jumlah penyewaan sepeda harian.
---
## Insight 

1. Hari dengan jumlah penyewaan tertinggi: Penyewaan sepeda tertinggi terjadi pada hari kerja dengan cuaca cerah, terutama di musim panas.
2. Perbandingan penyewaan antara hari kerja dan akhir pekan: Jumlah penyewaan sepeda cenderung lebih tinggi pada hari kerja dibandingkan akhir pekan, terutama pada jam sibuk pagi dan sore hari.


---

## Cara Menjalankan Dashboard
---
### Buat dan Masuk ke Virtual Environment
```
cd submission
pipenv install
pipenv shell
pip install -r requirements.txt
```
---

### Menggunakan Anaconda

```
conda create --name bike-ds python=3.9
conda activate bike-ds
pip install -r requirements.txt
```

### Menjalankan Aplikasi Streamlit

```
cd dashboard
streamlit run dashboard.py
```
