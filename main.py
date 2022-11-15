import pandas as pd
from time import sleep
import plotly.graph_objs as go

ships = pd.read_csv('AISDaily.csv', sep=';')
ships['line'] = ships.mmsi.apply(
    lambda x: str(x)) + ships.vessel_name \
    + ships.ts_pos_utc
ships['color'] = ships.mmsi.apply(
    lambda x: 'blue' if x == 273316240 
    else 'red') 


fig = go.Figure(go.Scattermapbox(
    lat=ships['latitude'],
    lon=ships['longitude'],
    text=ships['line'],
    mode='markers',
    marker=go.scattermapbox.Marker(
        size=10,
        color =  ships['color'],
        colorscale = 'RdYlGn_r',
        showscale=True,
        symbol = 'circle'),
    ))

map_center = go.layout.mapbox.Center(
    lat=(ships['latitude'].max()+ships['latitude'].min())/2,
    lon=(ships['longitude'].max()+ships['longitude'].min())/2)


fig.update_layout(mapbox_style="stamen-terrain", 
                  mapbox_zoom=3, 
                  mapbox_center = map_center,
                  margin={"r":0,"t":0,"l":0,"b":0})


if __name__ == '__main__':
    fig.show()
