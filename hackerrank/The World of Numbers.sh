# read x
# read y
# echo $(($x+$y))
# echo $(($x-$y))
# echo $(($x*$y))
# echo $(($x/$y))

#!/bin/bash
read X
read Y
printf "%s\n" $X{+,-,*,/}"($Y)" | bc