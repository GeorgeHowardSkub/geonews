const map = L.map('map').setView([20, 0], 2);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; OpenStreetMap contributors'
}).addTo(map);


let markers = [];

function clearMarkers() {
  markers.forEach(marker => map.removeLayer(marker));
  markers = [];
}

function addMarkers(data) {
  data.forEach(article => {
    article.locations.forEach(loc => {
      if (loc.lat && loc.lng) {
        const marker = L.marker([loc.lat, loc.lng]).addTo(map);
        marker.bindPopup(`
          <div class="popup-title">${article.title}</div>
          <a href="${article.url}" target="_blank">Read more</a>
        `);
        markers.push(marker);
      }
    });
  });
}

function searchNews() {
  const query = document.getElementById("searchBox").value || "world";

  clearMarkers();
  document.getElementById("status").textContent = "Searching...";

  fetch(`/news?q=${encodeURIComponent(query)}`)
    .then(response => response.json())
    .then(data => {
      addMarkers(data);
      document.getElementById("status").textContent = `Found ${data.length} articles`;
    })
    .catch(err => {
      console.error("Error fetching news:", err);
      document.getElementById("status").textContent = "Error fetching news.";
    });
}

searchNews();

