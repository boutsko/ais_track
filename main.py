import pandas as pd
from time import sleep
import plotly.graph_objs as go

token = open(".mapbox_token").read() 

ships = pd.read_csv('AISDaily.csv', sep=';')
#chosing one ship with mmsi 273316240
ship = ships[ships['mmsi'] == 273316240]
# setting text near symbol
ship['line'] = ship.mmsi.apply(
    lambda x: str(x)) + ship.vessel_name \
    + ships.ts_pos_utc

fig = go.Figure(go.Scattermapbox(
    lat=ship['latitude'],
    lon=ship['longitude'],
    text=ship['line'],
    # +lines connects points
    mode='markers+lines',
    marker=go.scattermapbox.Marker(
        size=10,
        colorscale = 'RdYlGn_r',
        showscale=True,
        symbol = 'ferry'),
    ))

map_center = go.layout.mapbox.Center(
    lat=(ship
         ['latitude'].max()+ship['latitude'].min())/2,
    lon=(ship['longitude'].max()+ship['longitude'].min())/2)


fig.update_layout(
    mapbox = {
        'accesstoken': token,
        'style': "outdoors", 'zoom': 0.7},
    # mapbox_style="stamen-terrain", 
    mapbox_zoom=3, 
    mapbox_center = map_center,
    margin={"r":0,"t":0,"l":0,"b":0})


if __name__ == '__main__':
    fig.show()
