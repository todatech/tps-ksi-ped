# Data
import pandas as pd

# Graphing
import plotly.graph_objects as go

# Dash
import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Output, Input

# Navbar
from app import app
from layouts import navbar


df = pd.read_csv('https://gist.githubusercontent.com/joelsewhere/f75da35d9e0c7ed71e5a93c10c52358d/raw/d8534e2f25495cc1de3cd604f952e8cbc0cc3d96/population_il_cities.csv')
df.set_index(df.iloc[:, 0], drop=True, inplace=True)
df = df.iloc[:, 1:]


header = html.H3(
    'Select the name of an Illinois city to see its population!'
)

options = [{'label': x.replace(', Illinois', ''), 'value': x}
           for x in df.columns]

dropdown = html.Div(dcc.Dropdown(
    id='pop_dropdown',
    options=options,
    value='Abingdon city, Illinois'
))

output = html.Div(id='output',
                  children=[],
                  )


def App():
    layout = html.Div([
        navbar,
        header,
        dropdown,
        output
    ])
    return layout


def build_graph(city):
    data = [go.Scatter(x=df.index,
                       y=df[city],
                       marker={'color': 'orange'})]
    graph = dcc.Graph(
        figure={
            'data': data,
            'layout': go.Layout(
                title='{} Population Change'.format(city),
                yaxis={'title': 'Population'},
                hovermode='closest'
            )
        }
    )
    return graph


@app.callback(
    Output('output', 'children'),
    [Input('pop_dropdown', 'value')]
)
def update_graph(city):
    graph = build_graph(city)
    return graph


if __name__ == "__main__":
    app.run_server(host='0.0.0.0', port=8050)
