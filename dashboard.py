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

st.subheader('Kualitas udara perjam kota Changping  ')


Jam_df = changping_df.groupby("hour").mean(numeric_only=True)

fig = plt.figure(figsize=(10,6))
plt.plot(Jam_df.index, Jam_df["PM2.5"], label="PM2.5")
plt.plot(Jam_df.index,Jam_df["PM10"], label="PM10")
plt.plot(Jam_df.index, Jam_df["SO2"], label="SO2")
plt.plot(Jam_df.index, Jam_df["NO2"], label="NO2")
plt.plot(Jam_df.index, Jam_df["O3"], label="O3")
plt.xlabel("Jam")
plt.ylabel("Konsentrasi Polusi(microgram/m3)")
plt.legend()
st.pyplot(fig)

#tren nilai CO

Jam_df = changping_df.groupby("hour").mean(numeric_only=True)

fig = plt.figure(figsize=(10,6))
plt.plot(Jam_df.index, Jam_df["CO"], label="CO")
plt.xlabel("Hour")
plt.ylabel("Konsentrasi Polusi (microgram/m3)")
plt.legend()
plt.show()
st.pyplot(fig)


st.subheader('Kualitas udara Perhari Kota Changping ')

Hari_df = changping_df.groupby("day").mean(numeric_only=True)

fig = plt.figure(figsize=(10,6))
plt.plot(Hari_df.index, Hari_df["PM2.5"], label="PM2.5")
plt.plot(Hari_df.index, Hari_df["PM10"], label="PM10")
plt.plot(Hari_df.index, Hari_df["SO2"], label="SO2")
plt.plot(Hari_df.index, Hari_df["NO2"], label="NO2")
plt.plot(Hari_df.index, Hari_df["O3"], label="O3")
plt.xlabel("tanggal")
plt.ylabel("Konsentrasi Polusi (microgram/m3)")
plt.legend()
plt.show()
st.pyplot(fig)


Hari_df = changping_df.groupby("day").mean(numeric_only=True)
fig = plt.figure(figsize=(10,6))
plt.plot(Hari_df.index, Hari_df["CO"], label="CO")
plt.xlabel("tanggal")
plt.ylabel("Konsentrasi Polusi (microgram/m3)")
plt.legend()
plt.show()
st.pyplot(fig)

st.subheader('Kualitas udara Perbulan Kota Changping ')

Bulan_df = changping_df.groupby("month").mean(numeric_only=True)

fig = plt.figure(figsize=(10,6))
plt.plot(Bulan_df.index, Bulan_df["PM2.5"], label="PM2.5")
plt.plot(Bulan_df.index, Bulan_df["PM10"], label="PM10")
plt.plot(Bulan_df.index, Bulan_df["SO2"], label="SO2")
plt.plot(Bulan_df.index, Bulan_df["NO2"], label="NO2")
plt.plot(Bulan_df.index, Bulan_df["O3"], label="O3")
plt.xlabel("bulan")
plt.ylabel("Konsentrasi Polusi (microgram/m3)")
plt.legend()
plt.show()
st.pyplot(fig)

Bulan_df = changping_df.groupby("month").mean(numeric_only=True)
fig = plt.figure(figsize=(10,6))
plt.plot(Bulan_df.index, Bulan_df["CO"], label="CO")
plt.xlabel("bulan")
plt.ylabel("Konsentrasi Polusi (microgram/m3)")
plt.legend()
plt.show()
st.pyplot(fig)

st.subheader('Kualitas udara Pertahun Kota Changping ')

Tahun_df = changping_df.groupby("year").mean(numeric_only=True)

fig = plt.figure(figsize=(10,6))
plt.plot(Tahun_df.index, Tahun_df["PM2.5"], label="PM2.5")
plt.plot(Tahun_df.index, Tahun_df["PM10"], label="PM10")
plt.plot(Tahun_df.index, Tahun_df["SO2"], label="SO2")
plt.plot(Tahun_df.index, Tahun_df["NO2"], label="NO2")
plt.plot(Tahun_df.index, Tahun_df["O3"], label="O3")
plt.xlabel("Tahun")
plt.ylabel("Konsentrasi Polusi (microgram/m3)")
plt.legend()
plt.show()
st.pyplot(fig)

fig = plt.figure(figsize=(10,6))
plt.plot(Tahun_df.index, Tahun_df["CO"], label="CO")
plt.xlabel("Tahun")
plt.ylabel("Konsentrasi Polusi (microgram/m3)")
plt.legend()
plt.show()
st.pyplot(fig)



st.subheader('Korelasi antar parameter ')


fig = plt.figure(figsize=(13,9))

sns.heatmap(changping_df.corr(numeric_only = True),cmap=plt.cm.Reds,annot=True)
plt.title("Korelasi Polusi Udara dan Parameter Meteorologi")
plt.show()

st.pyplot(fig)