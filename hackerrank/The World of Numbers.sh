read n1
read n2

echo $[n1 + n2]
echo $[n1 - n2]
echo $[n1 * n2]
echo $[n1 / n2]

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