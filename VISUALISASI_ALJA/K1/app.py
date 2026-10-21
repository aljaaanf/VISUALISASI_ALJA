
# =========================================================
# IDENTITAS MAHASISWA
# =========================================================
NAMA_MAHASISWA = "Al Zahra Nur Febrian"
NIM_MAHASISWA = "241051006"


import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(
    page_title="Bedah Kasus 1 — Dashboard Penjualan",
    page_icon="📊",
    layout="wide"
)

@st.cache_data
def load_data():
    df = pd.read_csv("data_sintesis_1000.csv", parse_dates=["Tanggal"])
    df["Omzet"] = df["Harga"] * df["Jumlah_Terjual"]
    return df

df = load_data()

# -----------------------------
# Header
# -----------------------------
st.title("📊 Bedah Kasus 1 — Dashboard Operasional Penjualan")

st.markdown(
    f"""
    <div style="
        background: linear-gradient(90deg, #eef6ff, #f7fbff);
        padding: 14px 18px;
        border-radius: 10px;
        border: 1px solid #cfe3ff;
        margin: 8px 0 16px 0;
    ">
        <b>👤 Nama:</b> {NAMA_MAHASISWA}
        &nbsp;&nbsp;&nbsp;&nbsp;
        <b>🆔 NIM:</b> {NIM_MAHASISWA}
    </div>
    """,
    unsafe_allow_html=True
)

st.caption(
    "Dataset sintesis 1.000 baris berdasarkan 2 data awal. "
    "Gunakan filter untuk eksplorasi kategori, produk, waktu, harga, dan volume."
)

# -----------------------------
# Sidebar filters
# -----------------------------
st.sidebar.header("🔎 Filter")

categories = sorted(df["Kategori"].unique())
selected_categories = st.sidebar.multiselect(
    "Kategori",
    categories,
    default=categories
)

filtered0 = df[df["Kategori"].isin(selected_categories)]

products = sorted(filtered0["Produk"].unique())
selected_products = st.sidebar.multiselect(
    "Produk",
    products,
    default=products
)

