#! /usr/bin/python3

import datetime
import pathlib

from set_wallpaper_permanent import set_wallpaper_permanent
from add_to_startup import add_to_startup
import bing_wallpaper_changer
import pod_wallpaper_changer
import unsplash_wallpaper_changer
import os

SHOW_DEBUG = True
#Directory to save images
saveDir = saveDir = os.path.join(os.getcwd(), r'WallPaper')

date = str(datetime.date.today())

def directoryCheck ():
    #create the directory directory if it does not exist
    pathlib.Path(saveDir).mkdir(parents=True, exist_ok=True)

if __name__=='__main__':

    #only on windows 
    #add_to_startup()
    choice = 0
    directoryCheck()
    print ("Choice: ? 0: APOD, 1: Bing, 2: Unsplash ",)
    choice = int(input())
    wp_bing = saveDir  + 'bingwallpaper' + date +'.jpg'
    wp_pod = saveDir + 'NASA_PoD' + date + '.jpg'
    wp_unsplash = saveDir + 'unsplash' + date + '.jpg'

    if choice == 1:
        bing_wallpaper_changer.change_wp( wp_bing, saveDir, SHOW_DEBUG)

    elif choice == 0: 
        pod_wallpaper_changer.change_wp( wp_pod, saveDir, SHOW_DEBUG)
    
    else:
        unsplash_wallpaper_changer.change_wp( wp_unsplash, saveDir, SHOW_DEBUG)
