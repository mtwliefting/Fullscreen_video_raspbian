from __future__ import print_function
from subprocess import Popen
import os,sys

path = '.'
 
if len(sys.argv) == 2:
    path = sys.argv[1]
 
files = os.listdir(path+"/video")

movie1 = "video/"+files[0]
#movie1 = ("/home/pi/Videos/video.mp4") #change video name or path here
Popen(['cvlc','--no-video-title-show','-f','-L', movie1])

