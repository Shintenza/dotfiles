#!/usr/bin/env bash

. $HOME/.zshrc
xsetroot -cursor_name left_ptr
feh --bg-fill --randomize $HOME/Pictures/wallpapers/* &
setxkbmap pl &
redshift -l 50.60705:22.10381 & 
/usr/bin/lxpolkit &
picom -b --experimental-backends &
dwmblocks &
xidlehook --not-when-fullscreen --not-when-audio \ 
    --timer 580 'xbacklight -set 5' \
    --timer 20 'xbacklight -set 100; betterlockscreen -l' \
    --timer 600 'systemctl suspend' \
    ''
