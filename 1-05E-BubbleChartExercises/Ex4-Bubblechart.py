#######
# Objective: Create a bubble chart that compares three other features
# from the mpg.csv dataset. Fields include: 'mpg', 'cylinders', 'displacement'
# 'horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'name'
######

# Perform imports here:
import plotly.offline as plt
import plotly.graph_objs as go
import pandas as pd

# create a DataFrame from the .csv file:
df = pd.read_csv('../Data/mpg.csv')
print(df)

# create data by choosing fields for x, y and marker size attributes

data = [go.Scatter(
    x=df['horsepower'],
    y=df['displacement'],
    mode='markers',
    marker=dict(
        size=df['mpg'],
        color=df['cylinders'],
        showscale=True
    )
)]

# create a layout with a title and axis labels
layout = go.Layout(
    title='Cars',
    xaxis= dict(title='horsepower'),
    yaxis= dict(title='acceleration'),
    hovermode='closest'
)


# create a fig from data & layout, and plot the fig
fig = go.Figure(data, layout)

plt.plot(fig)
