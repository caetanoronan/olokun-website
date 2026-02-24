import os
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

BASE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.normpath(os.path.join(BASE_DIR, '..', 'data'))
IMAGES_DIR = os.path.join(BASE_DIR, 'assets', 'images')
os.makedirs(IMAGES_DIR, exist_ok=True)

PUBLIC_F = os.path.join(DATA_DIR, 'escolas_publicas.geojson')
PRIVATE_F = os.path.join(DATA_DIR, 'escolas_privadas.geojson')

# Read data
pub = gpd.read_file(PUBLIC_F) if os.path.exists(PUBLIC_F) else gpd.GeoDataFrame()
priv = gpd.read_file(PRIVATE_F) if os.path.exists(PRIVATE_F) else gpd.GeoDataFrame()

# Ensure columns exist
for df in (pub, priv):
    if 'Município' not in df.columns and 'Municipio' in df.columns:
        df['Município'] = df['Municipio']

n_pub = len(pub)
n_priv = len(priv)

# KPI figure
plt.figure(figsize=(8,2))
plt.axis('off')
plt.text(0.05, 0.6, 'Total de Escolas', fontsize=12, color='#374151')
plt.text(0.05, 0.15, str(n_pub + n_priv), fontsize=28, fontweight='bold', color='#111827')
plt.text(0.35, 0.6, 'Públicas', fontsize=12, color='#16a34a')
plt.text(0.35, 0.15, str(n_pub), fontsize=28, fontweight='bold', color='#16a34a')
plt.text(0.65, 0.6, 'Privadas', fontsize=12, color='#ea580c')
plt.text(0.65, 0.15, str(n_priv), fontsize=28, fontweight='bold', color='#ea580c')
plt.tight_layout()
kpif = os.path.join(IMAGES_DIR, 'kpis.png')
plt.savefig(kpif, dpi=150, bbox_inches='tight')
plt.close()

# Combine and top municipalities
combined = pd.concat([pub, priv], ignore_index=True, sort=False)
if 'Município' in combined.columns:
    muni_counts = combined.groupby('Município').size().sort_values(ascending=False).head(10)
else:
    muni_counts = pd.Series(dtype=int)

# Municipality barplot
if not muni_counts.empty:
    plt.figure(figsize=(8,4))
    sns.set_style('whitegrid')
    sns.barplot(x=muni_counts.values, y=muni_counts.index, palette='viridis')
    plt.xlabel('Número de escolas')
    plt.title('Top 10 Municípios por número de escolas')
    plt.tight_layout()
    muni_f = os.path.join(IMAGES_DIR, 'municipios_top10.png')
    plt.savefig(muni_f, dpi=150)
    plt.close()
else:
    # create empty placeholder
    plt.figure(figsize=(8,4))
    plt.text(0.5,0.5,'Sem dados de município',ha='center',va='center')
    muni_f = os.path.join(IMAGES_DIR, 'municipios_top10.png')
    plt.savefig(muni_f, dpi=150)
    plt.close()

# Distribution by administrative dependency (public/private combined)
if 'Dependência Administrativa' in combined.columns or 'Dependencia Administrativa' in combined.columns:
    dep_col = 'Dependência Administrativa' if 'Dependência Administrativa' in combined.columns else 'Dependencia Administrativa'
    dep_counts = combined.groupby(dep_col).size().sort_values(ascending=False)
    plt.figure(figsize=(6,6))
    dep_counts.plot.pie(autopct='%1.1f%%', startangle=140, cmap='Set2')
    plt.ylabel('')
    plt.title('Distribuição por dependência administrativa')
    plt.tight_layout()
    dep_f = os.path.join(IMAGES_DIR, 'dependencia_pie.png')
    plt.savefig(dep_f, dpi=150)
    plt.close()
else:
    dep_f = None

print('Images written:')
print(kpif)
print(muni_f)
if dep_f:
    print(dep_f)
else:
    print('No dependência chart (missing column)')
