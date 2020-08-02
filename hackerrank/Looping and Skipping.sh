i=1
while [ "$i" != "101" ]
do 
    echo $i 
    i=$(($i+2))
done


for number in {1..99..2}
do
    echo $number
done