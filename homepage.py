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
                        html.Div(
                            [
                                html.H1("Advanced Methods of Data Analysis"),
                            ], style={'textAlign':'center'}

                        ),
                        html.Br(),
                        html.Div(
                            [
                                html.Img(src='/assets/school_logo.png'), 
                            ], style={ 'textAlign': 'center', 'vertical-align': 'middle' }

                        )
                    ]
                ),                
                dbc.Col(
                    [
                        html.A(
                            html.H4("Lab 1 - Movies Recommender Systems"),
                            href='/lab1'
                        ),
                        html.P(
                            """\
                            We are going to explore 4 different types of Recommender Systems. In this app, 
                            we are going to show how system perform tasks to recommend movies titles based 
                            on a series of users inputs, preferences, rating history using Big Data Analytics 
                            tools and techinques.
                            """
                        ),
                        html.Br(),
                        html.A(
                            html.H4("Lab 2 - Identifying Spam and Determining Sentiment in Text Messages"), 
                            href='/lab2'
                        ),
                        html.P(
                            """\
                            In the first part of this lab, we will be using text mining techniques to determine 
                            whether a message is a valid one or a spam. Next, we will then determine the sentiment
                            within the messages itself. Both problems fall under classification, but we use two 
                            different alogrithms to process them, 1.) SVM for spam identification and 2.) LSTM 
                            neural networks to analyze sentiment. """
                        ),
                        html.Br(),
                        html.A(
                            html.H4("Lab 3 - Time Series Analysis on Keywords from Google Trends"), 
                            href='/lab3'    
                        ),
                        html.P(
                            """\
                            In this lab, we are going to leverage on the real time data from the Google Trends API.
                            First, we will show you the search frequency of the keywords or phase of your choice. Then,
                            we will break down the time characteristics of this term into a graphical form that is easy
                            to digest."""
                        ),
                        html.Br(),
                        html.A(
                            html.H4("Settings"), 
                            href='/settings'    
                        ),
                        html.P(
                            """\
                            To load and unload some of the backend engines"""
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
