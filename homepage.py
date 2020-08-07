import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from layouts import navbar
from app import app


body = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        # html.Div(
                        #     [
                        #         html.H1("Prediction of the Level of Injury to Pedestrians in a possible vehicle collision"),
                        #     ], style={'textAlign': 'center'}

                        # ),
                        # html.Br(),
                        html.Div(
                            [
                                html.Img(src='/assets/school_logo.png'),
                            ], style={'textAlign': 'center', 'vertical-align': 'middle'}

                        )
                    ]
                ),
                dbc.Col(
                    [
                        html.Div(
                            [
                                html.A(
                                    html.H4("Pedestrian Injury Predictor"),
                                    href='/pip'
                                ),
                                html.P(
                                    """\
                                    This app predicts the severity of injury of pedestrian for any given traffic collision.
                                    By providing the system with 1. Apparent Drivers Action, 2) Drivers Condition, 3) 
                                    Vehicle Manouever, 4) Age of the injured person, the Machine Learning Algorithm can
                                    predict the severity of injury with an prediction accurary of 80% and above. The idea
                                    is to help dispatch teams to quickly prioritize actions based on the given situations. 
                                    
                                    The purpose of this app is to demonstrate the possiblity of leveraging big data in 
                                    this scenerio. However, this app is not fully tested for any real use cases. 
                                    """
                                ),
                            ],
                            style={'display': 'block', 'vertical-align': 'bottom'},
                        ),
                    ],
                    md=6,
                ),
            ]
        )
    ], className="mt-4",
)

def App():
    layout = html.Div([
        navbar,
        body
    ])
    return layout


if __name__ == "__main__":
    app.run_server()
