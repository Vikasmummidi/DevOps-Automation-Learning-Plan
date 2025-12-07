---

# 📝 **Day-16 Practice Worksheet**

### **Focus Area:** DevOps Integration

### **Topic:** AWS CLI & boto3 basics

### **Goal:**

Install and configure AWS CLI, use boto3 to automate EC2 & S3 operations.

---

## 📘 **1. Overview**

Today, you will:

✔ Install & configure AWS CLI
✔ Use AWS CLI commands to interact with EC2 & S3
✔ Write Python scripts using boto3
✔ Parse output and handle errors
✔ Practice real DevOps automation workflows

This forms the base for cloud deployment automation.

---

## 🔗 **2. Resources**

* Docker: Get started
  [https://docs.docker.com/get-started/](https://docs.docker.com/get-started/)
* AWS CLI: Getting started
  [https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html)
* Boto3 EC2 guide
  [https://boto3.amazonaws.com/v1/documentation/api/latest/guide/ec2-example-managing-instances.html](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/ec2-example-managing-instances.html)

---

## 🧠 **3. Concepts to Know**

Before starting, ensure you understand:

### AWS CLI Basics

* `aws configure`
* Profiles & IAM credentials
* Global flags: `--query`, `--profile`, `--output`

### boto3 Basics

* Client vs Resource APIs
* Managing EC2 instances
* Uploading & downloading S3 objects
* Common Exceptions (`NoCredentialsError`, `ClientError`)

---

## 🧪 **4. Practice Tasks**

---

### **Task 1: Install & Configure AWS CLI**

Steps:

```bash
sudo apt install awscli -y  # Linux example
aws --version
aws configure
```

Enter:

* Access Key
* Secret Key
* Default region (e.g., ap-south-1)
* Output format: json

Verify CLI config:

```bash
aws sts get-caller-identity
```

---

### **Task 2: EC2 Listing with AWS CLI**

Run commands:

✔ List ALL instances:

```bash
aws ec2 describe-instances --query "Reservations[].Instances[].InstanceId"
```

✔ List only **running** instances:

```bash
aws ec2 describe-instances \
  --filters "Name=instance-state-name,Values=running" \
  --query "Reservations[].Instances[].InstanceId"
```

✔ Count instances using JMESPath:

```bash
aws ec2 describe-instances \
  --query "length(Reservations[].Instances)"
```

---

### **Task 3: boto3 — List EC2 Instances**

Create `ec2_list.py`:

Requirements:

* List instance ID
* Print current state
* Handle missing credentials gracefully

Example Expected Output:

```
Instance: i-0abc123 | State: running
Instance: i-0xyz999 | State: stopped
```

---

### **Task 4: boto3 — Interact with S3**

Create `s3_demo.py`:

1️⃣ List buckets
2️⃣ Create a new bucket (use region parameter)
3️⃣ Upload a file
4️⃣ Download back the file
5️⃣ Delete uploaded object

✔ Use **try/except** for `ClientError`.

---

### **Task 5: Parse CLI output using Python**

Use `subprocess.run()` to get EC2 instance list:

Steps:

* Call AWS CLI command
* Capture JSON into Python dict using `json.loads()`
* Print only instance IDs

---

## 🧩 **5. Challenge Problems**

### **Challenge 1:**

Start and Stop an EC2 instance using boto3:

```
python ec2_control.py start i-0abc123
python ec2_control.py stop i-0abc123
```

Use `argparse`.

---

### **Challenge 2:**

Create an **S3 public URL** automation script:

* Upload file
* Add public read policy
* Print final URL

---

### **Challenge 3:**

Generate a **JSON report**:

```json
{
  "running": 3,
  "stopped": 1,
  "terminated": 0
}
```

Store to `ec2_report.json`.

---

## 📌 **6. Quick Interview Questions**

1️⃣ What does AWS CLI `configure` do?
2️⃣ What is the difference between Access key vs Secret key?
3️⃣ boto3 `client` vs `resource` — when to choose which?
4️⃣ What is an EC2 instance state?
5️⃣ What is a region & availability zone?
6️⃣ Why JSON is preferred output in automation?
7️⃣ How do DevOps teams avoid storing plain-text AWS keys?
8️⃣ What exception occurs when credentials expire?
9️⃣ What permissions do you need to manage EC2 instances?
🔟 Why S3 is commonly used in DevOps pipelines?

---

## 🏁 **7. Submission Checklist**

Before marking Day-16 complete:

✔ AWS CLI installed & configured
✔ EC2 instances listed successfully
✔ boto3 EC2 script works without crashing
✔ S3 upload/download tested
✔ Script handles errors properly

---

