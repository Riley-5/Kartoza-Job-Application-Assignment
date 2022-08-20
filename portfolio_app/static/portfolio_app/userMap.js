document.addEventListener("DOMContentLoaded", () => {
	const map = L.map("map").setView([-29, 22.9375], 6)

	// Adds OSM as a base layer
	var osm = L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
		attribution:
			'&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
	}).addTo(map)
})
