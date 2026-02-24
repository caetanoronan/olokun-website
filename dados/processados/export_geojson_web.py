import geopandas as gpd
from pathlib import Path

BASE = Path(r"c:/Users/caetanoronan/OneDrive - UFSC/Área de Trabalho/Olokun")
PROCESSADOS = BASE / "dados" / "processados"
WEB = BASE / "site" / "data"
WEB.mkdir(parents=True, exist_ok=True)

files = [
    ("municipio_florianopolis.gpkg", "municipio_florianopolis", "municipio_florianopolis.geojson"),
    ("municipios_grande_florianopolis.gpkg", "municipios_grande_florianopolis", "municipios_grande_florianopolis.geojson"),
    ("setores_florianopolis.gpkg", "setores_florianopolis", "setores_florianopolis.geojson"),
]

for gpkg_name, layer, out_name in files:
    gpkg_path = PROCESSADOS / gpkg_name
    if not gpkg_path.exists():
        print(f"Arquivo não encontrado: {gpkg_path}")
        continue
    gdf = gpd.read_file(gpkg_path, layer=layer)
    gdf = gdf.to_crs(4326)
    out_path = WEB / out_name
    gdf.to_file(out_path, driver="GeoJSON")
    print(f"Exportado: {out_path}")
