import pandas as pd
import matplotlib.pyplot as plt

NAMA_MAHASISWA = "Al Zahra Nur Febrian"
NIM_MAHASISWA = "241051006"

df = pd.read_csv("data_sintesis_cuaca_1000.csv")

print("=" * 75)
print("BEDAH KASUS 3 - DATASET PENGAMATAN CUACA")
print("Nama:", NAMA_MAHASISWA)
print("NIM :", NIM_MAHASISWA)
print("=" * 75)

print("\n[1] UKURAN DATA")
print("Baris:", len(df))
print("Kolom:", len(df.columns))

print("\n[2] TIPE DATA")
print(df.dtypes)

print("\n[3] MISSING VALUE")
print(df.isna().sum())

print("\n[4] DUPLIKAT")
print(df.duplicated().sum())

print("\n[5] STATISTIK DESKRIPTIF")
print(df[["Suhu_C", "Kelembaban_pct"]].describe().round(2))

print("\n[6] KOTA - NOMINAL")
kota = (
    df.groupby("Kota")
      .agg(
          Jumlah_Pengamatan=("Kota", "size"),
          Rata2_Suhu_C=("Suhu_C", "mean"),
          Rata2_Kelembaban_pct=("Kelembaban_pct", "mean")
      )
      .sort_values("Jumlah_Pengamatan", ascending=False)
)
kota["Persentase_%"] = kota["Jumlah_Pengamatan"] / len(df) * 100
print(kota.round(2))

print("\n[7] KONDISI - NOMINAL")
kondisi = (
    df.groupby("Kondisi")
      .agg(
          Jumlah_Pengamatan=("Kondisi", "size"),
          Rata2_Suhu_C=("Suhu_C", "mean"),
          Rata2_Kelembaban_pct=("Kelembaban_pct", "mean")
      )
      .sort_values("Jumlah_Pengamatan", ascending=False)
)
print(kondisi.round(2))

print("\n[8] SUHU - NUMERIK INTERVAL")
print("Minimum :", df["Suhu_C"].min())
print("Maksimum:", df["Suhu_C"].max())
print("Mean    :", round(df["Suhu_C"].mean(), 2))
print("Median  :", round(df["Suhu_C"].median(), 2))
print("Std     :", round(df["Suhu_C"].std(), 2))

print("\n[9] KELEMBABAN - NUMERIK RASIO")
print("Minimum :", df["Kelembaban_pct"].min())
print("Maksimum:", df["Kelembaban_pct"].max())
print("Mean    :", round(df["Kelembaban_pct"].mean(), 2))
print("Median  :", round(df["Kelembaban_pct"].median(), 2))
print("Std     :", round(df["Kelembaban_pct"].std(), 2))

print("\n[10] KORELASI")
corr = df[["Suhu_C", "Kelembaban_pct"]].corr()
print(corr.round(3))

print("\n[11] INSIGHT")
print("Kota dengan pengamatan terbanyak:", kota.index[0])
print("Kondisi paling sering:", kondisi.index[0])
print("Kota dengan suhu rata-rata tertinggi:", kota.Rata2_Suhu_C.idxmax())
print("Kota dengan kelembaban rata-rata tertinggi:", kota.Rata2_Kelembaban_pct.idxmax())
print("Rata-rata suhu:", round(df.Suhu_C.mean(), 2), "°C")
print("Rata-rata kelembaban:", round(df.Kelembaban_pct.mean(), 2), "%")
print("Korelasi Suhu-Kelembaban:", round(corr.loc["Suhu_C", "Kelembaban_pct"], 3))

plt.figure(figsize=(10, 6))
kota["Jumlah_Pengamatan"].sort_values().plot(kind="barh")
plt.title("Jumlah Pengamatan per Kota")
plt.xlabel("Jumlah Pengamatan")
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.hist(df["Suhu_C"], bins=18)
plt.title("Distribusi Suhu")
plt.xlabel("Suhu (°C)")
plt.ylabel("Frekuensi")
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.hist(df["Kelembaban_pct"], bins=18)
plt.title("Distribusi Kelembaban")
plt.xlabel("Kelembaban (%)")
plt.ylabel("Frekuensi")
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(df["Suhu_C"], df["Kelembaban_pct"], alpha=.45)
plt.title("Hubungan Suhu dan Kelembaban")
plt.xlabel("Suhu (°C)")
plt.ylabel("Kelembaban (%)")
plt.tight_layout()
plt.show()
