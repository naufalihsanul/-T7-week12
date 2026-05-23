# 🏪 Dashboard Visualisasi Data Supermarket

**Tugas 6 - Praktikum Pemrograman Visual**

| | |
|---|---|
| **Nama** | Naufal Ihsanul Islam |
| **NIM** | F1D02310084 |
| **Mata Kuliah** | Pemrograman Visual |

---

## 📋 Deskripsi

Aplikasi dashboard interaktif berbasis **PySide6** untuk menganalisis dan memvisualisasikan data penjualan supermarket. Dashboard menampilkan data dalam bentuk tabel, ringkasan statistik, serta grafik **Matplotlib** yang terintegrasi langsung di dalam aplikasi.

---

## 📊 Dataset

- **Nama Dataset**: Supermarket Sales Dataset
- **Sumber**: [Kaggle - Supermarket Sales](https://www.kaggle.com/datasets/faresashraf1001/supermarket-sales)
- **Jumlah Data**: 1.001 baris transaksi
- **Kolom Utama**:

| Kolom | Deskripsi |
|---|---|
| `Invoice ID` | ID unik transaksi |
| `Branch` | Cabang supermarket (Alex, Cairo, Giza) |
| `City` | Kota lokasi cabang |
| `Customer type` | Tipe pelanggan (Member / Normal) |
| `Gender` | Jenis kelamin pelanggan |
| `Product line` | Kategori produk |
| `Unit price` | Harga satuan produk |
| `Quantity` | Jumlah barang dibeli |
| `Tax 5%` | Pajak 5% dari total |
| `Sales` | Total penjualan |
| `Date` | Tanggal transaksi |
| `Time` | Waktu transaksi |
| `Payment` | Metode pembayaran |
| `cogs` | Harga pokok penjualan |
| `gross income` | Pendapatan kotor |
| `Rating` | Rating kepuasan pelanggan (1-10) |

---

## ✨ Fitur Aplikasi

1. **Tabel Data** — Menampilkan data mentah di `QTableWidget` dengan format rapi
2. **Kartu Ringkasan** — Total penjualan, jumlah transaksi, rata-rata rating, pendapatan kotor
3. **4 Tipe Chart Bar/Line**:
   - Penjualan per Lini Produk (Bar Horizontal)
   - Penjualan per Cabang (Bar Vertikal)
   - Rating Rata-rata per Produk (Bar Horizontal)
   - Tren Penjualan Harian (Line Chart)
4. **4 Tipe Chart Pie (Donut)**:
   - Distribusi Metode Pembayaran
   - Distribusi Gender Pelanggan
   - Distribusi Tipe Pelanggan
   - Proporsi Penjualan per Produk
5. **Filter Interaktif** — Filter berdasarkan Cabang, Gender, Pembayaran, Lini Produk
6. **Tombol Refresh** — Muat ulang data dan reset filter
7. **Tombol Export PNG** — Simpan chart sebagai file gambar PNG

---

## 🗂️ Struktur Project

```
T7-week12/
├── main.py                     # Entry point aplikasi
├── main_window.py              # Window utama dashboard
├── data_loader.py              # Pemuat dan pengolah data CSV
├── chart_widget.py             # Widget chart Matplotlib
├── style.qss                   # Stylesheet QSS terpisah
├── SuperMarket Analysis.csv    # Dataset
└── README.md                   # Dokumentasi
```

---

## 🚀 Cara Menjalankan

1. Pastikan Python 3.x sudah terinstall
2. Install dependensi:
   ```bash
   pip install PySide6 pandas matplotlib
   ```
3. Jalankan aplikasi:
   ```bash
   python main.py
   ```

---

## 📸 Screenshot

### 1. Dashboard Awal (Menampilkan 50+ Data, Chart Bar & Pie)
![Dashboard Awal](output/dasboard%20awal.png)

### 2. Filter Data Aktif
![Filter Data](output/filter%20.png)

### 3. Pilihan Tipe Chart
![Pilih Chart](output/pilih%20chart.png)

### 4. Hasil Perubahan Chart
![Hasil Perubahan Chart](output/hasil%20pilih%20chart%20baru.png)

### 5. Tombol Refresh
![Tombol Refresh](output/tombol%20refresh.png)

### 6. Tombol Export PNG
![Export PNG](output/export%20png.png)

---

## 🛠️ Teknologi

- **PySide6** — Framework GUI
- **Matplotlib** — Visualisasi chart (terintegrasi di PySide6)
- **Pandas** — Pengolahan dan analisis data
- **QSS** — Styling UI (file terpisah)
