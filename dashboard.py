import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

def create_airquality_hour_df(df):
    airquality_hour_df = changping_df.groupby(by="hour").agg({
        "PM2.5": ["max", "min", "mean", "std"],
    })
    airquality_hour_df = airquality_hour_df.reset_index()  
    
    return airquality_hour_df


def create_airquality_year_df(df):
    airquality_year_df = changping_df.groupby(by="year").agg({
        "PM2.5": ["max", "min", "mean", "std"],
    })
    airquality_year_df = airquality_year_df.reset_index()  
    
    return airquality_year_df


changping_df = pd.read_csv("changping.csv")


datetime_columns = ["date"]
changping_df.sort_values(by="date", inplace=True)
changping_df.reset_index(inplace=True)
 
for column in datetime_columns:
    changping_df[column] = pd.to_datetime(changping_df[column])

min_date = changping_df["date"].min()
max_date = changping_df["date"].max()
 
with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

main_df = changping_df[(changping_df["date"] >= str(start_date)) & 
                (changping_df["date"] <= str(end_date))]

airquality_hour_df = create_airquality_hour_df(main_df)
airquality_year_df = create_airquality_year_df(main_df)


st.subheader('Kualitas udara dalam perjam kota Changping')
fig, ax = plt.subplots(figsize=(20, 10))
mean_PM25_per_hour = airquality_hour_df['PM2.5']['mean']
plt.figure(figsize=(10, 5))

colors_ = ["#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3","#D3D3D3","#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", 
           "#D3D3D3","#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3","#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3",
           "#72BCD4", "#D3D3D3", "#D3D3D3"]

sns.barplot(
    y= mean_PM25_per_hour,
    x= 'hour',
    data=airquality_hour_df,
    palette=colors_
)
plt.title("Kualitas udara perjam berdasarkan parameter PM2.5", loc="center", fontsize=15)
plt.ylabel(None)
plt.xlabel(None)
plt.tick_params(axis='x', labelsize=12)
plt.show()

st.pyplot(fig)


st.subheader('Kualitas udara dalam pertahun kota Changping')
fig, ax = plt.subplots(figsize=(20, 10))
mean_PM25_per_year = airquality_year_df['PM2.5']['mean']
plt.figure(figsize=(10, 5))

colors_ = ["#D3D3D3", "#D3D3D3", "#D3D3D3","#72BCD4", "#72BCD4", ]

sns.barplot(
    y= mean_PM25_per_year,
    x= 'year',
    data=airquality_year_df,
    palette=colors_
)
plt.title("Rata-rata Kualitas udara pertahun berdasarkan parameter PM2.5", loc="center", fontsize=15)
plt.ylabel(None)
plt.xlabel(None)
plt.tick_params(axis='x', labelsize=12)
plt.show()

st.pyplot(fig)




