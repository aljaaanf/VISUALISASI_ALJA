# BEDAH KASUS 2 — DATASET PROFIL MAHASISWA

**Nama:** Al Zahra Nur Febrian
**NIM:** 241051006

## Isi
- data_sintesis_mahasiswa_1000.csv
- generate_data.py
- analisis_bedah_kasus_2.py
- app.py
- dashboard.py
- requirements.txt
- ringkasan_jurusan.csv
- ringkasan_semester.csv
- statistik_deskriptif.csv
- matriks_korelasi.csv

## Variabel
- Jurusan: kategorik nominal.
- Semester: kategorik ordinal (urutan 1–8).
- IPK: numerik kontinu.
- Usia: numerik.

## Menjalankan
```bash
python -m pip install -r requirements.txt
python generate_data.py
python analisis_bedah_kasus_2.py
python -m streamlit run app.py
```

## Catatan
2 data pada soal dipertahankan sebagai anchor. 998 baris lainnya adalah
data sintetis untuk kebutuhan pembelajaran, bukan data mahasiswa nyata.
