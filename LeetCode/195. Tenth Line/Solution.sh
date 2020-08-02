# Read from the file file.txt and output the tenth line to stdout.
sed '10q;d' file.txt


# Read from the file file.txt and output the tenth line to stdout.
sed -n '10p' file.txt