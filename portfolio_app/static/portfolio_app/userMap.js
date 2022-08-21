document.addEventListener("DOMContentLoaded", () => {
	const map = L.map("map").setView([-29, 22.9375], 6)
	const marker = L.marker()

	// Adds OSM as a base layer
	L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
		attribution:
			'&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
	}).addTo(map)

	/*
		Fetch all users
		Adds the user locations to the map as a marker
	*/
	fetch("get_users")
		.then((response) => response.json())
		.then((users) => {
			users.map((user) => {
				marker.setLatLng([user.location_latitude, user.location_longitude])
				marker.addTo(map)

				/*
					Popup content
					Username
					Home address
					Phone number
				*/
				const popupContent = `
					<div>
						<h1>${user.username}</h1>
						<p>Home Address: ${user.home_address}</p>
						<p>Phone Number: ${user.phone_number}</p>
					</div>
				`

				// Bind popup to marker and open on marker click
				marker.bindPopup(popupContent)
			})
		})
})
