import pandas as pd
import numpy as np
import time
import os
import streamlit as st

# Function to check Nash equilibrium
def is_nash_equilibrium(strategy_profile, payoff_matrix_player1, payoff_matrix_player2):
    u1 = payoff_matrix_player1.loc[strategy_profile[0], strategy_profile[1]]
    u2 = payoff_matrix_player2.loc[strategy_profile[0], strategy_profile[1]]

    deviation1 = payoff_matrix_player1.loc[strategy_profile[0], strategy_profile[1]] != payoff_matrix_player1.loc[strategy_profile[0], strategy_profile[1]]
    deviation2 = payoff_matrix_player2.loc[strategy_profile[0], strategy_profile[1]] != payoff_matrix_player2.loc[strategy_profile[0], strategy_profile[1]]

    return u1 >= u2 and not deviation1, u2 >= u1 and not deviation2

# Generate random payoff matrices
np.random.seed(42)
payoff_matrix_player1 = pd.DataFrame(np.random.randint(0, 5, size=(2, 2)), columns=['Up', 'Down'], index=['Up', 'Down'])
payoff_matrix_player2 = pd.DataFrame(np.random.randint(0, 5, size=(2, 2)), columns=['Up', 'Down'], index=['Up', 'Down'])

# Initialize players and strategies
players = ['Primary', 'Secondary']
current_strategy = {player: np.random.choice(['Up', 'Down']) for player in players}
frequency_records = []

# Simulate and measure time for Secondary to switch into Primary frequency 100 times
start_time = time.time()
data_frames = []
for simulation in range(100):
    current_strategy = {player: np.random.choice(['Up', 'Down']) for player in players}
    frequency_record = {'Primary': [], 'Secondary': [], 'Timestamp': []}

    for _ in range(20):  # Change this as needed
        # Check Nash equilibrium
        is_nash_p1, is_nash_p2 = is_nash_equilibrium((current_strategy['Primary'], current_strategy['Secondary']),
                                                      payoff_matrix_player1, payoff_matrix_player2)

        # Record frequencies and timestamp
        frequency_record['Primary'].append(current_strategy['Primary'])
        frequency_record['Secondary'].append(current_strategy['Secondary'])
        frequency_record['Timestamp'].append(time.time())

        # Update strategies ensuring the secondary is 'Up' when the primary is 'Down'
        if not is_nash_p2:
            primary_strategy_index = 'Down' if current_strategy['Primary'] == 'Up' else 'Up'
            current_strategy['Secondary'] = primary_strategy_index

    data_frames.append(pd.DataFrame(frequency_record))

# Concatenate all DataFrames into one
data = pd.concat(data_frames, ignore_index=True)

# Streamlit App
st.title('Strategy Frequency Data Visualization')

# Display the data table
st.write('## Strategy Frequency Data Table')
st.dataframe(data)

# Create and display charts
st.write('## Charts')
st.line_chart(data['Timestamp'])

# Save data to CSV on the local C drive
#csv_file_path = 'C:\Research_GameTheory_Methodology\strategy_frequency_data.csv'
#data.to_csv(csv_file_path, index=False)

# Save the Streamlit app code to a file
#streamlit_code_path = 'C:\Research_GameTheory_Methodology\strategy_frequency_data.csv_streamlit.py'
#with open(streamlit_code_path, 'w') as file:
 #  file.write('streamlit run strategy_frequency_data.csv_streamlit.py')

#st.write(f"Streamlit app code saved to: {streamlit_code_path}")

# Streamlit app
#st.title("Strategy Frequency Data")
#st.write("Here is the data recorded during the simulations:")
#st.write(data)

# Save the Streamlit app code to a file
# Save the Streamlit app code to a file
streamlit_code_path = 'C:\Research_GameTheory_Methodology\strategy_frequency_data_streamlit.py'
with open(streamlit_code_path, 'w') as file:
    file.write("""
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
""")



