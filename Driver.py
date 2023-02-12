from Profile import Profile
import Keys
# Driver file
# *  Handles all requests at all times.
# *  Provides and passes data to the glassCell() function.
# 
# Signal path: 
#      Profile.py --> 
#         Signals.py --> 
#            returns signal to Profile.py -->
#               --> utilizes DatabaseControls.py again to add profile.
#   --> (multiple accesses) DatabaseControls.py
#   --> return to master GlassCell.py function call
#      --> return to Driver signal call, begin next signal.
#
# *  Profile.py creates new keys and asks Signals.py for a new signal value to enter into database.
# *  Other parameters from driver file include information for site_controls, which are sent to
#   SiteControl.py

# Generate a new key
Keys.new_key_process()
