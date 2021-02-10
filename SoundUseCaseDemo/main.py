#!/usr/bin/python3

import demo_1_dowload as dm1
import demo_2_start_and_shutdown as dm2

dictionary_of_demos = {
    1: dm1.execute_demo1,
    2: dm2.execute_demo2
}

# Program start here
def main():
    main_loop()


# Function for looping the demos and selecting one of them
# Dosent brake until given input of 0
def main_loop():
    greeting_text()
    while True:

        try:
            demo_number = int(input("Demo to execute: "))
        except:
            print("Your input wasent correct! Try again...")
        
        if demo_number >= 1 and demo_number <= 4:
            print("Playing demo {} \n".format(demo_number))
            demo = dictionary_of_demos[demo_number]()
        elif demo_number == 0:
            goodbye()
            break
        


# Info texts about how to use the demo
# Excluded these to separate funtions to make the loop more clean
def greeting_text():
    print("\n-------------Sound demos for different use cases-------------\n")
    print("Hello and welcome to my simple program.")
    print("Just select number between 1 - 4 to run different demos")
    print("Selecting 0 will stop the program")
    print("")

def goodbye():
    print()
    print("Thank you for using demo")

if __name__ == "__main__":
    main()
