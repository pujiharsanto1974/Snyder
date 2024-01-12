import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Menambahkan style menggunakan st.markdown dengan HTML langsung
st.markdown("""
    <style>
        h1 {
            font-family: 'Arial Narrow', Arial Narrow;
            font-size: 25px; 
            color: red;
            }
        h2 {
            font-family: 'Arial Narrow', Arial Narrow;
            font-size: 20px;
            color: red;
            }
    </style>
""", unsafe_allow_html=True)

st.header("SNYDER METHOD")
#st.write("<p style='font-family:Arial Narrow; font-size: 14pt;'> \
  #       Hitungan ditulis dengan coding bahasa Python dan Streamlit. Keduanya open\
   #      source dan bisa digunakan oleh semua orang. Belajar penulisan coding dibantu dengan chatgpt :D.\
   #      </p>", unsafe_allow_html=True)

st.header("""
        TUGAS HIDROGRAF SATUAN DENGAN METODE SNYDER:
        - MAHASISWA MEMBUAT KEMBALI HITUNGAN DI BAWAH SAMPAI DENGAN GRAFIK DENGAN EXCEL BUKAN WORD;
        - DATA MENGGUNAKAN DATA MASING-MASING MAHASISWA;
        - DATA DALAM HITUNGAN DI BAWAH HANYA CONTOH;
        - BAGAIAN YANG DIKUMPULKAN ADALAH EXCEL YANG MEMUAT: HITUNGAN STEP BY STEP, SEMUA TABEL DAN GRAFIK HIDROGRAF SATUAN;
        - SILAHAKN BERKREASI DALAM MEMBUAT TAMPILAN DAN SELAMAT BELAJAR DENGAN MENGERJAKAN TUGAS INI.
          """)
          
st.header("Tipikal hidrograf satuan Snyder")
st.write("<p style='font-family:Arial Narrow; font-size: 14pt;'> \
         Gambar di bawah ini adalah tipikal hidrograf satuan dengan metode Snyder. \
         Konsep utama metode ini adalah mencari koordinat dari titik A, B, C, D, E, F dan G. \
         Koordinatnya adalah: A (0,0), B (t1,0.5Qp), C (t2,0.75Qp), D (tpp,Qp), E (t3,0.75Qp), F (t4,0.5Qp), G (tb,0). \
         </p>", unsafe_allow_html=True)

def main():
    # Specify the path to the image file
    image_path = "snyder.png"
    # Display a smaller version of the image
    st.image(image_path, caption="Tipikal hidrograf satuan sintetis Snyder", width=500)
if __name__ == "__main__":
    main()

#UNGGAH GAMBAR
st.header("Contoh, Daerah Aliran Sungai dengan data sebagai berikut:")
def main():
    # Specify the path to the image file
    image_path = "DAS.jpg"
    # Display a smaller version of the image
    st.image(image_path, width=800)
if __name__ == "__main__":
    main()

st.write("<p style='font-family:Arial Narrow; font-size: 14pt;'> \
         Panjang sungai utama, L dalam km:\
         </p>", unsafe_allow_html=True)
L=st.number_input('', value=14.6248)

def main():
    # Specify the path to the image file
    image_path = "SungaiUtama.jpg"
    # Display a smaller version of the image
    st.image(image_path, width=800)
if __name__ == "__main__":
    main()
st.write("<p style='font-family:Arial Narrow; font-size: 14pt;'> \
         Panjang sungai dari titik terdekat dengan titik berat DAS, Lc dalam km::\
         </p>", unsafe_allow_html=True)
Lc=st.number_input('', value=8.733)
def main():
    
    # Specify the path to the image file
    image_path = "LC.jpg"

    # Display a smaller version of the image
    st.image(image_path, width=800)

if __name__ == "__main__":
    main()

Ct=st.number_input('Koefisien Ct besarnya antara (0.3 - 6):', value=0.8)
A=st.number_input('Luas DAS, dalam km^2:', value=30.33)
Cp=st.number_input('Koefisien Cp besarnya antara (0.9 - 1.4):', value=1.0)
trp=st.number_input('Durasi hujan di DAS, trp:', value=3.0)




st.header("Step 1: menghitung waktu konsentrasi, tp")

st.latex(r'tp = Ct (L \cdot Lc)^{0.3} \quad \quad [pers.1]')

def main():
       st.write("""
   - **tp**: waktu konsentrasi adalah waktu yang dibutuhkan air mengalir dari titik terjauh\
                dari anak sungai sampai di outlet. Atau dengan kata lain semua anak sungai sudah\
                berkontribusi di outlet, karena titik terjauh sudah sampai outlet.\
                Hal ini memahamkan bahwa debit yang terjadi di outlet sudah maksismum.
    """)
