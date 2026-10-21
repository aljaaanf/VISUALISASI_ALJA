# BEDAH KASUS 3 — DATASET PENGAMATAN CUACA

**Nama:** Al Zahra Nur Febrian
**NIM:** 241051006

## Data awal
- Jakarta | Suhu 32.5°C | Kelembaban 75% | Cerah
- Bandung | Suhu 24.0°C | Kelembaban 85% | Hujan

## Dataset
Total 1.000 pengamatan:
- 2 observasi awal dipertahankan
- 998 observasi dibuat secara sintetis

## Jenis variabel
- Kota: Kategorik Nominal
- Suhu (°C): Numerik Interval
- Kelembaban (%): Numerik Rasio
- Kondisi: Kategorik Nominal

## Cara menjalankan

```bash
python -m pip install -r requirements.txt
python generate_data.py
python analisis_bedah_kasus_3.py
python -m streamlit run app.py
```

## Catatan
Dataset ini sintetis untuk kebutuhan pembelajaran visualisasi dan analisis data,
bukan data pengamatan cuaca nyata.
