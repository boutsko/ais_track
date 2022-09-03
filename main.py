import pandas as pd
from time import sleep
import plotly.graph_objs as go

ships = pd.read_csv('AISDaily.csv', sep=';')
ships['line'] = ships.mmsi.apply(lambda x: str(x)) + ships.vessel_name + ships.ts_pos_utc

fig = go.Figure(go.Scattermapbox(
    lat=ships['latitude'],
    lon=ships['longitude'],
    text=ships['line'],
    # marker = {'color' : 'green'}, mode='markers+text',))
    mode='markers+text',
    marker=dict(
            size=3,
            # I want the color to be green if
            # lower_limit ≤ y ≤ upper_limit
            # else red
            color=(
                (ships.mmsi == '309224000') &
                (ships.mmsi == '273316240')
            ).astype('int'),
            colorscale=[[0, 'red'], [1, 'green']]
        )))


map_center = go.layout.mapbox.Center(lat=(ships['latitude'].max()+ships['latitude'].min())/2,
                                     lon=(ships['longitude'].max()+ships['longitude'].min())/2)


fig.update_layout(mapbox_style="open-street-map", mapbox_zoom=3, mapbox_center = map_center,
    margin={"r":0,"t":0,"l":0,"b":0})

if __name__ == '__main__':
    fig.show()
