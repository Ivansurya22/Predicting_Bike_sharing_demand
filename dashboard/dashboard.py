import streamlit as st
import pandas as pd

# Load processed data
day_df = pd.read_csv('processed_day.csv')
hour_df = pd.read_csv('processed_hour.csv')

# Dashboard
st.title('Bike Sharing Analysis Dashboard')

# Filter by season
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
selected_season = st.selectbox('Select a season:', seasons)
filtered_day_df = day_df[day_df['season_label'] == selected_season]

# Show filtered data
st.header(f'Data for {selected_season}')
st.dataframe(filtered_day_df[['dteday', 'cnt', 'registered', 'casual']])

# Interactive visualizations
st.header('Average Rentals by Hour')
selected_workingday = st.radio('Filter by Working Day:', ['Working Day', 'Non-Working Day'])
workingday_flag = 1 if selected_workingday == 'Working Day' else 0
filtered_hour_df = hour_df[hour_df['workingday'] == workingday_flag]

hourly_data = filtered_hour_df.groupby('hr')['cnt'].mean().reset_index()
st.line_chart(hourly_data, x='hr', y='cnt')

st.header('RFM Analysis')
st.dataframe(pd.read_csv('rfm_analysis.csv'))