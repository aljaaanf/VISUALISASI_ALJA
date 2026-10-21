# Identitas Mahasiswa

- **Nama:** Al Zahra Nur Febrian
- **NIM:** 241051006

---

# Bedah Kasus 1 — Dataset Operasional Penjualan

## 1. Tujuan
Dataset awal hanya memiliki 2 observasi:
- Laptop — Elektronik — Rp8.500.000 — 45 unit — 01/01/2024
- Buku — Pendidikan — Rp75.000 — 120 unit — 02/01/2024

Karena 2 baris tidak cukup untuk analisis statistik maupun dashboard yang representatif, dibuat dataset sintesis sebanyak **1.000 baris**.

## 2. Metodologi Sintesis
- 2 data asli dipertahankan sebagai **anchor**.
- 998 baris tambahan dibuat secara sintetis.
- Kategori diperluas menjadi: Elektronik, Pendidikan, Rumah Tangga, Aksesori, dan Kantor.
- Produk diturunkan dari pola bisnis yang masuk akal berdasarkan dua contoh awal.
- Harga dibuat bervariasi di sekitar harga dasar tiap produk.
- Jumlah terjual dibuat dari baseline permintaan, variasi acak, pengaruh harga, dan faktor musiman bulanan.
- Periode data: 2024-01-01 sampai 2024-12-31.
- Random seed: **42**, sehingga dataset dapat direproduksi.

> Penting: data 998 baris adalah data sintetis/ilustratif, bukan data transaksi nyata.

## 3. Ringkasan Dataset
| Metrik | Nilai |
|---|---:|
| Jumlah baris | 1,000 |
| Produk unik | 32 |
| Kategori | 5 |
| Periode | 2024-01-01 s.d. 2024-12-31 |
| Total unit terjual | 92,916 |
| Total omzet | Rp70,806,261,000 |
| Rata-rata harga | Rp1,272,869 |
| Median harga | Rp357,500 |
| Rata-rata jumlah terjual/transaksi | 92.92 |
| Median jumlah terjual/transaksi | 80 |
| Rata-rata omzet/transaksi | Rp70,806,261 |
| Korelasi harga vs jumlah terjual | -0.415 |

## 4. Analisis Kategorik (Nominal)
Kategori cocok divisualisasikan dengan **bar chart** atau **pie chart** karena bersifat nominal.

Kategori dengan omzet terbesar adalah **Elektronik**, dengan omzet sekitar **Rp54,182,842,000** atau **76.52%** dari total omzet.

## 5. Analisis Numerik
### Harga (Rasio)
Harga memiliki nol absolut secara konseptual dan dapat dibandingkan dengan operasi rasio. Statistik penting:
- Minimum: Rp11,000
- Q1: Rp96,000
- Median: Rp357,500
- Q3: Rp1,531,500
- Maksimum: Rp9,206,000

### Jumlah Terjual (Diskrit/Rasio)
- Minimum: 21 unit
- Q1: 55
- Median: 80
- Q3: 115
- Maksimum: 473 unit

Histogram digunakan untuk melihat bentuk distribusi harga. Scatter plot digunakan untuk mengecek hubungan harga dengan volume penjualan.

## 6. Analisis Waktu
Tanggal termasuk data waktu dan pada studi kasus ini dipakai sebagai variabel temporal untuk **line chart**.

- Bulan dengan omzet tertinggi: **Dec 2024**, Rp9,070,842,000
- Bulan dengan omzet terendah: **Jan 2024**, Rp2,763,426,000

Karena data sintetis memasukkan faktor musiman, dashboard dapat dipakai untuk melihat pola perubahan omzet dan volume dari waktu ke waktu.

## 7. Analisis Produk
Produk dengan omzet terbesar:
- **Laptop** (Elektronik)
- Omzet: **Rp23,171,926,000**
- Unit terjual: **2,759**

## 8. Interpretasi Korelasi
Korelasi harga dan jumlah terjual = **-0.415**.

Nilai korelasi harus dibaca sebagai hubungan pada **data sintetis**, bukan bukti sebab-akibat. Korelasi negatif berarti produk dengan harga lebih tinggi cenderung memiliki volume lebih rendah, tetapi banyak faktor lain dapat memengaruhi penjualan.

## 9. Rekomendasi Visualisasi
1. **Bar chart** — omzet per kategori.
2. **Line chart** — tren omzet bulanan.
3. **Histogram** — distribusi harga.
4. **Scatter plot** — harga vs jumlah terjual.
5. **KPI cards** — total omzet, total unit, transaksi, produk unik.
6. **Tabel ranking** — produk/kategori dengan omzet tertinggi.

## 10. Cara Menjalankan Dashboard
```bash
pip install -r requirements.txt
streamlit run dashboard.py
```

Dashboard akan membaca `data_sintesis_1000.csv` dan menyediakan filter kategori, produk, serta rentang tanggal.
