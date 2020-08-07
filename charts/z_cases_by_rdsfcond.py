import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

from tps import tps

ds = tps.KSIData()

rs = ds.df.RDSFCOND.value_counts().sort_values(ascending=False)
rs2 = rs[:5]

fig = {
  "data": [
    {
      "values": rs2.values,
      "labels": rs2.index,
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

trace1 = go.Bar(
  name="District",
  x=rs2.values,
  y=rs2.index,
  orientation='h'
)

app = dash.Dash()
app.layout = html.Div(children=[
    html.H1(children='Sales Funnel Report'),
    html.Div(children='''National Sales Funnel Report.'''),
    dcc.Graph(
      id='example-graph',
      figure=fig),
    dcc.Graph(
      id='example-graph2',
      figure={
          'data': [trace1],
          'layout':
          go.Layout(title='Order Status by Customer')
      })
])

if __name__ == '__main__':
    app.run_server(debug=True)
