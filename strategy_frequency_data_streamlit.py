
import pandas as pd
import streamlit as st

# Load the data
data = pd.read_csv('C:\Research_GameTheory_Methodology\strategy_frequency_data.csv')

# Streamlit App
st.title('Strategy Frequency Data Visualization')

# Display the data table
st.write('## Strategy Frequency Data Table')
st.dataframe(data)

# Create and display charts
st.write('## Charts')
st.line_chart(data['Timestamp'])

# Streamlit app
st.title("Strategy Frequency Data")
st.write("Here is the data recorded during the simulations:")
st.write(data)
