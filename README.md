# Dashboard Penyewaan Sepeda 🚲

Dokumen ini berisi panduan untuk menjalankan dashboard interaktif yang dibuat untuk menganalisis faktor-faktor yang memengaruhi penyewaan sepeda. Analisis ini bertujuan untuk memahami pola penyewaan sepeda berdasarkan faktor cuaca dan musim.

---
## Insight

1. **Faktor Cuaca di Setiap Bulan pada Tahun 2012:**
   - Cuaca cerah dan suhu yang lebih hangat cenderung meningkatkan jumlah penyewaan sepeda.
   - Bulan-bulan musim panas memiliki rata-rata penyewaan yang lebih tinggi dibandingkan bulan lainnya.
   
2. **Pola Penyewaan Sepeda Berdasarkan Musim dan Kondisi Cuaca:**
   - Penyewaan sepeda meningkat di musim panas dan menurun di musim dingin.
   - Kondisi cuaca yang buruk seperti hujan atau salju menyebabkan penurunan signifikan dalam jumlah penyewaan.

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

