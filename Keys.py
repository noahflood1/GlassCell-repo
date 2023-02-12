import csv

'''
Create, store, access, and return unique keys using a CSV file.
'''

# csv file where user keys are stored. store on gitHub later
keys_path = ""

# define a function to generate a new key and make sure it is unique

# define a function to define and create a new user number

'''
Reads in keys from csv file.
'''
def read_in_keys():
   # working dictionary of keys
   user_keys = []

   # read in
   with open(keys_path, 'r') as file:
    reader = csv.reader(file)
    for line in reader:
        for header, value in row.items():
            keys[header] = value 

   
   # return result
   return user_keys