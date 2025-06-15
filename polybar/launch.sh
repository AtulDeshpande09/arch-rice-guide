#!/bin/bash

# Kill any running bars
killall -q polybar

# Wait until they are gone
while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done

# Reload wallpaper (if needed)
feh --bg-scale ~/wallpapers/japan1.png &

# Launch main bar
polybar mybar &

