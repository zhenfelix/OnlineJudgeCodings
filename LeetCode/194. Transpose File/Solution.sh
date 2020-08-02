# Read from the file file.txt and print its transposed content to stdout.
awk '
{
    for (i = 1; i <= NF; i++) {
        if(NR == 1) {
            s[i] = $i;
        } else {
            s[i] = s[i] " " $i;
        }
    }
}
END {
    for (i = 1; s[i] != ""; i++) {
        print s[i];
    }
}' file.txt


awkle(){
   awk '
    {
        for (i = 1; i <= NF; i++) {
           if(NR == 1) {
               print "\nNR == 1";
               s[i] = $i;
               print $i;
           } else {
              print "\nNR != 1";
              print s[i];
              s[i] = s[i] " " $i;
              print s[i];
           }
        }
    }
    END {
        for (i = 1; s[i] != ""; i++) {
           print s[i];
        }
    }'  $1
}

# NR == 1
# name

# NR == 1
# age

# NR != 1
# name
# name alice

# NR != 1
# age
# age 21

# NR != 1
# name alice
# name alice ryan

# NR != 1
# age 21
# age 21 30
# name alice ryan
# age 21 30
