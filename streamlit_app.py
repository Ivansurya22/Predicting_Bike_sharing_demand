import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load Data
seasonal_data = pd.read_csv(r'\dashboard\seasonal_trend.csv')
weather_data = pd.read_csv(r'\weather_influence.csv')
weekday_data = pd.read_csv(r'\dashboard\weekday_trend.csv')
hourly_data = pd.read_csv(r'\dashboard\hourly_trend.csv')
predictions = pd.read_csv(r'\predictions_day.csv')
rfm_data = pd.read_csv(r'\dashboard\rfm_analysis.csv')

# Dashboard
st.title("Bike Sharing Analysis Dashboard")

# 1. Tren Musiman
st.header("1. Tren Musiman")
st.bar_chart(data=seasonal_data, x='season_label', y='cnt', use_container_width=True)

# 2. Pengaruh Cuaca
st.header("2. Pengaruh Cuaca")
st.bar_chart(data=weather_data, x='weather_label', y='cnt', use_container_width=True)

# 3. Kebiasaan Harian
st.header("3. Kebiasaan Harian")
st.bar_chart(data=weekday_data, x='workingday_label', y='cnt', use_container_width=True)

# 4. Perilaku Berdasarkan Jam
st.header("4. Perilaku Berdasarkan Jam")
st.line_chart(data=hourly_data, x='hr', y='cnt', use_container_width=True)

# 5. Prediksi vs Aktual
st.header("5. Prediksi Total Peminjaman")
st.write(predictions)

# 6. Analisis RFM
st.header("6. Analisis RFM")
st.dataframe(rfm_data)
