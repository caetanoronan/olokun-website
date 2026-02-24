import geopandas as gpd
from pathlib import Path
import pyogrio
import unicodedata


def normalize_text(value: str) -> str:
    if value is None:
        return ""
    text = str(value)
    text = unicodedata.normalize("NFKD", text)
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    return text.upper().strip()

BASE = Path(r"c:/Users/caetanoronan/OneDrive - UFSC/Área de Trabalho/Olokun")
BRUTOS = BASE / "dados" / "brutos" / "Metadados"
PROCESSADOS = BASE / "dados" / "processados"
PROCESSADOS.mkdir(parents=True, exist_ok=True)

municipios_path = BRUTOS / "SC_Municipios_2024" / "SC_Municipios_2024.shp"
rg_imediatas_path = BRUTOS / "SC_RG_Imediatas_2024" / "SC_RG_Imediatas_2024.shp"
setores_gpkg = BRUTOS / "SC_setores_CD2022.gpkg"

# Read base layers
municipios = gpd.read_file(municipios_path)
rg_imediatas = gpd.read_file(rg_imediatas_path)

# Normalize name column detection
name_cols = [c for c in municipios.columns if c.lower() in {"nm_mun", "nome", "nm_municip", "municipio", "nome_mun", "nm_mun_2024"}]
if not name_cols:
    # fallback: choose first object column
    name_cols = [c for c in municipios.columns if municipios[c].dtype == object]

mun_name_col = name_cols[0]

# Florianópolis municipality
florianopolis = municipios[municipios[mun_name_col].apply(normalize_text) == "FLORIANOPOLIS"].copy()

# Grande Florianópolis by RG Imediata (intersect)
rg_name_cols = [c for c in rg_imediatas.columns if c.lower() in {"nm_rgi", "nome", "nm_rg", "nm_rg_im", "nm_imedi", "rg_imediata"}]
if not rg_name_cols:
    rg_name_cols = [c for c in rg_imediatas.columns if rg_imediatas[c].dtype == object]

rg_name_col = rg_name_cols[0]
rg_floripa = rg_imediatas[rg_imediatas[rg_name_col].apply(normalize_text).str.contains("FLORIANOPOLIS")].copy()

# Ensure same CRS
if florianopolis.crs != rg_floripa.crs:
    rg_floripa = rg_floripa.to_crs(florianopolis.crs)

# Intersect municipalities with RG Imediata Florianópolis
rg_union = rg_floripa.geometry.unary_union
municipios_grande = municipios[municipios.geometry.intersects(rg_union)].copy()

# Save municipalities
florianopolis.to_file(PROCESSADOS / "municipio_florianopolis.gpkg", layer="municipio_florianopolis", driver="GPKG")
municipios_grande.to_file(PROCESSADOS / "municipios_grande_florianopolis.gpkg", layer="municipios_grande_florianopolis", driver="GPKG")

# Read setores layer from gpkg
layers = [layer[0] for layer in pyogrio.list_layers(setores_gpkg)]
if len(layers) == 1:
    setores_layer = layers[0]
else:
    # pick layer with 'setor' in name
    setor_candidates = [l for l in layers if "setor" in l.lower()]
    setores_layer = setor_candidates[0] if setor_candidates else layers[0]

setores = gpd.read_file(setores_gpkg, layer=setores_layer)

# Ensure CRS matches
if setores.crs != florianopolis.crs:
    setores = setores.to_crs(florianopolis.crs)

# Clip setores
setores_floripa = gpd.overlay(setores, florianopolis, how="intersection")
setores_grande = gpd.overlay(setores, municipios_grande, how="intersection")

# Save setores
setores_floripa.to_file(PROCESSADOS / "setores_florianopolis.gpkg", layer="setores_florianopolis", driver="GPKG")
setores_grande.to_file(PROCESSADOS / "setores_grande_florianopolis.gpkg", layer="setores_grande_florianopolis", driver="GPKG")

print("Recortes concluídos:")
print("- municipio_florianopolis.gpkg")
print("- municipios_grande_florianopolis.gpkg")
print("- setores_florianopolis.gpkg")
print("- setores_grande_florianopolis.gpkg")
