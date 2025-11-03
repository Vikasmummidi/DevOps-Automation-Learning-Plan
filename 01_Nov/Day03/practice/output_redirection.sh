echo "Hello DevOps" > output.txt      # writes (overwrites) output.txt
cat output.txt

echo "Appending line" >> output.txt    # appends
cat output.txt
sort < output.txt #input redirection

#error redirection
ls /not/here 2> error.log
cat error.log

echo "redirects both stdout + stderr"
ls /root /not/here &> all_output.log
cat all_output.log

