# Master function calls. Uses glassCell(), which is the form of an incoming request that instantiates subclasses.
import Profiles
from Profiles import Profile
import DatabaseControl
import SiteControl
from DatabaseControl import profiles_database_array

# Master class which is instantiated and called in the driver file when a request comes in from the website.
# *As of now, requests can only be made from the driver file and output can be printed to the screen.
#
# Client-side and Driver.py are responsible for specifying information.
# 
# A Glass Cell == a request.
#
class GlassCell:
   default_message = "Please help! I am in danger."

   def __init__(self, location, signal_date_time, keyword='unspecified', distress_level=3, message=default_message, signal_index=None):
      self.location = location
      self.date_time = signal_date_time
      self.keyword = keyword
      self.distress_level = distress_level
      self.message = message
      self.signal_index = signal_index

      def get_keyword(self):
         return self.keyword
      
      def get_location(self):
         return self.location
      
      def get_signal_date_time(self):
         return self.signal_date_time
      
      def get_distress_level(self):
         return self.distress_level
      
      def get_msg(self):
         return self.message
        
   # based on input data, create a function that assigned the signal
   # the correct index and identifies the screen name.
   # perhaps, do this in profile() since it is responsible for creation of profiles

# Module functions-----------------------------------------------------------------------

# create new profile, signal or add to existing one using logic and DatabaseControls.py
def glassCell(new_GlassCell_request):
   posed_keyword = new_GlassCell_request.keyword
   print("POSED KEYWORD: " + posed_keyword)

   # Check and apply for noniexstent key
   if(posed_keyword == 'unspecified' or DatabaseControl.check_profile_existence(posed_keyword) == False):
      if(posed_keyword != 'unspecified'):
         SiteControl.broadcast_nonexistant_key(posed_keyword, "unfound")
      if(posed_keyword == 'unspecified'):
         SiteControl.broadcast_nonexistant_key(posed_keyword, "new")

   #apply case that key DOES EXIST:
   #TODO
   if(DatabaseControl.check_profile_existence(posed_keyword) == True):

      #add a new signal to existing profile, update database

       # confirm to console
      print("Success! New signal added to exisitng profile: ")
      print("[INSERT HERE]")

      # finally, rewrite file based on master_profile_array
      DatabaseControl.rewrite_database()
   
   else: #create a new profile, add signals, update database

      #creation statement, comes from Profile.py, uses the request obj
      new_profile = Profiles.create_new_profile(new_GlassCell_request)

      # add the new profile to the master_profile_array
      profiles_database_array.append(new_profile)

      # confirm to console
      print("Success! New profile added to master profile array: ")
      print(new_profile)

      # finally, rewrite file based on master_profile_array
      DatabaseControl.rewrite_database()