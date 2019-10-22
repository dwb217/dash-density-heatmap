import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
import pandas as pd
import pickle

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title='iraq protests'

########## Define the data
df = pd.read_csv('resources/iraq_protests.csv')

########## Define the figure

fig = go.Figure(go.Densitymapbox(lat=df['latitude'], lon=df['longitude'], z=df['fatalities'], radius=10))
fig.update_layout(mapbox_style="stamen-terrain",
                  mapbox_center_lon=44.4213,
                  mapbox_center_lat=33.3248,
                  mapbox_zoom=3,
                 )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

########### Set up the layout

app.layout = html.Div(children=[
    html.H1('Iraq Protests'),
    html.Div([
        dcc.Graph(id='figure-1', figure=fig),
        html.A('Code on Github', href='https://github.com/dwb217/dash-density-heatmap'),
        html.Br(),
        html.A('Source:', href='https://plot.ly/python/mapbox-density-heatmaps')
    ])
])


############ Execute the app
if __name__ == '__main__':
    app.run_server(debug=True)
