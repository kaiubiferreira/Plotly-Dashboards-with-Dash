import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np

app = dash.Dash()

# Creating DATA
np.random.seed(42)
random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

data = [go.Scatter(x=random_x, y=random_y, mode='markers', marker={
    'size': 12,
    'color': 'rgb(51,204,153)',
    'symbol': 'pentagon',
    'line': {'width': 2}
})]

data2 = [go.Scatter(x=random_x, y=np.random.randint(1, 101, 100), mode='markers', marker={
    'size': 12,
    'color': 'rgb(200,204,53)',
    'symbol': 'pentagon',
    'line': {'width': 2}
})]
layout = go.Layout(title='My Scatterplot', xaxis=dict(title='Some X title'))

app.layout = html.Div(
    [dcc.Graph(id='scatterplot', figure={'data': data, 'layout': layout}),
     dcc.Graph(id='scatterplot2', figure={'data': data2, 'layout': layout}),
     html.H2("Plot")
    ]
)

if __name__ == '__main__':
    app.run_server()
