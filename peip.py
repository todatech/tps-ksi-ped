import dash

import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
# import dash_table as dt

from app import ds

from layouts import navbar


def App():

    cols = ['MANOEUVER', 'DRIVACT', 'DRIVCOND', 'INJURY']
    input_list = {}
    for i in cols:
        a = ds.get_column_dictionary(i)
        new_item = {i: a}
        input_list.update(new_item.copy())

    age_list = ds.age_list_index

    body = dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.H2(
                                children="Pedestrian Injury Predictor",
                                style={
                                    'textAlign': 'center'
                                }
                            ),
                            html.P(
                                """\
                                Please provide the following information to predict the severity of the injurer at the scene."""
                            ),
                            html.Div(
                                [
                                    dcc.Dropdown(
                                        id='debug-show-hide',
                                        options=[
                                            {'label': 'Debug - Show element',
                                                'value': 'on'},
                                            {'label': 'Debug - Hide element',
                                                'value': 'off'}
                                        ],
                                        value='off'
                                    ),
                                ],
                                # for debugging 'block' = enable, 'none' = disable
                                style={'display': 'enable'}
                            )
                        ], className="m-4",
                    ),
                ],
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.H5("1. Apparent Driver Action"),
                            dcc.Dropdown(
                                id='lab1app-dropdown-1',
                                options=[{'label': v, 'value': k}
                                        for (k, v) in input_list['DRIVACT'].items()],
                            ),
                            html.Div(
                                [
                                    html.Div("Placeholder", id='lab1app-display-value-1', )
                                ], style={'display': 'block'},
                            ), 
                        ],
                        md=6,
                    ),
                    dbc.Col(
                        [
                            html.H5("2. Driver Condition"),
                            dcc.Dropdown(
                                id='lab1app-dropdown-2',
                                options=[{'label': v, 'value': k}
                                        for (k, v) in input_list['DRIVCOND'].items()],
                            ),
                            html.Div(
                                [
                                    html.Div("Placeholder", id='lab1app-display-value-2', )
                                ], style={'display': 'block'},
                            ),
                        ],
                        md=6,
                    ),
                ],  className="m-4",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.H5("3. Vehicle Manouever"),
                            dcc.Dropdown(
                                id='lab1app-dropdown-3',
                                options=[{'label': v, 'value': k}
                                        for (k, v) in input_list['MANOEUVER'].items()],
                            ),
                            html.Div(
                                [
                                    html.Div("Placeholder", id='lab1app-display-value-3'),
                                ], style={'display': 'block'}
                            ),
                        ],
                        md=6,
                    ),
                    dbc.Col(
                        [
                            html.H5("4. Age of the Injurer"),
                            dcc.Dropdown(
                                id='lab1app-dropdown-4',
                                options=[{'label': v, 'value': k}
                                        for (k, v) in age_list.items()],
                            ),                            
                            html.Div(
                                [
                                    html.Div('Placeholder', id='lab1app-display-value-4'),
                                ], style={'display': 'block'}
                            ),
                        ],
                        md=6,
                    ),
                ], className="m-4",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dbc.Button(
                                "Get Outcome", id="lab1app-button-1", color="default",
                                style={'float': 'right'}
                            ),
                            html.Div(
                                [
                                    html.Div("Placeholder", id='lab1app-display-value-5', )
                                ], style={'display': 'block'},
                            ),
                        ]
                    ),
                ], className="m-4",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.H4(
                                children="Possible Outcome",
                            ),
                            html.Div(
                                [
                                    html.Div("Placeholder", id='lab1app-outcome', )
                                ], style={'display': 'block'},
                            ),
                            # dt.DataTable(
                            #     id='table',
                            #     #columns=[{"name": i, "id": i} for i in df.columns],
                            #     # data=df.to_dict('records'),
                            #     data=None,
                            # ),
                        ]
                    ),
                ], className="m-4",
            ),
        ], className="mt-4",
    )

    # colors = {
    #     'background': '#111111',
    #     'text': '#7FDBFF'
    # }

    layout = html.Div([
        navbar,
        body
    ])
    return layout


if __name__ == "__main__":
    app = dash.Dash(__name__, external_stylesheets=[dbc.themes.UNITED])
    app.layout = App()
    app.run_server()
