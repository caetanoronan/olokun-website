# 🌊 Instituto Olokun — Plataforma Territorial

Este repositório reúne os materiais web do Instituto Olokun para apresentação institucional, dashboard de estratégia territorial, mapa de resultados e mapas interativos de escolas.

## 🎯 Sobre o Projeto

O Instituto Olokun é uma organização dedicada à **preservação e conservação costeira** com foco em educação ambiental territorialmente ancorada e soluções orientadas por dados. Este projeto implementa uma plataforma web integrada para:

- 📊 **Dashboard territorial** com indicadores de alinhamento estratégico
- 🗺️ **Mapas interativos** de escolas, cobertura de serviços e resultados
- 🏤 **Apresentação institucional** com abas temáticas para diferentes públicos
- 📈 **Visualização de dados** geoespaciais em tempo real

---

## 🔗 Acessos Públicos (GitHub Pages)

**Apresentação Institucional:**
- URL: https://caetanoronan.github.io/olokun-website/olokun/index-instituicoes-tabs.html
- Contém 6 abas: Apresentação, Sobre o Programa, Projetos, Produtos & Serviços, Para Instituições, Contato

**Dashboards e Mapas:**
- Dashboard Territorial: https://caetanoronan.github.io/olokun-website/olokun/dashboard_olokun_tabs.html
- Dashboard Escolas: https://caetanoronan.github.io/olokun-website/olokun/dashboard_escolas.html
- Mapa de Resultados: https://caetanoronan.github.io/olokun-website/olokun/mapa_resultados.html
- Mapa de Escolas: https://caetanoronan.github.io/olokun-website/mapa_escolas.html

---

## 📂 Estrutura do Projeto

```
olokun-website/
├── README.md                          # Este arquivo
├── olokun/                            # 📦 Pasta publicada no GitHub Pages
│   ├── index-instituicoes-tabs.html  # Apresentação institucional (6 abas)
│   ├── dashboard_olokun_tabs.html    # Dashboard com indicadores estratégicos
│   ├── dashboard_escolas.html        # Dashboard com dados das escolas
│   ├── mapa_resultados.html          # Mapa interativo de resultados
│   ├── mapa_olokun.html              # Mapa alternativo
│   └── assets/                        # Recursos (CSS, JS, imagens)
│
├── dados/                             # 📊 Dados brutos e metadados
│   ├── brutos/                        # Dados originais (CSVs, shapefiles)
│   ├── processados/                   # GPKGs, GéoJSONs processados
│   ├── metadados/                     # Dicionários de variáveis, checklists
│   └── templates/                     # Templates de importação
│
├── gis/                               # 🗺️ Dados geoespaciais
│   └── Residuos_solidos_Olokun/       # Camadas SIG específicas
│
├── docs/                              # 📚 Documentação técnica
│   ├── GUIA_DE_USO.md                # Guide para usuários finais
│   ├── RESUMO_EXECUTIVO.md           # Resumo do projeto
│   ├── TRANSFORMACAO_PARA_ONG.md     # Guia de transformação operacional
│   └── [outros arquivos auxiliares]
│
├── gh-pages-temp/                     # 🔄 Área de trabalho (ramo gh-pages)
│   └── [versões em edição]
│
├── site/                              # 📁 Backup/sincronia com master
│   ├── olokun/                        # Cópia dos arquivos publicados
│   └── [estrutura similar a /olokun]
│
└── midia/                             # 🎥 Vídeos, imagens e recursos de mídia
```

---

## 🚀 Processo de Desenvolvimento e Deploy

### Branches do Repositório

| Branch | Função | Deploy | Usado para |
|--------|--------|--------|-----------|
| `ghpages` | Production | ✅ Ativo (GitHub Pages) | Publicação ao vivo |
| `master` | Backup | ⚠️ Secundário | Sincronização de arquivos |
| `gh-pages` | Desenvolvimento | ⛔ Inativo | Histórico de commits |
| `gh-pages-temp` | Workspace | ❌ Não publicado | Testes locais |

> **Importante:** GitHub Pages está configurado para servir da branch **`ghpages`**. Qualquer mudança feita nessa branch é publicada automaticamente em ~1-2 minutos.

### Fluxo de Trabalho: Adicionar um Novo Link

Exemplo: adicionar link para `mapa_resultados.html` na apresentação institucional.

#### Passo 1: Localizar o arquivo
```bash
# O arquivo está em /olokun/index-instituicoes-tabs.html
ls olokun/index-instituicoes-tabs.html
```

#### Passo 2: Editar localmente
Abra `olokun/index-instituicoes-tabs.html` e encontre o header com os botões de navegação:

```html
<div class="flex items-center gap-2">
  <a href="../dashboard_olokun_tabs.html" ...>Dashboard</a>
  <a href="../mapa_escolas.html" ...>Ver Mapa</a>
  <!-- Adicione aqui o novo link -->
  <a href="https://caetanoronan.github.io/olokun-website/olokun/mapa_resultados.html" 
     class="inline-flex items-center gap-2 px-4 py-2 rounded-lg bg-emerald-600 text-white hover:bg-emerald-700 transition text-sm" 
     target="_blank" rel="noopener noreferrer">
    <i class="fas fa-map-marked-alt"></i> Mapa de Resultados
  </a>
</div>
```

#### Passo 3: Testar localmente
```bash
python -m http.server 8000
# Acesse http://localhost:8000/olokun/index-instituicoes-tabs.html
```

#### Passo 4: Sincronizar para ambas as pastas
Para garantir deployment correto, copie para:
- `gh-pages-temp/olokun/`
- `site/olokun/`

