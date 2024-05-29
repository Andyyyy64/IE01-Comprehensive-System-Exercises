import webiopi
import os


SAVEDIR = '/home/andy/IE01-Comprehensive-System-Exercises/ex6'
@webiopi.macro

def camera(no):
    filename = SAVEDIR + '/camera_' + no + '.jpg'
    command = 'fswebcam -r 320x240 -d /dev/video0 ' + filename
    os.system(command)
    os.system('sync')
