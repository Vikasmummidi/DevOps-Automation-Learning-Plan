

# 🧠 **Day-11 Interview Questions (JSON, YAML, Parsing, and DevOps Use Cases)**

These are real DevOps-level questions asked in companies like Deloitte, TCS, Infosys, Cognizant, HCL, and product-based firms.

---

# ⭐ **SECTION 1 — JSON Parsing (Python + DevOps)**

---

### **Q1. What is JSON and why is it used in DevOps?**

**A:**
JSON (JavaScript Object Notation) is a lightweight data-interchange format used across APIs, cloud services, and automation tools.
In DevOps it's used for:

* AWS CLI responses
* Kubernetes commands (`kubectl get pods -o json`)
* REST API automation
* Logging and monitoring tools

---

### **Q2. How do you load a JSON file in Python?**

```python
import json
with open("config.json") as f:
    data = json.load(f)
```

---

### **Q3. How do you parse nested JSON values?**

**Example:**

```python
data["instances"][0]["cpu"]
```

---

### **Q4. What’s the difference between `json.load()` and `json.loads()`?**

**A:**

* `json.load(f)` → loads JSON from **file**
* `json.loads(s)` → loads JSON from **string**

---

### **Q5. How do you modify JSON data and write it back to file?**

```python
data["key"] = "value"
json.dump(data, open("out.json", "w"), indent=4)
```

---

### **Q6. Common error: `TypeError: 'NoneType' object is not subscriptable` — Why?**

**A:**
It means your key doesn’t exist or YAML/JSON didn’t load properly.
Example:

```python
d["spec"]["template"] → None
```

---

### **Q7. How do you loop through all keys in a JSON object?**

```python
for key, value in data.items():
    print(key, value)
```

---

# ⭐ **SECTION 2 — YAML (Concepts & DevOps Use Cases)**

---

### **Q8. What are the main data types in YAML?**

**A:**

1. Scalar (simple values)
2. Map (dictionary)
3. List (sequence)

---

### **Q9. What is the difference between a YAML list and YAML map?**

**A:**

* List → `- item` (starts with hyphen)
* Map → `key: value`

---

### **Q10. Why does YAML require indentation?**

**A:**
Indentation defines hierarchy.
YAML uses spaces to indicate nested objects or lists.
Incorrect indentation breaks the structure.

---

### **Q11. What does this YAML represent?**

```yaml
containers:
  - name: app
    image: nginx
```

**A:**
`containers` is a **list of dictionaries**, each dictionary contains fields like `name` and `image`.

---

### **Q12. How do you load and parse YAML in Python?**

```python
import yaml
d = yaml.safe_load(open("file.yaml"))
```

---

### **Q13. What is the difference between `yaml.load()` and `yaml.safe_load()`?**

**A:**

* `safe_load()` → secure, recommended
* `load()` → can execute arbitrary code (unsafe)

---

### **Q14. How do you update a value inside a Kubernetes YAML file using Python?**

```python
d["spec"]["template"]["spec"]["containers"][0]["image"] = "nginx:latest"
yaml.safe_dump(d, open("deployment.yaml", "w"))
```

---

### **Q15. How do you write YAML back to a file?**

```python
yaml.safe_dump(d, open("output.yaml", "w"), sort_keys=False)
```

---

# ⭐ **SECTION 3 — Kubernetes YAML (Spec, Template, Containers)**

---

### **Q16. How do you access the first container image from a deployment YAML?**

```python
d["spec"]["template"]["spec"]["containers"][0]["image"]
```

---

### **Q17. What does `containers:` represent in Kubernetes?**

**A:**
It's a **list of containers** that run inside the Pod.

---

### **Q18. What is the purpose of `spec.template` in Kubernetes Deployments?**

**A:**
`template` defines the Pod specification used to create replicas.

---

### **Q19. Why is YAML important in Kubernetes?**

**A:**
Because all Kubernetes manifest files (deployments, services, pods, ingress) are written in YAML for easy configuration management.

---

### **Q20. How do you modify replicas in a deployment YAML using Python?**

```python
d["spec"]["replicas"] = 5
```

---

# ⭐ **SECTION 4 — Real DevOps Use Cases**

---

### **Q21. How do you extract non-running pods using JSON and Python?**

```python
pods = json.loads(out.stdout)
bad = [p["metadata"]["name"] for p in pods["items"] if p["status"]["phase"] != "Running"]
```

---

### **Q22. How do you read Ansible variable files in Python?**

```python
vars = yaml.safe_load(open("vars.yaml"))
print(vars["app_port"])
```

---

### **Q23. How do you update environment variables in a Kubernetes manifest?**

```python
d["spec"]["template"]["spec"]["containers"][0]["env"].append(
    {"name": "NEW_VAR", "value": "123"}
)
```

---

### **Q24. How do you print all container names inside a deployment YAML?**

```python
for c in d["spec"]["template"]["spec"]["containers"]:
    print(c["name"])
```

---

### **Q25. What tool can you use in Linux to validate YAML?**

**A:**
Tools like:

* `yq`
* `yamllint`
* `python3 -m yaml`
* `kubectl apply --dry-run=client`

---


