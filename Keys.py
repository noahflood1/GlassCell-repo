import csv
import random
import requests
'''Create new keys
'''

'''
Define a class that contains all the necesssary information for key generation.

@param string dictionary_url ---- the URL of the dictionary API
@param NULL master_keys ---- the working file of user keys that gets read in and exported
'''
class KeyMaker:
    def __init__(self, dictionary_url, master_keys=None, master_screennames=None):
       self.dictionary_url = dictionary_url
       self.master_keys = master_keys
       self.master_screennames = master_screennames

    # Function to read in existing keys
    def read_in_keys(self, master_profiles_array):
        # temp array
        existing_keys = []

        # read in keys from all profiles
        for profile in master_profiles_array:
            existing_keys.append(profile.get_keyword())

        # make local assignment
        self.master_keys = existing_keys
    
    # Function to read in existing screen names
    def read_in_screen_names(self, master_profiles_array):
        # temp array
        existing_screen_names = []

        # read in keys from all profiles
        for profile in master_profiles_array:
            existing_screen_names.append(profile.get_screen_name())
        
        # make local assignment
        self.master_screen_names = existing_screen_names
    
    # Generate keys to be used in different scenarios, that are not necessarily unique.
    def generate_key(self):
        # Get the list of words from the dictionary API
        words = requests.get(self.dictionary_url).text.splitlines()
        word = random.choice(words)
        number = str(random.randint(0, 999)).zfill(3)
        keyword = (word + number)
        return keyword
    
    # Getter for the master_keys list
    def get_key_list(self):
        return self._master_keys
    
# MODULE FIELDS ------------------------------------------------------------------------
dictionary_url = "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"
    
# MODULE FUNCTIONS ----------------------------------------------------------------------

# Instantiate a KeyMaker that will work for all of our cases
# when called, reads in all keys and generates a new key
def new_key_process(master_profiles_array):

    # Create the object and read-in from database
    master_key_maker = KeyMaker(dictionary_url)
    master_key_maker.read_in_keys(master_profiles_array)

    # Generate a new keyword and add it to the list because why not
    while True:
        new_keyword = master_key_maker.generate_key()
        if new_keyword not in master_key_maker.get_key_list():
            print("New Keyword Added!\n" + new_keyword)
            break
    
    return new_keyword

# Repeat, but for unique screen names
def new_screen_name_process(master_profiles_array):
    # Create the object and read-in from database
    master_screen_name_maker = KeyMaker(dictionary_url)
    master_screen_name_maker.read_in_screen_names(master_profiles_array)

    # Generate a new keyword and add it to the list because why not
    while True:
        new_screen_name = master_screen_name_maker.generate_key()
        if new_screen_name not in master_screen_name_maker.get_key_list():
            print("New Screen Name Added!\n" + new_screen_name)
            break
    
    return new_screen_name
