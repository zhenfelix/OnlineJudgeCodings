read a
read b 
read c 
if [ "$a" == "$b" -a "$a" == "$c" -a "$b" == "$c" ]; then
    echo "EQUILATERAL"
elif [ "$a" == "$b" -o "$a" == "$c" -o "$b" == "$c" ]; then
    echo "ISOSCELES"
else
    echo "SCALENE"
fi