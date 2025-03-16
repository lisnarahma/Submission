import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("dashboard/main_data.csv")
data['dteday'] = pd.to_datetime(data['dteday'])


data_2012 = data[data['dteday'].dt.year == 2012]
data_2012['month'] = data_2012['dteday'].dt.month

monthly_avg = data_2012.groupby("month")[["temp", "hum", "windspeed"]].mean().reset_index()

fig1, ax1 = plt.subplots(figsize=(10, 5))
sns.lineplot(data=monthly_avg, x="month", y="temp", label="Temperature", marker="o")
sns.lineplot(data=monthly_avg, x="month", y="hum", label="Humidity", marker="s")
sns.lineplot(data=monthly_avg, x="month", y="windspeed", label="Windspeed", marker="^")

ax1.set_title("Perbandingan Faktor Cuaca per Bulan (2012)")
ax1.set_xlabel("Bulan")
ax1.set_ylabel("Nilai")
ax1.legend()

st.title("Dashboard Penyewaan Sepeda")
st.pyplot(fig1)

st.markdown("<br><br>", unsafe_allow_html=True)

rent_by_season = data_2012.groupby("season")["cnt"].mean().reset_index()
rent_by_weather = data_2012.groupby("weathersit")["cnt"].mean().reset_index()

season_labels = ["Winter", "Spring", "Summer", "Fall"]
weather_labels = ["Cerah/Berawan", "Berkabut", "Hujan/Salju"]

fig2, axes = plt.subplots(1, 2, figsize=(14, 5))

sns.barplot(x=season_labels, y=rent_by_season["cnt"], ax=axes[0])
axes[0].set_title("Rata-rata Penyewaan Sepeda Berdasarkan Musim")
axes[0].set_ylabel("Jumlah Penyewaan (Rata-rata)")
axes[0].set_xlabel("Musim")

sns.barplot(x=weather_labels, y=rent_by_weather["cnt"], ax=axes[1])
axes[1].set_title("Rata-rata Penyewaan Sepeda Berdasarkan Kondisi Cuaca")
axes[1].set_ylabel("Jumlah Penyewaan (Rata-rata)")
axes[1].set_xlabel("Kondisi Cuaca")

plt.tight_layout()

st.pyplot(fig2)

# Menambahkan fitur interaktif - Pilihan bulan
st.markdown("---")
st.subheader("Eksplorasi Data Berdasarkan Bulan")

bulan_mapping = {
    1: "Januari", 2: "Februari", 3: "Maret", 4: "April",
    5: "Mei", 6: "Juni", 7: "Juli", 8: "Agustus",
    9: "September", 10: "Oktober", 11: "November", 12: "Desember"
}
selected_month = st.selectbox("Pilih Bulan untuk Dieksplorasi", list(bulan_mapping.values()), index=0)

# Ubah nama bulan ke angka untuk filtering
selected_month_num = [k for k, v in bulan_mapping.items() if v == selected_month][0]

# Filter data berdasarkan bulan yang dipilih
filtered_data = data_2012[data_2012["month"] == selected_month_num]

# Visualisasi faktor cuaca pada bulan tertentu
fig3, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(data=filtered_data, x="dteday", y="temp", label="Temperature", marker="o")
sns.lineplot(data=filtered_data, x="dteday", y="hum", label="Humidity", marker="s")
sns.lineplot(data=filtered_data, x="dteday", y="windspeed", label="Windspeed", marker="^")

ax.set_title(f"Perbandingan Faktor Cuaca - {selected_month} 2012")
ax.set_xlabel("Tanggal")
ax.set_ylabel("Nilai")
ax.legend()
st.pyplot(fig3)

