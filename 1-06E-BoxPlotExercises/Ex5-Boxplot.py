#######
# Objective: Make a DataFrame using the Abalone dataset (../data/abalone.csv).
# Take two independent random samples of different sizes from the 'rings' field.
# HINT: np.random.choice(df['rings'],10,replace=False) takes 10 random values
# Use box plots to show that the samples do derive from the same population.
######

# Perform imports here:
import plotly.offline as plt
import plotly.graph_objs as go
import pandas as pd
import numpy as np

# create a DataFrame from the .csv file:
df = pd.read_csv('../Data/abalone.csv')
print(df)

# take two random samples of different sizes:

traces = [go.Box(
    name=sample,
    y=np.random.choice(df['rings'], 10, replace=False),
    boxpoints='all',
    pointpos=0,
    jitter=0.5
) for sample in range(1, 10)]

# create a data variable with two Box plots:
data = traces

# add a layout
layout = go.Layout(title='Abalone')

# create a fig from data & layout, and plot the fig
fig = go.Figure(data, layout)
plt.plot(fig)
