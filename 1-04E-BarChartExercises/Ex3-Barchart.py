#######
# Objective: Create a stacked bar chart from
# the file ../data/mocksurvey.csv. Note that questions appear in
# the index (and should be used for the x-axis), while responses
# appear as column labels.  Extra Credit: make a horizontal bar chart!
######

# Perform imports here:
import pandas as pd
import plotly.offline as plt
import plotly.graph_objs as go


# create a DataFrame from the .csv file:
df = pd.read_csv('../Data/mocksurvey.csv')
print(df)
print(df['Unnamed: 0'])


# create traces using a list comprehension:
traces = [go.Bar(
    x=df[column],
    y=df['Unnamed: 0'],

    orientation='h'
) for column in df.columns if column != 'Unnamed: 0']

# create a layout, remember to set the barmode here
layout = go.Layout(title='Mock Survey Results', barmode='stack')

# create a fig from data & layout, and plot the fig.
Figure = go.Figure(data=traces, layout=layout)

plt.plot(Figure)
