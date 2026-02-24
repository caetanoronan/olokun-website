const map = L.map("map").setView([-27.5954, -48.548], 10);

L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  maxZoom: 19,
  attribution: "&copy; OpenStreetMap",
}).addTo(map);

const layersControl = L.control.layers(null, null, { collapsed: false }).addTo(map);
const layerList = document.getElementById("layer-list");

const layerConfigs = [
  {
    name: "Limite Florianópolis",
    url: "../data/municipio_florianopolis.geojson",
    style: { color: "#60a5fa", weight: 2, fillOpacity: 0.05 },
  },
  {
    name: "Grande Florianópolis",
    url: "../data/municipios_grande_florianopolis.geojson",
    style: { color: "#34d399", weight: 2, fillOpacity: 0.03 },
  },
  {
    name: "Setores censitários",
    url: "../data/setores_florianopolis.geojson",
    style: { color: "#a78bfa", weight: 1, fillOpacity: 0.06 },
  },
  {
    name: "Voronoi Escolas",
    url: "../data/voronoi_escolas.geojson",
    style: { color: "#c084fc", weight: 1.5, fillOpacity: 0.05 },
  },
  {
    name: "Cobertura 3km (Escolas)",
    url: "../data/cobertura_3km_escolas.geojson",
    style: { color: "#f59e0b", weight: 1.5, fillOpacity: 0.08 },
  },
  {
    name: "Pontos de parceiros",
    url: "../data/pontos_olokun.geojson",
    pointToLayer: (f, latlng) => L.circleMarker(latlng, { radius: 6, color: "#fb923c", fillOpacity: 0.8 }),
  },
  {
    name: "Escolas (públicas/privadas)",
    url: "../data/escolas_olokun.geojson",
    pointToLayer: (f, latlng) => L.circleMarker(latlng, { radius: 5, color: "#f97316", fillOpacity: 0.85 }),
  },
  {
    name: "Empresas (públicas/privadas)",
    url: "../data/empresas_olokun.geojson",
    pointToLayer: (f, latlng) => L.circleMarker(latlng, { radius: 5, color: "#38bdf8", fillOpacity: 0.85 }),
  },
];

layerConfigs.forEach((cfg) => {
  fetch(cfg.url)
    .then((res) => res.json())
    .then((geojson) => {
      const layer = L.geoJSON(geojson, {
        style: cfg.style,
        pointToLayer: cfg.pointToLayer,
      }).addTo(map);
      layersControl.addOverlay(layer, cfg.name);
      const item = document.createElement("label");
      item.className = "checkbox";
      item.innerHTML = `<input type="checkbox" checked /> ${cfg.name}`;
      const input = item.querySelector("input");
      input.addEventListener("change", () => {
        if (input.checked) {
          map.addLayer(layer);
        } else {
          map.removeLayer(layer);
        }
      });
      layerList.appendChild(item);
      if (geojson.features.length && geojson.features[0].geometry.type !== "Point") {
        map.fitBounds(layer.getBounds(), { padding: [20, 20] });
      }
    })
    .catch(() => {
      const item = document.createElement("div");
      item.textContent = `${cfg.name}: arquivo não encontrado.`;
      layerList.appendChild(item);
    });
});

fetch("../data/heat_points_escolas.json")
  .then((res) => res.json())
  .then((points) => {
    if (!Array.isArray(points) || points.length === 0) {
      return;
    }
    const heatLayer = L.heatLayer(points, { radius: 22, blur: 18, maxZoom: 13 });
    heatLayer.addTo(map);
    layersControl.addOverlay(heatLayer, "Heatmap Escolas");
  })
  .catch(() => {
    // ignore if file is not present
  });
