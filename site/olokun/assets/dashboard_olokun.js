const scopeSelect = document.getElementById("filter-escopo");
const municipiosSelect = document.getElementById("filter-municipio");
const scoreSlider = document.getElementById("filter-score");
const scoreValue = document.getElementById("filter-score-value");

const statSetores = document.getElementById("stat-setores");
const statParceiros = document.getElementById("stat-parceiros");
const statScore = document.getElementById("stat-score");
const statTopArea = document.getElementById("stat-top-area");
const mcdaSummary = document.getElementById("mcda-summary");

scoreSlider.addEventListener("input", () => {
  scoreValue.textContent = scoreSlider.value;
  updateDashboard();
});

scopeSelect.addEventListener("change", () => {
  loadSetores(scopeSelect.value).then(updateDashboard);
});

municipiosSelect.addEventListener("change", updateDashboard);

document.getElementById("filter-parceiro").addEventListener("change", updateDashboard);

let setores = [];
let parceiros = [];

Promise.all([
  fetch("../data/parceiros_resumo.json").then((res) => res.json()).catch(() => []),
  fetch("../data/municipios_grande_florianopolis.csv").then((res) => res.text()).catch(() => ""),
]).then(async ([parceirosData, municipiosCsv]) => {
  parceiros = parceirosData;

  if (municipiosCsv) {
    const lines = municipiosCsv.trim().split(/\r?\n/).slice(1);
    lines.forEach((line) => {
      const [cd, nm] = line.split(",");
      const option = document.createElement("option");
      option.value = nm;
      option.textContent = nm;
      municipiosSelect.appendChild(option);
    });
  }

  buildCharts();
  await loadSetores(scopeSelect.value);
  updateDashboard();
});

let chartScore;
let chartParceiros;

function buildCharts() {
  const ctxScore = document.getElementById("chart-score");
  const ctxParceiros = document.getElementById("chart-parceiros");

  chartScore = new Chart(ctxScore, {
    type: "bar",
    data: {
      labels: ["0-20", "20-40", "40-60", "60-80", "80-100"],
      datasets: [{
        label: "Setores",
        data: [0, 0, 0, 0, 0],
        backgroundColor: "#38bdf8",
      }],
    },
    options: { responsive: true, plugins: { legend: { display: false } } },
  });

  chartParceiros = new Chart(ctxParceiros, {
    type: "doughnut",
    data: {
      labels: ["Escolas", "ONGs", "Empresas"],
      datasets: [{ data: [0, 0, 0], backgroundColor: ["#22c55e", "#f97316", "#60a5fa"] }],
    },
  });
}

async function loadSetores(scope) {
  const url = scope === "grande" ? "../data/setores_resumo_grande.json" : "../data/setores_resumo.json";
  setores = await fetch(url).then((res) => res.json()).catch(() => []);
}

function updateDashboard() {
  const municipio = municipiosSelect.value;
  const parceiroTipo = document.getElementById("filter-parceiro").value;
  const minScore = Number(scoreSlider.value);

  const setoresFiltrados = setores.filter((s) => {
    const okMunicipio = municipio === "all" || s.municipio === municipio;
    return okMunicipio && s.score >= minScore;
  });

  const parceirosFiltrados = parceiros.filter((p) => {
    const okMunicipio = municipio === "all" || p.municipio === municipio;
    const okTipo = parceiroTipo === "all" || p.tipo === parceiroTipo;
    return okMunicipio && okTipo;
  });

  statSetores.textContent = setoresFiltrados.length;
  statParceiros.textContent = parceirosFiltrados.length;
  const media = setoresFiltrados.length ? (setoresFiltrados.reduce((acc, s) => acc + s.score, 0) / setoresFiltrados.length) : 0;
  statScore.textContent = media.toFixed(1);
  statTopArea.textContent = setoresFiltrados.sort((a, b) => b.score - a.score)[0]?.nome || "-";

  updateCharts(setoresFiltrados, parceirosFiltrados);
  updateMcda(setoresFiltrados);
}

function updateCharts(setoresFiltrados, parceirosFiltrados) {
  const bins = [0, 0, 0, 0, 0];
  setoresFiltrados.forEach((s) => {
    const idx = Math.min(4, Math.floor(s.score / 20));
    bins[idx] += 1;
  });
  chartScore.data.datasets[0].data = bins;
  chartScore.update();

  const tipos = { escola: 0, ong: 0, empresa: 0 };
  parceirosFiltrados.forEach((p) => { tipos[p.tipo] = (tipos[p.tipo] || 0) + 1; });
  chartParceiros.data.datasets[0].data = [tipos.escola, tipos.ong, tipos.empresa];
  chartParceiros.update();
}

function updateMcda(setoresFiltrados) {
  if (!setoresFiltrados.length) {
    mcdaSummary.textContent = "Sem dados suficientes para o resumo.";
    return;
  }
  const top = setoresFiltrados.slice(0, 5).map((s) => `• ${s.nome} (${s.score.toFixed(1)})`).join("<br>");
  mcdaSummary.innerHTML = `<strong>Top 5 setores</strong><br>${top}`;
}
