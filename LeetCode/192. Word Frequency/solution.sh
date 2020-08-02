# Read from the file words.txt and output the word frequency list to stdout.
cat words.txt | tr -s ' ' '\n' | sort | uniq -c | sort -nr | awk '{ print $2, $1 }'


# Read from the file words.txt and output the word frequency list to stdout.
sed -E 's/ /\n/g' words.txt | grep -v "^$" | sort | uniq -c | sort -nr | awk '{print $2, $1}'