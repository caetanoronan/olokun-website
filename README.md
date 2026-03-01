# 🌊 Instituto Olokun — Plataforma Territorial

Este repositório reúne os materiais web do Instituto Olokun para apresentação institucional, dashboard de estratégia territorial, mapa de resultados e mapas interativos de escolas.

## 🎯 Sobre o Projeto

O Instituto Olokun é uma organização dedicada à **preservação e conservação costeira**, com foco em educação ambiental territorialmente ancorada e soluções orientadas por dados.

A plataforma integra:

- 📊 **Dashboard territorial** com indicadores de alinhamento estratégico
- 🗺️ **Mapas interativos** de escolas, cobertura de serviços e resultados
- 🏛️ **Apresentação institucional** com abas temáticas para diferentes públicos
- 📈 **Visualização geoespacial** para apoio à decisão

---

## 🔗 Acessos Públicos (GitHub Pages)

### 🌍 Apresentação Institucional (Multilíngue)

Com seletor de idiomas e modo escuro/claro:

| Idioma | URL |
|--------|-----|
| 🇧🇷 Português | https://caetanoronan.github.io/olokun-website/olokun/index-instituicoes-tabs.html |
| 🇬🇧 English | https://caetanoronan.github.io/olokun-website/olokun/index-instituicoes-tabs.en.html |
| 🇪🇸 Español | https://caetanoronan.github.io/olokun-website/olokun/index-instituicoes-tabs.es.html |

**Conteúdo:** 6 abas — Apresentação, Sobre o Programa, Projetos, Produtos & Serviços, Para Instituições e Contato.

### 📊 Dashboard Territorial (Multilíngue)

| Idioma | URL |
|--------|-----|
| 🇧🇷 Português | https://caetanoronan.github.io/olokun-website/olokun/dashboard_olokun_tabs.html |
| 🇬🇧 English | https://caetanoronan.github.io/olokun-website/olokun/dashboard_olokun_tabs.en.html |
| 🇪🇸 Español | https://caetanoronan.github.io/olokun-website/olokun/dashboard_olokun_tabs.es.html |

### 🗺️ Outros Dashboards e Mapas

- **Dashboard Escolas:** https://caetanoronan.github.io/olokun-website/olokun/dashboard_escolas.html
- **Mapa de Resultados:** https://caetanoronan.github.io/olokun-website/olokun/mapa_resultados.html
- **Mapa de Escolas:** https://caetanoronan.github.io/olokun-website/mapa_escolas.html

---

## 📢 Banner Informativo de Funcionalidades

A apresentação institucional possui um banner de boas-vindas (dismissível) para orientar novos visitantes.

Funcionalidades destacadas:

1. 🌐 **Idioma** (PT/EN/ES)
2. 🌙 **Tema** (claro/escuro)
3. 📊 **Dashboard**
4. 🗺️ **Ver Mapa**
5. 📍 **Mapa de Resultados**

Arquivos com banner:

- `olokun/index-instituicoes-tabs.html`
- `olokun/index-instituicoes-tabs.en.html`
- `olokun/index-instituicoes-tabs.es.html`
- `olokun/index-instituicoes-tabs.original.html`

---

## 📂 Estrutura do Projeto

```text
olokun-website/
├── README.md
├── olokun/
│   ├── index-instituicoes-tabs.html
│   ├── index-instituicoes-tabs.en.html
│   ├── index-instituicoes-tabs.es.html
│   ├── index-instituicoes-tabs.original.html
│   ├── dashboard_olokun_tabs.html
│   ├── dashboard_olokun_tabs.en.html
│   ├── dashboard_olokun_tabs.es.html
│   ├── dashboard_olokun_tabs.original.html
│   ├── dashboard_escolas.html
│   ├── mapa_resultados.html
│   └── mapa_olokun.html
├── dados/
├── gis/
├── docs/
├── gh-pages-temp/
├── site/
└── midia/
```

---

## 🧭 Como Rodar Localmente

### Pré-requisitos

- Python 3.7+
- Git

### Passos

```bash
git clone https://github.com/caetanoronan/olokun-website.git
cd olokun-website
python -m http.server 8000
```

Acesse:

- http://localhost:8000/olokun/index-instituicoes-tabs.html
- http://localhost:8000/olokun/dashboard_olokun_tabs.html
- http://localhost:8000/olokun/mapa_resultados.html

---

## 🛠️ Tecnologias Utilizadas

### Frontend

- HTML5 / CSS3
- Tailwind CSS
- JavaScript Vanilla
- Chart.js 4.4.0
- AOS 2.3.1
- Leaflet.js
- Font Awesome 6.5.1

### Dados

- GeoJSON
- CSV
- GeoPackage (.gpkg)

### Deploy

- GitHub Pages
- Git

---

## 📚 Documentação Adicional

- [Guia de Uso](docs/GUIA_DE_USO.md)
- [Resumo Executivo](docs/RESUMO_EXECUTIVO.md)
- [Dicionário de Variáveis](dados/metadados/DICIONARIO_VARIAVEIS.md)
- [Matriz de Alinhamento](dados/Matriz_Alinhamento_Estrategico_Olokun.csv)

---

## 📬 Contato

- **Email:** olokun.ambiental@gmail.com
- **Local:** Florianópolis, SC — Brasil
- **GitHub:** https://github.com/caetanoronan/olokun-website

---

## 📄 Licença

Projeto em evolução contínua para apoio à tomada de decisão territorial com impacto socioambiental.

**Última atualização:** Março de 2026 (README recodificado em UTF-8 e conteúdo multilíngue atualizado)
