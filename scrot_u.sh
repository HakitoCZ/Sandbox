#!/bin/bash
scrot '%s_$wx$h.png' -e 'mv $f ~/Pictures/scrots/' -u && notify-send 'Saved' '~/Pictures/scrots/' -i '/home/hrnekbezucha/.local/share/.screenshot.svg'
