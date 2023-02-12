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
# Every profile contains nested dictionaries
class Profile:
    def __init__(self, keyword, screen_name, creation_date, recent_location, signals_arr):
        self.keyword = keyword
        self.screen_name = screen_name
        self.creation_date = creation_date
        self.recent_location = recent_location
        self.signals_arr = signals_arr #contains the signal objects for this profile
    
    # To String method
    def __str__(self):
        signals_string = ""
        for signal in self.signals_arr:
            signals_string = signals_string + signal.__str__() + "\n"

        return "KEYWORD: {}\nScreen name: {}\nCreation date: {}\nRecent location: {}\nSignals:\n{}".format(
            self.keyword,
            self.screen_name,
            self.creation_date,
            self.recent_location,
            signals_string 
        )
    
    def get_keyword(self):
        return self.keyword

    def get_screen_name(self):
        return self.screen_name
    
    def get_creation_date(self):
        return self.creation_date
    
    def get_recent_location(self):
        return self.recent_location
    
    def get_signals_arr(self):
        return self.signals_arr

# Module functions ----------------------------------------------------------------------
def generate_keyword():
    unique_keyword = "empty"
    return unique_keyword

def generate_screenname():
    unique_screenname = "empty"
    return unique_screenname