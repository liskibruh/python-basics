"""
The atexit module in Python provides a simple way 
to register functions to be called when a program is exiting
"""

import atexit

some_list = list(range(1,100))

def cleanup(some_list):
	print ("Cleaning up..")
	del some_list

atexit.register(cleanup, some_list)