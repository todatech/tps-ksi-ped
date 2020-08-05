import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

from tps import tps

ds = tps.KSIData()

involvement_per_case = ds.df.groupby(['ACCNUM'])['Index_'].count()
ic = pd.DataFrame({'count': involvement_per_case.value_counts().sort_index()}).reset_index()
ic.columns = ['INV','CNT']

trace1 = go.Bar(x=ic.INV, y=ic.CNT)

app = dash.Dash()
app.layout = html.Div(children=[
    html.H1(children='Sales Funnel Report'),
    html.Div(children='''National Sales Funnel Report.'''),
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [trace1, ],
            'layout':
            go.Layout(title='Order Status by Customer', barmode='stack')
        })
])

if __name__ == '__main__':
    app.run_server(debug=True)
