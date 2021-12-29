#Andy Pen
#simple password genrator python program that creates passwords
#based on the length and amount of passwords the user wants
#uses strings and nested for loops

import random

random_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12345789!$"


password_len = int(input("What length would you like your password to be? Suggested length would be at least 8 characters. "))
password_count = int(input("How many passwords would you like to generate? "))
for x in range(0,password_count):
    password = ""
    for x in range(0,password_len):
        password_char = random.choice(random_characters)        #selects random character from char string
        password = password + password_char
    print("Here are the random generated password/passwords : ", password)
