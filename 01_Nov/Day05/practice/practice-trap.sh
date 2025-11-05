#!/bin/bash

trap "echo 'cleaning up.. byee'" SIGINT EXIT

echo "script running. Press Ctrl+C to stop.."
sleep 10

echo "Done!"
