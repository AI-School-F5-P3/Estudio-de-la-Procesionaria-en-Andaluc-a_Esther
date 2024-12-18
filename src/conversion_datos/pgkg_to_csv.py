import geopandas as gpd
import fiona

# Ruta al archivo GeoPackage
gpkg_path = "C:/Users/Administrator/Desktop/Proyecto Personal_Estudio de la Procesionaria/datos extraidos/094-dera-12-servicios-gpkg.gpkg"

# Listar las capas disponibles
print("Capas disponibles en el GeoPackage:")
print(fiona.listlayers(gpkg_path))

# Cargar el archivo GeoPackage
layer_name = "T12_04_Farmacia"  # Cambia esto al nombre de la capa en el GeoPackage
gdf = gpd.read_file(gpkg_path, layer=layer_name)

# Convertir el GeoDataFrame a CSV con codificación UTF-8
csv_path = "C:/Users/Administrator/Desktop/Proyecto Personal_Estudio de la Procesionaria/dataset/farmacia.csv"
gdf.to_csv(csv_path, index=False, encoding='utf-8')

print(f"Archivo CSV guardado en: {csv_path}")

