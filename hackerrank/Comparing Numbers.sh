read X
read Y
if (( $X == $Y )); then
    echo "X is equal to Y"
elif (( $X < $Y )); then
    echo "X is less than Y"
else
    echo "X is greater than Y"
fi


#!/bin/bash
read x
read y
[[ $x -gt $y ]] && echo 'X is greater than Y'
[[ $x -eq $y ]] && echo 'X is equal to Y'
[[ $x -lt $y ]] && echo 'X is less than Y'