const PALETTE = {
  rose: '#C17A6F',
  roseDeep: '#A35F54',
  sage: '#7C9070',
  sageDeep: '#5F7355',
  sand: '#D9C7A8',
  clay: '#BFA98A',
  ink: '#2E2C28',
  inkSoft: '#5C5850',
  grid: 'rgba(46,44,40,0.08)'
};

const baseOptions = {
  responsive: true,
  maintainAspectRatio: false,
  animation: { duration: 900, easing: 'easeOutQuart' },
  plugins: {
    legend: { display: false },
    tooltip: {
      backgroundColor: '#2E2C28',
      titleFont: { family: 'Inter', size: 12 },
      bodyFont: { family: 'JetBrains Mono', size: 13 },
      padding: 10,
      cornerRadius: 8,
      displayColors: false,
      callbacks: { label: (ctx) => ctx.parsed.x !== undefined && ctx.parsed.x !== null
        ? ctx.parsed.x + '% churn rate'
        : ctx.parsed.y + '% churn rate' }
    }
  },
  scales: {
    x: { grid: { display: false }, ticks: { font: { family: 'Inter', size: 12 }, color: PALETTE.inkSoft } },
    y: { grid: { color: PALETTE.grid }, ticks: { font: { family: 'Inter', size: 12 }, color: PALETTE.inkSoft, callback: v => v + '%' } }
  }
};

function makeHBar(id, labels, data, colors) {
  const el = document.getElementById(id);
  if (!el) return;
  new Chart(el, {
    type: 'bar',
    data: { labels, datasets: [{ data, backgroundColor: colors, borderRadius: 6, barThickness: 22 }] },
    options: {
      ...baseOptions,
      indexAxis: 'y',
      scales: {
        x: { grid: { color: PALETTE.grid }, ticks: { font: { family: 'Inter', size: 12 }, color: PALETTE.inkSoft, callback: v => v + '%' }, max: Math.max(...data) * 1.25 },
        y: { grid: { display: false }, ticks: { font: { family: 'Inter', size: 12.5 }, color: PALETTE.ink } }
      }
    }
  });
}

makeHBar('chartTenure',
  ['0–3 months', '4–6 months', '7–12 months', '1–2 years', '2+ years'],
  [41.9, 7.5, 5.7, 6.5, 0],
  [PALETTE.rose, PALETTE.sand, PALETTE.sand, PALETTE.sand, PALETTE.sage]
);

makeHBar('chartComplaint',
  ['No complaint', 'Complaint filed'],
  [10.9, 31.7],
  [PALETTE.sage, PALETTE.rose]
);

makeHBar('chartCity',
  ['Tier 1', 'Tier 2', 'Tier 3'],
  [14.5, 19.8, 21.4],
  [PALETTE.clay, PALETTE.clay, PALETTE.rose]
);

makeHBar('chartSat',
  ['Score 1', 'Score 2', 'Score 3', 'Score 4', 'Score 5'],
  [11.5, 12.6, 17.2, 17.1, 23.8],
  [PALETTE.sage, PALETTE.sand, PALETTE.sand, PALETTE.sand, PALETTE.rose]
);