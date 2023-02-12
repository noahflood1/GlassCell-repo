import csv
import random
import requests
'''Create, store, access, and return unique keys using a CSV file.
'''

'''
Define a class that contains all the necesssary information for key generation.

@param string dictionary_url ---- the URL of the dictionary API
@param string keys_path ---- the path of where the keys storage file is located
@param NULL master_keys ---- the working file of user keys that gets read in and exported
'''
class KeyMaker:
    def __init__(self, keys_path, dictionary_url, master_keys=None):
       self._keys_path = keys_path
       self._dictionary_url = dictionary_url
       self._master_keys = []

    # Function to read in keys that are stored in the csv file
    def read_in_keys(self):
        # working dictionary of keys
        user_keys = []

        # read in keys from file
        with open(self._keys_path, 'r') as file:
            reader = csv.reader(file)
            for line in reader:
                user_keys.append(line[0])

        # make local assignment
        self._master_keys = user_keys
    
    # Generate and return new keywords, that are not necessarily unique.
    def generate_keyword(self):
        # Get the list of words from the dictionary API
        words = requests.get(self._dictionary_url).text.splitlines()
        word = random.choice(words)
        number = str(random.randint(0, 999)).zfill(3)
        keyword = (word + number)
        return keyword

    # Update master_keys with a new key, also rewrites the file
    def update_key_list(self, new_key):
        self._master_keys.append(new_key)
        # Open the file in write mode
        with open(self._keys_path, 'w', newline='') as file:
        # Write the contents of the array into the file
            for item in self._master_keys:
                file.write(item + '\n')

        # Verify the contents of the file
        print("NEW CONTENTS OF THE FILE: ")
        with open(self._keys_path, 'r') as file:
            contents = file.read()
            print(contents)
    
    # Getter for the master_keys list
    def get_key_list(self):
        return self._master_keys
    
# MODULE FUNCTIONS ----------------------------------------------------------------------

# when called, reads in all keys, adds a new key, and updates file
def new_key_process():
    # Instantiate a KeyMaker that will work for all of our cases-----------------------------
    keys_path = "/Users/noahflood/Downloads/AU Hackathon/GlassCell-repo/serverside-data/glassCells-data.csv"
    dictionary_url = "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"

    # Create the object and read-in from file
    master_key_maker = KeyMaker(keys_path, dictionary_url)
    master_key_maker.read_in_keys()

    # Generate a new keyword and add it to the list, then update the file
    while True:
        new_keyword = master_key_maker.generate_keyword()
        if new_keyword not in master_key_maker.get_key_list():
            master_key_maker.update_key_list(new_keyword)
            print("NEW KEYWORD ADDED: " + new_keyword)
            break
