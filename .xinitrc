(conky | while read LINE; do xsetroot -name "$LINE"; done) &
exec redshift.sh &
exec dwm 
