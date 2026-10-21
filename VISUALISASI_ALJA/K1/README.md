# Identitas Mahasiswa

**Nama:** Al Zahra Nur Febrian  
**NIM:** 241051006

---

# Bedah Kasus 1 — Dashboard Operasional Penjualan

## Isi folder
- `data_sintesis_1000.csv` — 1.000 baris data.
- `analisis_bedah_kasus_1.py` — analisis eksploratif + visualisasi Python.
- `ANALISIS_BEDAH_KASUS_1.md` — laporan analisis lengkap.
- `dashboard.py` — aplikasi Streamlit interaktif.
- `requirements.txt` — dependensi.
- `01_omzet_per_kategori.png` s.d. `04_harga_vs_jumlah.png` — hasil visualisasi statis.

## Menjalankan
```bash
cd bedah_kasus_1
pip install -r requirements.txt
streamlit run dashboard.py
```

## Konsep data
Variabel pada kasus:
- `Produk` → kategorik nominal
- `Kategori` → kategorik nominal
- `Harga` → numerik kontinu, rasio
- `Jumlah_Terjual` → numerik diskrit, rasio
- `Tanggal` → waktu

`Omzet` adalah variabel turunan:
`Omzet = Harga × Jumlah_Terjual`

Dataset bersifat sintetis/ilustratif. Jangan menyebut hasilnya sebagai performa penjualan riil.


## Identitas
- **Nama:** Al Zahra Nur Febrian
- **NIM:** 241051006

## Menjalankan dashboard
Gunakan file `app.py` agar dashboard menampilkan nama dan NIM secara jelas:

```bash
python -m streamlit run app.py
```

Alternatif:
```bash
python -m streamlit run dashboard.py
```
