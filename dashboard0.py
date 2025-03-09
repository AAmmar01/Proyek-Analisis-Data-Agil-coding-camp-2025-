import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Load dataset
day_url = "https://raw.githubusercontent.com/AAmmar01/Proyek-Analisis-Data-Agil-coding-camp-2025-/main/day.csv"
hour_url = "https://raw.githubusercontent.com/AAmmar01/Proyek-Analisis-Data-Agil-coding-camp-2025-/main/hour.csv"

day_df = pd.read_csv(day_url)
hour_df = pd.read_csv(hour_url)

day_df["dteday"] = pd.to_datetime(day_df["dteday"])
hour_df["dteday"] = pd.to_datetime(hour_df["dteday"])

# Streamlit app
st.title("Dashboard Analisis Peminjaman Sepeda")

# Sidebar
st.sidebar.header("Pengaturan")
view_data = st.sidebar.checkbox("Lihat Data Mentah")

if view_data:
    st.subheader("Dataset Harian")
    st.write(day_df.head())
    st.subheader("Dataset Per Jam")
    st.write(hour_df.head())

# Statistik Deskriptif
st.subheader("Statistik Deskriptif")
st.write(day_df.describe())

# Visualisasi Pola Peminjaman per Jam
st.subheader("Pola Peminjaman Sepeda per Jam")
hourly_trend = hour_df.groupby("hr").cnt.mean()
fig, ax = plt.subplots(figsize=(12,5))
sns.lineplot(x=hourly_trend.index, y=hourly_trend.values, marker="o", color="b", ax=ax)
ax.set_title("Pola Peminjaman Sepeda Berdasarkan Jam")
ax.set_xlabel("Jam dalam Sehari")
ax.set_ylabel("Rata-rata Peminjaman Sepeda")
st.pyplot(fig)

# Pola Peminjaman per Hari dalam Seminggu
st.subheader("Pola Peminjaman Sepeda Berdasarkan Hari dalam Seminggu")
weekday_trend = hour_df.groupby("weekday").cnt.mean()
fig, ax = plt.subplots(figsize=(10,5))
sns.barplot(x=weekday_trend.index, y=weekday_trend.values, palette="viridis", ax=ax)
ax.set_title("Pola Peminjaman Sepeda Berdasarkan Hari dalam Seminggu")
ax.set_xlabel("Hari dalam Seminggu (0 = Minggu, 6 = Sabtu)")
ax.set_ylabel("Rata-rata Peminjaman Sepeda")
ax.set_xticks(range(0,7))
ax.set_xticklabels(["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"])
st.pyplot(fig)

# Hubungan Faktor Lingkungan dengan Peminjaman Sepeda
st.subheader("Analisis Faktor Lingkungan")
factors = ["temp", "hum", "windspeed"]
factor_names = ["Suhu", "Kelembaban", "Kecepatan Angin"]

for i, factor in enumerate(factors):
    fig, ax = plt.subplots(figsize=(10,5))
    sns.scatterplot(x=hour_df[factor], y=hour_df["cnt"], alpha=0.5, ax=ax)
    ax.set_title(f"Hubungan {factor_names[i]} dengan Peminjaman Sepeda")
    ax.set_xlabel(factor_names[i])
    ax.set_ylabel("Jumlah Peminjaman Sepeda")
    st.pyplot(fig)

# Clustering Klasifikasi Waktu
st.subheader("Clustering: Klasifikasi Waktu")
def categorize_hour(hour):
    if 0 <= hour < 6:
        return 'Malam'
    elif 6 <= hour < 12:
        return 'Pagi'
    elif 12 <= hour < 18:
        return 'Siang'
    else:
        return 'Malam'

hour_df['time_of_day'] = hour_df['hr'].apply(categorize_hour)
clustering_result = hour_df.groupby('time_of_day').cnt.mean().reset_index()
fig, ax = plt.subplots(figsize=(8,5))
sns.barplot(x='time_of_day', y='cnt', data=clustering_result, palette='coolwarm', ax=ax)
ax.set_title('Rata-rata Peminjaman Sepeda berdasarkan Waktu dalam Sehari')
st.pyplot(fig)

# Clustering Permintaan Sepeda
st.subheader("Clustering: Klasifikasi Permintaan Sepeda")
bins = [0, 100, 300, hour_df['cnt'].max()]
labels = ['Rendah', 'Sedang', 'Tinggi']
hour_df['demand_cluster'] = pd.cut(hour_df['cnt'], bins=bins, labels=labels)

cluster_counts = hour_df['demand_cluster'].value_counts()
fig, ax = plt.subplots(figsize=(8,5))
sns.barplot(x=cluster_counts.index, y=cluster_counts.values, palette='viridis', ax=ax)
ax.set_title("Distribusi Cluster Permintaan Sepeda")
st.pyplot(fig)