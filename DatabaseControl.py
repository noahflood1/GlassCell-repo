# Bottom level processes; verifies requests and modifies database accordingly. Parses database.
# The database uses nested dictionaries.
import csv
import re
import random
import requests
import Profiles
import Signals

# Module functions ----------------------------------------------------------------------

# reads the database into program and stores profiles in Driver.py
def read_in_database(file_path):
   profiles_database_array = []

   # for every row, create a new profile object
   with open(file_path, 'r') as file:
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

            
   
   # for every profile object, give it subsequent signal objects
   return profiles_database_array

# Called frequently, after every modification to the database
def rewrite_database():
   return 

# Returns a profile object by parsing a line of the database given a keyword
def add_profile(new_profile):
   return

# Returns a profile object by parsing a line of the database given a keyword
def get_profile(keyword):
   return

# Adds a signal to the specified profile 
def add_signal(keyword, signal):
   return

def check_profile_existence(profile_obj):
   return

def get_profile_index(profile_obj):
   return