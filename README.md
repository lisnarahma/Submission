# Dashboard Penyewaan Sepeda 🚲

Dokumen ini berisi panduan untuk menjalankan dashboard yang telah dibuat untuk projek akhir dalam course analisis data menggunakan python. Analisis ini bertujuan untuk memahami pola penyewaan sepeda berdasarkan faktor waktu dan jenis hari (hari kerja vs akhir pekan). Data yang digunakan mencakup variabel-variabel seperti tanggal, musim, kondisi cuaca, dan jumlah penyewaan sepeda harian.



---

## 📌 Persiapan Lingkungan

### 1️⃣ Menggunakan Anaconda

```sh
conda create --name bike-share python=3.9
conda activate bike-share
pip install -r requirements.txt
```

### 2️⃣ Menggunakan Terminal/Shell

```sh
mkdir proyek_dashboard
cd proyek_dashboard
python -m venv env
source env/bin/activate  # Untuk Linux & Mac
env\Scripts\activate  # Untuk Windows
pip install -r requirements.txt
```

---

## 🚀 Menjalankan Aplikasi Streamlit

```sh
streamlit run dashboard/dashboard.py
```

---

## 📂 Struktur Folder

```
submission/
│── dashboard/
│   ├── dashboard.py
│   ├── main_data.csv
│── data/
│   ├── day.csv
│   ├── hour.csv
│── notebook.ipynb
│── requirements.txt
│── README.md
```

Pastikan semua file dan folder sudah sesuai dengan struktur di atas sebelum menjalankan aplikasi.

---

## 🔗 Link Deployment

Jika dashboard sudah dideploy, tambahkan link di bawah ini:
[🚀 Buka Dashboard](URL_DASHBOARD_KAMU)

---

Semoga bermanfaat! 🎉

