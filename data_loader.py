# Nama  : Naufal Ihsanul Islam
# NIM   : F1D02310084
# Tugas 6 - Visualisasi Data

import pandas as pd
import os


class DataLoader:
    # Kelas utama pemuat data CSV

    def __init__(self, file_path=None):
        # Path default 
        if file_path is None:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(base_dir, "SuperMarket Analysis.csv")
        self.file_path = file_path
        self.df = None
        self.muat_data()

    def muat_data(self):
        # Muat CSV ke DataFrame
        try:
            self.df = pd.read_csv(self.file_path)
            # Konversi kolom tanggal
            self.df['Date'] = pd.to_datetime(self.df['Date'], format='mixed')
            # Urutkan berdasarkan tanggal
            self.df = self.df.sort_values('Date').reset_index(drop=True)
            return self.df
        except Exception as e:
            print(f"[ERROR] Gagal muat: {e}")
            self.df = pd.DataFrame()
            return self.df

    def ambil_data(self):
        # Ambil salinan data
        return self.df.copy()

    def filter_data(self, cabang=None, gender=None, pembayaran=None, lini_produk=None):
        # Filter berdasarkan kriteria
        df = self.df.copy()

        if cabang and cabang != "Semua":
            df = df[df['Branch'] == cabang]
        if gender and gender != "Semua":
            df = df[df['Gender'] == gender]
        if pembayaran and pembayaran != "Semua":
            df = df[df['Payment'] == pembayaran]
        if lini_produk and lini_produk != "Semua":
            df = df[df['Product line'] == lini_produk]

        return df

    def ambil_nilai_unik(self, kolom):
        # Ambil nilai unik kolom
        if self.df is not None and kolom in self.df.columns:
            return sorted(self.df[kolom].unique().tolist())
        return []

    def hitung_ringkasan(self, df=None):
        # Hitung statistik ringkasan
        if df is None:
            df = self.df

        if df is None or df.empty:
            return {
                'total_penjualan': 0,
                'jumlah_transaksi': 0,
                'rata_rating': 0,
                'total_pendapatan_kotor': 0,
            }

        return {
            'total_penjualan': df['Sales'].sum(),
            'jumlah_transaksi': len(df),
            'rata_rating': df['Rating'].mean(),
            'total_pendapatan_kotor': df['gross income'].sum(),
        }
