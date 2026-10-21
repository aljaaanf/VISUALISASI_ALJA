import pandas as pd
import matplotlib.pyplot as plt

NAMA_MAHASISWA = "Al Zahra Nur Febrian"
NIM_MAHASISWA = "241051006"

df = pd.read_csv("data_sintesis_mahasiswa_1000.csv")

print("="*70)
print("BEDAH KASUS 2 - DATASET PROFIL MAHASISWA")
print("Nama:", NAMA_MAHASISWA)
print("NIM :", NIM_MAHASISWA)
print("="*70)

print("\n1. UKURAN DATA")
print(df.shape)
print("\n2. TIPE DATA")
print(df.dtypes)
print("\n3. MISSING VALUE")
print(df.isna().sum())
print("\n4. DUPLIKAT")
print(df.duplicated().sum())
print("\n5. STATISTIK DESKRIPTIF")
print(df[["Semester","IPK","Usia"]].describe().round(2))

jur = (df.groupby("Jurusan")
       .agg(Jumlah_Mahasiswa=("Jurusan","size"),
            Rata2_IPK=("IPK","mean"),
            Rata2_Usia=("Usia","mean"),
            Rata2_Semester=("Semester","mean"))
       .sort_values("Jumlah_Mahasiswa", ascending=False))
jur["Persentase_%"] = jur["Jumlah_Mahasiswa"]/len(df)*100

print("\n6. JURUSAN (NOMINAL)")
print(jur.round(2))

sem = (df.groupby("Semester")
       .agg(Jumlah_Mahasiswa=("Semester","size"),
            Rata2_IPK=("IPK","mean"),
            Rata2_Usia=("Usia","mean")))
print("\n7. SEMESTER (ORDINAL)")
print(sem.round(2))

print("\n8. IPK (NUMERIK KONTINU)")
print("Min:", df.IPK.min())
print("Max:", df.IPK.max())
print("Mean:", round(df.IPK.mean(),3))
print("Median:", round(df.IPK.median(),3))
print("Std:", round(df.IPK.std(),3))

print("\n9. USIA")
print("Min:", df.Usia.min())
print("Max:", df.Usia.max())
print("Mean:", round(df.Usia.mean(),2))
print("Median:", df.Usia.median())

corr = df[["Semester","IPK","Usia"]].corr()
print("\n10. KORELASI")
print(corr.round(3))

print("\n11. INSIGHT")
print("Jurusan terbanyak:", jur.index[0])
print("Jurusan dengan IPK rata-rata tertinggi:", jur.Rata2_IPK.idxmax())
print("Semester terbanyak:", sem.Jumlah_Mahasiswa.idxmax())
print("Rata-rata IPK:", round(df.IPK.mean(),2))
print("Rata-rata usia:", round(df.Usia.mean(),2))
print("Korelasi Semester-IPK:", round(corr.loc["Semester","IPK"],3))
print("Korelasi Semester-Usia:", round(corr.loc["Semester","Usia"],3))

plt.figure(figsize=(10,6))
jur["Jumlah_Mahasiswa"].sort_values().plot(kind="barh")
plt.title("Jumlah Mahasiswa per Jurusan")
plt.xlabel("Jumlah Mahasiswa")
plt.tight_layout()
plt.show()

plt.figure(figsize=(10,6))
plt.hist(df["IPK"], bins=18)
plt.title("Distribusi IPK")
plt.xlabel("IPK")
plt.ylabel("Frekuensi")
plt.tight_layout()
plt.show()

plt.figure(figsize=(10,6))
plt.scatter(df["Semester"], df["IPK"], alpha=.45)
plt.title("Hubungan Semester dan IPK")
plt.xlabel("Semester")
plt.ylabel("IPK")
plt.xticks(range(1,9))
plt.tight_layout()
plt.show()

plt.figure(figsize=(10,6))
plt.scatter(df["Usia"], df["IPK"], alpha=.45)
plt.title("Hubungan Usia dan IPK")
plt.xlabel("Usia")
plt.ylabel("IPK")
plt.tight_layout()
plt.show()
