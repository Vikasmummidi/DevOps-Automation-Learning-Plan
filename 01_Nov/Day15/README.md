
---

# 📝 **Day-15 Practice Worksheet**

### **Date:** 15-Nov-2025

### **Focus Area:** DevOps Integration

### **Topic:** *Automate Docker via Shell & Python*

### **Goal:**

Automate building, running, and managing containers using scripts.
Integrate AWS CLI & Boto3 for DevOps-style automation.

---

# 📘 **1. Overview**

Today you will learn how to:

✔ Automate Docker builds through Shell scripts
✔ Run and stop containers with Python (`subprocess`)
✔ Create a small Dockerized application
✔ Use AWS CLI to list EC2 instances (DevOps-style integration)
✔ Use Boto3 to interact with AWS using Python

---

# 🔗 **2. Resources**

* Docker: Get started
  [https://docs.docker.com/get-started/](https://docs.docker.com/get-started/)
* AWS CLI: Getting started
  [https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html)
* Boto3 EC2 guide
  [https://boto3.amazonaws.com/v1/documentation/api/latest/guide/ec2-example-managing-instances.html](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/ec2-example-managing-instances.html)

---

# 🧠 **3. Concepts to Know (Before Starting)**

### **Docker**

* `Dockerfile` basics (FROM, COPY, CMD, EXPOSE)
* `docker build -t`
* `docker run -d`, `docker stop`, `docker rm`
* Image layers & caching
* Container logs (`docker logs`)

### **Shell Automation**

* Variables
* Functions
* Exit codes
* `$(command)` for capturing command output

### **Python Automation**

* Using `subprocess.run()` to call Docker commands
* Handling stdout/stderr
* Capturing command results
* Basic error handling

### **AWS CLI**

* Configuring credentials (`aws configure`)
* `aws ec2 describe-instances`
* Parsing JSON output with JMESPath or `jq`

### **Boto3**

* Authenticating
* Listing EC2 instances
* Filtering by instance state
* Error handling (`botocore.exceptions`)

---

# 🧪 **4. Practice Tasks**

---

## **Task 1: Create a simple Dockerfile**

Create a file named `Dockerfile`:

**Requirements:**

* Base image: `python:3.10-slim`
* Copy `app.py` into container
* Install dependencies (if any)
* Run the app using `CMD ["python", "app.py"]`

Example `app.py`:

```python
print("Hello from inside Docker!")
```

✔ Build it
✔ Run it
✔ Verify output

---

## **Task 2: Write a Shell Script to Build & Run the Container**

Create `run_docker.sh`:

### **Script Must:**

* Build image: `docker build -t myapp:latest .`
* Run container detached
* Print container ID
* Show logs after start
* Exit with error if build/run fails

Test:

```bash
chmod +x run_docker.sh
./run_docker.sh
```

---

## **Task 3: Write a Python Script to Automate Docker Commands**

Create `docker_automation.py`.

### **Requirements:**

Use `subprocess.run()` to:

* Build the image
* Run the container
* Print container logs
* Stop & remove container

### Example function:

```python
def run_command(cmd):
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result
```

Tasks:

* Implement `build_image()`
* Implement `run_container()`
* Implement `stop_container()`
* Implement `show_logs()`

---

## **Task 4: Use AWS CLI to list EC2 instances**

Run:

```bash
aws ec2 describe-instances --query "Reservations[].Instances[].InstanceId"
```

Tasks:

* Save the output to `instances.txt`
* Modify the query to print ONLY **running instances**
* Try using `--output table`

---

## **Task 5: Python + Boto3 EC2 Scanner**

Create `aws_ec2_list.py`.

### Requirements:

* Connect using boto3
* List all instance IDs
* List instance state name
* Print in readable format:

```
Instance: i-0abc123
State: running
```

Bonus:

* Filter only running instances
* Count number of running instances

---

# 🧩 **5. Challenge Problems**

### **Challenge 1:**

Modify the Shell script to:

* Accept an image name as an argument
* Push the image to Docker Hub (optional)

```
./run_docker.sh myrepo/myimage:latest
```

---

### **Challenge 2:**

In Python, build a CLI using `argparse`:

```
python docker_automation.py --build
python docker_automation.py --run
python docker_automation.py --stop <container_id>
```

---

### **Challenge 3:**

Create a small Flask app and dockerize it.
Expose port 5000.
Test via:

```
curl localhost:5000
```

---

### **Challenge 4:**

Use Boto3 to:

* Start a stopped EC2 instance
* Stop a running EC2 instance
* Handle exceptions properly

---

# 🎯 **6. Quick Interview Questions (Day-15 Focus)**

1. Difference between Docker image and container?
2. What is the purpose of `CMD` in Dockerfile?
3. How does Docker caching work during builds?
4. How to pass environment variables to Docker containers?
5. Difference between shell script vs Python automation?
6. What is `subprocess.run()` used for?
7. What is an AMI in AWS?
8. How does `aws ec2 describe-instances` retrieve data?
9. What is an EC2 instance state model (pending/running/stopped)?
10. Explain IAM role vs IAM user for Boto3.

---

# 🏁 **7. Submission Checklist**

Before closing Day-15, ensure:

✔ `Dockerfile` works and prints output
✔ Shell script builds & runs the image
✔ Python docker automation works
✔ AWS CLI can list instances
✔ Boto3 script lists instance states

---


