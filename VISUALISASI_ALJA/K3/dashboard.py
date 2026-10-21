import streamlit as st
import pandas as pd
import plotly.express as px

NAMA_MAHASISWA = "Al Zahra Nur Febrian"
NIM_MAHASISWA = "241051006"

st.set_page_config(
    page_title="Bedah Kasus 3 - Pengamatan Cuaca",
    page_icon="🌦️",
    layout="wide"
)

@st.cache_data
def load_data():
    return pd.read_csv("data_sintesis_cuaca_1000.csv")

df = load_data()

st.title("🌦️ Bedah Kasus 3 — Dashboard Pengamatan Cuaca")

st.markdown(f"""
<div style="background:#eef6ff;padding:16px 20px;border-radius:12px;
border:1px solid #cfe3ff;margin-bottom:18px">
<b>👤 Nama:</b> {NAMA_MAHASISWA}
&nbsp;&nbsp;&nbsp;&nbsp;
<b>🆔 NIM:</b> {NIM_MAHASISWA}
</div>
""", unsafe_allow_html=True)

st.caption(
    "Dataset 1.000 pengamatan cuaca sintetis berdasarkan 2 data awal pada Bedah Kasus 3."
)

st.sidebar.header("🔎 Filter Data")

kota_pilih = st.sidebar.multiselect(
    "Kota",
    sorted(df["Kota"].unique()),
    default=sorted(df["Kota"].unique())
)

kondisi_pilih = st.sidebar.multiselect(
    "Kondisi",
    sorted(df["Kondisi"].unique()),
    default=sorted(df["Kondisi"].unique())
)

suhu_range = st.sidebar.slider(
    "Rentang Suhu (°C)",
    float(df["Suhu_C"].min()),
    float(df["Suhu_C"].max()),
    (float(df["Suhu_C"].min()), float(df["Suhu_C"].max())),
    step=.1
)

hum_range = st.sidebar.slider(
    "Rentang Kelembaban (%)",
    float(df["Kelembaban_pct"].min()),
    float(df["Kelembaban_pct"].max()),
    (float(df["Kelembaban_pct"].min()), float(df["Kelembaban_pct"].max())),
    step=.1
)

data = df[
    df["Kota"].isin(kota_pilih)
    & df["Kondisi"].isin(kondisi_pilih)
    & df["Suhu_C"].between(*suhu_range)
    & df["Kelembaban_pct"].between(*hum_range)
].copy()

if data.empty:
    st.warning("Tidak ada data yang sesuai dengan filter.")
    st.stop()

c1, c2, c3, c4 = st.columns(4)
c1.metric("📍 Pengamatan", f"{len(data):,}")
c2.metric("🌡️ Rata-rata Suhu", f"{data['Suhu_C'].mean():.1f} °C")
c3.metric("💧 Rata-rata Kelembaban", f"{data['Kelembaban_pct'].mean():.1f} %")
c4.metric("☁️ Kondisi Dominan", data["Kondisi"].mode().iloc[0])

st.divider()

tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Kategori",
    "📈 Distribusi",
    "🔬 Hubungan Variabel",
    "📋 Data"
])

with tab1:
    a, b = st.columns(2)

    kota_df = (
        data.groupby("Kota")
        .size()
        .reset_index(name="Jumlah")
        .sort_values("Jumlah", ascending=False)
    )

    with a:
        fig = px.bar(
            kota_df, x="Kota", y="Jumlah", text_auto=True,
            title="1. Jumlah Pengamatan per Kota (Nominal)"
        )
        st.plotly_chart(fig, use_container_width=True)

    kondisi_df = (
        data.groupby("Kondisi")
        .size()
        .reset_index(name="Jumlah")
        .sort_values("Jumlah", ascending=False)
    )

    with b:
        fig = px.bar(
            kondisi_df, x="Kondisi", y="Jumlah", text_auto=True,
            title="2. Distribusi Kondisi Cuaca (Nominal)"
        )
        st.plotly_chart(fig, use_container_width=True)

    fig = px.pie(
        kota_df, names="Kota", values="Jumlah", hole=.45,
        title="Proporsi Pengamatan berdasarkan Kota"
    )
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    a, b = st.columns(2)

    with a:
        fig = px.histogram(
            data, x="Suhu_C", nbins=18,
            title="3. Distribusi Suhu — Numerik Interval",
            labels={"Suhu_C": "Suhu (°C)"}
        )
        st.plotly_chart(fig, use_container_width=True)

    with b:
        fig = px.histogram(
            data, x="Kelembaban_pct", nbins=18,
            title="4. Distribusi Kelembaban — Numerik Rasio",
            labels={"Kelembaban_pct": "Kelembaban (%)"}
        )
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("Statistik Deskriptif")
    st.dataframe(
        data[["Suhu_C", "Kelembaban_pct"]].describe().T.round(2),
        use_container_width=True
    )

with tab3:
    a, b = st.columns(2)

    with a:
        fig = px.scatter(
            data,
            x="Suhu_C",
            y="Kelembaban_pct",
            color="Kondisi",
            hover_data=["Kota"],
            title="5. Hubungan Suhu dan Kelembaban",
            labels={
                "Suhu_C": "Suhu (°C)",
                "Kelembaban_pct": "Kelembaban (%)"
            }
        )
        st.plotly_chart(fig, use_container_width=True)

    with b:
        kota_rata = (
            data.groupby("Kota", as_index=False)
            .agg(
                Rata2_Suhu=("Suhu_C", "mean"),
                Rata2_Kelembaban=("Kelembaban_pct", "mean")
            )
        )
        fig = px.scatter(
            kota_rata,
            x="Rata2_Suhu",
            y="Rata2_Kelembaban",
            text="Kota",
            title="6. Rata-rata Suhu vs Kelembaban per Kota"
        )
        fig.update_traces(textposition="top center")
        st.plotly_chart(fig, use_container_width=True)

    corr = data[["Suhu_C", "Kelembaban_pct"]].corr()

    st.subheader("Matriks Korelasi")
    st.dataframe(corr.round(3), use_container_width=True)

    r = corr.loc["Suhu_C", "Kelembaban_pct"]
    st.info(
        f"Korelasi Suhu–Kelembaban = **{r:.3f}**. "
        "Nilai korelasi menunjukkan arah dan kekuatan hubungan linear, "
        "bukan hubungan sebab-akibat."
    )

with tab4:
    st.subheader("📋 Data Pengamatan Cuaca")
    st.dataframe(
        data.sort_values(["Kota", "Kondisi"]),
        use_container_width=True,
        height=520
    )

    csv = data.to_csv(index=False).encode("utf-8-sig")
    st.download_button(
        "⬇️ Download Data Hasil Filter",
        csv,
        "data_cuaca_hasil_filter.csv",
        "text/csv"
    )

st.divider()
st.caption(
    f"Bedah Kasus 3 | {NAMA_MAHASISWA} | NIM {NIM_MAHASISWA}"
)
