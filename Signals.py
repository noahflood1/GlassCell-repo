# Signal.py takes parameters from original request --> Master --> Profile and creates a new signal object.
# It must call from DatabaseControls.py before processing signal to check existance and index.
import time
import requests
import DatabaseControl

class Signal:
    def __init__(self, location, date_time, keyword, distress_level, message):
        self.location = location
        self.date_time = date_time
        self.keyword = keyword
        self.keyword = keyword
        self.healthbar = distress_level
        self.message = message
    
    def broadcast():
        # send
        return
    
# Module functions ----------------------------------------------------------------------