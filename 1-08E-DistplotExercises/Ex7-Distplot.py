#######
# Objective: Using the iris dataset, develop a Distplot
# that compares the petal lengths of each class.
# File: '../data/iris.csv'
# Fields: 'sepal_length','sepal_width','petal_length','petal_width','class'
# Classes: 'Iris-setosa','Iris-versicolor','Iris-virginica'
######

# Perform imports here:
import pandas as pd
import plotly.offline as plt
import plotly.figure_factory as ff

# create a DataFrame from the .csv file:
df = pd.read_csv('../Data/iris.csv')

# Define a data variable
group_labels = df['class'].unique()
traces = [df[df['class'] == flower]['petal_length'] for flower in group_labels]

# Create a fig from data and layout, and plot the fig
fig = ff.create_distplot(traces, group_labels, bin_size=0.2)
plt.plot(fig)