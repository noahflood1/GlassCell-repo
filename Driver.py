from Profiles import Profile
import Keys
'''
Driver file.

Handles all requests from website, app, and other input from vocal assistants
like Amazon Alexa 

Creates new signals from the input recieved at any given time.

Those signals are processed in Profiles.

Profiles use new keys.

Site controls 
'''

# Generate a new key
Keys.new_key_process()