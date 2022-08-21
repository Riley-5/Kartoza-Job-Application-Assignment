document.addEventListener("DOMContentLoaded", () => {
	const map = L.map("map").setView([-29, 22.9375], 6)
	const marker = L.marker()

	// Adds OSM as a base layer
	L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
		attribution:
			'&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
	}).addTo(map)

	/*
		Fetch all users and place in users array
	*/
	fetch("get_users")
		.then((response) => response.json())
		.then((users) => {
			users.map((user) => {
				marker.setLatLng([user.location_latitude, user.location_longitude])
				marker.addTo(map)
			})
		})
})
