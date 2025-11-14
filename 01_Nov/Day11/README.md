

# 🧭 **Day-11 (11-Nov-2025) — Python: JSON & YAML Parsing**

**Focus Area:** Python
**Topic:** JSON & YAML parsing
**Overview:** Parse config files and API responses (very important for DevOps)

Let’s create a **clear, structured Day-11 worksheet**, aligned with your DevOps workflow.

---

# 📘 **Day-11 Practice Worksheet — JSON & YAML Parsing (DevOps Focused)**

## ⏱️ **2-Hour Study Plan**

| Time       | Topic              | Focus                                       |
| ---------- | ------------------ | ------------------------------------------- |
| 0–20 min   | JSON basics        | Python `json` module                        |
| 20–45 min  | Parse complex JSON | Nested dicts, lists, API-style JSON         |
| 45–75 min  | YAML basics        | PyYAML: load, safe_load, dump               |
| 75–120 min | DevOps use cases   | Kubernetes YAML, Ansible vars, config files |

---

# 🧩 **1️⃣ JSON Basics (20 min)**

Python uses the built-in `json` module.

### ✔️ Load JSON string → Python dict

```python
import json

data = '{"name": "Vikas", "role": "DevOps"}'
parsed = json.loads(data)
print(parsed["role"])
```

---

### ✔️ Load JSON file

```python
with open("config.json") as f:
    data = json.load(f)

print(data["aws"]["region"])
```

---

### ✔️ Write JSON to file

```python
with open("output.json", "w") as f:
    json.dump(data, f, indent=4)
```

---

# 🧩 **2️⃣ Parsing Complex JSON (25 min)**

Example JSON (typical API):

```json
{
  "status": "OK",
  "instances": [
    {"id": "i-1", "cpu": 72},
    {"id": "i-2", "cpu": 84}
  ]
}
```

### ✔️ Access nested values

```python
with open("instances.json") as f:
    d = json.load(f)

high_cpu = [i["id"] for i in d["instances"] if i["cpu"] > 80]
print(high_cpu)
```

→ Output: `['i-2']`

---

### ✔️ Real DevOps Example

Check unhealthy pods from `kubectl get pods -o json`:

```python
import json
import subprocess

out = subprocess.run(
    ["kubectl", "get", "pods", "-o", "json"],
    capture_output=True,
    text=True
)

pods = json.loads(out.stdout)

not_ready = [
    p["metadata"]["name"]
    for p in pods["items"]
    if p["status"]["phase"] != "Running"
]

print("Not running:", not_ready)
```

---

# 🧩 **3️⃣ YAML Basics (30 min)**

YAML is everywhere in DevOps:

* Kubernetes
* Ansible
* GitHub Actions
* Jenkinsfiles (YAML versions)
* ArgoCD
* Helm values

Install PyYAML:

```bash
pip install pyyaml
```

---

### ✔️ Load YAML file

```python
import yaml

with open("config.yaml") as f:
    data = yaml.safe_load(f)

print(data["database"]["host"])
```

---

### ✔️ Write YAML file

```python
with open("output.yaml", "w") as f:
    yaml.safe_dump(data, f)
```

---

### ✔️ YAML vs JSON

* YAML supports comments (`#`)
* Easier for humans, more common in DevOps
* JSON is stricter (no comments, must be quoted)

---

# 🧩 **4️⃣ DevOps Use Cases (45 min)**

### **Use Case 1: Parse Kubernetes YAML**

```python
import yaml

with open("deployment.yaml") as f:
    d = yaml.safe_load(f)

print(d["spec"]["template"]["spec"]["containers"][0]["image"])
```

---

### **Use Case 2: Modify image in a K8s manifest**

```python
d["spec"]["template"]["spec"]["containers"][0]["image"] = "nginx:latest"

with open("deployment.yaml", "w") as f:
    yaml.safe_dump(d, f)
```

---

### **Use Case 3: Read Ansible variables**

```python
with open("vars.yaml") as f:
    vars = yaml.safe_load(f)

print(vars["app_port"])
```

---

### **Use Case 4: Parse AWS CLI JSON output**

```python
import json, subprocess

out = subprocess.run(
    ["aws", "ec2", "describe-instances"],
    capture_output=True,
    text=True
)

data = json.loads(out.stdout)

instances = [
    i["InstanceId"]
    for r in data["Reservations"]
    for i in r["Instances"]
]

print(instances)
```

---

# 🧠 **Day-11 Key Notes Summary**

| Topic          | Python Tool         | Why DevOps Needs It                    |
| -------------- | ------------------- | -------------------------------------- |
| JSON           | `json.load`/`loads` | Parse AWS, Kubernetes API responses    |
| YAML           | `yaml.safe_load`    | Work with K8s manifests, Helm, Ansible |
| Modify configs | `dump`              | Automate config generation             |
| API Responses  | JSON parsing        | Monitoring, automation tools           |
| CI/CD          | YAML parsing        | GitHub Actions, GitLab CI, ArgoCD      |

---

# 🧪 **Practice Exercises (10 tasks)**

### 1. Load `config.json` and print a nested key.

### 2. Modify JSON and write back to file.

### 3. Convert JSON → YAML using Python.

### 4. Convert YAML → JSON.

### 5. Parse Kubernetes deployment YAML and print:

* image name
* replica count

### 6. Write a script that checks if pods are "Running".

### 7. Parse AWS EC2 instances JSON and print instance IDs.

### 8. Read `values.yaml` (Helm) and update an environment variable.

### 9. Read a multi-document YAML and print all documents.

### 10. Merge two YAML files into one final config.

---


