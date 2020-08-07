# import dash_core_components as dcc
import dash_bootstrap_components as dbc
# import dash_html_components as html

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("by students@York SCS", href="https://continue.yorku.ca/")),
        dbc.NavItem(dbc.NavLink("in colloboration with Toronto Police Service Open Data", href="https://data.torontopolice.on.ca/")),
        # dbc.NavItem(dbc.NavLink("Link 3", href="/lab3")),

        # dbc.DropdownMenu(
        #     nav=True,
        #     in_navbar=True,
        #     label="Labs",
        #     children=[
        #         dbc.DropdownMenuItem("Lab 1 - Recommender System",
        #                 href="/lab1"),
        #         dbc.DropdownMenuItem("Lab 2 - blah",
        #                 href="/lab2"),
        #         dbc.DropdownMenuItem("Lab 3 - blash",
        #                 href="/lab3"),
        #     ],
        # ),
    ],
    brand="Pedestrian Injury Predictor",
    brand_href="/",
    sticky="top",
)

# layout1 = html.Div(
#     style={'backgroundColor': colors['background']},
#     children=[
#         html.H1(
#             children='Hello Dash',
#             style={
#                 'textAlign': 'center',
#                 'color': colors['text']
#             }
#         ),
#         html.Div(children='Dash: A web application framework for Python.',
#             style={
#                 'textAlign': 'center',
#                 'color': colors['text']
#             }
#         ),
#         dcc.Graph(
#             id='Graph1',
#             figure={
#                 'data': [
#                     {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar',
#                       'name': 'SF'},
#                     {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name':
#                       u'Montréal'},
#                 ],
#                 'layout': {
#                     'plot_bgcolor': colors['background'],
#                     'paper_bgcolor': colors['background'],
#                     'font': {
#                         'color': colors['text']
#                     }
#                 }
#             }
#         )
#     ]
# )
