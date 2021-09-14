import pprint
import pandas as pd
import dash
from dash import dcc
from dash import html

#load data
data = pd.read_csv('C:\\Users\\Frederico\\Desktop\\python\\covid_rs\\imunizacao.csv')
data2 = pd.read_csv('C:\\Users\\Frederico\\Desktop\\python\\covid_rs\\populacao_vacinavel.csv', delimiter =';')
#print(data.dtypes)
#print(data.describe())
##print(data2.dtypes)
#print(data2.describe())
#print(data2)

app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(children="Vaccines Covid Analytics",),
        html.P(
            children="Analyze how the population of RS"
            " is being vaccinated",
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data2["Data"],
                        "y": data2["pelo menos uma dose"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Esquema vacinal - pelo menos uma dose"},
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data2["Data"],
                        "y": data2["esquema vacinal completo"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Esquema vacinal completo"},
            },
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)