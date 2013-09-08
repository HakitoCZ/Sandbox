while true; do
    xsetroot -name "$( date +"%F %R" )"
    sleep 1m    # Update time every minute
done &
(conky | while read LINE; do xsetroot -name "$LINE"; done) &
exec dwm &
exec redshift -l 50.059079:14.405973
