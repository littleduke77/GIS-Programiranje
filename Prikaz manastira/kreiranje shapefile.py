import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

# Učitavanje .txt fajla pomoću pandas (assumed structure: latitude, longitude)
# Moguće je menjati način razdvajanja kolona (delimeter = npr. whitespace, comma)
df = pd.read_csv('Manastiri.txt', delimiter=',', names=['longitude', 'latitude'])

# Kreira geometrijske kolone pomoću Shapely
df['geometrija'] = df.apply(lambda row: Point(row['longitude'], row['latitude']), axis=1)

# Pretvaranje pandas DataFrame u GeoDataFrame
gdf = gpd.GeoDataFrame(df, geometry='geometrija')

# Postavljanje u koordinatni sistem(CRS)
gdf.set_crs(epsg=6316, inplace=True)

# Ispisivanje GeoDataFrame u shapefile
gdf.to_file('ManastiriPython.shp', driver='ESRI Shapefile')

print("Shapefile kreiran uspesno!")