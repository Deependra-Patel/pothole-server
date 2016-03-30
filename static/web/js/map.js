var mumbaiLatLng = {
  lat: 19.130340,
  lng: 72.907428
};

function initMap() {
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 12,
    center: mumbaiLatLng
  });
  var markers = [];
  var colorMap = {
    'a': 'white',
    'r': 'red',
    'd': 'green',
    'f': 'black'
  };
  var iconMap = {
    'p': google.maps.SymbolPath.CIRCLE,
    's': google.maps.SymbolPath.FORWARD_OPEN_ARROW
  };
  $.ajax({
    type: 'GET',
    url: '/api/complaint',
    async: false,
    success: function(response) {
      for (i = 0; i < response.length; i++) {
        markers.push([response[i].Lat, response[i].Long,
            colorMap[response[i].Status],
            iconMap[response[i].Type]
        ]);
      }
    }
  });

  for (i = 0; i < markers.length; i++) {
    var position = new google.maps.LatLng(markers[i][0], markers[i][1]);
    marker = new google.maps.Marker({
      position: position,
      map: map,
      icon: {
        path: markers[i][3],
        fillColor: markers[i][2],
        fillOpacity: .6,
        scale: 4.5,
        strokeColor: 'white',
        strokeWeight: 1
      }
    });
  }
}
