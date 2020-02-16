#!/bin/bash
echo update
apt-get update
apt-get install
apt autoremove
echo Install vlc
apt-get install vlc
echo Install video
cp  video/video.mp4 ~/Videos/video.mp4
echo Install python script
cp  play_video.py ~/Videos/play_video.py
echo change permissions to execute script 755
chmod 755 ~/Videos/play_video.py
echo copy autostart to LXDE-pi

if [ -d "~/.config/lxsession/LXDE-pi" ] 
then
    echo "Directory /path/to/dir exists." 
else
    echo "Directory /path/to/dir does not exists.Now we make them."
    mkdir -p ~/.config/lxsession/LXDE-pi
fi
echo "Created autostart file"
cp  autostart ~/.config/lxsession/LXDE-pi/autostart
#chmod 755 ~/.config/lxsession/LXDE-pi/autostart


