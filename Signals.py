# Signal.py takes parameters from original request --> Master --> Profile and creates a new signal object.
# It must call from DatabaseControls.py before processing signal to check existance and index.
import time
import requests
import DatabaseControl
import Profiles

# Every signal contains nested dictionaries
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
    
# Module functions ----------------------------------------------------------------------