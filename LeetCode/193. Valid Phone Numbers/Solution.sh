# Read from the file file.txt and output all valid phone numbers to stdout.
grep -P '^(\(\d{3}\)\ |\d{3}\-)\d{3}\-\d{4}$' file.txt
grep -P '^(\d{3}-|\(\d{3}\) )\d{3}-\d{4}$' file.txt


grep -e '\(^[0-9]\{3\}-[0-9]\{3\}-[0-9]\{4\}$\)' -e '\(^([0-9]\{3\})[ ]\{1\}[0-9]\{3\}-\([0-9]\{4\}\)$\)'  file.txt


sed -n -r '/^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$/p' file.txt
awk '/^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$/' file.txt

