import pandas as pd
import geopandas as gpd
from pathlib import Path

BASE = Path(r"C:/Users/caetanoronan/OneDrive - UFSC/Área de Trabalho/Olokun")
CSV_PATH = BASE / "dados" / "brutos" / "Análise - Tabela da lista das escolas - Detalhado.csv"
MUN_CSV = BASE / "dados" / "processados" / "municipios_grande_florianopolis.csv"
OUT = BASE / "site" / "data" / "escolas_olokun.geojson"

# Load schools CSV
escolas = pd.read_csv(CSV_PATH, dtype=str)

# Normalize columns
escolas.columns = [c.strip() for c in escolas.columns]

# Filter UF = SC
escolas = escolas[escolas["UF"].str.upper() == "SC"].copy()

# Load Grande Florianópolis municipalities
mun_df = pd.read_csv(MUN_CSV, dtype=str)
municipios_grande = set(mun_df["NM_MUN"].str.strip().str.upper())

# Filter to Grande Florianópolis
escolas["Município"] = escolas["Município"].astype(str).str.strip()
escolas = escolas[escolas["Município"].str.upper().isin(municipios_grande)].copy()

# Drop rows without coordinates
escolas["Latitude"] = pd.to_numeric(escolas["Latitude"], errors="coerce")
escolas["Longitude"] = pd.to_numeric(escolas["Longitude"], errors="coerce")
escolas = escolas.dropna(subset=["Latitude", "Longitude"]).copy()

# Build GeoDataFrame
geometry = gpd.points_from_xy(escolas["Longitude"], escolas["Latitude"], crs="EPSG:4326")
gdf = gpd.GeoDataFrame(escolas, geometry=geometry)

# Keep relevant columns
keep_cols = [
    "Escola",
    "Código INEP",
    "UF",
    "Município",
    "Categoria Administrativa",
    "Dependência Administrativa",
    "Categoria Escola Privada",
    "Endereço",
    "Localização",
    "Porte da Escola",
    "Etapas e Modalidade de Ensino Oferecidas",
    "Latitude",
    "Longitude",
]
keep_cols = [c for c in keep_cols if c in gdf.columns] + ["geometry"]

out_gdf = gdf[keep_cols].copy()
out_gdf.to_file(OUT, driver="GeoJSON")

print(f"Escolas exportadas: {len(out_gdf)} -> {OUT}")
