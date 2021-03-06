mapboxgl.accessToken = 'pk.eyJ1IjoiYnVzdW5raW05NiIsImEiOiJjaWx4ZDI1Y24wN3lxdmdrc3NkeHNqbzN5In0.oI1GbKPDTensdmbB-XcF_g';
var map = new mapboxgl.Map({
  container: 'map',
  style: 'mapbox://styles/mapbox/dark-v8',
  center: [-96,37.8],
  zoom: 3
});

map.on('style.load', function() {
   map.addSource("cities", {
       "type": "geojson",
       "data": "json/cities.geojson"
   });

  
   map.addLayer({
     "id": "cities", // An id for this layer
     "type": "circle", // As a point layer, we need style a symbol for each point.
     "source": "cities", // The source layer we defined above
     "paint": {
         "circle-radius": 10,
         "circle-color": "#FF5600",
	"circle-opacity": 0.8
     }
   });
});

