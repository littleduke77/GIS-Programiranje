from shapely.geometry import Polygon, Point
import geopandas as gpd
import matplotlib.pyplot as plt

# Definisanje geometrije za poligon i tačke
polygon_geom = Polygon([(-20, -20), (-20, 20), (20, 20), (20, -20)])
point_geom = [Point(-10, -10), Point(0, 0), Point(10, 10)]

# Kreiranje GeoDataFrame-a za poligon i tačke, sa CRS (Koordinatnim sistemom)
polygon_gdf = gpd.GeoDataFrame({'Okrug': ['Raski']}, geometry=[polygon_geom], crs="EPSG:6316")
points_gdf = gpd.GeoDataFrame({'name': ['Point 1', 'Point 2', 'Point 3']}, geometry=point_geom, crs="EPSG:6316")

# Učitavanje shapefile-a za prvu mapu
mapa = gpd.read_file('Okruzi SRB.shp')

# Filtriranje poligona na osnovu kolone 'okrug' koja ima vrednost 'Raski'
highlighted_polygon = mapa[mapa['Okrug'] == 'Raski']

# Prikaz prve mape na kojoj se vidi polozaj raskog okruga
fig, ax = plt.subplots(figsize=(10, 10))
mapa.plot(ax=ax, color='orange')
highlighted_polygon.plot(ax=ax, color='lightgray', edgecolor='black')  # Istaknuti poligon

# Isticanje poligona koji pripada okrugu 'Raski'
highlighted_polygon.plot(ax=ax, color='red', edgecolor='black')

plt.title("Положај Рашког округа")
plt.show()

# Učitavanje shapefile-a sa tačkama za drugu mapu
manastiri = gpd.read_file('ManastiriPython.shp')

# Kombinovani prikaz obe mape (osnovna mapa i tačke)
fig, ax = plt.subplots(figsize=(10, 10))
highlighted_polygon.plot(ax=ax, color='lightgray', edgecolor='black')  # Istaknuti poligon
manastiri.plot(ax=ax, marker='o', color='red', markersize=5)  # Dodavanje tačaka
plt.title("Положаји манастира у Рашком округу")
plt.show()

# Sačuvaj kartu sa tačkama i istaknutim poligonom
output_path = 'Polozaj manastira.jpg'
fig.savefig(output_path, dpi=300)

print(f"Карта је сачувана као {output_path}")

