from Profiles import Profile
import time
import requests

'''Process new signal requets from the website.
For now, the driver program serves as input from the website.
'''





'''
A signal contains info sent from the client at websites. It must be parsed and processed.
Signals will be broadcast based on keyword.

SIGNALS.PY handles signals and processing in database.s

explicity from client:
    keyword: can be specific or empty
    healthbar: can be a number 1-5 or empty
    message: can be empty, is set to something generic of not specified

sourced from client:
    location data: necesssary, without it cannot broadcast. need to process both cases

'''
class Signal:
    def __init__(self, keyword, healthbar, message):
        self._keyword = keyword
        self._keyword = keyword
        self._healthbar = healthbar
        self._message = message
    
    def broadcast():
        # send
        return