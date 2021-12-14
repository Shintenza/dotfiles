#!/bin/zsh

wallpaper &
# ./.config/polybar/launch.sh &
setxkbmap pl &
 redshift -l 50.60705:22.10381 & 
# xautolock -time 10 -locker 'i3lock-fancy' &│
/usr/bin/lxpolkit &
picom -b &
sleep 2; dwmblocks &
xautolock -time 10 -locker "betterlockscreen -l blur" -detectsleep

