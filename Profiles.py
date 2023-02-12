'''
For creating user profiles that will be uploaded to the database.
'''
import time
import requests

'''
A Profile contains all the user info associated with a specific key that can be stored
in the database.

Information for a Profile comes from a signal object.

'''
class Profile:
    def __init__(self, name, current_status, location=None):
        self._current_status = current_status
        self._time_of_creation = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        self._location = location
        self._message = None

    def update_location(self):
        response = requests.get(f'https://maps.googleapis.com/maps/api/geolocation/json?key={AIzaSyCR3TJ9WEg90UBZKPhAOjoKwLmy3wgR69M}')
        response_json = response.json()
        if response_json['status'] == 'OK':
            self.location = response_json['location']