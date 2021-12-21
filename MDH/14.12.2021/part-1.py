# Create a HTML 
import dash
from dash import html

app=dash.Dash("owls")

app.layout=html.Div([

    html.Img(src="https://www.dogalize.com/wp-content/uploads/2017/06/La-sverminazione-e-la-pulizia-del-cucciolo-del-cane-2-800x400-800x400.jpg")
    ,html.H1("Pao,Edmundo,Ruben,Seth",style={"color":"red"})
    ,html.P("Todos trabajamos en DEACERO y estamos en el curso de Data Translator en DHM",style={"color":"blue","border":" 20px solid black"})
    

])

app.run_server(debug=True)
