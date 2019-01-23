import plotly.offline as plt
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('../Data/mpg.csv')

data = [go.Histogram(x=df['mpg'], xbins=dict(start=0, end=50, size=2))]
layout = go.Layout(title='Histogram')
fig = go.Figure(data, layout)
plt.plot(fig)