```bash
Copy-Item "olokun/index-instituicoes-tabs.html" "gh-pages-temp/olokun/"
Copy-Item "olokun/index-instituicoes-tabs.html" "site/olokun/"
```

#### Passo 5: Fazer commit na branch de produção
```bash
# Certifique-se de estar na branch ghpages
git checkout ghpages
git add olokun/index-instituicoes-tabs.html
git commit -m "feat: adicionar link para mapa_resultados na apresentação"
git push origin ghpages
```

#### Passo 6: Aguardar e validar
- GitHub Pages fará rebuild automaticamente (1-2 minutos)
- Limpe cache do navegador: **Ctrl+Shift+R**
- Acesse: https://caetanoronan.github.io/olokun-website/olokun/index-instituicoes-tabs.html
- Verifique se o novo link aparece

---

## 🧭 Como Rodar Localmente

### Pré-requisitos
- Python 3.7+
- Git

### Passos

1. **Clone o repositório**
```bash
git clone https://github.com/caetanoronan/olokun-website.git
cd olokun-website
```

2. **Inicie servidor HTTP local**
```bash
python -m http.server 8000
```

3. **Acesse no navegador**

| Página | URL |
|--------|-----|
| Apresentação Institucional | http://localhost:8000/olokun/index-instituicoes-tabs.html |
| Dashboard Territorial | http://localhost:8000/olokun/dashboard_olokun_tabs.html |
| Dashboard Escolas | http://localhost:8000/olokun/dashboard_escolas.html |
| Mapa de Resultados | http://localhost:8000/olokun/mapa_resultados.html |
| Mapa de Escolas | http://localhost:8000/mapa_escolas.html |

---

## 📊 Tecnologias Utilizadas

### Frontend
- **HTML5 / CSS3** — Markup e estilização
- **Tailwind CSS** — Framework de utility-first CSS
- **JavaScript Vanilla** — Interatividade sem dependências pesadas
- **Leaflet.js** — Mapas interativos
- **Cluster Markers** — Plugin para agrupamento de pontos

### Dados
- **GeoJSON** — Formato para dados geoespaciais
- **CSV** — Tabulação de dados estruturados
- **GeoPackage (.gpkg)** — Banco de dados geoespacial (QGIS)

### Deployment
- **GitHub Pages** — Hospedagem estática da branch `ghpages`
- **Git** — Controle de versão

---

## ✏️ Guia de Edição

### Editar Apresentação Institucional

Arquivo: `olokun/index-instituicoes-tabs.html`

**Estrutura de abas:**
```html
<!-- Botões de abas -->
<nav class="flex flex-nowrap -mb-px gap-2">
  <button class="tab-button" data-tab="apresentacao">Apresentação</button>
  <button class="tab-button" data-tab="sobre">Sobre o Programa</button>
  <!-- ... mais botões ... -->
</nav>

<!-- Conteúdo das abas -->
<div id="apresentacao" class="tab-content active">
  <!-- Conteúdo aqui -->
</div>
```

**Adicionando nova aba:**
1. Adicione um botão `<button>` com `data-tab="seu-nome"`
2. Crie uma `<div>` com `id="seu-nome"` na seção de conteúdo
3. A classe `.tab-content` é ativada automaticamente via JavaScript

### Adicionar Novo Mapa

1. Prepare seus dados em GeoJSON
2. Crie novo arquivo HTML em `olokun/`
3. Importe Leaflet CSS/JS:
```html
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.css" />
<script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.js"></script>
```
4. Inicialize mapa:
```javascript
const map = L.map('map-container').setView([-27.5969, -48.5440], 11);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);
```
5. Adicione camadas GeoJSON
6. Publique em `olokun/` → commit → push em `ghpages`

---

## 🔍 Troubleshooting

### Problema: Link não aparece após push

**Causas comuns:**
- ❌ Push feito em branch errada (não é `ghpages`)
- ❌ Cache do navegador (use Ctrl+Shift+R)
- ❌ Arquivo travado ou conflito de merge

**Solução:**
```bash
git checkout ghpages
git log -1 --oneline  # Verifique se está em ghpages
git push origin ghpages
```

### Problema: Arquivo não sincroniza entre pastas

As pastas `olokun/`, `gh-pages-temp/olokun/` e `site/olokun/` precisam estar sempre síncronas. Se editar em uma, copie para as outras:

```bash
Copy-Item "olokun/arquivo.html" "gh-pages-temp/olokun/" -Force
Copy-Item "olokun/arquivo.html" "site/olokun/" -Force
```

### Problema: Mapa não carrega dados

1. Verifique se o arquivo GeoJSON está acessível
2. Abra console do navegador (F12) para ver erros
3. Confirme URL relativa/absoluta está correta
4. Valide GeoJSON em http://geojson.io

---

## 📚 Documentação Adicional

- [Guia de Uso](docs/GUIA_DE_USO.md) — Manual completo para usuários finais
- [Resumo Executivo](docs/RESUMO_EXECUTIVO.md) — Visão geral do projeto
- [Dicionário de Variáveis](dados/metadados/DICIONARIO_VARIAVEIS.md) — Definição dos indicadores
- [Matriz de Alinhamento](dados/Matriz_Alinhamento_Estrategico_Olokun.csv) — Matriz ESG e indicadores

---

## 📬 Contato

- **Email:** olokun.ambiental@gmail.com
- **Local:** Florianópolis, SC — Brasil
- **GitHub:** https://github.com/caetanoronan/olokun-website

---

## 📄 Licença

Projeto em evolução contínua para apoio à tomada de decisão territorial com impacto socioambiental.

**Última atualização:** Fevereiro de 2026

<!-- Trigger: 2026-03-01 113903 -->