min_date = df["Tanggal"].min().date()
max_date = df["Tanggal"].max().date()
selected_dates = st.sidebar.date_input(
    "Rentang tanggal",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

if len(selected_dates) == 2:
    start_date, end_date = pd.to_datetime(selected_dates[0]), pd.to_datetime(selected_dates[1])
else:
    start_date = pd.to_datetime(min_date)
    end_date = pd.to_datetime(max_date)

min_price = int(df["Harga"].min())
max_price = int(df["Harga"].max())
price_range = st.sidebar.slider(
    "Rentang harga (Rp)",
    min_value=min_price,
    max_value=max_price,
    value=(min_price, max_price),
    step=10000
)

mask = (
    df["Kategori"].isin(selected_categories)
    & df["Produk"].isin(selected_products)
    & df["Tanggal"].between(start_date, end_date)
    & df["Harga"].between(price_range[0], price_range[1])
)
data = df.loc[mask].copy()

# -----------------------------
# KPI
# -----------------------------
total_omzet = data["Omzet"].sum()
total_unit = data["Jumlah_Terjual"].sum()
total_transaksi = len(data)
produk_unik = data["Produk"].nunique()

c1, c2, c3, c4 = st.columns(4)
c1.metric("💰 Total Omzet", f"Rp{total_omzet:,.0f}")
c2.metric("📦 Unit Terjual", f"{total_unit:,.0f}")
c3.metric("🧾 Transaksi", f"{total_transaksi:,.0f}")
c4.metric("🏷️ Produk Unik", f"{produk_unik:,.0f}")

st.divider()

if data.empty:
    st.warning("Tidak ada data yang cocok dengan filter.")
    st.stop()

# -----------------------------
# Tabs
# -----------------------------
tab1, tab2, tab3, tab4 = st.tabs([
    "📈 Tren & Kategori",
    "🔬 Analisis Numerik",
    "🏆 Ranking",
    "📋 Data"
])

with tab1:
    left, right = st.columns(2)

    category = (
        data.groupby("Kategori", as_index=False)
            .agg(Omzet=("Omzet", "sum"), Unit=("Jumlah_Terjual", "sum"))
            .sort_values("Omzet", ascending=False)
    )
    with left:
        fig = px.bar(
            category,
            x="Kategori",
            y="Omzet",
            title="Omzet per Kategori",
            labels={"Omzet": "Omzet (Rp)", "Kategori": "Kategori"},
            text_auto=".2s"
        )
        st.plotly_chart(fig, use_container_width=True)

    monthly = (
        data.set_index("Tanggal")
            .resample("MS")
            .agg(Omzet=("Omzet", "sum"), Unit=("Jumlah_Terjual", "sum"))
            .reset_index()
    )
    with right:
        fig = px.line(
            monthly,
            x="Tanggal",
            y="Omzet",
            markers=True,
            title="Tren Omzet Bulanan",
            labels={"Omzet": "Omzet (Rp)", "Tanggal": "Bulan"}
        )
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("Komposisi Omzet")
    pie = px.pie(
        category,
        names="Kategori",
        values="Omzet",
        hole=0.45,
        title="Share Omzet per Kategori"
    )
    st.plotly_chart(pie, use_container_width=True)

with tab2:
    left, right = st.columns(2)

    with left:
        fig = px.histogram(
            data,
            x="Harga",
            nbins=30,
            title="Distribusi Harga",
            labels={"Harga": "Harga (Rp)"}
        )
        st.plotly_chart(fig, use_container_width=True)

    with right:
        fig = px.scatter(
            data,
            x="Harga",
            y="Jumlah_Terjual",
            color="Kategori",
            hover_data=["Produk", "Tanggal", "Omzet"],
            title="Harga vs Jumlah Terjual",
            labels={
                "Harga": "Harga (Rp)",
                "Jumlah_Terjual": "Jumlah Terjual"
            }
        )
        st.plotly_chart(fig, use_container_width=True)

    corr = data["Harga"].corr(data["Jumlah_Terjual"])
    st.info(
        f"**Korelasi harga vs jumlah terjual: {corr:.3f}.** "
        "Korelasi tidak membuktikan sebab-akibat; hasil ini berlaku untuk dataset sintesis yang digunakan."
    )

    stats = data[["Harga", "Jumlah_Terjual", "Omzet"]].describe().T
    st.subheader("Statistik Deskriptif")
    st.dataframe(stats, use_container_width=True)

with tab3:
    product = (
        data.groupby(["Produk", "Kategori"], as_index=False)
            .agg(
                Transaksi=("Produk", "size"),
                Unit_Terjual=("Jumlah_Terjual", "sum"),
                Omzet=("Omzet", "sum"),
                Harga_Rata2=("Harga", "mean")
            )
            .sort_values("Omzet", ascending=False)
    )

    st.subheader("Top 10 Produk Berdasarkan Omzet")
    st.dataframe(product.head(10), use_container_width=True)

    fig = px.bar(
        product.head(10).sort_values("Omzet"),
        x="Omzet",
        y="Produk",
        orientation="h",
        color="Kategori",
        title="Top 10 Produk — Omzet"
    )
    st.plotly_chart(fig, use_container_width=True)

with tab4:
    st.subheader("Data hasil filter")
    st.dataframe(
        data.sort_values("Tanggal", ascending=False),
        use_container_width=True,
        height=520
    )

    csv = data.to_csv(index=False).encode("utf-8-sig")
    st.download_button(
        "⬇️ Download data hasil filter (CSV)",
        data=csv,
        file_name="data_hasil_filter.csv",
        mime="text/csv"
    )

st.divider()
st.caption(
    "Catatan: 2 baris pertama berasal dari data kasus; 998 baris berikutnya adalah data sintetis "
    "untuk kebutuhan latihan analisis dan visualisasi."
)
