#!/bin/bash
#my_script.sh

name=$1
echo "Hello $name"

echo "Script name: $0"
echo "First arg: $1"
echo "All args: $@"
echo "arg count: $#"

num=6
if [[ $num -gt 10 ]]; then
	echo "Greater than 10"
else
	echo "Less than or equal to 10"
fi
