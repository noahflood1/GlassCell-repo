# For creating user profiles that will be uploaded to the database.
import time
import datetime
import requests
import Signals
import Keys
import DatabaseControl

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
    # Getters ----------------------------------------------------------------------
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
    
    # Setters ----------------------------------------------------------------------
    def set_keyword(self, k):
        self.keyword = k

    def set_screen_name(self, sm):
        self.screen_name = sm
    
    def set_creation_date(self, cd):
        self.creation_date = cd
    
    def set_recent_location(self, loc):
        self.recent_location = loc
    
    def set_signals_arr(self, arr):
        self.signals_arr = arr

# Module functions ----------------------------------------------------------------------
def generate_keyword(profiles_database_array):
    unique_keyword = Keys.new_key_process(profiles_database_array)
    return unique_keyword

def generate_screen_name():
    unique_screen_name = Keys.new_screen_name_process(profiles_database_array)
    return unique_screen_name

def create_new_profile(new_GlassCell_request):
    # read in the existing database
    DatabaseControl.read_in_database()

    # generate a unique keyword
    new_keyword = generate_keyword(profiles_database_array)

    # generate a unique screen name
    new_screen_name = generate_screen_name(profiles_database_array)

    # get creation date for today
    now = datetime.datetime.now()
    new_creation_date = now.strftime("%B %d, %Y %H:%M:%S")

    # get recent location
    new_recent_location = new_GlassCell_request.getLocation()

    # create an empty the signal array
    signal_array = []

    # create the only signal object available for the profile
    first_signal = Signals.Signal(
                  keyword=new_GlassCell_request.get_keyword(),
                  location=new_GlassCell_request.get_location(),
                  date_time=new_GlassCell_request.get_date_time(),
                  distress_level=new_GlassCell_request.get_distress_level(),
                  message=new_GlassCell_request.get_msg(),
                  index=0)

    #append it to the array
    signal_array.append(first_signal)

    # finally, instantiate a new profile
    new_profile = Profile(
            keyword=new_keyword,
            screen_name=new_screen_name,
            creation_date=new_creation_date,
            recent_location=new_recent_location,
            signals_arr=signal_array)
    
    # return it
    return new_profile

#TODO
def add_signal_to_existing_profile(new_GlassCell_request):
    # add a signal to existing profile obj
    # make updates to recent location, 
    return 