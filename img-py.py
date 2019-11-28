#!/usr/bin/env python3
"""
A small little tool to test the Raspberry pi camera
"""
__VERSION__ = 0.1
__CREATOR__ = "Kristján Orri"

from picamera import PiCamera
from time import sleep
import os

path = '/home/{}/Pictures/'

user = 'pi' ## os.uname()

file_extension = 'jpg'

video_set = set(['video', 'v', 'vid', 'vídjó', '2'])

image_set = set(['image', 'picture', 'i', 'img', 'p', 'pic', '1'])

quit_set = set(['quit', 'exit', 'stop', 'q'])

camera = PiCamera()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(bcolors.HEADER + 'Welcome to PiImage CLI' + bcolors.ENDC)

if __name__ == "__main__":
    print('#####################################\n# Image for Image related function  #\n# Video for Video related functions #\n# Exit to quit                      #\n#####################################')
    while True:
        selector = input(bcolors.OKBLUE + '> ' + bcolors.ENDC)
        if selector.lower() in image_set:
            while True:
                print('1. take one photo\n2. take multiple photos\nBack to main menu')
                second_selector = input(bcolors.OKBLUE + 'image> ' + bcolors.ENDC)
                ss = second_selector
                if ss == '1':
                    inp = input('Filename: ')
                    filename = 'image' if inp == '' else inp
                    inp = input('Extension: ')

                    ## make file extension selector work
                    camera.capture(path.format(user) + filename + '.' + file_extension )
                elif ss == '2':
                    inp = input('Filename: ')
                    filename = 'image' if inp == '' else inp
                    inp = input('Extension: ')
                    number_of_pictures = int(input('Number Of Pictures: '))
                    deley = int(input('sec betwen pic: '))
                    for i in range(number_of_pictures):
                        camera.capture(path.format(user) + filename + str(i) + '.' + file_extension )
                        sleep(deley)
                else:
                        break
        elif selector.lower() in video_set:
            print('this is under construction')
        elif selector.lower() in quit_set:
            x = input('Are you sure you want to exit(y/N)')
            if x.lower() == 'y':
                break



