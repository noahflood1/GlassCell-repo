# For creating user profiles that will be uploaded to the database.
import time
import requests
import Signal

# A Profile contains all the user info associated with a specific key that can be stored
# in the database.
#
# Indirectly handles data control of profiles in database.
#
# Information for a Profile comes from a signal object.
class Profile:
    def __init__(self, keyword, signals_array, screen_name=None,  recent_location=None):
        self.keyword = keyword
        self.signals_array = signals_array
        self.screen_name = screen_name
        self.screen_name = recent_location