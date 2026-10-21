import pandas as pd
import numpy as np

rng = np.random.default_rng(241051006)
asli = pd.DataFrame({
    "Jurusan":["Sistem Informasi","Manajemen"],
    "Semester":[3,1],"IPK":[3.85,3.50],"Usia":[20,19]
})
info = {
    "Sistem Informasi":(.30,3.42),"Manajemen":(.24,3.28),
    "Akuntansi":(.18,3.34),"Teknik Informatika":(.16,3.38),
    "Ilmu Komunikasi":(.12,3.22)
}
js=list(info); ps=[info[x][0] for x in js]
rows=[]
for _ in range(998):
    j=rng.choice(js,p=ps)
    s=int(rng.choice(np.arange(1,9),p=np.array([.18,.17,.16,.14,.13,.10,.07,.05])))
    u=int(np.clip(round(rng.normal(18.4+.72*s,.75)),17,26))
    ipk=round(float(np.clip(rng.normal(info[j][1]+.035*min(s,6),.32),2.2,4.0)),2)
    rows.append({"Jurusan":j,"Semester":s,"IPK":ipk,"Usia":u})
df=pd.concat([asli,pd.DataFrame(rows)],ignore_index=True)
df.to_csv("data_sintesis_mahasiswa_1000.csv",index=False,encoding="utf-8-sig")
print("Berhasil membuat",len(df),"data.")
