
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data_sintesis_1000.csv", parse_dates=["Tanggal"])
df["Omzet"] = df["Harga"] * df["Jumlah_Terjual"]

print("\n=== PROFIL DATA ===")
print(df.info())
print("\n=== DESKRIPSI NUMERIK ===")
print(df[["Harga", "Jumlah_Terjual", "Omzet"]].describe())

print("\n=== MISSING VALUE ===")
print(df.isna().sum())

print("\n=== KATEGORI ===")
category_summary = (
    df.groupby("Kategori")
      .agg(
          Transaksi=("Produk", "size"),
          Unit_Terjual=("Jumlah_Terjual", "sum"),
          Omzet=("Omzet", "sum"),
          Harga_Rata2=("Harga", "mean"),
      )
      .sort_values("Omzet", ascending=False)
)
print(category_summary)

print("\n=== TOP 10 PRODUK ===")
product_summary = (
    df.groupby(["Produk", "Kategori"])
      .agg(
          Transaksi=("Produk", "size"),
          Unit_Terjual=("Jumlah_Terjual", "sum"),
          Omzet=("Omzet", "sum"),
      )
      .sort_values("Omzet", ascending=False)
)
print(product_summary.head(10))

print("\n=== BULANAN ===")
monthly = (
    df.set_index("Tanggal")
      .resample("MS")
      .agg(Transaksi=("Produk", "size"),
           Unit_Terjual=("Jumlah_Terjual", "sum"),
           Omzet=("Omzet", "sum"))
)
print(monthly)

print("\n=== KORELASI ===")
print("Korelasi Harga vs Jumlah Terjual:",
      df["Harga"].corr(df["Jumlah_Terjual"]))

plt.figure(figsize=(10, 5))
category_summary["Omzet"].plot(kind="bar")
plt.title("Omzet per Kategori")
plt.ylabel("Omzet (Rp)")
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))
monthly["Omzet"].plot(marker="o")
plt.title("Tren Omzet Bulanan")
plt.ylabel("Omzet (Rp)")
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))
plt.hist(df["Harga"], bins=30)
plt.title("Distribusi Harga")
plt.xlabel("Harga (Rp)")
plt.ylabel("Frekuensi")
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))
plt.scatter(df["Harga"], df["Jumlah_Terjual"], alpha=0.4)
plt.title("Harga vs Jumlah Terjual")
plt.xlabel("Harga (Rp)")
plt.ylabel("Jumlah Terjual")
plt.tight_layout()
plt.show()
