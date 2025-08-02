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
  fetch(`http://127.0.0.1:8000/news?q=${encodeURIComponent(query)}`)
    .then(response => response.json())
    .then(data => {
      clearMarkers();
      addMarkers(data);
    })
    .catch(err => console.error("Error fetching news:", err));
}

searchNews();

