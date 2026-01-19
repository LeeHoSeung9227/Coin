// fetch_data.js

const FETCH_INTERVAL = 20 * 60 * 1000; // 20분

function formatDateTime(dateString) {
    const date = new Date(dateString);
    return `${date.getFullYear()}-${String(date.getMonth() + 1).padStart(2, '0')}-${String(date.getDate()).padStart(2, '0')} ${String(date.getHours()).padStart(2, '0')}:${String(date.getMinutes()).padStart(2, '0')}`;
}

function updateNextFetchTime() {
    const nextFetchTime = new Date(lastFetchTime + FETCH_INTERVAL);
    document.getElementById('next_update').innerText = formatDateTime(nextFetchTime);
}

function updateDisplay(data) {
    document.getElementById('wave_height').innerText = `${data.wave_height}m, ${formatDateTime(data.wave_time)}`;
    document.getElementById('tide_level').innerText = `${data.tide_level}cm, ${formatDateTime(data.tide_time)}`;
    document.getElementById('fetch_time').innerText = formatDateTime(data.fetch_time);
    lastFetchTime = Date.now();
    updateNextFetchTime();
}

function fetchData() {
    if (Date.now() - lastFetchTime < FETCH_INTERVAL) return;
    fetch(`/lifeguard/get_wave_and_tide_data`)
        .then(response => response.json())
        .then(data => {
            if (data.error) throw new Error(data.error);
            updateDisplay(data);
        })
        .catch(error => console.error('Error:', error));
}

fetchData();
setInterval(fetchData, FETCH_INTERVAL);
setInterval(updateNextFetchTime, 60000);
