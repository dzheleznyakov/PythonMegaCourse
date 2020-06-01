import folium
import pandas

f_map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")

fg_volcanoes = folium.FeatureGroup(name='Volcanoes')

data = pandas.read_csv('data/Volcanoes.txt')
lat = list(data['LAT'])
lon = list(data['LON'])
names = list(data['NAME'])
elev = list(data['ELEV'])

html = """<h4>Volcano information:</h4>
Name: %s
<br />
Height: %s m
"""


def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif elevation < 3000:
        return 'orange'
    return 'red'


for lt, ln, name, el in zip(lat, lon, names, elev):
    iframe = folium.IFrame(html=html % (name, str(el)), width=200, height=150)
    popup = folium.Popup(iframe)
    icon = folium.Icon(color=color_producer(el))
    location = [lt, ln]
    fg_volcanoes.add_child(folium.CircleMarker(
        location=location,
        radius=6,
        color='grey',
        popup=popup,
        fill_color=color_producer(el),
        fill_opacity=0.7))

fg_population = folium.FeatureGroup(name='Population')
geo_json_data = open('data/world.json', 'r', encoding='utf-8-sig').read()
fg_population.add_child(folium.GeoJson(
    data=geo_json_data,
    style_function=lambda x: {'fillColor':
                                  'green' if x['properties']['POP2005'] < 10000000
                                  else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
                                  else 'red'}))

f_map.add_child(fg_volcanoes)
f_map.add_child(fg_population)
f_map.add_child(folium.LayerControl())

f_map.save("Map1.html")
