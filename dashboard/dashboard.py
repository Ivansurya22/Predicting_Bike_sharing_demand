import streamlit as st
import pandas as pd

# Load processed data
day_df = pd.read_csv('processed_day.csv')
hour_df = pd.read_csv('processed_hour.csv')

# Streamlit dashboard
st.title("Bike Share Dashboard")

# Sidebar filters
st.sidebar.header("Filters")
season_filter = st.sidebar.multiselect(
    "Select Season(s):", 
    options=day_df['season_label'].unique(), 
    default=day_df['season_label'].unique()
)
hour_filter = st.sidebar.slider(
    "Select Hour Range:", 
    min_value=int(hour_df['hr'].min()), 
    max_value=int(hour_df['hr'].max()), 
    value=(0, 23)
)

# Filtered data
filtered_day_df = day_df[day_df['season_label'].isin(season_filter)]
filtered_hour_df = hour_df[(hour_df['hr'] >= hour_filter[0]) & (hour_df['hr'] <= hour_filter[1])]

# Visualization 1: Average Rentals by Season
st.subheader("Average Rentals by Season")
seasonal_data = filtered_day_df.groupby('season_label')['cnt'].mean()
st.bar_chart(seasonal_data)

# Visualization 2: Average Rentals by Hour
st.subheader("Average Rentals by Hour (Filtered)")
hourly_data = filtered_hour_df.groupby('hr')['cnt'].mean()
st.line_chart(hourly_data)

# Display raw data
st.subheader("Filtered Dataset")
st.write(filtered_day_df)
