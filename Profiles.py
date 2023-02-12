'''
For creating user profiles that will be uploaded to the database.
'''
import time
import requests

class Profile:
    def __init__(self, name, current_status, location=None):
        self.name = name
        self.current_status = current_status
        self.time_of_creation = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        self.location = location
        self.message = None

    def update_location(self):
        response = requests.get(f'https://maps.googleapis.com/maps/api/geolocation/json?key={AIzaSyCR3TJ9WEg90UBZKPhAOjoKwLmy3wgR69M}')
        response_json = response.json()
        if response_json['status'] == 'OK':
            self.location = response_json['location']

    def set_message(self, message):
        self.message = message