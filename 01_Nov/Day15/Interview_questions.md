Structured into:

* Basic (Docker Fundamentals)
* Intermediate (Shell + Python Automation)
* Advanced (AWS CLI & Boto3 Integration)
* Scenario-Based DevOps Questions

---

# 🟢 **Basic: Docker Fundamentals**

### 1️⃣ What is Docker?

**Answer:** Docker is a containerization platform that packages applications with dependencies into lightweight, isolated containers that can run consistently across environments.

---

### 2️⃣ Docker image vs Container?

| Image                        | Container                          |
| ---------------------------- | ---------------------------------- |
| Blueprint of the application | Running instance of the image      |
| Read-only                    | Writable layer on top of the image |

---

### 3️⃣ What does `FROM` do in Dockerfile?

**Answer:** Sets the base image from which the image will be built. It is always the first instruction.

---

### 4️⃣ Difference between `CMD` and `ENTRYPOINT`?

| CMD                                 | ENTRYPOINT         |
| ----------------------------------- | ------------------ |
| Default command                     | Main command       |
| Can be overridden from `docker run` | Harder to override |

---

### 5️⃣ What is the purpose of `docker build -t myapp:latest .`?

**Answer:**

* Builds an image from Dockerfile in current directory (`.`)
* Tags it as `myapp:latest`

---

### 6️⃣ How do you view running container logs?

```bash
docker logs <container_id>
```

---

### 7️⃣ What happens if a container exits immediately after starting?

**Answer:** The process defined by CMD/ENTRYPOINT finished running → container exits.
Fix: keep a long-running process (server/app).

---

---

# 🟡 **Intermediate: Shell & Python Automation**

### 8️⃣ Why automate Docker with Shell or Python?

**Answer:** To ensure consistency, reduce manual effort, avoid human error, and integrate with CI/CD pipelines.

---

### 9️⃣ What does `$?` mean in shell scripts?

**Answer:** The exit status of the last executed command.
`0 = success, Non-zero = failure`

---

### 🔟 What is `subprocess.run()` used for in Python?

**Answer:** Executes shell commands programmatically.
Used for automation scripts that interact with CLI tools like Docker, Git, AWS.

---

### 1️⃣1️⃣ Why use `capture_output=True, text=True`?

**Answer:**

* `capture_output=True` → Captures stdout/stderr
* `text=True` → Returns output as string instead of bytes

---

### 1️⃣2️⃣ Why use `sys.exit(1)` in automation?

**Answer:**
Exits script with an error code so CI/CD pipelines can detect failure.

---

### 1️⃣3️⃣ How do you handle Docker command errors in Python?

**Answer:** Check `returncode` from `subprocess.run()` → log & exit gracefully.

---

### 1️⃣4️⃣ What is the benefit of using `argparse` in automation scripts?

**Answer:** Enable CLI arguments to choose operations like:

```
python build.py --build
python build.py --run
```

---

---

# 🔵 **Advanced: AWS CLI & Boto3 Integration**

### 1️⃣5️⃣ What does AWS CLI do in DevOps pipelines?

**Answer:** Automates cloud actions such as launching/stopping EC2, managing S3, deploying apps, etc.

---

### 1️⃣6️⃣ What command lists EC2 instance IDs?

```bash
aws ec2 describe-instances --query "Reservations[].Instances[].InstanceId"
```

---

### 1️⃣7️⃣ What is Boto3?

**Answer:** The official AWS SDK for Python — used to automate cloud operations programmatically.

---

### 1️⃣8️⃣ What exception is raised for missing AWS credentials?

**Answer:** `NoCredentialsError` from `botocore.exceptions`.

---

### 1️⃣9️⃣ Difference between `boto3.client` & `boto3.resource`?

| boto3.client                  | boto3.resource                         |
| ----------------------------- | -------------------------------------- |
| Low-level API                 | High-level, object-oriented            |
| Requires detailed params      | More Pythonic                          |
| Faster for automation scripts | Easier for complex resource operations |

---

### 2️⃣0️⃣ How to filter only running EC2 instances in CLI?

```bash
aws ec2 describe-instances \
 --filters "Name=instance-state-name,Values=running"
```

---

---

# 🚀 **Scenario-Based DevOps Questions**

### 2️⃣1️⃣ Docker container exits immediately — how do you fix it?

**Answer:**

* Ensure long-running foreground process (`gunicorn`, `python app.py`)
* Check logs: `docker logs <id>`
* Validate entrypoint/script isn’t crashing

---

### 2️⃣2️⃣ Docker build is slow — how do you speed it up?

**Answer:**

* Use multi-stage builds
* Order layers to maximize caching
* Avoid copying unnecessary files (use `.dockerignore`)

---

### 2️⃣3️⃣ How to automatically remove stopped containers & dangling images?

```bash
docker system prune -f
```

---

### 2️⃣4️⃣ How do you integrate Docker automation into CI/CD?

**Answer:**

* Write a script → Run through Jenkins/GitHub-Actions
* Automate: build → test → push → deploy
* Use exit codes to detect failures

---

### 2️⃣5️⃣ EC2 list script fails due to expired credentials — solution?

**Answer:**

* Refresh credentials via `aws configure`
* Or use IAM roles when running inside EC2/EKS
  (No stored keys)

---

---

# 🧠 Quick Revision Table

| Area                | Must Know                            |
| ------------------- | ------------------------------------ |
| Docker automation   | `build`, `run`, `logs`, `stop`       |
| Shell scripting     | `$?`, functions, exit codes          |
| Python + subprocess | `capture_output`, `returncode`       |
| AWS CLI             | `describe-instances`, filters        |
| Boto3               | `client vs resource`, error handling |

---