if __name__ == '__main__':
    main()

def main():
       st.write("""
   - **L**: Panjang dasar diukur sepanjang aliran air dari bagian pemisah daerah aliran hingga stasiun pengukuran di kilometer.
    - **Lca**: Jarak sepanjang aliran utama dari stasiun pengukuran ke suatu titik \
    berlawanan dengan pusat massa daerah aliran sungai di kilometer.
    - **Ct**: Konstanta regional yang mewakili kemiringan dan penyimpanan daerah aliran. \
    Nilai Ct dalam studi Snyder berkisar dari 1,35 hingga 1,65. \
    Namun, penelitian oleh banyak peneliti menunjukkan bahwa Ct bergantung pada daerah yang \
    diteliti dan variasi luas dengan nilai Ct berkisar dari 0,3 hingga 6,0 telah dilaporkan.
    """)
   
   
    


if __name__ == '__main__':
    main()

st.markdown("[Jurnal referensi nilai konsanta Ct dan Cp #1](https://drive.google.com/file/d/1PN9ZaCE0PfVVvUrZz91DPTS1ca1me1jQ/view?usp=sharing)")
st.write("Snyder, F. F. (1938). Synthetic unit‐graphs. Eos, Transactions American Geophysical Union, 19(1), 447-454.")


st.markdown("[Jurnal referensi nilai konsanta Ct dan Cp #2](https://drive.google.com/file/d/1KIctTHwDQdtFvIA0HSryXZ3xTF2_td34/view?usp=sharing)")
st.write("Thapa, G., & Wijesekera, N. T. S. (2017). Computation and optimization of Snyder’s synthetic unit hydrograph parameters.")

st.markdown("[Jurnal referensi nilai konsanta Ct dan Cp #3](https://drive.google.com/file/d/11ZCkQmt3ypfeQgwVwGio3S3Ry7CyeZ_J/view?usp=sharing)")
st.write("Natakusumah, D. K., Hatmoko, W., & Harlan, D. (2011). Prosedur umum perhitungan hidrograf satuan sintetis dengan Cara ITB dan Beberapa Contoh Penerapannya. Jurnal Teknik Sipil, 18(3), 251-291.")


tp=Ct*(L*Lc)**0.3
st.write("Nilai waktu konsentrasi, tp (jam) adalah:")
st.write(f"{tp:.3f} jam")
st.write("Silahkan coba cek hitungan tp dengan Persamaan 1, hitung dengan bantuan excel")



st.header("Step 2: menghitung lama durasi hujan")
st.latex(r'tr = \frac {tp} {5.5} \quad \quad [pers.2]')
tr=tp/5.5

def main():
       st.write("""
   - **tr**: adalah durasi hujan standar menurut Snyder. Jika durasi hujan di DAS yang dianalisa tidak sama\
                dengan durasi hujan standar Snyder, maka nilai tp di sesuaikan dengan persamaan berikut:
    """)
if __name__ == '__main__':
    main()

st.header("Step 3: menghitung waktu konsentrasi penyesuaian, tpp")

st.latex(r'tpp = tp + \frac {trp-tr} {4} \quad \quad [pers.3]')
tpp=tp+(trp-tr)/4

def main():
       st.write("""
   - **tpp**: adalah waktu konsentrasi penyesuaian.
   - **trp**: adalah durasi hujan sesuai rencana, atau durasi hujan di DAS yang dianalisa. Dalam contoh ini 3 jam
    """)
if __name__ == '__main__':
    main()

st.write("Nilai waktu konsentrasi penyesuaian, tpp (jam):")
st.write(f"{tpp:.3f} jam")

st.header("Step 4: menghitung debit puncak, Qp")
st.latex(r'Qp = \frac {2.78 \cdot Cp \cdot A} {tpp} \quad \quad [pers.4]')


Qp = (2.78*Cp*A)/ tpp
st.write("Nilai debit puncak snyder, Qp (m3/detik) adalah:")
st.write(f"{Qp:.3f} m3/detik")

st.header("Step 5: menghitung waktu dasar hidrograf satuan")
st.latex(r'tb = 3 + \frac {tpp} {8} \quad \quad [pers.5]')

tb=(3+tpp/8)

st.write("Nilai waktu dasar hidrograf satuan, tb (hari) adalah:")
st.write(f"{tb:.3f} hari")
st.write("atau")
tb24=tb*24
st.write("Nilai waktu dasar hidrograf satuan, tb (jam) adalah:")
st.write(f"{tb24:.3f} jam")

