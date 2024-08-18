import DatabaseControl
# Handles all site changes.

# Module functions ----------------------------------------------------------------------

# tell user if they specify a key in their signal request but it doesn't exist.
def broadcast_nonexistant_key(posed_key, flag):
   if(flag == 'unfound'):
      print("Specified key does not exist. Broadcast overwritten with new key: [insert new keyword created here]", )
   if(flag == 'new'):
      print("Keyword unspecified. [insert new keyword created here]")

def display_current_profiles():
   # for ever profiles in the database, only display current ones that are not older than 1 year.
   # those can be accessed later in a list form.
   #
   # for now, displays profiles screen name and previous locations in console
   print("\n")
   current_profiles = DatabaseControl.get_current_profiles()
   for profile in current_profiles:
      print("\n\n")
      signals_string = ""
      for signal in profile.get_signals_arr():
         signal_string = signal_string + signal.get_location() + ", "
      print("Profile: " + profile.get_screen_name() + "Current location: " + profile.get_current_location() + "Previous Locations: ")

   # connects to Google Maps API later.....

# sends commands to site to change pages and stuff based on criteria, not yet known
def change_page():
   return