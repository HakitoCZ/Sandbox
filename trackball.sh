#!/bin/bash
dev="Logitech USB Trackball"
we="Evdev Wheel Emulation"
xinput set-int-prop "$dev" "$we Button" 8 8
xinput set-int-prop "$dev" "$we" 8 1

# xinput set-int-prop "$dev" "$we" 8 1
# xinput set-int-prop "$dev" "$we Button" 8 9
# xinput set-int-prop "$dev" "$we X Axis" 8 6 7
# xinput set-int-prop "$dev" "$we Y Axis" 8 4 5
# xinput set-int-prop "$dev" "Drag Lock Buttons" 8 8 
