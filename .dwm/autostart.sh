#!/bin/zsh

#!/bin/zsh

. $HOME/.zshrc
xsetroot -cursor_name left_ptr
feh --bg-fill --randomize $HOME/Pictures/wallpapers/* &
setxkbmap pl &
redshift -l 50.60705:22.10381 & 
/usr/bin/lxpolkit &
picom -b --experimental-backends &
sleep 2; dwmblocks &
xidlehook --not-when-fullscreen --not-when-audio --timer 600 'betterlockscreen -l blur'
