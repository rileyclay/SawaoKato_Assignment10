# Name: Sawao Kato - Anna Hauer, Brooke Pohlman, Riley Clayton, and Sabrina Harrington
# email: hauerac@mail.uc.edu, pohlmabe@mail.uc.edu, claytorm@mail.uc.edu, & harrinsr@mail.uc.edu
# Assignment Title: Assignment 10
# Course: IS 4010
# Semester/Year: Spring 2023
# Brief Description: In this assignment we modified the PyDev project we created in class to make an API call with a URL.
# Citations:
# Anything else that's relevant: Group Assignment

# main.py

import requests
import json
from functionPackage.function import *

# build a URL with a data request and submit to server
response = requests.get('https://api.nasa.gov/planetary/apod?api_key=IYW7DEdA6tFlrPPjXbIr3KDel9ncY8xA6QTRTgW1')
json_string = response.content

# converting into a dictionary
dictionary = json.loads(json_string)

# extract interesting data
keys_print = ["explanation"]
iterate_dictionary(dictionary, keys_print)
