"""
Lab # 4
"""

import random

def main():
    print("Welcome to Evader!")
    print("You and your crew of street racers are trying to make it back to the garage while evading the police.")
    print("The police will do whatever it takes to catch you!")
    print("Do you have what it takes to run these streets?")

    #variables
    miles_traveled = 0
    car_damage = 0
    pursuing_cops = -20

    # Boolean data type.

    done = False
    while not done:
        print("A. Drive as fast as possible.")
        print("B. Drive at the speed of traffic.")
        print("C. Stop and hide.")
        print("D. Fix the car.")
        print("E. Status check.")
        print("Q. Quit")

        user_input = input("What is your choice? ")

        # Quit
        if user_input.upper() == "Q":
            print("Thank you for playing!")
            done = True

        # Status check
        elif user_input.upper() == "E":
            print("Miles traveled: " + str(miles_traveled))
            print("Car damage: " + str(car_damage))
            print("The cops are " + str(miles_traveled - pursuing_cops) + " miles behind you.")

        # Fix the car
        elif user_input.upper() == "D":
            car_damage = 0
            print("The car was fixed.")
            pursuing_cops = pursuing_cops + random.randrange(7, 15)

        # Stop and hide
        elif user_input.upper() == "C":
            print("The cops are looking for you in your last known location.")
            pursuing_cops = pursuing_cops + random.randrange(7, 15)

        # Ahead full speed
        elif user_input.upper() == "A":
            print("Driven like a true champ, just be aware of the damage to the car.")
            print("Miles driven: " + str(miles_traveled + random.randrange(10,21)))
            car_damage = car_damage + random.randrange(10, 26)
            pursuing_cops = pursuing_cops + random.randrange(7, 15)
            oasis = random.randrange(1, 21)

        # Ahead moderate speed
        elif user_input.upper() == "B":
            print("Your car thanks you, but the cops are catching up now.")
            print("miles traveled: " + str(miles_traveled + random.randrange(5, 13)))
            pursuing_cops = pursuing_cops + random.randrange(7, 15)
            car_damage = car_damage + random.randrange(5, 16)
            oasis = random.randrange(1, 21)

        if oasis == 20:
            car_damage = 0
            print("You have found an oasis! Your car's damage has been fully fixed.")
        if pursuing_cops >= 15:
            print("The cops are getting close!")
        if miles_traveled >= 200 and not done:
            print("You have successfuly evaded the cops and made it back to your garage.")
            print("Slick wheel work!")
            done = True
        if pursuing_cops >= miles_traveled:
            print("The cops have caught you!")
            print("You are going to jail!")
            done = True
        if car_damage >= 60 and not done:
            print("Your car is in bad shape. It needs fixed.")
        if car_damage >= 100:
            print("Your car has broken down. You are going to jail!")
            done = True

main()