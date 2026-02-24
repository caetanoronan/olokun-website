import geopandas as gpd
import json
from pathlib import Path
from shapely.ops import voronoi_diagram

BASE = Path(r"C:/Users/caetanoronan/OneDrive - UFSC/Área de Trabalho/Olokun")
BRUTOS = BASE / "dados" / "brutos" / "Metadados"
PROCESSADOS = BASE / "dados" / "processados"
SITE = BASE / "site" / "data"
SITE.mkdir(parents=True, exist_ok=True)

# Camadas base
municipio = gpd.read_file(PROCESSADOS / "municipio_florianopolis.gpkg", layer="municipio_florianopolis")
municipio = municipio.to_crs(4674)

grande_path = PROCESSADOS / "municipios_grande_florianopolis.gpkg"
if grande_path.exists():
    municipios_grande = gpd.read_file(grande_path, layer="municipios_grande_florianopolis").to_crs(4674)
    area_clip = municipios_grande
else:
    area_clip = municipio

# Fonte BC25 (SC)
edf_ensino_p = BRUTOS / "bc25_sc_shapefile_2020-10-01" / "edf_edif_ensino_p.shp"

# Leitura (prioriza escolas importadas do CSV)
escolas_geojson = SITE / "escolas_olokun.geojson"
if escolas_geojson.exists():
    escolas = gpd.read_file(escolas_geojson)
else:
    escolas = gpd.read_file(edf_ensino_p)

# Recorte por Florianópolis (apenas se necessário)
if "geometry" in escolas.columns:
    escolas = escolas.to_crs(area_clip.crs)
    escolas = gpd.sjoin(escolas, area_clip, predicate="intersects", how="inner").drop(columns=["index_right"], errors="ignore")


# Exportar escolas (pontos)
escolas = escolas.to_crs(4326)
escolas.to_file(SITE / "escolas_olokun.geojson", driver="GeoJSON")

# Projeção métrica para buffers/voronoi
escolas_proj = escolas.to_crs(31982)
mun_proj = area_clip.to_crs(31982)

# Cobertura 3km (Escolas)
cobertura_escolas = escolas_proj.copy()
cobertura_escolas["geometry"] = cobertura_escolas.geometry.buffer(3000)
cobertura_escolas = cobertura_escolas.to_crs(4326)
cobertura_escolas.to_file(SITE / "cobertura_3km_escolas.geojson", driver="GeoJSON")

def export_voronoi(points_proj, out_name: str) -> None:
    try:
        if len(points_proj) > 2:
            diagram = voronoi_diagram(points_proj.unary_union)
            vor_gdf = gpd.GeoDataFrame(geometry=list(diagram.geoms), crs=points_proj.crs)
            vor_gdf = gpd.overlay(vor_gdf, mun_proj, how="intersection")
            vor_gdf = vor_gdf.to_crs(4326)
            vor_gdf.to_file(SITE / out_name, driver="GeoJSON")
        else:
            gpd.GeoDataFrame(geometry=[], crs=4326).to_file(SITE / out_name, driver="GeoJSON")
    except Exception:
        gpd.GeoDataFrame(geometry=[], crs=4326).to_file(SITE / out_name, driver="GeoJSON")

# Voronoi (Escolas)
export_voronoi(escolas_proj.geometry, "voronoi_escolas.geojson")

# Heatmap points (Escolas)
heat_escolas = []
for geom in escolas.geometry:
    if geom is None or geom.is_empty:
        continue
    heat_escolas.append([geom.y, geom.x, 1.0])

(SITE / "heat_points_escolas.json").write_text(json.dumps(heat_escolas, ensure_ascii=False, indent=2), encoding="utf-8")

print(f"Escolas: {len(escolas)} | Heat Escolas: {len(heat_escolas)}")
