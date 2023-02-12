# Master function calls. Uses glassCell(), which is the form of an incoming request that instantiates subclasses.
import Profiles
import DatabaseControl
import SiteControl

# Master class which is instantiated and called in the driver file when a request comes in from the website.
# *As of now, requests can only be made from the driver file and output can be printed to the screen.
#
# Client-side and Driver.py are responsible for specifying information.
# 
# A Glass Cell == a request.
#
class GlassCell:
   default_message = "Please help! I am in danger."

   def __innit__(self, location, signal_date_time, keyword='unspecified', distress_level=3, message=default_message, signal_index=None):
      self.location = location
      self.date_time = signal_date_time
      self.keyword = keyword
      self.distress_level = distress_level
      self.message = message
      self.signal_index = signal_index

      def get_keyword(self):
         return self.keyword
        
   # based on input data, create a function that assigned the signal
   # the correct index and identifies the screen name.
   # perhaps, do this in profile() since it is responsible for creation of profiles

# Module functions-----------------------------------------------------------------------

def glassCell(new_GlassCell_request):
   posed_keyword = new_GlassCell_request.get_keyword()

   # Check and apply for noniexstent key
   if(posed_keyword == 'unspecified' or DatabaseControl.check_profile_existence(posed_keyword) == False):
      if(posed_keyword != 'unspecified'):
         SiteControl.broadcast_nonexistant_key(posed_keyword, "Key not heard")
      if(posed_keyword == 'unspecified'):
         SiteControl.broadcast_nonexistant_key(posed_keyword, "Key not heard")
   
   # create new profile, signal or add to existing one using logic and DatabaseControls.py
   return
