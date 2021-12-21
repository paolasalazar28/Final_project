import pandas as pd
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px

df=pd.read_csv("auto-mpg.csv")

#print(df["horsepower"].unique())

print(df[df["horsepower"]=="?"])

app=dash.Dash(__name__)


