import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

from tps import tps

ds = tps.KSIData()

ds.df['SEASON'] = (ds.df['DATE'].dt.month % 12 + 3)//3
cs = ds.df.groupby(['YEAR', 'SEASON'])['ACCNUM'].nunique()


trace1 = go.Bar(
    name="Season 1",
    x=cs.unstack().index,
    y=cs[0::4],
    # offsetgroup=0,
)
trace2 = go.Bar(
    name="Season 2",
    x=cs.unstack().index,
    y=cs[1::4],
    # offsetgroup=1,
)
trace3 = go.Bar(
    name="Season 3",
    x=cs.unstack().index,
    y=cs[2::4],
    # offsetgroup=2,
)
trace4 = go.Bar(
    name="Season 4",
    x=cs.unstack().index,
    y=cs[3::4],
    # offsetgroup=3,
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
            'data': [trace1, trace2, trace3, trace4],
            'layout':
            go.Layout(title='Order Status by Customer')
        })
])

if __name__ == '__main__':
    app.run_server(debug=True)
