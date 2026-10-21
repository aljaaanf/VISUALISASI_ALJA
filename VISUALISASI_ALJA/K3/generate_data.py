import pandas as pd
import numpy as np

NAMA_MAHASISWA = "Al Zahra Nur Febrian"
NIM_MAHASISWA = "241051006"

rng = np.random.default_rng(241051006)

data_asli = pd.DataFrame({
    "Kota": ["Jakarta", "Bandung"],
    "Suhu_C": [32.5, 24.0],
    "Kelembaban_pct": [75.0, 85.0],
    "Kondisi": ["Cerah", "Hujan"]
})

kota_info = {
    "Jakarta": {"p": .22, "temp": 31.0, "hum": 75},
    "Bandung": {"p": .16, "temp": 24.0, "hum": 82},
    "Surabaya": {"p": .16, "temp": 31.5, "hum": 73},
    "Yogyakarta": {"p": .13, "temp": 28.0, "hum": 78},
    "Semarang": {"p": .12, "temp": 29.5, "hum": 76},
    "Medan": {"p": .11, "temp": 30.0, "hum": 80},
    "Makassar": {"p": .10, "temp": 30.5, "hum": 77},
}

kota_list = list(kota_info)
probs = [kota_info[k]["p"] for k in kota_list]
rows = []

for _ in range(998):
    kota = rng.choice(kota_list, p=probs)
    info = kota_info[kota]
    suhu = float(np.clip(rng.normal(info["temp"], 2.2), 18, 36))
    kelembaban = float(np.clip(rng.normal(info["hum"], 7.0), 35, 100))
    r = rng.random()

    if kelembaban >= 86:
        kondisi = "Hujan" if r < .78 else "Berawan"
    elif kelembaban >= 78:
        kondisi = "Berawan" if r < .65 else ("Hujan" if r < .78 else "Cerah")
    elif suhu >= 30:
        kondisi = "Cerah" if r < .72 else "Berawan"
    else:
        kondisi = "Cerah" if r < .55 else "Berawan"

    rows.append({
        "Kota": kota,
        "Suhu_C": round(suhu, 1),
        "Kelembaban_pct": round(kelembaban, 1),
        "Kondisi": kondisi
    })

df = pd.concat([data_asli, pd.DataFrame(rows)], ignore_index=True)
df.to_csv("data_sintesis_cuaca_1000.csv", index=False, encoding="utf-8-sig")
print("Dataset berhasil dibuat:", len(df), "baris")
