import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

from tps import tps

ds = tps.KSIData()

cn = ds.df.groupby('Hood_ID')['ACCNUM'].nunique().sort_values(ascending=False)
cn2 = pd.DataFrame({'COUNT': cn}).reset_index()
cn2['HOOD_NAME'] = cn2.Hood_ID.apply(lambda x: ds.get_hood_dict(x))
cn3 = cn2[:10]

trace1 = go.Bar(x=cn3.HOOD_NAME, y=cn3.COUNT)

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
