from PIL import Image, ImageFilter, ImageChops
from Manip import *
import sys

print('Welcome to the quick image editor. Enter "help" for command options. ')
manip = Manip()

if(len(sys.argv) == 2):
    try:
        im = Image.open(sys.argv[1])
        manip.path = sys.argv[1]
    except FileNotFoundError:
        print("Invalid initial path")

while(True):
    inp = input("> ").lower()
    #print(inp)

    if(inp == "help"):
        manip.help()

    elif(inp == "quit" or inp == "exit"):
        break

    elif(inp == "show"):
        if(manip.validPath()):
            manip.showImage()

    elif(inp == "resize"):
        if(manip.validPath()):
            print("Skip to set value automatically, requires at least width or height. ")
            try:
                widthIn = input("Enter new width: ")
                if(widthIn != "" and int(widthIn) <= 0):
                    raise ValueError
                width = -1 if widthIn=="" else int(widthIn)
                heightIn = input("Enter a new height: ")
                if(heightIn != "" and int(heightIn) <= 0):
                    raise ValueError
                height = -1 if heightIn=="" else int(heightIn)
            except ValueError:
                print("Please enter a positive integer.")
                continue

            if(height == -1 and width == -1):
                print("Please specify at least one dimension. ")
                continue

            #scheme = input("Enter scheme: ")
            manip.resize(width, height)
    
    elif(inp == "path"):
        path = input("Enter Path: ")
        if(path == ""):
            if(manip.path == ""):
                print("Path has not been added")
            else:
                print("Current path: " + manip.path)
        else:
            try:
                im = Image.open(path)
                manip.path = path
            except FileNotFoundError:
                print("Invalid path")
    else:
        print('Not a valid command. Use "help" for list of commands')
    
