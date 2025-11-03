#!/bin/bash

ls /etc > /dev/null
echo $?   # should print 0

ls /no/such/path > /dev/null
echo $?   # should print non-zero

echo "==========================="
echo "conditional using exit code"
echo "==========================="

ls /etc > /dev/null
if [ $? -eq 0 ]; then
	echo "command succeed"
else
	echo "command failed"
fi

echo "=========================="
echo "using set -e"
echo "=========================="
set -e
echo "starting ...."
ls /fake/path
echo "this will not run"	
