import dash
import dash.dependencies as dd
# import dash_core_components as dcc
import dash_html_components as html
# import plotly
# import plotly.graph_objs as go
# from plotly.offline import plot
from wordcloud import WordCloud

# import random
# import pandas as pd
from tps import tps

from io import BytesIO
import base64

ds = tps.KSIData()

# words = ds.df["INVTYPE"].str.split("(").str[0].value_counts().keys()

# wc = WordCloud(scale=5, max_words=1000, colormap="rainbow", background_color="black").generate(" ".join(words))

# words = dir(go)[:30]
# colors = [plotly.colors.DEFAULT_PLOTLY_COLORS[random.randrange(1, 10)] for i in range(30)]
# weights = [random.randint(15, 35) for i in range(30)]


# data = go.Scatter(x=[random.random() for i in range(30)],
#                   y=[random.random() for i in range(30)],
#                   mode='text',
#                   text=words,
#                   marker={'opacity': 0.3},
#                   textfont={'size': weights,
#                             'color': colors})
# mylayout = go.Layout({'xaxis': {'showgrid': False, 'showticklabels': False, 'zeroline': False},
#                     'yaxis': {'showgrid': False, 'showticklabels': False, 'zeroline': False}})
# fig = go.Figure(data=[data], layout=mylayout)

#plot(fig)



# trace1 = go.Bar(x=ic.INV, y=ic.CNT)

app = dash.Dash()
app.layout = html.Div(children=[
    html.H1(children='Sales Funnel Report'),
    html.Div(children='''National Sales Funnel Report.'''),
    html.Img(id="image_wc"),
    #dcc.Graph(
        #id='example-graph',
        #barmode='stack',
        # figure={
        #     'data': [trace1, trace2],
        #     'layout':
        #     go.Layout(title='Order Status by Customer', barmode='stack')
        # })
        #figure=fig
    #)
])


# dfm = pd.DataFrame({'word': ['apple', 'pear', 'orange'], 'freq': [1,3,9]})

def plot_wordcloud():
    # d = {a: x for a, x in data.values}
    words = ds.df["INVTYPE"].str.split("(").str[0].value_counts().keys()
    wc = WordCloud(scale=5, max_words=1000, colormap="rainbow", background_color="black").generate(" ".join(words))
    # wc = WordCloud(background_color='black', width=480, height=360)
    # wc.fit_words(d)
    return wc.to_image()

@app.callback(dd.Output('image_wc', 'src'), [dd.Input('image_wc', 'id')])
def make_image(b):
    img = BytesIO()
    plot_wordcloud().save(img, format='PNG')
    return 'data:image/png;base64,{}'.format(base64.b64encode(img.getvalue()).decode())


if __name__ == '__main__':
    app.run_server(debug=True)
