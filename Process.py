from Profiles import Profile
import time
import requests

'''
Process control.
'''

#Defines request objects
class Request:
    def __init__(self, name, current_status, location, msg):
        self.name = name
        self.current_status = current_status
        self.time_of_creation = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        self.location = location
        self.message = msg


def upload_profile():
    new_user = Profile(name, status, location=None)

# Checks if the request includes a parameter at all or if it
# @param: boolean--inquire_parameterized
# @param: params--params for a new profile object
def process_request(inquire_parameterized, params):
    return
