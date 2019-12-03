var API_KEY = "pk.eyJ1IjoiaXJldGVtaSIsImEiOiJjazJ2NWM2YjYwMWp5M2JudXVjcTQxN3JmIn0.13iRNa-JIDBBalkazka2fw";

var mymap = L.map('map').setView([51.505, -0.09], 13);

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    accessToken: API_KEY
}).addTo(mymap);

locations.forEach(d => {
    L.marker(d).addTo(mymap);
})