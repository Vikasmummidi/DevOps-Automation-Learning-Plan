

---

# 🔥 **DAY-13 — INTERVIEW QUESTIONS (WITH ANSWERS)**

*You can use these for practice, mock interviews, or notes.*

---

# ✅ **SECTION 1 — Virtual Environments & Dependency Management**

### **1. What is a virtual environment and why is it important in DevOps?**

A virtual environment isolates Python packages for each project so updates or conflicts do not affect other deployments. This ensures reproducible builds across dev/staging/prod.

---

### **2. How do you create and activate a virtual environment in Linux and Windows?**

**Linux/macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**

```cmd
python -m venv venv
venv\Scripts\activate
```

---

### **3. What happens internally when you activate a venv?**

It modifies `PATH` to point Python and pip to the venv’s `bin/` location instead of the system Python.

---

### **4. How do you check which Python interpreter is being used inside venv?**

```bash
which python
```

or

```python
import sys
print(sys.executable)
```

---

### **5. Can you have multiple virtual environments in a single machine? Why?**

Yes — each project can maintain its own dependencies without conflict.

---

# ✅ **SECTION 2 — pip Commands**

### **6. Difference between `pip install package` and `pip install -r file.txt`?**

`pip install package` installs one library.
`pip install -r requirements.txt` installs a full environment snapshot.

---

### **7. What does `pip freeze` do and when do you use it?**

It prints all installed packages with exact versions — used to generate `requirements.txt` for deployment.

---

### **8. What does `pip check` do?**

It validates if installed dependencies are consistent and warns about version conflicts.

---

### **9. What is the purpose of pip cache?**

Speeds up installations by reusing previously downloaded wheels and source archives.

---

### **10. Why is `pip search` deprecated?**

Because PyPI disabled its backend API for security and traffic concerns.

---

# ✅ **SECTION 3 — Python Packaging (setup.py, wheels, sdist)**

### **11. What is a wheel file and why is it preferred?**

A wheel (`.whl`) is a pre-built binary distribution.
It installs instantly with no compilation required.

---

### **12. What is the difference between sdist and wheel?**

sdist = source tarball (.tar.gz)
wheel = pre-built binary (.whl)
Most CI/CD pipelines use wheels for faster installs.

---

### **13. What is `__init__.py` used for?**

It marks a folder as a Python package and enables package imports.

---

### **14. What does `setup.py` do?**

It defines package metadata (name, version, author) and instructs `pip` how to build and install the package.

---

### **15. What are entry points in setup.py?**

They create CLI commands that run Python functions, e.g.:

```bash
mytool
```

---

### **16. How do you find where a Python package is located?**

```python
import package
print(package.__file__)
```

---

### **17. Why is `python setup.py install` deprecated?**

Replaced by standards-based builds using `build` and `pip install <wheel>` for security and consistency.

---

### **18. What does `find_packages()` do in setup.py?**

Automatically discovers all packages and subpackages.

---

# ✅ **SECTION 4 — Subprocess & Automation**

### **19. How do you install a Python package from inside a Python script?**

Using subprocess:

```python
subprocess.run(["pip", "install", "package"])
```

---

### **20. How do you check if a package is installed in Python?**

```python
import pkg_resources
pkg_resources.get_distribution("requests")
```

---

### **21. What are risks of running pip from subprocess in CI/CD?**

* May require root access
* Can cause dependency drift
* Should be avoided in production unless strictly needed

---

# ✅ **SECTION 5 — Real DevOps Use Cases**

### **22. How do you use virtual environments in CI/CD pipelines?**

Create a clean venv → install dependencies → run tests/build → discard environment.

---

### **23. How do Python wheels help deployment in production?**

They enable fast, reproducible installs without compiling code each deployment.

---

### **24. Why do we maintain a requirements.txt file?**

To ensure exact dependency versions are installed in dev/staging/prod.

---

### **25. How do you package Python code for AWS Lambda?**

Use a venv → install dependencies → zip the `site-packages` + your lambda code.

---

### **26. How do internal DevOps teams use packaging?**

To distribute internal utilities such as cleanup scripts, monitoring checks, automation tools.

---

### **27. How do you isolate dependencies in EKS, EC2, or on-prem servers?**

Each service or script uses its own virtual environment or container.

---


