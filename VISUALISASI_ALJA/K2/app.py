import streamlit as st
import pandas as pd
import plotly.express as px

NAMA_MAHASISWA = "Al Zahra Nur Febrian"
NIM_MAHASISWA = "241051006"

st.set_page_config(
    page_title="Bedah Kasus 2 - Profil Mahasiswa",
    page_icon="🎓",
    layout="wide"
)

@st.cache_data
def load_data():
    return pd.read_csv("data_sintesis_mahasiswa_1000.csv")

df = load_data()

st.title("🎓 Bedah Kasus 2 — Dashboard Profil Mahasiswa")

st.markdown(f"""
<div style="background:#eef6ff;padding:16px 20px;border-radius:12px;
border:1px solid #cfe3ff;margin-bottom:18px">
<b>👤 Nama:</b> {NAMA_MAHASISWA}
&nbsp;&nbsp;&nbsp;&nbsp;
<b>🆔 NIM:</b> {NIM_MAHASISWA}
</div>
""", unsafe_allow_html=True)

st.caption("Dataset 1.000 mahasiswa sintetis berdasarkan 2 data awal pada Bedah Kasus 2.")

st.sidebar.header("🔎 Filter Data")

jurusan_pilih = st.sidebar.multiselect(
    "Jurusan", sorted(df.Jurusan.unique()),
    default=sorted(df.Jurusan.unique())
)
semester_pilih = st.sidebar.multiselect(
    "Semester", sorted(df.Semester.unique()),
    default=sorted(df.Semester.unique())
)
ipk_range = st.sidebar.slider(
    "Rentang IPK", float(df.IPK.min()), float(df.IPK.max()),
    (float(df.IPK.min()), float(df.IPK.max())), step=.01
)
usia_range = st.sidebar.slider(
    "Rentang Usia", int(df.Usia.min()), int(df.Usia.max()),
    (int(df.Usia.min()), int(df.Usia.max()))
)

data = df[
    df.Jurusan.isin(jurusan_pilih)
    & df.Semester.isin(semester_pilih)
    & df.IPK.between(*ipk_range)
    & df.Usia.between(*usia_range)
].copy()

if data.empty:
    st.warning("Tidak ada data yang sesuai dengan filter.")
    st.stop()

c1,c2,c3,c4 = st.columns(4)
c1.metric("👥 Mahasiswa", f"{len(data):,}")
c2.metric("🎯 Rata-rata IPK", f"{data.IPK.mean():.2f}")
c3.metric("📚 Rata-rata Semester", f"{data.Semester.mean():.2f}")
c4.metric("🎂 Rata-rata Usia", f"{data.Usia.mean():.1f} tahun")

st.divider()

tab1,tab2,tab3,tab4 = st.tabs([
    "📊 Kategori","📈 Distribusi","🔬 Hubungan Variabel","📋 Data"
])

with tab1:
    a,b=st.columns(2)
    jdf=data.groupby("Jurusan").size().reset_index(name="Jumlah").sort_values("Jumlah",ascending=False)
    with a:
        fig=px.bar(jdf,x="Jurusan",y="Jumlah",text_auto=True,
                   title="1. Jumlah Mahasiswa per Jurusan (Nominal)")
        st.plotly_chart(fig,use_container_width=True)
    sdf=data.groupby("Semester").size().reset_index(name="Jumlah")
    with b:
        fig=px.bar(sdf,x="Semester",y="Jumlah",text_auto=True,
                   title="2. Distribusi Mahasiswa per Semester (Ordinal)")
        fig.update_xaxes(dtick=1)
        st.plotly_chart(fig,use_container_width=True)
    fig=px.pie(jdf,names="Jurusan",values="Jumlah",hole=.45,
               title="Proporsi Mahasiswa berdasarkan Jurusan")
    st.plotly_chart(fig,use_container_width=True)

with tab2:
    a,b=st.columns(2)
    with a:
        fig=px.histogram(data,x="IPK",nbins=18,
                         title="3. Distribusi IPK (Numerik Kontinu)")
        st.plotly_chart(fig,use_container_width=True)
    with b:
        fig=px.histogram(data,x="Usia",nbins=max(5,data.Usia.nunique()),
                         title="4. Distribusi Usia")
        st.plotly_chart(fig,use_container_width=True)
    st.subheader("Statistik Deskriptif")
    st.dataframe(data[["Semester","IPK","Usia"]].describe().T.round(2),
                 use_container_width=True)

with tab3:
    a,b=st.columns(2)
    with a:
        fig=px.scatter(data,x="Semester",y="IPK",color="Jurusan",
                       hover_data=["Usia"],
                       title="5. Hubungan Semester dan IPK")
        fig.update_xaxes(dtick=1)
        st.plotly_chart(fig,use_container_width=True)
    with b:
        fig=px.scatter(data,x="Usia",y="IPK",color="Jurusan",
                       hover_data=["Semester"],
                       title="6. Hubungan Usia dan IPK")
        st.plotly_chart(fig,use_container_width=True)

    corr=data[["Semester","IPK","Usia"]].corr()
    st.subheader("Matriks Korelasi")
    st.dataframe(corr.round(3),use_container_width=True)
    st.info(
        f"Korelasi Semester–IPK = {corr.loc['Semester','IPK']:.3f} | "
        f"Korelasi Semester–Usia = {corr.loc['Semester','Usia']:.3f}. "
        "Korelasi menunjukkan hubungan linear, bukan sebab-akibat."
    )

with tab4:
    st.subheader("📋 Data Mahasiswa")
    st.dataframe(data.sort_values(["Semester","Jurusan"]),
                 use_container_width=True,height=520)
    csv=data.to_csv(index=False).encode("utf-8-sig")
    st.download_button("⬇️ Download Data Hasil Filter",csv,
                       "data_mahasiswa_hasil_filter.csv","text/csv")

st.divider()
st.caption(f"Bedah Kasus 2 | {NAMA_MAHASISWA} | NIM {NIM_MAHASISWA}")
