# ANALISIS DETAIL BEDAH KASUS 3

**Nama:** Al Zahra Nur Febrian
**NIM:** 241051006

## 1. Tujuan
Membuat dataset sintetis sebanyak 1.000 pengamatan cuaca berdasarkan dua
data awal, melakukan eksplorasi dan analisis statistik menggunakan Python,
kemudian menyajikannya dalam dashboard Streamlit.

## 2. Data awal

| Kota | Suhu (°C) | Kelembaban (%) | Kondisi |
|---|---:|---:|---|
| Jakarta | 32.5 | 75 | Cerah |
| Bandung | 24.0 | 85 | Hujan |

Dua baris tersebut dipertahankan sebagai data anchor.

## 3. Klasifikasi variabel

### Kota — Kategorik Nominal
Kota adalah label tanpa urutan. Jakarta tidak lebih tinggi/rendah dari Bandung
dalam skala nominal. Visualisasi yang sesuai adalah bar chart dan pie/donut chart.

### Suhu — Numerik Interval
Suhu Celsius termasuk skala interval: selisih 20°C dan 10°C sama-sama
menunjukkan selisih 10 derajat, tetapi 20°C tidak dapat diartikan dua kali
lebih panas daripada 10°C. Histogram dan scatter plot sesuai untuk analisisnya.

### Kelembaban — Numerik Rasio
Kelembaban persen diperlakukan sebagai variabel rasio pada kasus ini karena
0% mempunyai makna absolut, yaitu tidak ada kelembaban. Histogram, box plot,
dan scatter plot sesuai.

### Kondisi — Kategorik Nominal
Cerah, Berawan, dan Hujan adalah label tanpa urutan. Bar chart dan pie chart
sesuai untuk melihat frekuensinya.

## 4. Analisis Python
Analisis mencakup:
- ukuran dataset
- tipe data
- missing value
- duplikasi
- statistik deskriptif suhu dan kelembaban
- jumlah pengamatan per kota
- distribusi kondisi cuaca
- rata-rata suhu dan kelembaban per kota
- korelasi suhu dan kelembaban
- insight otomatis
- visualisasi distribusi dan hubungan variabel

## 5. Dashboard
Dashboard Streamlit menyediakan filter:
- Kota
- Kondisi
- Rentang suhu
- Rentang kelembaban

Dashboard menampilkan KPI, bar chart, pie chart, histogram, scatter plot,
matriks korelasi, tabel data, dan tombol download hasil filter.

## 6. Catatan metodologi
Sebanyak 998 observasi dibuat secara sintetis dengan distribusi yang dibuat
masuk akal untuk konteks cuaca kota-kota Indonesia. Data sintetis tidak boleh
dianggap sebagai data cuaca aktual atau hasil pengukuran resmi.
