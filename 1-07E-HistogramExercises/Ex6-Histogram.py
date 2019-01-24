#######
# Objective: Create a histogram that plots the 'length' field
# from the Abalone dataset (../data/abalone.csv).
# Set the range from 0 to 1, with a bin size of 0.02
######

# Perform imports here:
import pandas as pd
import plotly.offline as plt
import plotly.graph_objs as go

# create a DataFrame from the .csv file:
df = pd.read_csv('../Data/abalone.csv')

# create a data variable:
data = [go.Histogram(x=df['length'])]


# add a layout
layout = go.Layout(title='Histogram')

# create a fig from data & layout, and plot the fig
fig = go.Figure(data, layout)

plt.plot(fig)
