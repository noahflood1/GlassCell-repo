import Master
import Profiles
import Signals
import os
import datetime
import DatabaseControl
import SiteControl
import requests
import random
import string
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
#    signal index: derived on client side

# MODULE FIELDS ----------------------------------------------------------------------

# don't this API key with anyone or publicize this file yet since people could abuse it. I can figure out how to encrypt it later
NOAHS_GOOGLE_MAPS_API_KEY = 'AIzaSyCE_nCrG1MGT_TLMwqHYJAbwfP_z2MWZuI'
brownn_kopel = "Engineering Shops, 152 Wilmore Dr, Auburn, AL 36849" #Brown-kopel lol

#generate a random address in given state
# THIS DOESN'T WORK
def generate_random_address(state):
   # this random address thing never works
   # address = ''.join(random.choices(string.ascii_uppercase + string.digits, k=20))

   address = "Engineering Shops, 152 Wilmore Dr, Auburn, AL 36849"

   api_key = NOAHS_GOOGLE_MAPS_API_KEY

   # Make a request to the Google Maps Geocoding API
   url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}"
   response = requests.get(url)
   data = response.json()
   #print(data)

   # Check if the response is valid
   if data["status"] == "OK":
      for result in data["results"]:
         for component in result["address_components"]:
               if "administrative_area_level_1" in component["types"] and component["short_name"] == state:
                  print("New Address Pinged!", result["formatted_address"])
                  return result["formatted_address"]
   return None
    
# Accesses Google map's API to provide some "clientside" location data with a random address parameter
def get_coordinates(address):
   # The address you want to geocode
   api_key = NOAHS_GOOGLE_MAPS_API_KEY

   # Make a request to the Google Maps Geocoding API
   url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}"
   response = requests.get(url)
   data = response.json()
   #print(data)

   # Check if the response is valid and if the results list is not empty
   if data["status"] == "OK" and len(data["results"]) > 0:
      latitude = data["results"][0]["geometry"]["location"]["lat"]
      longitude = data["results"][0]["geometry"]["location"]["lng"]
      print("New location pinged!")
      print("Latitude:", latitude)
      print("Longitude:", longitude, "\n")
      return latitude +longitude
   else:
      print("Unable to retrieve latitude and longitude for the address.")


# Print all profiles from the database to console.
def print_profiles(profiles_db):
   for profile in profiles_db:
      print(profile)
   return

def get_example_time():
   # Get the current time
   now = datetime.datetime.now()

   # Format the date and time into a readable string
   readable_time = now.strftime("%Y-%m-%d %H:%M:%S")
   print("New time pinged!")
   print(readable_time, "\n")

   return readable_time

# DRIVER CODE ---------------------------------------------------------------------------

# Read in the current database, store it in the DatabaseControls.py module.
DatabaseControl.read_in_database()

# REQUEST EXAMPLES ----------------------------------------------------------------------

ex_address = "Engineering Shops, 152 Wilmore Dr, Auburn, AL 36849"
ex_location = get_coordinates(ex_address)
ex_time = get_example_time()

# New request: create a new profile that doesn't exist yet, and provides necessary parameters
NEW_REQUEST = Master.GlassCell(location=ex_location, signal_date_time=ex_time)
Master.glassCell(NEW_REQUEST)

# New request: create a new profile with specified keyword that just doesn't exist
NEW_REQUEST = Master.GlassCell(location=ex_location, signal_date_time=ex_time)
Master.glassCell(NEW_REQUEST)

# MORE EXAMPLES:
# New request: create a new profile with some necessary pamaters
# New request: create a new profile with some necessary pamaters (2)
# New request: create a new profile with some necessary pamaters (2)

#TODO
# perpetual loop of reading new requests from site

#TODO
# New request: Request to add a signal to a profile that already exists

# FINALIZATION/TESTING ------------------------------------------------------------------

# Print active profiles to console
SiteControl.display_current_profiles()

# print existing database to a new csv file as a test
# db_path2 = '/Users/noahflood/Downloads/AU Hackathon/GlassCell-repo/serverside-data/glassCells-database2.csv'
# DatabaseControl.rewrite_database(file_path=db_path2, profiles=glassCells_database)