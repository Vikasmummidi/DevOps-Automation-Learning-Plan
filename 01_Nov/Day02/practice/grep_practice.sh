#!/bin/bash
#grep (global regular expression print)

echo "searching for boo in the file a_file.txt"
grep "boo" a_file.txt

echo "negative serach for boo in the file a_file.txt"
grep -vn "boo" a_file.txt

echo "count the no.of occurences in the file a_file.txt"
grep -c "boo" a_file.txt

grep -l "boo" *
grep -i "boo" a_file.txt
grep -A2 “mach” a_file.txt

echo "search the file for lines ending with the letter e"
grep "e$" a_file.txt

echo "output of egrep command"
grep -E "boots?" a_file.txt

echo "You can also combine multiple searches using the pipe (|) which means 'or' so can do things like:"
grep -E "boot|boots" a_file.txt

echo "printing the lines with speacial character $"
grep '\$' a_file.txt
