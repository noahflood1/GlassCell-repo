from Profiles import Profile
import Keys
'''
Driver file.
*  Handles all requests at all times.
*  Provides and passes data to the glassCell() function.
*  Signal path: Master.py --> Profile.py --> Signals.py --> (retun signal to Profile.py) --> (return to master function call)
*  Profile.py creates new keys and asks Signals.py for a new signal value to enter into database.
*  Other parameters from driver file include information for site_controls, which are sent to
   SiteControl.py
'''

# Generate a new key
Keys.new_key_process()
