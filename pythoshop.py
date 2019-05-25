from __future__ import print_function
from PIL import Image
import os
import time

os.system('cls')
print("Welcome to Pythoshop! Edit your photoSSS now.\nEnter the file name of the image you want to edit.")
file_name = input()
im = Image.open(file_name)
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
            im_mod = im.rotate(90)
            time.sleep(2)
            print("Done.")
            im_mod.show()
        elif resp2 == '180':
            im_mod = im.rotate(180)
            time.sleep(2)
            print("Done.")
            im_mod.show()
        elif resp2 == '270':
            im_mod = im.rotate(270)
            time.sleep(2)
            print("Done.")
            im_mod.show()
        else:
            print("Try entering one of the numbers.")
    #elif resp == '2':

    #elif resp == '3':

    #elif resp == '4':

    elif resp == '5':
        print("Hope you enjoyed it. Bye!")
        break
    else:
        print("Don't know what you talkin bout.")
