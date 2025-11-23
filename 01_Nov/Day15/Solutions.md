
---

# ✅ **SOLUTION 1 — Dockerfile + Sample App**

Create **Dockerfile**:

```dockerfile
# Use official lightweight Python image
FROM python:3.10-slim

# Work directory inside container
WORKDIR /app

# Copy application files
COPY app.py /app/

# (Optional) Install dependencies if you have requirements.txt
# RUN pip install -r requirements.txt

# Default command
CMD ["python", "app.py"]
```

Create **app.py**:

```python
print("Hello from inside Docker!")
```

Build & test:

```bash
docker build -t myapp:latest .
docker run --rm myapp:latest
```

---

# ✅ **SOLUTION 2 — Shell Script to Build & Run Docker Container**

Create **run_docker.sh**:

```bash
#!/bin/bash

IMAGE_NAME="myapp:latest"

echo "[INFO] Building Docker image..."
docker build -t $IMAGE_NAME .
if [ $? -ne 0 ]; then
    echo "[ERROR] Build failed!"
    exit 1
fi

echo "[INFO] Running container..."
CID=$(docker run -d $IMAGE_NAME)
if [ $? -ne 0 ]; then
    echo "[ERROR] Failed to run container!"
    exit 1
fi

echo "[INFO] Container ID: $CID"

echo "[INFO] Logs:"
docker logs $CID

echo "[INFO] Stopping container..."
docker stop $CID >/dev/null

echo "[INFO] Removing container..."
docker rm $CID >/dev/null

echo "[SUCCESS] Build + Run completed!"
```

Make executable:

```bash
chmod +x run_docker.sh
```

Run:

```bash
./run_docker.sh
```

---

# ✅ **SOLUTION 3 — Python Script to Automate Docker Commands**

Create **docker_automation.py**:

```python
import subprocess
import sys

def run_cmd(cmd):
    """ Run system command safely and return output """
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"[ERROR] Command failed: {' '.join(cmd)}")
        print(result.stderr)
        sys.exit(1)
    return result.stdout.strip()

def build_image(tag="myapp:latest"):
    print("[INFO] Building image...")
    run_cmd(["docker", "build", "-t", tag, "."])
    print("[SUCCESS] Image built.")

def run_container(tag="myapp:latest"):
    print("[INFO] Running container...")
    cid = run_cmd(["docker", "run", "-d", tag])
    print("[INFO] Container ID:", cid)
    return cid

def show_logs(container_id):
    print("[INFO] Logs:")
    logs = run_cmd(["docker", "logs", container_id])
    print(logs)

def stop_container(container_id):
    print("[INFO] Stopping container...")
    run_cmd(["docker", "stop", container_id])
    print("[INFO] Removing container...")
    run_cmd(["docker", "rm", container_id])
    print("[SUCCESS] Container cleaned up.")

if __name__ == "__main__":
    build_image()
    cid = run_container()
    show_logs(cid)
    stop_container(cid)
```

Run:

```bash
python3 docker_automation.py
```

---

# ✅ **SOLUTION 4 — AWS CLI Task**

### **List all EC2 instances**

```
aws ec2 describe-instances --query "Reservations[].Instances[].InstanceId"
```

### **List only running instances**

```
aws ec2 describe-instances \
  --filters "Name=instance-state-name,Values=running" \
  --query "Reservations[].Instances[].InstanceId"
```

### **Save to file**

```
aws ec2 describe-instances \
  --query "Reservations[].Instances[].InstanceId" \
  > instances.txt
```

### **Pretty table output**

```
aws ec2 describe-instances --output table
```

---

# ✅ **SOLUTION 5 — Boto3 Script to List EC2 Instances**

Create **aws_ec2_list.py**:

```python
import boto3
from botocore.exceptions import NoCredentialsError, ClientError

def list_instances():
    ec2 = boto3.client("ec2")

    try:
        response = ec2.describe_instances()
    except NoCredentialsError:
        print("[ERROR] AWS credentials not configured. Run 'aws configure'.")
        return
    except ClientError as e:
        print(f"[ERROR] AWS error: {e}")
        return

    print("\n=== EC2 Instances ===\n")

    count = 0

    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            instance_id = instance["InstanceId"]
            state = instance["State"]["Name"]

            print(f"Instance: {instance_id}")
            print(f"State   : {state}")
            print("-" * 30)

            count += 1

    print(f"\nTotal Instances: {count}")

def list_running_instances():
    ec2 = boto3.client("ec2")

    response = ec2.describe_instances(
        Filters=[{"Name": "instance-state-name", "Values": ["running"]}]
    )

    print("\n=== Running Instances ===\n")

    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            print(f"Running Instance: {instance['InstanceId']}")

if __name__ == "__main__":
    list_instances()
    list_running_instances()
```

Run:

```bash
python3 aws_ec2_list.py
```

---

