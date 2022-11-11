import numpy as np
import datetime as dt

restart = "yes"
while restart == "yes": 

    width = int(input("Enter the width of the tire in mm (ex 205): "))
    aspect = int(input("Enter the aspect ratio of the tire (ex 60): "))
    diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))
    date = dt.datetime.now()
    volume = round(float((np.pi*(width**2)*aspect*(width*aspect+2540*diameter))/(10000000000)),2)

    print(f'\nThe approximate volume is {volume} liters')

    with open("volumes.txt", "at") as volume_file:
        print(f"{date:%Y-%m-%d}, {width}, {aspect}, {diameter}, {volume}")


    # Read last two lines or restart process (My personalized addition)

    #with open("volumes.txt") as v:
        #lines = v.readlines()
        #print(f'\nHistory: \n\n{lines[-2]} \n{lines[-1]}')

    restart = input("Restart process? (yes/no): ")
    print()

if restart != "yes":
    print("Have a nice day!")




