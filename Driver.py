import Master
import Profile
import Signal
import DatabaseControls
import SiteControl
# Description
# -----------
# *  Handles all requests at all times.
# *  Provides and passes data to the glassCell() function.
# *  Handles top-level management of all processes
# *  Sends site changes to live, such as updating the website with current signals.
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
#    SiteControl.py
#
# Data Collection
# ---------------
# explicity from client:
#    keyword: can be specific or empty
#    distress_level: can be a number 1-5 or empty
#    message: can be empty, is set to something generic of not specified
#
# implicit from client:
#    location: necesssary, without it cannot broadcast. need to process both cases
#    date & time: necessary, can be accessed from server side if needed.
#
#    signal index: derived on client side
#
# Website

# Generate a new key
Keys.new_key_process()
