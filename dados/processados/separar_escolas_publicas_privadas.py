import geopandas as gpd
from pathlib import Path

BASE = Path(r"C:/Users/caetanoronan/OneDrive - UFSC/Área de Trabalho/Olokun")
INPUT = BASE / "site" / "data" / "escolas_olokun.geojson"
OUT_PUBLICAS = BASE / "site" / "data" / "escolas_publicas.geojson"
OUT_PRIVADAS = BASE / "site" / "data" / "escolas_privadas.geojson"

# Carregar todas as escolas
escolas = gpd.read_file(INPUT)

# Separar por Dependência Administrativa
# Públicas: Municipal, Estadual, Federal
# Privadas: Privada
publicas = escolas[escolas["Dependência Administrativa"].isin(["Municipal", "Estadual", "Federal"])].copy()
privadas = escolas[escolas["Dependência Administrativa"] == "Privada"].copy()

# Exportar
publicas.to_file(OUT_PUBLICAS, driver="GeoJSON")
privadas.to_file(OUT_PRIVADAS, driver="GeoJSON")

print(f"✓ Escolas Públicas: {len(publicas)} -> {OUT_PUBLICAS.name}")
print(f"  - Municipal: {len(publicas[publicas['Dependência Administrativa'] == 'Municipal'])}")
print(f"  - Estadual: {len(publicas[publicas['Dependência Administrativa'] == 'Estadual'])}")
print(f"  - Federal: {len(publicas[publicas['Dependência Administrativa'] == 'Federal'])}")
print(f"\n✓ Escolas Privadas: {len(privadas)} -> {OUT_PRIVADAS.name}")
print(f"\nTotal: {len(escolas)} escolas")
