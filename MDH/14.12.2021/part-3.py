import pandas as pd
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px

df=pd.read_csv("auto-mpg.csv")

print(df.head())

app=dash.Dash(__name__)

grafico=px.scatter(df,x="displacement",y="weight",trendline="ols")


app.layout=html.Div([
    html.H1("Displacements vs Weight")
    ,html.Img(src="https://i.pinimg.com/originals/79/a2/a2/79a2a25fce3ef30bd85a4c3d155845d5.jpg")
    ,dcc.Graph(figure=grafico)


])

app.run_server(debug=True)