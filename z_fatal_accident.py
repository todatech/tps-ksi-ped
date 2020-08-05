import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

from tps import tps

ds = tps.KSIData()
accidents = ds.df.ACCLASS.value_counts().sort_index(ascending=True)
accidents

fig = {
  "data": [
    {
      "values": accidents.values,
      "labels": accidents.index,
      "domain": {"x": [0, .5]},
      "name": "Number Of Students Rates",
      "hoverinfo":"label+percent+name",
      "hole": .3,
      "type": "pie"
    }, ],
  "layout": {
        "title": "Universities Number of Students rates",
        "annotations": [
            {
                "font": {"size": 20},
                "showarrow": False,
                "text": "Number of Students",
                "x": 0.20,
                "y": 1
            },
        ]
    }
}

app = dash.Dash()
app.layout = html.Div(children=[
    html.H1(children='Sales Funnel Report'),
    html.Div(children='''National Sales Funnel Report.'''),
    dcc.Graph(
        id='example-graph',
        figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)
