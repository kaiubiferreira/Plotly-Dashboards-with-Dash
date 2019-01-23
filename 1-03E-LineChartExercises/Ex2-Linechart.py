#######
# Objective: Using the file 2010YumaAZ.csv, develop a Line Chart
# that plots seven days worth of temperature data on one graph.
# You can use a for loop to assign each day to its own trace.
######

# Perform imports here:
import pandas as pd
import plotly.offline as plt
import plotly.graph_objs as go



# Create a pandas DataFrame from 2010YumaAZ.csv
df = pd.read_csv('../Data/2010YumaAZ.csv')

# Use a for loop (or list comprehension to create traces for the data list)
data = [go.Scatter(
        x=df['LST_TIME'],
        y=df[df['DAY'] == weekday]['T_HR_AVG'],
        name=weekday,
        mode='lines+markers') for weekday in df['DAY'].unique()]


# Define the layout
layout = go.Layout(title='Temperatures', hovermode='closest')

# Create a fig from data and layout, and plot the fig
fig = go.Figure(data, layout)
plt.plot(fig)
