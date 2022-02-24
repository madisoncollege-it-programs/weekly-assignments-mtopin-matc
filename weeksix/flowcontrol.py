#!/usr/bin/env python3 

# Madison Topin
# This Is A Flow Control Lab Involving Selecting Different Doors And Options

print("""You Enter A Dark Room With Three Doors. 
Do You Go Through Door #1, Door #2, Or Door #3?""")


door = input("-> ")

# == Door Number 1 logic =======================
if door == "1":

    print("There's A Very Confused Looking Bear Here Eating A Cheese Cake.")
    print("What Do You Do?\n")

    print("1. Take The Cake.")
    print("2. Scream At The Bear.")
    print("3. Ask Politely To Share.")
    # == Bear logic ============================
    bear = input("-> ")

    if bear == "1":
        print("1) The Bear Is Sad Because You Stole Its Cake... You Are Bad And You Should Feel Bad!")
    elif bear == "2":
        print("2) The Bear Is Sad Because You Screamed At It... You Are Bad And You Should Feel Bad!")
    elif bear == "3":
        print("3) The Bear Is Kind And Shares Some Cheese Cake With You. It's Also No Longer Confused")
    else:
        print(f"{bear}?) Well, Doing {bear} Wasn't A Choice... Now The Bear Is Even More Confused.")
        print("Bear Tells You To Start Over And Follow The Options This Time Dummy.")

# == Door Number 2 Logic =====================
elif door == "2":
    print("You See The Eye Of Cthulu Staringg Back At You.\n")
 
    print("1. Poke Cthulu In The Eye.")
    print("2. Clap Your Hands In Front Of The Eye To Try And Make It Blink.")
    print("3. Have A Staring Contest.")
 # == Insanity Logic ======================
    cthulu = input("-> ")

    if cthulu == "1" or cthulu == "2":
        print(f"{cthulu}) That Was Kind Of Mean... You Shouldn't Have Done That...")
        print("ZAP!")
    elif cthulu == "3":
        print(f"{cthulu}) You Win The Staring Contest! Cthulu Is So Impressed He Gives You Godlike Powers!")
        print("Good job!")
    else:
        print(f"{cthulu}?) Cthulu Doesn't Think That Was An Option...Confusion Ensues")
# == Door Number 3 Logic ================
elif door == "3":
    print("You Enter A Room Containing Three Small Balls Of Different Colors.\n")

    print("1. Pick Up Blue Ball")
    print("2. Pick Up Red Ball")
    print("3. Pick Up Green Ball")
 # == Ball Logic =====================
    ball = input("-> ")

    if ball == "1":
        print("1) You Chose The Blue Ball And Gained The Power Of Water!")
    elif ball == "2":
        print("2) You Chose the Red ball And Gained the Power Of Fire!")
    elif ball == "3":
        print("3) You Chose The Green Ball And Gained the Power Of Earth!")
    else:
        print("You Tried To Pick Up A Ball That Doesn't Exist And Have No Ball... How Sad!")

else:
    print("You Did Not Select A Door... What Is Your Problem? Are You Trying To Break This? Jerk!")
