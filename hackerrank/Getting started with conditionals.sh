read yn
[ "$yn" == "y" -o "$yn" == "Y" ] && echo "YES" && exit 0
[ "$yn" == "n" -o "$yn" == "N" ] && echo "NO" && exit 0


read c
[[ "$c" == [yY] ]] && echo "YES" || echo "NO"

read char; echo -e "YES\nNO\n" | grep -i $char

