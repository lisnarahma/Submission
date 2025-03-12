import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

main_data = pd.read_csv('dashboard/main_data.csv')

main_data['dteday'] = pd.to_datetime(main_data['dteday'])

st.title('Dashboard Analisis Penyewaan Sepeda')

st.subheader('Jumlah Penyewaan Sepeda per Hari dalam Seminggu')
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
plt.figure(figsize=(10,5))
sns.barplot(x='weekday', y='cnt', data=main_data, order=day_order, palette='viridis')
plt.xlabel('Hari')
plt.ylabel('Jumlah Penyewaan')
plt.title('Penyewaan Sepeda Berdasarkan Hari')
st.pyplot(plt)

st.subheader('Perbandingan Penyewaan Sepeda: Hari Kerja vs Akhir Pekan')
main_data['weekend'] = main_data['weekday'].apply(lambda x: 'Weekend' if x in ['Saturday', 'Sunday'] else 'Weekday')

plt.figure(figsize=(8,5))
sns.barplot(x='weekend', y='cnt', data=main_data, palette=['blue', 'red'])
plt.xlabel('Jenis Hari')
plt.ylabel('Jumlah Penyewaan')
plt.title('Penyewaan Sepeda: Weekday vs Weekend')
st.pyplot(plt)

st.sidebar.header("Filter Tanggal")
start_date = st.sidebar.date_input("Tanggal Mulai", main_data['dteday'].min())
end_date = st.sidebar.date_input("Tanggal Akhir", main_data['dteday'].max())

filtered_data = main_data[(main_data['dteday'] >= pd.to_datetime(start_date)) & 
                          (main_data['dteday'] <= pd.to_datetime(end_date))]

st.write(f"Menampilkan data dari **{start_date}** sampai **{end_date}**")
st.dataframe(filtered_data)

st.subheader("Total Penyewaan Sepeda per Hari dalam Seminggu")
plt.figure(figsize=(10, 5))
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
filtered_data['weekday'] = filtered_data['weekday'].astype('category')
filtered_data['weekday'] = filtered_data['weekday'].cat.set_categories(day_order)
sns.barplot(x='weekday', y='cnt', data=filtered_data, order=day_order, palette='viridis')
plt.xlabel('Hari')
plt.ylabel('Jumlah Penyewaan')
plt.title('Penyewaan Sepeda per Hari dalam Seminggu')
st.pyplot(plt)

