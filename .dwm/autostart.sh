#!/bin/zsh

. $HOME/.zshrc
wallpaper &
setxkbmap pl &
redshift -l 50.60705:22.10381 & 
/usr/bin/lxpolkit &
picom -b &
sleep 2; dwmblocks &
xautolock -time 10 -locker "betterlockscreen -l blur" -detectsleep
