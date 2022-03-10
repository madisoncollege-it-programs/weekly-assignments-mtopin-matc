#!/usr/bin/env python3

# Author: Madison Topin
# This Script Will Make A Mini Interactive Sequence Of Events Inspired By Jurassic Park
# It Will Simulate Password Protection With Limited Attempts, And If Succesful Will Allow Commands
print("Name: Madison Topin")


# Establish Our Lists For Login Info And Commands
password_database = {"Username":"dnedry",
                     "Password":"please"}

command_database = {"reboot":"OK. I Will Reboot All Park Systems.",
                    "shutdown":"Ok. I Will Shut Down All Park Systems.",
                    "done":"I Hate All This Hacker Stuff."} 

# Establish Our Variables
white_rabbit_object = 0
counter = 0
othercounter = 0

# Our While Loop For Logging In
while (white_rabbit_object == 0) and (counter < 3):
    input_user = input("Username: ")
    input_password = input("Password: ")
    if (input_user == password_database["Username"]) and (input_password == password_database["Password"]):
        white_rabbit_object = 1
    else:
        counter += 1
        print(f"You Didn't Say The Magic Word: {counter}")

# After A Succesful Login You Can Input Commands Or Trigger Lysine Contingency With A Wrong Input
if white_rabbit_object == 1:
    print("Hi Dennis. You're Still The Best Hacker In Jurassic Park.")
    input_command = input("Please Enter A Command (reboot, shutdown, done): ")
    if input_command in command_database:
        print(f"{command_database[input_command]}")
    else:
        print("The Lysine Contingency Has Been Put Into Effect")
# After 3 Failed Login Attempts
elif counter == 3:
    for i in range(25):
        print ("You Didn't Say The Magic Word!")
# Fail Safe
else:
    print("Something Went Horribly Wrong, You Should Literally Never See The Result Of This Else Statement")














# Trial And Error Stuff I Did Not End Up Using

#for userkey in password_database.keys():
 #       if userkey == "Username":
  #          if input_user == password_database.values():
   #             for passkey in password_database.keys():
    #                if passkey == "Password":
     #                   if input_password == password-database.values():
      #                      white_rabbit_object = 1
       #                 else:
        #                    counter += 1
         #                   print(f"You Didn't Say The Magic Word: {counter}")
          #  else:
           #     counter += 1
            #    print(f"You Didn't Say The Magic Word: {counter}")
