import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
data = pd.read_csv("dashboard/main_data.csv")

# Set title
st.title("Dashboard Penyewaan Sepeda")

# Visualisasi 1: Perbandingan Faktor Cuaca per Bulan
st.subheader("Perbandingan Faktor Cuaca per Bulan di Tahun 2012")
fig, ax = plt.subplots()
sns.lineplot(data=data, x="month", y="temp", label="Temperature", marker="o")
sns.lineplot(data=data, x="month", y="hum", label="Humidity", marker="o")
sns.lineplot(data=data, x="month", y="windspeed", label="Windspeed", marker="o")
ax.set_xlabel("Bulan")
ax.set_ylabel("Rata-rata Nilai")
st.pyplot(fig)

# Visualisasi 2: Penyewaan Berdasarkan Musim
st.subheader("Rata-rata Penyewaan Sepeda Berdasarkan Musim")
avg_season = data.groupby("season")["cnt"].mean()
fig, ax = plt.subplots()
avg_season.plot(kind="bar", ax=ax, color="steelblue")
ax.set_xlabel("Musim")
ax.set_ylabel("Jumlah Penyewaan (Rata-rata)")
st.pyplot(fig)

# Visualisasi 3: Penyewaan Berdasarkan Kondisi Cuaca
st.subheader("Rata-rata Penyewaan Sepeda Berdasarkan Kondisi Cuaca")
avg_weather = data.groupby("weathersit")["cnt"].mean()
fig, ax = plt.subplots()
avg_weather.plot(kind="bar", ax=ax, color="steelblue")
ax.set_xlabel("Kondisi Cuaca")
ax.set_ylabel("Jumlah Penyewaan (Rata-rata)")
st.pyplot(fig)
