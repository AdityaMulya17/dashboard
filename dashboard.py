import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

changping_df = pd.read_csv("changping.csv")

changping_df['date'] = pd.to_datetime(changping_df[['year', 'month', 'day']])



datetime_columns = ["date"]
changping_df.sort_values(by="date", inplace=True)
changping_df.reset_index(inplace=True)
 
for column in datetime_columns:
    changping_df[column] = pd.to_datetime(changping_df[column])

min_date = changping_df["date"].min()
max_date = changping_df["date"].max()
 
with st.sidebar:
    
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )


st.header('Kualitas Udara di Kota Changping :sparkles:')

main_df = changping_df[(changping_df["date"] >= str(start_date)) & 
                (changping_df["date"] <= str(end_date))]

st.subheader('Kualitas udara tahunan berdasarkan berbagai parameter ')

Tahun_df = main_df.groupby("year").mean(numeric_only=True)

fig = plt.figure(figsize=(10,6))
plt.plot(Tahun_df.index, Tahun_df["PM2.5"], label="PM2.5")
plt.xlabel("Tahun")
plt.ylabel("Konsentrasi Kualitas Udara(microgram/m3)")
plt.legend()
st.pyplot(fig)


Tahun_df = main_df.groupby("year").mean(numeric_only=True)

fig = plt.figure(figsize=(10,6))
plt.plot(Tahun_df.index, Tahun_df["PM10"], label="PM10")
plt.xlabel("Tahun")
plt.ylabel("Konsentrasi Kualitas Udara(microgram/m3)")
plt.legend()
st.pyplot(fig)


Tahun_df = main_df.groupby("year").mean(numeric_only=True)

fig = plt.figure(figsize=(10,6))
plt.plot(Tahun_df.index, Tahun_df["SO2"], label="SO2")
plt.xlabel("Tahun")
plt.ylabel("Konsentrasi Kualitas Udara(microgram/m3)")
plt.legend()
st.pyplot(fig)

Tahun_df = main_df.groupby("year").mean(numeric_only=True)

fig = plt.figure(figsize=(10,6))
plt.plot(Tahun_df.index, Tahun_df["CO"], label="CO")
plt.xlabel("Tahun")
plt.ylabel("Konsentrasi Kualitas Udara(microgram/m3)")
plt.legend()
st.pyplot(fig)

st.subheader('Kualitas udara PERBULAN berdasarkan berbagai parameter ')


Bulan_df = main_df.groupby("month").mean(numeric_only=True)

fig = plt.figure(figsize=(10,6))
plt.plot(Tahun_df.index, Tahun_df["CO"], label="CO")
plt.xlabel("Bulan")
plt.ylabel("Konsentrasi Kualitas Udara(microgram/m3)")
plt.legend()
st.pyplot(fig)

Bulan_df = main_df.groupby("month").mean(numeric_only=True)

fig = plt.figure(figsize=(10,6))
plt.plot(Tahun_df.index, Tahun_df["PM2.5"], label="PM2.5")
plt.xlabel("Bulan")
plt.ylabel("Konsentrasi Kualitas Udara(microgram/m3)")
plt.legend()
st.pyplot(fig)

Bulan_df = main_df.groupby("month").mean(numeric_only=True)

fig = plt.figure(figsize=(10,6))
plt.plot(Tahun_df.index, Tahun_df["PM10"], label="PM10")
plt.xlabel("Bulan")
plt.ylabel("Konsentrasi Kualitas Udara(microgram/m3)")
plt.legend()
st.pyplot(fig)