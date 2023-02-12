import Master
import Profiles
import Signals
import DatabaseControl
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

# Module functions ----------------------------------------------------------------------

# Print all profiles from the database to console.
def print_profiles(profiles_db):
   for profile in profiles_db:
      print(profile)
   return

# Drive code ----------------------------------------------------------------------------

# Read in the current database and store it in a 2D array
db_path = '/Users/noahflood/Downloads/AU Hackathon/GlassCell-repo/serverside-data/glassCells-database.csv'
glassCells_database = DatabaseControl.read_in_database(db_path)

# print new database to console
print_profiles(glassCells_database)

# print existing database to a new csv file as a test
db_path2 = '/Users/noahflood/Downloads/AU Hackathon/GlassCell-repo/serverside-data/glassCells-database2.csv'
DatabaseControl.rewrite_database(glassCells_database, db_path2)






# perpetual loop of reading new requests

# send requests to master

# add profiles as necessary
