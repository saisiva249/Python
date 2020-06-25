#https://python-visualization.github.io/folium/quickstart.html
#for creating maps we use the module folium we can isntall using 
#python -m pip install folium
# The default tiles are set to OpenStreetMap, but Stamen Terrain, 
# Stamen Toner, Mapbox Bright, and Mapbox Control Room, and many others tiles are built in.
import folium as foli

ftGroup = foli.FeatureGroup(name="Sample Map")

ch = ftGroup.add_child(foli.Marker(location=[27,78],popup='hello',icon=foli.Icon(color='blue')))

map = foli.Map(tiles='Stamen Terrain').add_child(ch)

map.save('index.html')
