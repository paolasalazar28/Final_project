
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout=html.Div(children=[

    html.Div(dcc.Input(id="exponent",value="3",type="number"))
    ,html.Div(id="result")

])

@app.callback(
    Output(component_id="result",component_property="children")
    ,Input(component_id="exponent",component_property="value")
  )



def Inpout (owl):
    return f"You will raise 2 to the {owl} power = {2**float(owl)}"

app.run_server(debug=True)
