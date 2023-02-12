# For creating user profiles that will be uploaded to the database.
import time
import requests
import Signals

# A Profile contains all the user info associated with a specific key that can be stored
# in the database.
#
# Indirectly handles data control of profiles in database.
#
# Information for a Profile comes from a signal object.
class Profile:
    def __init__(self, keyword, signals_array, profile_dict=None, screen_name=None,  recent_location=None, creation_date=None):
        self.profile_dict = profile_dict
        self.keyword = keyword
        self.signals_array = signals_array
        self.screen_name = screen_name
        self.screen_name = recent_location
        self.creation_date = creation_date
    
    def get_keyword(self):
        return self.keyword

    def get_screen_name(self):
        return self.screen_name


# Module functions ----------------------------------------------------------------------
def generate_keyword():
    unique_keyword = "empty"
    return unique_keyword