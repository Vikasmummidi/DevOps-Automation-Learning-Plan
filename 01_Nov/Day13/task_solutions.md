

---

# ✅ **SHORT ANSWERS**

---

## **1. What is a virtual environment and why do we use it?**

A virtual environment (venv) is an isolated Python workspace that has its own packages and dependencies.
We use it to prevent version conflicts between projects and to ensure reproducible builds.

---

## **2. Difference between `pip install` and `pip install -r`?**

* `pip install package` → installs a single package.
* `pip install -r requirements.txt` → installs all packages listed in a requirements file (used for deploying consistent environments).

---

## **3. What does `pip freeze` do?**

`pip freeze` outputs all installed packages and their exact versions in the current environment.
Commonly used to generate `requirements.txt` for deployment.

---

## **4. What is a wheel file?**

A `.whl` file is a **built Python package** (binary distribution).
It installs faster than source distributions because it doesn’t need to compile anything.

---

## **5. What is `__init__.py` used for?**

It marks a directory as a Python package.
It allows imports like:

```python
from mypackage import module
```

---

## **6. How do you check from where a package is imported?**

Use:

```python
import package
print(package.__file__)
```

This prints the path to the installed package.

---

# ✅ **HANDS-ON CODING QUESTIONS**

---

## **1. Script: Print all installed packages and versions**

```python
import pkg_resources

for dist in pkg_resources.working_set:
    print(dist.project_name, dist.version)
```

---

## **2. Script: Check if `requests` is installed; if not, install it using subprocess**

```python
import subprocess
import pkg_resources

package = "requests"

try:
    pkg_resources.get_distribution(package)
    print("requests is already installed.")
except pkg_resources.DistributionNotFound:
    print("requests not found. Installing...")
    subprocess.run(["pip", "install", package])
```

---

## **3. Create venv, install boto3, and print S3 buckets**

### **Step 1: Create venv**

```bash
python3 -m venv awsenv
source awsenv/bin/activate
pip install boto3
```

### **Step 2: Python script — list_buckets.py**

```python
import boto3

s3 = boto3.client("s3")
response = s3.list_buckets()

for bucket in response["Buckets"]:
    print(bucket["Name"])
```

⚠️ Requires AWS CLI already configured (`aws configure`).

---

## **4. Modify `setup.py` to include author and description**

```python
from setuptools import setup, find_packages

setup(
    name="mycalculator",
    version="0.1",
    packages=find_packages(),
    author="Vikas Mummidi",
    description="A simple calculator package with basic math operations.",
)
```

---

## **5. Create a custom CLI command using entry points**

### **Step 1: Add entry point in setup.py**

```python
from setuptools import setup, find_packages

setup(
    name="mycalculator",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "mycalc = mycalculator.cli:main"
        ]
    },
)
```

### **Step 2: Create file `mycalculator/cli.py`**

```python
from mycalculator.operations import add

def main():
    print("Sum of 5 and 10 is:", add(5, 10))
```

After reinstalling the wheel, you can run:

```bash
mycalc
```

This executes your CLI tool.

---

# ✅ **4. REAL DEVOPS USE CASES**

---

## **1. Isolated environments for deployment scripts**

DevOps teams use virtual environments to avoid dependency conflicts between tools like AWS SDK, Ansible, Kubernetes Python clients, etc.

---

## **2. Packaging internal tools**

Internal automation tools (cleanup scripts, monitoring checks, log-processing utilities) are packaged as wheels and installed across servers.

---

## **3. Using requirements.txt in CI/CD pipelines**

CI pipelines install exact versions using:

```bash
pip install -r requirements.txt
```

This ensures builds deploy consistently across dev/staging/production.

---

## **4. Reproducible builds**

Using venv + requirements.txt ensures:

* Same dependency versions
* Same behavior across environments
* No “works on my machine” issues

---

## **5. Lambda function dependencies**

Python Lambda functions often require external libraries.
Teams package:

```
venv/lib/python3.*/site-packages
```

into a ZIP so AWS Lambda can run with the correct dependencies.

---


