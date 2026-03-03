# Read from the file file.txt and output the tenth line to stdout.
# had to look at answer for this one
awk 'NR==10 {print; exit}' file.txt