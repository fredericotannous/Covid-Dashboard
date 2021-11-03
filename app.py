import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd

data = pd.read_csv('novo_por_data_de_aplicacao.csv')

external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
        "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Vacinação no RS"

app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.P(children='💉', className='header-emoji'),
                html.H1(
                    children='Vacinação no RS', className='header-title'
                ),
                html.P(children='Acompanhe a evolução da vacinação no Rio Grande do Sul!', className='header-description',
                  ),        
            ],
            className='header',
        ),
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(
                        id='grafico-1',
                        config={'displayModeBar': False},
                        figure={
                            'data': [
                                {
                                    'x': data['Data'],
                                    'y': data['pelo menos uma dose'],
                                    'type': 'lines',
                                    
                                },
                            ],
                            'layout': {
                                'title': {
                                    'text': 'População com pelo menos uma dose da vacina',
                                    'x:': 0.05,
                                    'xanchor': 'left', 
                                },
                                'xaxis': {'fixedrange': True},
                                'yaxis': {
                                    'ticksuffix': '%',
                                    'fixedrange': True,
                                },
                                'colorway': ['#17B897'],
                            },
                        },
                    ),                    
                    className='card',
                ),
                html.Div(
                    children=dcc.Graph(
                        id='grafico-2',
                        config={'displayModeBar': False},
                        figure={
                            'data': [
                                {
                                    'x': data['Data'],
                                    'y': data['esquema vacinal completo'],
                                    'type': 'lines',
                                
                                },
                            ],
                            'layout': {
                                'title': {
                                    'text': 'População com esquema vacinal completo',
                                    'x': 0.05,
                                    'xanchor': 'left',
                                },
                                'xaxis': {'fixedrange': True},
                                'yaxis': {'ticksuffix': '%', 'fixedrange': True},
                                'colorway': ['#E12D39'],
                            },
                        },
                    ),
                    className='card',
                ),
            ],
            className='wrapper',
        ),          
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)