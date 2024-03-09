// chart-script.js

// Load Chart.js library dynamically
function loadChartJsLibrary() {
    return new Promise((resolve, reject) => {
        const script = document.createElement('script');
        script.src = 'https://cdn.jsdelivr.net/npm/chart.js';
        script.onload = resolve;
        script.onerror = reject;
        document.head.appendChild(script);
    });
}

let apiurl = 'http://127.0.0.1:8000/stats/';
// let apiurl = 'https://shrin13.pythonanywhere.com/stats/';

async function initializeChart() {
    // Load Chart.js library dynamically
    await loadChartJsLibrary();

    // Continue with the rest of your code
    async function fetchChartData() {
        try {
            const response = await fetch(apiurl);
            const data = await response.json();
            return data;
        } catch (error) {
            console.error('Error fetching chart data:', error);
            return null;
        }
    }

    const apiChartData = await fetchChartData();

    if (apiChartData) {
        const ctx = document.getElementById('voteDoughnutChart').getContext('2d');
        new Chart(ctx, {
            type: apiChartData.type,
            data: apiChartData.data,
            options: {
                title: {
                    display: true,
                    text: 'Vote Doughnut Chart'
                }
            }
        });
    }
}

initializeChart();
