import geopandas as gpd
import json
from pathlib import Path
import pandas as pd

base = Path(r"C:/Users/caetanoronan/OneDrive - UFSC/Área de Trabalho/Olokun")


def export_resumo(gpkg_name: str, layer: str, out_name: str, fallback_municipio: str) -> None:
    gdf = gpd.read_file(base / "dados" / "processados" / gpkg_name, layer=layer)
    name_col = "NM_BAIRRO" if "NM_BAIRRO" in gdf.columns else ("NM_NU" if "NM_NU" in gdf.columns else "CD_SETOR")
    area_col = "AREA_KM2_1" if "AREA_KM2_1" in gdf.columns else None

    records = []
    for _, row in gdf.iterrows():
        nome = row.get(name_col)
        if pd.isna(nome):
            nome = None
        records.append(
            {
                "id": row.get("CD_SETOR"),
                "nome": nome or row.get("CD_SETOR"),
                "municipio": row.get("NM_MUN_1") or fallback_municipio,
                "area_km2": float(row.get(area_col)) if area_col and row.get(area_col) is not None else None,
                "score": 0,
            }
        )

    out = base / "site" / "data" / out_name
    out.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Exportado: {out} ({len(records)} registros)")


export_resumo("setores_florianopolis.gpkg", "setores_florianopolis", "setores_resumo.json", "Florianópolis")
export_resumo("setores_grande_florianopolis.gpkg", "setores_grande_florianopolis", "setores_resumo_grande.json", "Grande Florianópolis")