st.header("Step 6: menghitung W50")
st.latex(r'W50 = 5.87 [\frac {Qp} {A}]^{-1.075} \quad \quad [pers.6]')

W50=5.87*(Qp/A)**(-1.075)
st.write("Nilai W50 (jam) adalah:")
st.write(f"{W50:.3f} jam")


st.header("Step 7: menghitung W75")
st.latex(r'W75 = \frac {5.85} {1.75} [\frac {Qp} {A}]^{-1.075} \quad \quad [pers.7]')

W75=((5.87)/(1.75))*(Qp/A)**(-1.075)
st.write("Nilai W75 (jam) adalah:")
st.write(f"{W75:.3f} jam")


st.header("Step 8a: Tabel rekap koordinat, #1")
# Sample data with variable values
data = {'Titik': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
        'T (jam)': [0, "t1", "t2", "tpp", "t4", "t5", "tb24"],
        'Debit (m/detik)': [0, "0.5QP", "0.75QP", "Qp", "0.75Qp", "0.50Qp", 0],
        }

# Create a DataFrame
df = pd.DataFrame(data)
# Display the table using Streamlit
st.table(df)

st.header("Step 8b: Tabel rekap koordinat, #2")
st.write("<p style='font-family:Arial Narrow; font-size: 14pt;'> \
         Lihat dan pahami gambar tipikal hidrograf Snyder di atas \
         </p>", unsafe_allow_html=True)
st.write(f"0.75Qp = 0.75 x {Qp:.3f}")
st.write(f"0.75Qp = {0.75*Qp:.3f}")
st.write(f"0.50Qp = 0.50 x {Qp:.3f}")
st.write(f"0.50Qp = {0.50*Qp:.3f}")
# Sample data with variable values
data = {'Titik': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
        'T (jam)': [0, "t1", "t2", f"{tpp:.3f}", "t4", "t5", f"{tb24:.3f}"],
        'Debit (m/detik)': [0, f"{0.5*Qp:0.3f}", f"{0.75*Qp:0.3f}", f"{Qp:.3f}", f"{0.75*Qp:0.3f}", f"{0.5*Qp:0.3f}", 0],
        }

# Create a DataFrame
df = pd.DataFrame(data)

# Display the table using Streamlit
st.table(df)

st.header("Step 8c: Tabel rekap koordinat, #3")
st.write("<p style='font-family:Arial Narrow; font-size: 14pt;'> \
         Lihat dan pahami gambar tipikal hidrograf Snyder di atas \
         </p>", unsafe_allow_html=True)
st.write(f"t1 = tpp - 1/3 * W50")
st.write(f"t1 = {tpp:.3f} - 1/3 * {W50:.3f} ")
st.write(f"t1 = {tpp-W50/3:.3f}")
st.write("")

st.write(f"t2 = tpp - 1/3 * W75")
st.write(f"t2 = {tpp:.3f} - 1/3 * {W75:.3f} ")
st.write(f"t2 = {tpp-W75/3:.3f}")
st.write("")

st.write(f"t3 = tpp + 2/3 * W75")
st.write(f"t3 = {tpp:.3f} + 2/3 * {W75:.3f} ")
st.write(f"t3 = {tpp+W75*2/3:.3f}")
st.write("")

st.write(f"t4 = tpp + 2/3 * W50")
st.write(f"t4 = {tpp:.3f} + 2/3 * {W50:.3f} ")
st.write(f"t4 = {tpp+W50*2/3:.3f}")
st.write("")
# Sample data with variable values
data = {'Titik': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
        'T (jam)': [0, f"{tpp-W50/3:.3f}", f"{tpp-W75/3:.3f}", f"{tpp:.3f}", f"{tpp+W75*2/3:.3f}", f"{tpp+W50*2/3:.3f}", f"{tb24:.3f}"],
        'Debit (m/detik)': [0, f"{0.5*Qp:0.3f}", f"{0.75*Qp:0.3f}", f"{Qp:.3f}", f"{0.75*Qp:0.3f}", f"{0.5*Qp:0.3f}", 0],
        }

# Create a DataFrame
df = pd.DataFrame(data)

# Display the table using Streamlit
st.table(df)


import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


data_x = [0, tpp - W50/3, tpp - W75/3, tpp, tpp + W75*2/3, tpp + W50*2/3, tb24]
data_y = [0, 0.5*Qp, 0.75*Qp, Qp, 0.75*Qp, 0.5*Qp, 0]

# Streamlit app
st.header("Step 9: Membuat grafik hidrograf satuan Snyder")
st.header('Grafik Hidrograf Satuan Sintetis Metode Snyder')

