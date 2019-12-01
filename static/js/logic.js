var API_KEY = "pk.eyJ1IjoiaXJldGVtaSIsImEiOiJjazJ2NWM2YjYwMWp5M2JudXVjcTQxN3JmIn0.13iRNa-JIDBBalkazka2fw";
// Store our API endpoint inside queryUrl
var queryUrl = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson";
console.log(queryUrl);
// Perform a GET request to the query URL
d3.json(queryUrl, function (data) {
    // Once we get a response, send the data.Features object to the createFeatures function
    createFeatures(data.features);
});

function createFeatures(earthquakeData) {
// Define a function we want to run once for each feature in the features array
    // Give each feature a popup describing the place and time of the earthquake
    function onEachfeature(features, layer) {
        layer.bindPopup("<h3>" + features.properties.place + "</h3><hr><p>" + new Date(features.properties.time) + "</p>");
    }

    var earthquakes = L.geoJSON(earthquakeData, {
        onEachFeature: onEachfeature,
        pointToLayer: function (features, latlng) {
            var geoJSONMarker = {
                radius: markerSize(features.properties.mag),
                fillColor: fillColor(features.properties.mag),
                color: "pink",
                weight: 0.5,
                opacity: 0.5,
                fillOpacity: 0.8
            };

            return L.circleMarker(latlng, geoJSONMarker);
        },
    })
    // Sending our earthquakes layer to the createMap function
    createMap(earthquakes);
};

function createMap(earthquakes) {
    var streetmap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
        attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
        maxZoom: 18,
        id: "mapbox.streets",
        accessToken: API_KEY
    });

    var darkmap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
        attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
        maxZoom: 18,
        id: "mapbox.dark",
        accessToken: API_KEY
    });

    // Define a baseMaps object to hold our base layers
    var baseMaps = {
        "Street Map": streetmap,
        "Dark Map": darkmap
    };

    // Create overlay object to hold our overlay layer
    var overlayMaps = {
        "Earthquakes": earthquakes
    };

    // Create our map, giving it the streetmap and earthquakes layers to display on load
    var myMap = L.map("map", {
        center: [37.09, -95.71],
        zoom: 5,
        layers: [streetmap, earthquakes]
    });

    // Create a layer control
    // Pass in our baseMaps and overlayMaps
    // Add the layer control to the map
    L.control.layers(baseMaps, overlayMaps, {
        collapsed: false
    }).addTo(myMap);

    var legend = L.control({ position: 'bottomright' });

    legend.onAdd = function () {
        var div = L.DomUtil.create('div', 'legend'),
            magnitude = [0, 1.0, 2.0, 3.0, 4.0, 5.0],
            labels = [];
        // loop through our magnitude intervals and generate a label with a colored square for each interval
        div.innerHTML ='<div><b>Earthquake <br/> Magnitude</b></div';
        for (var i = 0; i < magnitude.length; i++) {
            div.innerHTML += '<i style= "background:' + fillColor(magnitude[i]) + '"></i> ' +
            magnitude[i] + (magnitude[i + 1] ? '&ndash;' + magnitude[i + 1] + '<br>' : '+');
        }
        return div;
    };
    legend.addTo(myMap);
}
function fillColor(mag) {
    switch (true) {
        case mag >= 5.0:
            return '#d73027';
        case mag >= 4.0:
            return '#fc8d59';
        case mag >= 3.0:
            return '#fee08b';
        case mag >= 2.0:
            return '#d9ef8b';
        case mag >= 1.0:
            return '#91cf60';
        case mag < 1.0:
            return '#1a9850';
    };
};
function markerSize(mag) {
    return mag * 4
};