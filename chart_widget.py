# Nama  : Naufal Ihsanul Islam
# NIM   : F1D02310084
# Tugas 6 - Visualisasi Data

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt

# Warna chart sederhana
WARNA = ['#4F6D7A', '#7A9E9F', '#B8D4D4', '#D4A574', '#E8C39E', '#9BB5C4']
BG = '#FFFFFF'
TEKS = '#333333'
GRID = '#E5E7EB'


class ChartCanvas(FigureCanvas):
    # Canvas Matplotlib PySide6

    def __init__(self, parent=None, width=5, height=3.5, dpi=100):
        # Inisialisasi canvas
        self.fig = Figure(figsize=(width, height), dpi=dpi, facecolor=BG)
        self.axes = self.fig.add_subplot(111)
        super().__init__(self.fig)
        self.setParent(parent)
        self._atur_style()

    def _atur_style(self):
        # Style default chart
        self.axes.set_facecolor(BG)
        self.axes.tick_params(colors=TEKS, labelsize=8)
        self.axes.spines['top'].set_visible(False)
        self.axes.spines['right'].set_visible(False)
        self.axes.spines['bottom'].set_color(GRID)
        self.axes.spines['left'].set_color(GRID)
        self.axes.xaxis.label.set_color(TEKS)
        self.axes.yaxis.label.set_color(TEKS)
        self.axes.title.set_color(TEKS)
        self.axes.grid(axis='y', color=GRID, linewidth=0.5, alpha=0.7)

    def bersihkan(self):
        # Reset canvas
        self.fig.clear()
        self.axes = self.fig.add_subplot(111)
        self._atur_style()

    # ===== BAR CHART =====

    def bar_penjualan_per_lini(self, df):
        # Bar penjualan per produk
        self.bersihkan()
        data = df.groupby('Product line')['Sales'].sum().sort_values(ascending=True)

        bars = self.axes.barh(range(len(data)), data.values,
                              color=WARNA[0], height=0.5, edgecolor='none')
        self.axes.set_yticks(range(len(data)))
        self.axes.set_yticklabels(data.index, fontsize=8)
        self.axes.set_title('Penjualan per Lini Produk', fontsize=12, pad=10)

        for bar, val in zip(bars, data.values):
            self.axes.text(val + data.max() * 0.01,
                           bar.get_y() + bar.get_height() / 2,
                           f'{val:,.0f}', va='center', fontsize=7, color=TEKS)

        self.fig.tight_layout(pad=2.0)
        self.draw()

    def bar_penjualan_per_cabang(self, df):
        # Bar penjualan per cabang
        self.bersihkan()
        data = df.groupby('Branch')['Sales'].sum().sort_values(ascending=False)

        self.axes.bar(range(len(data)), data.values,
                      color=WARNA[:len(data)], width=0.4, edgecolor='none')
        self.axes.set_xticks(range(len(data)))
        self.axes.set_xticklabels(data.index, fontsize=9)
        self.axes.set_title('Penjualan per Cabang', fontsize=12, pad=10)

        self.axes.yaxis.set_major_formatter(
            ticker.FuncFormatter(lambda x, p: f'{x:,.0f}'))
        self.fig.tight_layout(pad=2.0)
        self.draw()

    def line_tren_penjualan(self, df):
        # Line tren harian
        self.bersihkan()
        data = df.groupby('Date')['Sales'].sum().sort_index()

        self.axes.plot(data.index, data.values, color=WARNA[0], linewidth=1.2)
        self.axes.fill_between(data.index, data.values, alpha=0.08, color=WARNA[0])

        rata = data.mean()
        self.axes.axhline(y=rata, color=WARNA[3], linestyle='--',
                          linewidth=1, label=f'Rata-rata: {rata:,.0f}')

        self.axes.set_title('Tren Penjualan Harian', fontsize=12, pad=10)
        self.axes.legend(fontsize=8, framealpha=0.8)
        self.fig.autofmt_xdate(rotation=30)
        self.fig.tight_layout(pad=2.0)
        self.draw()

    # ===== PIE CHART =====

    def pie_metode_pembayaran(self, df):
        # Pie distribusi pembayaran
        self.bersihkan()
        data = df['Payment'].value_counts()

        self.axes.pie(data.values, labels=data.index, colors=WARNA[:len(data)],
                      autopct='%1.1f%%', startangle=140,
                      textprops={'fontsize': 9, 'color': TEKS})
        self.axes.set_title('Distribusi Metode Pembayaran', fontsize=12, pad=10)
        self.fig.tight_layout(pad=2.0)
        self.draw()

    def pie_distribusi_gender(self, df):
        # Pie distribusi gender
        self.bersihkan()
        data = df['Gender'].value_counts()

        self.axes.pie(data.values, labels=data.index, colors=[WARNA[0], WARNA[3]],
                      autopct='%1.1f%%', startangle=140,
                      textprops={'fontsize': 9, 'color': TEKS})
        self.axes.set_title('Distribusi Gender', fontsize=12, pad=10)
        self.fig.tight_layout(pad=2.0)
        self.draw()

    def pie_tipe_pelanggan(self, df):
        # Pie tipe pelanggan
        self.bersihkan()
        data = df['Customer type'].value_counts()

        self.axes.pie(data.values, labels=data.index, colors=[WARNA[1], WARNA[4]],
                      autopct='%1.1f%%', startangle=140,
                      textprops={'fontsize': 9, 'color': TEKS})
        self.axes.set_title('Distribusi Tipe Pelanggan', fontsize=12, pad=10)
        self.fig.tight_layout(pad=2.0)
        self.draw()
