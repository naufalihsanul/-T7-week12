# Nama  : Naufal Ihsanul Islam
# NIM   : F1D02310084
# Tugas 6 - Visualisasi Data

from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QComboBox, QPushButton, QTableWidget,
    QTableWidgetItem, QFrame, QHeaderView, QFileDialog,
    QSplitter, QMessageBox
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

from data_loader import DataLoader
from chart_widget import ChartCanvas


class KartuRingkasan(QFrame):
    # Kelas widget kartu ringkasan

    def __init__(self, ikon, judul, nilai):
        super().__init__()
        self.setObjectName("kartuRingkasan")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(14, 12, 14, 12)
        layout.setSpacing(4)

        # Ikon
        lbl_ikon = QLabel(ikon)
        lbl_ikon.setObjectName("kartuIkon")
        layout.addWidget(lbl_ikon)

        # Judul
        self.lbl_judul = QLabel(judul)
        self.lbl_judul.setObjectName("kartuJudul")
        layout.addWidget(self.lbl_judul)

        # Nilai
        self.lbl_nilai = QLabel(str(nilai))
        self.lbl_nilai.setObjectName("kartuNilai")
        layout.addWidget(self.lbl_nilai)

    def perbarui_nilai(self, nilai):
        # Update nilai kartu
        self.lbl_nilai.setText(str(nilai))


