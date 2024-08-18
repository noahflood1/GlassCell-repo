# Bottom level processes; verifies requests and modifies database accordingly. Parses database.
# The database uses nested dictionaries.
import csv
import re
import datetime
import random
import requests
import Profiles
import Signals
import SiteControl

# Fields -------------------------------------------------------------------------------

# you must change this to the path that you are using

DB_PATH = '/Users/noahflood/Library/CloudStorage/OneDrive-AuburnUniversity/Auburn University/ACM/Auburn Hacks 2023/GlassCell-repo/serverside-data/glassCells-database.csv'
profiles_database_array = [] #MASTER DATABASE VARIABLE

# Module functions ----------------------------------------------------------------------

# reads the database into program and stores profiles in Driver.py
def read_in_database():

   # for every row, create a new profile object
   with open(DB_PATH, 'r') as file:
      reader  = csv.reader(file)
      for row in reader:
         keyword = row[0].strip()
         screen_name = row[1].strip()
         creation_date = row[2].strip()
         recent_location = row[3].strip()

         # remaining items are arrays representing signal object parameters
         signal_objects_array = []

         # for every signal specified in the row
         for i in range(4, len(row) - 1):
            signal_string = row[i].strip(" [] ")
            signal_params_array = signal_string.split(";")

            index = signal_params_array[0].strip()
            location = signal_params_array[1].strip()
            date_time = signal_params_array[2].strip()
            distress = signal_params_array[3].strip()
            msg = signal_params_array[4].strip()
            
            new_signal = Signals.Signal(
                  keyword=keyword,
                  location=location,
                  date_time=date_time,
                  distress_level=distress,
                  message=msg,
                  index=index)

            signal_objects_array.append(new_signal)
         
         # finally, instantiate a new Profile object
         new_profile = Profiles.Profile(
               keyword=keyword,
               screen_name=screen_name,
               creation_date=creation_date,
               recent_location=recent_location,
               signals_arr=signal_objects_array)

         # most finally, add the profile object to the database_array that will be returned from this file
         profiles_database_array.append(new_profile)
         
   return profiles_database_array

# Called frequently, after every modification to the database.
def rewrite_database(file_path, profiles):


   with open(file_path, 'w') as f:
        for profile in profiles:
            
            # avoid a string concatenation error by just overwriting a NoneType with a MISSING_VALUE indicator
            if profile.get_recent_location() is None:
               profile_str = profile.get_keyword() + ', ' + profile.get_screen_name() + ', ' + profile.get_creation_date() + ', ' + "MISSING_LOCATION_VALUE"
            else:
               profile_str = profile.get_keyword() + ', ' + profile.get_screen_name() + ', ' + profile.get_creation_date() + ', ' + profile.get_recent_location()
            
            for signal in profile.get_signals_arr():
               profile_str += ', ' + '[{}; {}; {}; {}; {}]'.format(signal.get_index(), signal.get_location(), signal.get_date_time(), signal.get_distress_level(), signal.get_msg())
            f.write(profile_str + '\n')
   print("Success: Database overwritten with master profile array.")


# Returns a profile object by parsing a line of the database given a keyword
def add_profile(new_profile):
   return

# Returns a profile object by parsing a line of the database given a keyword
def get_profile(keyword):
   return

# Adds a signal to the specified profile 
def add_signal(keyword, signal):
   return

# important: get's the current profiles from the array 
def get_current_profiles():
   current_profiles = []
   read_in_database()
   for profile in profiles_database_array:
      date_str = profile.get_creation_date()
      date_object = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
      # Get the current date and time
      now = datetime.datetime.now()

      # Calculate the difference between the two dates
      difference = now - date_object

      # Check if the difference is less than one year (365 days)
      if difference < datetime.timedelta(days=365):
         current_profiles.append(profile)
      
      return current_profiles

# Checks if a profile exists in the database when given a keyword
def check_profile_existence(keyword):
   for profile in read_in_database():
      if(profile.get_keyword() == keyword):
         return True
   return False