import time
import requests

# Signal.py takes parameters from original request --> Master --> Profile and creates a new signal object.
# It must check the database returns that ob

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