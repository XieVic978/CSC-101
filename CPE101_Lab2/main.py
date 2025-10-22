# This is a header block example for lab 2.
# You will need to supply the following information.

# Name:
# Section:

# Create a welcome message
# Input: a name as a string
# Result: a string
def welcome_message(name : str) -> str:
   message = "Hello, " + name + "."
   return message

message = welcome_message("vyxie@calpoly.edu")
print (message)
    #1. We are using the addition operator in this example. In other words String Concatenation. 