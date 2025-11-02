# 📅 Date: 02-Nov-2025
## 🧭 Focus Area
Shell

## 🧩 Topic
Common tools: grep / awk / sed / cut / tr / find

## 🧠 Overview
Hands-on with essential text-processing commands in Linux. Learn through practical examples and usage notes.

## 🔗 Resources
- [Bash scripting guide](https://tldp.org/LDP/abs/html/)
- [ShellCheck (linting)](https://www.shellcheck.net/)
- [grep/awk/sed guide (PDF)](https://www-users.york.ac.uk/~mijp1/teaching/2nd_year_Comp_Lab/guides/grep_awk_sed.pdf)

## 🧰 Practice Task
Write and run a bash script that finds the top 5 CPU-consuming processes and logs the output to a file.

```bash
#!/bin/bash
# top_cpu_processes.sh
# Description: Logs top 5 CPU-consuming processes to a file.

LOG_FILE="top_processes.log"
echo "Top 5 CPU Processes - $(date)" > "$LOG_FILE"
ps -eo pid,comm,%cpu --sort=-%cpu | head -n 6 >> "$LOG_FILE"

echo "Log saved to $LOG_FILE"




#🧠 Understanding `grep` Commands with Examples

Assume we have saved the following lines in a file called **a_file.txt**:

```
boot
book
booze
machine
boots
bungie
bark
aardvark
broken$tuff
robots
```

---

## 1️⃣ `grep "boo" a_file.txt`
**Explanation:**  
Searches for all lines in `a_file.txt` that contain the substring **"boo"**.

**Output:**
```
boot
book
booze
boots
```

These lines contain the sequence `boo` anywhere in the text.

---

## 2️⃣ `grep -vn "boo" a_file.txt`
**Explanation:**  
- `-v` → Inverts the match (shows lines **NOT** containing "boo")  
- `-n` → Shows **line numbers** of matched lines

**Output:**
```
4:machine
6:bungie
7:bark
8:aardvark
9:broken$tuff
10:robots
```

These are all lines that **don’t** contain "boo".

---

## 3️⃣ `grep -c "boo" a_file.txt`
**Explanation:**  
- `-c` → Counts the number of lines that match the pattern

**Output:**
```
4
```

There are 4 lines containing "boo".

---

## 4️⃣ `grep -l "boo" *`
**Explanation:**  
- `-l` → Lists **file names only** that contain the matching text  
If there are multiple files in the directory, it prints only the file names where `"boo"` occurs.

**Output (example):**
```
a_file.txt
```

---

## 5️⃣ `grep -i "boo" a_file.txt`
**Explanation:**  
- `-i` → Makes the search **case-insensitive** (ignores uppercase/lowercase differences)

**Output:**
```
boot
book
booze
boots
```

If the file had entries like **"BOOT"** or **"Book"**, those would also appear.

---

## 6️⃣ `grep -A2 "mach" a_file`
**Explanation:**  
- `-A2` → Shows the **matching line** and the **2 lines after** it (A = After)

**Output:**
```
machine
boots
bungie
```

Here, `"machine"` is matched, and the next two lines (`boots` and `bungie`) are also displayed.

---

## ✅ Summary Table

| Command | Description | Example Output (short) |
|----------|--------------|------------------------|
| `grep "boo" a_file.txt` | Match lines containing "boo" | boot, book, booze, boots |
| `grep -vn "boo" a_file.txt` | Invert match & show line numbers | 4:machine ... |
| `grep -c "boo" a_file.txt` | Count matches | 4 |
| `grep -l "boo" *` | Show files containing "boo" | a_file.txt |
| `grep -i "boo" a_file.txt` | Case-insensitive search | boot, Book, BOOZE |
| `grep -A2 "mach" a_file` | Match + 2 lines after | machine, boots, bungie |

---

🔍 **Tip:**  
You can combine options too, e.g.:
```bash
grep -in "boo" a_file.txt
```


# 🦾 Understanding AWK — A Powerful Text Processing Tool

## 🔹 Overview
**AWK** is a versatile text processing language commonly used for data extraction, transformation, and reporting.  
It operates **line by line** on input files and applies patterns or commands to each line to produce formatted output.

---

## 🔹 Basic Structure of an AWK Program

An AWK program can have up to three main sections:

```awk
BEGIN { … initialization commands … }
{ … commands for each line of the file … }
END { … finalization commands … }
```

1. **BEGIN Block**
   - Executes **before** reading any lines from the input file.
   - Typically used for initializing variables or printing headers.

2. **Main Block `{}`**
   - Executes **for each line** of the input file.
   - Performs actions like filtering, calculations, or formatting.

3. **END Block**
   - Executes **after** all lines have been read.
   - Used for summary calculations, cleanup, or final print statements.

---

## 🔹 How AWK Processes Input

- For each line in the input file:
  - If a **pattern** is specified, AWK executes commands **only for lines matching that pattern**.
  - If no pattern is given, the commands apply to **all lines**.
- Patterns can include **regular expressions** (similar to `grep`).

---

## 🔹 Working with Fields

AWK treats each line as a collection of **fields** separated by a *field separator (FS)*.

Example:

```
this is a line of text
```

This line contains **6 fields**.

| Field | Variable | Value |
|--------|-----------|--------|
| 1 | `$1` | this |
| 2 | `$2` | is |
| 3 | `$3` | a |
| 4 | `$4` | line |
| 5 | `$5` | of |
| 6 | `$6` | text |
| — | `$0` | whole line |

- **Default Field Separator (FS):** whitespace  
- **Custom Separator Example:**

```bash
awk 'BEGIN {FS=":"} {print $1}' /etc/passwd
```

---

## 🔹 Useful Built-in Variables

| Variable | Meaning |
|-----------|----------|
| `$0` | Entire line |
| `$1, $2, …` | Individual fields |
| `FS` | Field separator |
| `NF` | Number of fields in the current line |
| `NR` | Current line number (record number) |
| `FNR` | Line number within the current file (if multiple files are processed) |

---

## 🔹 Example: Calculating Total File Size

Suppose we run:

```bash
ls -l
```

and we want to calculate the **total size** of all files (the 5th column shows file size).  
We can use AWK as follows:

```bash
ls -l | awk 'BEGIN {sum=0} {sum=sum+$5} END {print sum}'
```

### 🔸 Explanation:
- **BEGIN {sum=0}** → Initialize variable `sum` to 0 before processing any line.
- **{sum=sum+$5}** → For each line, add the 5th field (file size) to `sum`.
- **END {print sum}** → After reading all lines, print the final total.

**Output:**

```
2668269
```

🧠 **Tip:**  
`print sum` prints the variable value.  
`print $sum` would instead print the *field number* stored in `sum` (e.g., `$2` if sum=2).

---

## 🔹 Example: Mean or Standard Deviation

You can easily extend AWK to calculate the **mean** and **standard deviation**:

- Use `sum_x` to accumulate the total of all numbers.
- Use `sum_x2` to accumulate the squares.
- In the `END` block, compute:

```awk
mean = sum_x / NR
std_dev = sqrt(sum_x2/NR - mean^2)
```

---

## 🔹 Loops and Branching in AWK

AWK supports:
- **Loops** → `for`, `while`
- **Conditionals** → `if`, `else if`, `else`

### Example: Print Every 3rd Line

```bash
ls -l | awk '{for (i=1; i<3; i++) {getline}; print NR, $0}'
```

### 🔸 Explanation:
- The `for` loop runs for `i=1` and `i=2` because of `i<3`.
- Each iteration calls `getline`, which reads and skips the next line.
- After skipping two lines, the `print` command prints the **3rd line**.

This repeats — printing line 3, 6, 9, etc.

If the file doesn’t end perfectly on a multiple of 3, AWK finishes early, and you may see the final partial line printed (like line 10 in the example).

**Output:**

```
3  -rw------- 1 user user 6948 Oct 22 00:17 random_numbers.f90
6  -rw------- 1 user user 289936 Oct 21 11:59 uniform_rand_period_1.agr
9  -rw------- 1 user user 494666 Oct 21 12:09 uniform_rand_period_4.agr
10 -rw------- 1 user user 376286 Oct 21 12:05 uniform_rand_period.agr
```

---

## 🔹 Summary

| Concept | Description |
|----------|--------------|
| `BEGIN {}` | Initialization before processing |
| `{}` | Main logic for each line |
| `END {}` | Final summary or cleanup |
| `$0` | Entire line |
| `$1, $2, …` | Individual fields |
| `FS` | Field separator |
| `NR` | Current line number |
| `NF` | Number of fields in the line |
| `getline` | Reads the next input line manually |
| Loops & Conditions | Allow complex data processing |

---

✅ **In short:**  
AWK is a *mini programming language for text and data streams* — perfect for transforming structured text, analyzing logs, and automating reporting in DevOps workflows.

