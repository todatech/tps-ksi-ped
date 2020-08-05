import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

from tps import tps

ds = tps.KSIData()

fy = ds.df.groupby(ds.df.DATE.dt.year)['ACCLASS'].value_counts()
fy

trace1 = go.Bar(
    name="False",
    x=fy.unstack().index,
    y=fy.unstack()[0],
    offsetgroup=0,
)
trace2 = go.Bar(
    name='True',
    x=fy.unstack().index,
    y=fy.unstack()[1],
    offsetgroup=0,
    base=fy.unstack()[0],
)


# trace1 = go.Bar(x=ic.INV, y=ic.CNT)

app = dash.Dash()
app.layout = html.Div(children=[
    html.H1(children='Sales Funnel Report'),
    html.Div(children='''National Sales Funnel Report.'''),
    dcc.Graph(
        id='example-graph',
        #barmode='stack',
        figure={
            'data': [trace1, trace2],
            'layout':
            go.Layout(title='Order Status by Customer', barmode='stack')
        })
])

if __name__ == '__main__':
    app.run_server(debug=True)
