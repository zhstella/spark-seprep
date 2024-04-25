FORECAST=$(curl -sS wttr.in/Boston)
#this file will output the weather forecast for today and the next two days in Boston
echo "$FORECAST"
echo
exit 0
