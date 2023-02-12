# Signal.py takes parameters from original request --> Master --> Profile and creates a new signal object.
# It must call from DatabaseControls.py before processing signal to check existance and index.
import time
import requests
import DatabaseControl
import Profiles

# Every signal contains criteria. Parameter management held elsewhere
class Signal:
    def __init__(self, keyword, location, date_time, distress_level, message, index):
        self.keyword = keyword
        self.location = location
        self.date_time = date_time
        self.distress_level = distress_level
        self.message = message
        self.index = index

    def __str__(self):
        return "#{} {} {} distress: {} msg: {}".format(
            self.index,
            self.date_time,
            self.location,
            self.distress_level,
            self.message
        )
    
    def get_keyword(self):
        return self.keyword
    
    def get_location(self):
        return self.location
    
    def get_date_time(self):
        return self.date_time
    
    def get_distress_level(self):
        return self.distress_level

    def get_msg(self):
        return self.message
    
    def get_index(self):
        return self.index
    

# Module functions ----------------------------------------------------------------------