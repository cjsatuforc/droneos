import os
import time
from datetime import datetime
from math import *

def take_picture(last_pic_time):
    time_difference = datetime.now() - last_pic_time
    surveil = 'image'
    interval = 1
    if surveil == 'image' and (time_difference.total_seconds() >= interval):
<<<<<<< HEAD
        image = '/home/amber/droneos/RPi_code/image/"' + str(datetime.now()) + '.jpg"'
        #print(image)
        cmd = 'fswebcam -d /dev/video0 -r 1200*720 -F2 ' + image
        print(cmd)
        os.system(cmd)
=======
        image = '/tmp/image/"' + str(datetime.now()) + '.jpg"'
        #print(image)
        cmd = 'fswebcam -d /dev/video1 -r 1200*720 -F2 ' + image
        print(cmd)
        os.system(cmd)
        print(cmd)
>>>>>>> e8f7b34679a54b190cce189c46f1fef55d19994c
        return True
    else:
        return False

if '__main__' == __name__:
    i = 0
    while i < 5:
        last_pic_taken_at = datetime.now()
        time.sleep(2)
        print(last_pic_taken_at)
        i += 1
        if take_picture(last_pic_taken_at):
            last_pic_taken_at = datetime.now()
        
        
    
