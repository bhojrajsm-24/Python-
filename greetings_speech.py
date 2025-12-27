# import time

# name = input("enter your name :- ")

# gender = input("enter your gender :-")

# timeNow = int(time.strftime('%H%M%S'))

# if (timeNow < 120000):
#     if (gender == male):
#         print("Good Morning ",name ,"  sir. ")
#     else :
#         print("Good Morning ",name ,"  ma'am. ")    
# elif (timeNow < 180000):
#     if (gender == "male"):
#         print("Good Afternoon ",name ,"  sir. ")
#     else :
#         print("Good Afternoon ",name ,"  ma'am. ")
# elif (timeNow < 210000):
#     if (gender == "male"):
#         print("Good Evening ",name ,"  sir. ")
#     else :
#         print("Good Evening ",name ,"  ma'am. ")
# else :
#     if (gender == "male"):
#         print("Good Night",name ,"  sir. ")
#     else :
#         print("Good Night",name ,"  ma'am. ")

import time
import pyttsx3

# Initialize engine
engine = pyttsx3.init()

name = input("Enter your name: ")
gender = input("Enter your gender (male/female): ").lower()

timeNow = int(time.strftime('%H%M%S'))

if timeNow < 120000:
    greeting = "Good Morning"
elif timeNow < 170000:
    greeting = "Good Afternoon"
elif timeNow < 210000:
    greeting = "Good Evening"
else:
    greeting = "Good Night"

# Message banake
if gender == "male":
    message = f"{greeting}, {name} sir. \n how are you !!!"
else:
    message = f"{greeting}, {name} ma'am. \n how are you !!! "

# Print + Speak
print(message)
engine.say(message)
engine.runAndWait()
