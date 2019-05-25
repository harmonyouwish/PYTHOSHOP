"""
A simple photo editing program
"""

from __future__ import print_function
from PIL import Image
import os
import time

os.system('cls')
print("Welcome to Pythoshop! Edit your photoSSS now.\nEnter the file name of the image you want to edit.\nYour file should be '.jpg' but give us just name")
file_name = input()
im = Image.open(file_name+".jpg")
time.sleep(3)
print("Approved. File properties are: ", im.format, im.size, im.mode)
im.show()
while True:
    print("Try...\nRotating it (1) or\nChanging the size (2) or\nAdding black & white filter (3) and...\nSave your results! (4)\nLeave the program (5)")
    resp = input()
    if resp == '1':
        print("90? 180? 270 degrees?")
        resp2 = input()
        if resp2 == '90':
            im = im.rotate(90)
            time.sleep(2)
            print("Done!")
            im.show()
        elif resp2 == '180':
            im = im.rotate(180)
            time.sleep(2)
            print("Done!")
            im.show()
        elif resp2 == '270':
            im = im.rotate(270)
            time.sleep(2)
            print("Done!")
            im.show()
        else:
            print("Try entering one of the numbers.")
    #elif resp == '2':

    elif resp == '3':
        im2 = im
        while True:
            decision = input("To add black & white filter choose (a), \nto stay in colour/remove black & white filter choose (b) and \nto end changing filters choose (c)\n")
            if decision == 'a':
                im2 = im.convert("L")
                time.sleep(2)
                print("Done!")
                im2.show()
            elif decision == 'b':
                im2 = im.convert("RGB")
                time.sleep(2)
                print("Done!")
                im2.show()
            elif decision == 'c':
                time.sleep(2)
                print("Done!")
                break
            else:
                print("Wrong character, try again.")
        im = im2

    elif resp == '4':
       decision = input("Would you like to rewrite your file (1), or save it as a new one (2)?\n")
        if decision == "1":
            im.save(file_name+'.jpg')
            print("Done!")
        elif decision == "2":
            output_name = input("How would you like to name your file?\n")
            im.save(output_name+'.jpg')
            print("Done!")
        else:
            print("Unknown input, try again")

    elif resp == '5':
        print("Hope you enjoyed it. Bye!")
        break
    else:
        print("Don't know what you talkin' bout.")
