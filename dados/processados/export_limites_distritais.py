import geopandas as gpd
import os
import json

# Paths
processados_dir = os.path.dirname(__file__)
gpkg_file = os.path.join(processados_dir, 'municipio_florianopolis.gpkg')
municipios_file = os.path.join(processados_dir, 'municipios_grande_florianopolis.gpkg')
web_data_dir = os.path.normpath(os.path.join(processados_dir, '..', '..', 'site', 'data'))
os.makedirs(web_data_dir, exist_ok=True)

print(f"Lendo: {gpkg_file}")
# Read Florianópolis boundaries
if os.path.exists(gpkg_file):
    gdf_flor = gpd.read_file(gpkg_file)
    print(f"Colunas disponíveis: {gdf_flor.columns.tolist()}")
    print(f"Dados de Florianópolis carregados: {len(gdf_flor)} features")
    
    # Ensure EPSG:4326 (WGS84)
    if gdf_flor.crs != 'EPSG:4326':
        gdf_flor = gdf_flor.to_crs('EPSG:4326')
    
    # Export to GeoJSON
    output_flor = os.path.join(web_data_dir, 'florianopolis_limite.geojson')
    gdf_flor.to_file(output_flor, driver='GeoJSON')
    print(f"✓ Exportado: {output_flor}")
else:
    print(f"⚠ Arquivo não encontrado: {gpkg_file}")

# Read Grande Florianópolis boundaries
print(f"\nLendo: {municipios_file}")
if os.path.exists(municipios_file):
    gdf_grande = gpd.read_file(municipios_file)
    print(f"Colunas disponíveis: {gdf_grande.columns.tolist()}")
    print(f"Dados de Grande Florianópolis carregados: {len(gdf_grande)} features")
    
    # Ensure EPSG:4326
    if gdf_grande.crs != 'EPSG:4326':
        gdf_grande = gdf_grande.to_crs('EPSG:4326')
    
    # Export to GeoJSON
    output_grande = os.path.join(web_data_dir, 'grande_florianopolis_limites.geojson')
    gdf_grande.to_file(output_grande, driver='GeoJSON')
    print(f"✓ Exportado: {output_grande}")
else:
    print(f"⚠ Arquivo não encontrado: {municipios_file}")

print("\n✓ Limites distritais exportados com sucesso!")
