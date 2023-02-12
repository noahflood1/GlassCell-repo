# Signal.py takes parameters from original request --> Master --> Profile and creates a new signal object.
# It must call from DatabaseControls.py before processing signal to check existance and index.
import time
import requests
import DatabaseControls

class Signal:
    def __init__(self, keyword, healthbar, message):
        self._keyword = keyword
        self._keyword = keyword
        self._healthbar = healthbar
        self._message = message
    
    def broadcast():
        # send
        return