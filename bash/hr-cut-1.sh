# Problem: Cut - 1
# Goal: Master extracting characters using the `cut` command.

while read -r line;
do
    echo "${line}" | cut -c 3
done
