# Name: Sawao Kato - Anna Hauer, Brooke Pohlman, Riley Clayton, and Sabrina Harrington
# email: hauerac@mail.uc.edu, pohlmabe@mail.uc.edu, claytorm@mail.uc.edu, & harrinsr@mail.uc.edu
# Assignment Title: Assignment 10
# Course: IS 4010
# Semester/Year: Spring 2023
# Brief Description: In this assignment we modified the PyDev project we created in class to make an API call with a URL.
# Citations:
# Anything else that's relevant: Group Assignment

#function.py

def iterate_dictionary(myDictionary, keys_print=None):
    for k, v in myDictionary.items():
        if keys_print is None or k in keys_print:
            print("{0} : {1}".format(k, v))
        if isinstance(v, dict):
            iterate_dictionary(v, keys_print)
        elif isinstance(v, list):
            for vv in v:
                if (isinstance(vv, dict)):
                        iterate_dictionary(vv, keys_print)