<!DOCTYPE html>
<html>
  <head>
    <title>Glasscell</title>
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
    <meta charset="utf-8">
    <style>
      /* Always set the map height explicitly to define the size of the div
       * element that contains the map. */
      #map {
        height: 100%;
      }
      /* Optional: Makes the sample page fill the window. */
      html, body {
        height: 100%;
        margin: 0;
        padding: 0;
      }
    </style>
  </head>
  <body>
  <button id="myBtn">Location</button>
    <div id="map"></div>
    <script>
      // Note: This example requires that you consent to location sharing when
      // prompted by your browser. If you see the error "The Geolocation service
      // failed.", it means you probably did not give permission for the browser to
      // locate you.
      var map, infoWindow;
      function initMap() {
        map = new google.maps.Map(document.getElementById('map'), {
          center: {lat: 32.605, lng: -85.485},

          zoom: 18
        });
        infoWindow = new google.maps.InfoWindow;

        document.getElementById("myBtn").addEventListener("click", function(){
        // Try HTML5 geolocation.
        if (navigator.geolocation) {
          navigator.geolocation.getCurrentPosition(function(position) {
            var pos = {
              lat: position.coords.latitude,
              lng: position.coords.longitude
            };

            infoWindow.setPosition(pos);
            infoWindow.setContent('You are here');
            /*
            infoWindow.setContent('Location found: ' + pos.lat + ',' + pos.lng);*/

            infoWindow.open(map);
            map.setCenter(pos);



            var pinz = [
                          {
                              'location':{
                                  'lat' : 32.60485452726591,
                                  'lng' : -85.48493892880751
                              }
                          },
                          {
                              'location':{
                                  'lat' : 32.60565805640315,
                                  'lng' : -85.48649902178823
                              }
                          },
                          {
                              'location':{
                                  'lat' : 32.60483344331394,
                                  'lng' : -85.48634329058162
                              }
                          }]


          for (var i = 0; i <= pinz.length;i++){
            var myLatLng = new google.maps.LatLng(pinz[i].location.lat, pinz[i].location.lng);
            //var marker = new google.maps.marker.AdvancedMarkerView({
            
            var marker = new google.maps.Marker({
            position: myLatLng, 
            map: map,
/*            icon :{path: 'sos2.png',
                   size: new google.maps.Size(400, 400)                    
           }*/
            });
            infoWindow.open(marker);
            }

            
          }, function() {
            handleLocationError(true, infoWindow, map.getCenter());
          });
        } else {
          // Browser doesn't support Geolocation
          handleLocationError(false, infoWindow, map.getCenter());
        }

    });    
      }

      function handleLocationError(browserHasGeolocation, infoWindow, pos) {
        infoWindow.setPosition(pos);
        infoWindow.setContent(browserHasGeolocation ?
                              'Error: The Geolocation service failed.' :
                              'Error: Your browser doesn\'t support geolocation.');
        infoWindow.open(map);
      }
    </script>
    <script async defer
    src="https://maps.googleapis.com/maps/api/js?key=AIzaSyCR3TJ9WEg90UBZKPhAOjoKwLmy3wgR69M&callback=initMap">
    </script>
  </body>
</html>