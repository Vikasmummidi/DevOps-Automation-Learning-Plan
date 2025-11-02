#!/bin/bash

echo "printing total size of all files"
ls -l|awk 'BEGIN {sum=0} {sum=sum+$5} END{print sum}'

echo "printing Alternative rows in ls -l"
ls -l | awk '{for (i=1; i<3; i++) {getline}; print NR, $0}'
