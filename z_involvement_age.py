import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

from tps import tps

ds = tps.KSIData()

ia = ds.df.INVAGE_cc.value_counts().sort_index(ascending=True)
ia2 = pd.DataFrame({'COUNT': ia}).reset_index()
ia2['INVAGE_NAME'] = ia.index.map(lambda x: ds.age_list_index[x])

trace1 = go.Bar(
    name="False",
    # x=fy.unstack().index,
    # y=fy.unstack()[0],
    x=ia2.INVAGE_NAME,
    y=ia2.COUNT,
    offsetgroup=0,
)


# trace1 = go.Bar(x=ic.INV, y=ic.CNT)

app = dash.Dash()
app.layout = html.Div(children=[
    html.H1(children='Sales Funnel Report'),
    html.Div(children='''National Sales Funnel Report.'''),
    dcc.Graph(
        id='example-graph',
        # barmode='stack',
        figure={
            'data': [trace1, ],
            'layout':
            go.Layout(title='Order Status by Customer',
                      # barmode='stack'
            )
        })
])

if __name__ == '__main__':
    app.run_server(debug=True)