class DashboardWindow(QMainWindow):
    # Window utama dashboard

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dashboard Analisis Supermarket")
        self.setMinimumSize(1000, 650)
        self.resize(1200, 780)

        # Muat data
        self.loader = DataLoader()

        # Setup UI
        self._buat_ui()
        self._hubungkan_sinyal()
        self._perbarui_dashboard()

    def _buat_ui(self):
        # Buat seluruh UI
        widget_utama = QWidget()
        self.setCentralWidget(widget_utama)
        layout_utama = QVBoxLayout(widget_utama)
        layout_utama.setContentsMargins(16, 12, 16, 12)
        layout_utama.setSpacing(10)

        # Header
        self._buat_header(layout_utama)

        # Kartu ringkasan
        self._buat_kartu(layout_utama)

        # Filter bar
        self._buat_filter(layout_utama)

        # Splitter chart + tabel
        splitter = QSplitter(Qt.Vertical)

        # Area 2 chart
        widget_chart = QWidget()
        layout_chart = QHBoxLayout(widget_chart)
        layout_chart.setContentsMargins(0, 0, 0, 0)
        layout_chart.setSpacing(8)

        self.chart_kiri = ChartCanvas(width=5, height=3.5)
        self.chart_kiri.setObjectName("chartKiri")
        layout_chart.addWidget(self.chart_kiri)

        self.chart_kanan = ChartCanvas(width=5, height=3.5)
        self.chart_kanan.setObjectName("chartKanan")
        layout_chart.addWidget(self.chart_kanan)

        splitter.addWidget(widget_chart)

        # Tabel data
        self._buat_tabel()
        splitter.addWidget(self.tabel)

        splitter.setStretchFactor(0, 3)
        splitter.setStretchFactor(1, 2)
        layout_utama.addWidget(splitter, 1)

    def _buat_header(self, layout):
        # Header judul
        frame = QFrame()
        frame.setObjectName("frameHeader")
        lay = QHBoxLayout(frame)
        lay.setContentsMargins(16, 10, 16, 10)

        judul = QLabel("Dashboard Analisis Penjualan Supermarket")
        judul.setObjectName("judulDashboard")
        lay.addWidget(judul)

        lay.addStretch()

        jumlah = len(self.loader.df) if self.loader.df is not None else 0
        info = QLabel(f"{jumlah} transaksi  |  Dataset Kaggle")
        info.setObjectName("infoDataset")
        lay.addWidget(info)

        layout.addWidget(frame)

    def _buat_kartu(self, layout):
        # Buat 4 kartu ringkasan
        lay = QHBoxLayout()
        lay.setSpacing(8)

        self.kartu_penjualan = KartuRingkasan("💰", "Total Penjualan", "$0")
        self.kartu_transaksi = KartuRingkasan("🛒", "Jumlah Transaksi", "0")
        self.kartu_rating = KartuRingkasan("⭐", "Rata-rata Rating", "0")
        self.kartu_pendapatan = KartuRingkasan("📈", "Pendapatan Kotor", "$0")

        lay.addWidget(self.kartu_penjualan)
        lay.addWidget(self.kartu_transaksi)
        lay.addWidget(self.kartu_rating)
        lay.addWidget(self.kartu_pendapatan)

        layout.addLayout(lay)

    def _buat_filter(self, layout):
        # Filter dan kontrol
        frame = QFrame()
        frame.setObjectName("frameFilter")
        lay = QHBoxLayout(frame)
        lay.setContentsMargins(12, 8, 12, 8)
        lay.setSpacing(8)

        # Filter cabang
        lay.addWidget(QLabel("Cabang:"))
        self.cmb_cabang = self._combo(self.loader.ambil_nilai_unik('Branch'))
        lay.addWidget(self.cmb_cabang)

        # Filter produk
        lay.addWidget(QLabel("Produk:"))
        self.cmb_produk = self._combo(self.loader.ambil_nilai_unik('Product line'))
        lay.addWidget(self.cmb_produk)

        # Filter pembayaran
        lay.addWidget(QLabel("Bayar:"))
        self.cmb_pembayaran = self._combo(self.loader.ambil_nilai_unik('Payment'))
        lay.addWidget(self.cmb_pembayaran)

        lay.addStretch()

        # Pilih tipe chart kiri
        lay.addWidget(QLabel("Chart 1:"))
        self.cmb_chart_kiri = QComboBox()
        self.cmb_chart_kiri.addItems([
            "Penjualan per Produk",
            "Penjualan per Cabang",
            "Tren Penjualan",
        ])
        lay.addWidget(self.cmb_chart_kiri)

        # Pilih tipe chart kanan
        lay.addWidget(QLabel("Chart 2:"))
        self.cmb_chart_kanan = QComboBox()
        self.cmb_chart_kanan.addItems([
            "Metode Pembayaran",
            "Distribusi Gender",
            "Tipe Pelanggan",
        ])
        lay.addWidget(self.cmb_chart_kanan)

        lay.addStretch()

        # Tombol refresh
        self.btn_refresh = QPushButton("Refresh")
        self.btn_refresh.setObjectName("btnRefresh")
        lay.addWidget(self.btn_refresh)

        # Tombol export
        self.btn_export = QPushButton("Export PNG")
        self.btn_export.setObjectName("btnExport")
        lay.addWidget(self.btn_export)

        layout.addWidget(frame)

    def _combo(self, items):
        # Buat combo box
        c = QComboBox()
        c.addItem("Semua")
        c.addItems([str(i) for i in items])
        c.setMinimumWidth(90)
        return c

    def _buat_tabel(self):
        # Buat tabel data
        self.tabel = QTableWidget()
        self.tabel.setObjectName("tabelData")
        self.tabel.setAlternatingRowColors(True)
        self.tabel.setSelectionBehavior(QTableWidget.SelectRows)
        self.tabel.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tabel.verticalHeader().setDefaultSectionSize(28)
        header = self.tabel.horizontalHeader()
        header.setStretchLastSection(True)
        header.setSectionResizeMode(QHeaderView.Interactive)

    def _hubungkan_sinyal(self):
        # Hubungkan sinyal
        self.cmb_cabang.currentIndexChanged.connect(self._perbarui_dashboard)
        self.cmb_produk.currentIndexChanged.connect(self._perbarui_dashboard)
        self.cmb_pembayaran.currentIndexChanged.connect(self._perbarui_dashboard)
        self.cmb_chart_kiri.currentIndexChanged.connect(self._update_kiri)
        self.cmb_chart_kanan.currentIndexChanged.connect(self._update_kanan)
        self.btn_refresh.clicked.connect(self._refresh)
        self.btn_export.clicked.connect(self._export)

    def _data_filter(self):
        # Ambil data terfilter
        return self.loader.filter_data(
            cabang=self.cmb_cabang.currentText(),
            lini_produk=self.cmb_produk.currentText(),
            pembayaran=self.cmb_pembayaran.currentText()
        )

    def _perbarui_dashboard(self):
        # Perbarui semua
        df = self._data_filter()
        self._perbarui_kartu(df)
        self._perbarui_tabel(df)
        self._update_kiri(df_data=df)
        self._update_kanan(df_data=df)

    def _perbarui_kartu(self, df):
        # Update kartu
        r = self.loader.hitung_ringkasan(df)
        self.kartu_penjualan.perbarui_nilai(f"${r['total_penjualan']:,.2f}")
        self.kartu_transaksi.perbarui_nilai(f"{r['jumlah_transaksi']:,}")
        self.kartu_rating.perbarui_nilai(f"{r['rata_rating']:.1f} / 10")
        self.kartu_pendapatan.perbarui_nilai(f"${r['total_pendapatan_kotor']:,.2f}")

    def _perbarui_tabel(self, df):
        # Update tabel
        self.tabel.setRowCount(0)
        if df.empty:
            return

        kolom = ['Invoice ID', 'Branch', 'City', 'Customer type',
                 'Gender', 'Product line', 'Unit price', 'Quantity',
                 'Sales', 'Date', 'Payment', 'Rating']
        self.tabel.setColumnCount(len(kolom))
        self.tabel.setHorizontalHeaderLabels(kolom)
        self.tabel.setRowCount(len(df))

        for i, (_, baris) in enumerate(df.iterrows()):
            for j, kol in enumerate(kolom):
                if kol == 'Date':
                    val = baris[kol].strftime('%d/%m/%Y')
                elif kol in ['Unit price', 'Sales']:
                    val = f"{baris[kol]:,.2f}"
                elif kol == 'Rating':
                    val = f"{baris[kol]:.1f}"
                else:
                    val = str(baris.get(kol, ''))
                item = QTableWidgetItem(val)
                item.setTextAlignment(Qt.AlignCenter)
                self.tabel.setItem(i, j, item)

    def _update_kiri(self, df_data=None):
        # Update chart kiri
        df = df_data if df_data is not None else self._data_filter()
        tipe = self.cmb_chart_kiri.currentText()

        if "Produk" in tipe:
            self.chart_kiri.bar_penjualan_per_lini(df)
        elif "Cabang" in tipe:
            self.chart_kiri.bar_penjualan_per_cabang(df)
        elif "Tren" in tipe:
            self.chart_kiri.line_tren_penjualan(df)

    def _update_kanan(self, df_data=None):
        # Update chart kanan
        df = df_data if df_data is not None else self._data_filter()
        tipe = self.cmb_chart_kanan.currentText()

        if "Pembayaran" in tipe:
            self.chart_kanan.pie_metode_pembayaran(df)
        elif "Gender" in tipe:
            self.chart_kanan.pie_distribusi_gender(df)
        elif "Pelanggan" in tipe:
            self.chart_kanan.pie_tipe_pelanggan(df)

    def _refresh(self):
        # Refresh data
        self.loader.muat_data()
        self.cmb_cabang.setCurrentIndex(0)
        self.cmb_produk.setCurrentIndex(0)
        self.cmb_pembayaran.setCurrentIndex(0)
        self._perbarui_dashboard()
        QMessageBox.information(self, "Refresh", "Data berhasil dimuat ulang!")

    def _export(self):
        # Export chart PNG
        path, _ = QFileDialog.getSaveFileName(
            self, "Simpan Chart", "chart.png", "PNG (*.png)")
        if path:
            try:
                p1 = path.replace('.png', '_chart1.png')
                p2 = path.replace('.png', '_chart2.png')
                self.chart_kiri.fig.savefig(p1, dpi=150, bbox_inches='tight',
                                            facecolor='white')
                self.chart_kanan.fig.savefig(p2, dpi=150, bbox_inches='tight',
                                             facecolor='white')
                QMessageBox.information(
                    self, "Export Berhasil",
                    f"Tersimpan:\n{p1}\n{p2}")
            except Exception as e:
                QMessageBox.warning(self, "Gagal", str(e))