# Plotting dengan Matplotlib
fig, ax = plt.subplots()
ax.plot(data_x, data_y, linestyle='--', color='red', label='Connecting Line')
ax.scatter(data_x, data_y, marker='o', color='red', label='Data Points')

# Menambahkan label dan judul
ax.set_xlabel('Waktu (jam)')
ax.set_ylabel('Debit (m3/s)')
ax.set_title('Hidrograf satuan sintetis metode Snyder')
ax.legend()

# Menampilkan grafik di Streamlit
st.pyplot(fig)


st.header("Step 10: Membuat tabel untuk setiap waktu t dari 0 dengan interval 1 jam")
st.write("<p style='font-family:Arial Narrow; font-size: 14pt;'> \
         Hal ini dilakukan karena hidrograf satuan sintetis nantinya akan dikalikan dengan hujan jam-jaman dengan interval 1 jam. \
         Jadi agar interval hidrgraf satuan sama dengan interval hujan, yaitu 1 jam. \
         Perhatikan nilai t untuk tiap waktu di hidrogarf satuan tidak bulat (1,2,3, dst). \
         Sehingga untuk mendapatkan nilai Q untuk tiap waktu t = 1, 2, 3, dst dengan cara interpolasi. \
         </p>", unsafe_allow_html=True)
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def linear_interpolation(x, x1, y1, x2, y2):
    """Interpolasi linier."""
    return y1 + (y2 - y1) * ((x - x1) / (x2 - x1))

def interpolate_values(data, x_values):
    """Interpolasi nilai y untuk setiap nilai x integer."""
    interpolated_values = []
    x_data = data['x']
    y_data = data['y']

    for x_int in x_values:
        # Temukan dua titik data terdekat
        idx_before = np.searchsorted(x_data, x_int, side="right") - 1
        idx_after = idx_before + 1

        # Lakukan interpolasi linier
        x1, y1 = x_data.iloc[idx_before], y_data.iloc[idx_before]
        x2, y2 = x_data.iloc[idx_after], y_data.iloc[idx_after]

        interpolated_y = linear_interpolation(x_int, x1, y1, x2, y2)
        interpolated_values.append(interpolated_y)

    return interpolated_values

def main():
    st.header("Interpolasi Nilai debit, q untuk Setiap Nilai waktu, t Integer.")

    # Data yang diberikan
    data = {
        'x': [0, tpp - W50/3, tpp - W75/3, tpp, tpp + W75*2/3, tpp + W50*2/3, tb24],
        'y': [0, 0.5*Qp, 0.75*Qp, Qp, 0.75*Qp, 0.5*Qp, 0]
    }


    df = pd.DataFrame(data)

    # Menampilkan tabel data
    st.write("Data hasil pasangan t dan q dari snyder:")
    st.write(df)

    # Mendapatkan rentang nilai x integer dari pengguna
    start_x = st.slider("Pilih nilai x awal:", min_value=int(df['x'].min()), max_value=int(df['x'].max()), value=int(df['x'].min()))
    end_x = st.slider("Pilih nilai x akhir:", min_value=int(df['x'].min()), max_value=int(df['x'].max()), value=int(df['x'].max()))

    # Membuat rentang nilai x integer
    x_range = range(start_x, end_x + 1)

    # Melakukan interpolasi nilai y untuk setiap nilai x integer
    interpolated_values = interpolate_values(df, x_range)

    # Menampilkan hasil interpolasi
    st.header("Interpolasi nilai q untuk setiap nilai waktu Integer:")
    st.write("<p style='font-family:Arial Narrow; font-size: 14pt;'> \
         Letakkan kursor di tabel dan scroll untuk melihat tabel secara keseluruhan. \
         </p>", unsafe_allow_html=True)
    result_df = pd.DataFrame({'x': x_range, 'Interpolated Y': interpolated_values})
    st.write(result_df)

    # Membuat grafik dengan Matplotlib
    fig, ax = plt.subplots()
    #ax.scatter(df['x'], df['y'], label='Data Asli', marker='o')
    ax.set_facecolor('#ADD8E6')
    ax.plot(result_df['x'], result_df['Interpolated Y'], label='HSS Snyder', linestyle='--', marker='o', linewidth=0.5, color='red', markersize=2, markerfacecolor='black', markeredgecolor='black')
    ax.set_xlabel('Waktu (jam)', fontname='Arial Narrow', fontsize=11)
    ax.set_ylabel('Debit (m3/detik)', fontname='Arial Narrow', fontsize=11)
    ax.legend()
    fig.set_facecolor('pink')
    
    # Menampilkan grafik menggunakan Streamlit
    st.pyplot(fig)

if __name__ == "__main__":
    main()
    st.write("HSS: Hidrograf Satuan Sintetis")


