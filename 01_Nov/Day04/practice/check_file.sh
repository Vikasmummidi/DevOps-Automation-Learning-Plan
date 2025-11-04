#!/bin/bash

FILE=$1

if [[ -f "$FILE" ]]; then
	echo "$FILE is a file"
elif [[ -d "$FILE" ]]; then
	echo "$FILE is a directory"
else
	echo "$FILE not found"
fi


