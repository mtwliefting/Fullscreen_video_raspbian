from __future__ import print_function
from subprocess import Popen
import os,sys

path = '.'
 
if len(sys.argv) == 2:
    path = sys.argv[1]
 
files = os.listdir(path+"/video")

movie1 = "video/"+files[0]
#movie1 = "/home/pi/Videos/video.mp4" #if autopath doesn't work

os.system("omxplayer --aspect-mode fill --no-osd -b --loop --vol 0 "+movie1) #for using omxplayer
#Popen(['cvlc','--no-video-title-show','-f','-L', movie1]) # for using vlc


