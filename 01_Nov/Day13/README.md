

---

# ✅ **Day-13 Practice Worksheet**

**Focus Area:** Python
**Topic:** Virtualenv, pip & Packaging
**Overview:** Create virtual environments, install packages, explore pip commands, create a basic Python package
**Estimated Time:** 2 hours

---

# 📌 **1. Concepts to Learn (Quick Theory – 10 minutes)**

### 👉 **Virtual Environments**

* What is a virtual environment?
* Why DevOps uses venvs (isolated dependencies, reproducible builds)
* Creating & activating venv:

  * Windows: `python -m venv venv`, `venv\Scripts\activate`
  * Linux/Mac: `python3 -m venv venv`, `source venv/bin/activate`

### 👉 **pip Basics**

* Installing packages
  `pip install requests`
* Listing packages
  `pip list`
* Freeze dependencies
  `pip freeze > requirements.txt`
* Installing from requirements file
  `pip install -r requirements.txt`

### 👉 **Packaging**

* Project structure

```
myproject/
    mypackage/
        __init__.py
        main.py
    setup.py
```

* Writing a simple `setup.py`
* Creating a wheel file

---

# 📝 **2. Practice Tasks (Hands-On)**

## **Task 1: Create a Virtual Environment**

1. Create a directory:

   ```
   mkdir day13_practice && cd day13_practice
   ```
2. Create a virtual environment:

   ```
   python3 -m venv venv
   ```
3. Activate it.

### ✔ Verify activation using:

```
which python
pip list
```

---

## **Task 2: Install & Manage Packages**

1. Install:

   ```
   pip install requests flask
   ```
2. Check installed versions:

   ```
   pip show requests
   ```
3. List packages:

   ```
   pip list
   ```
4. Freeze them:

   ```
   pip freeze > requirements.txt
   ```
5. Delete venv, recreate, and reinstall using:

   ```
   pip install -r requirements.txt
   ```

---

## **Task 3: Explore pip Commands**

Run the following:

```
pip search http
pip uninstall flask
pip check
pip cache dir
pip cache list
```

Write 2–3 lines explaining each command.

---

## **Task 4: Build Your First Python Package**

### Step 1: Create folder structure

```
mycalculator/
    mycalculator/
        __init__.py
        operations.py
    setup.py
```

### Step 2: Add sample code

**operations.py**

```python
def add(a, b):
    return a + b
```

### Step 3: Write **setup.py**

```python
from setuptools import setup

setup(
    name="mycalculator",
    version="0.1",
    packages=["mycalculator"]
)
```

### Step 4: Build package

```
pip install setuptools wheel
python setup.py sdist bdist_wheel
```

### Step 5: Install your package locally

```
pip install dist/mycalculator-0.1-py3-none-any.whl
```

Test your package:

```python
from mycalculator.operations import add
print(add(5, 10))
```

---

## **Task 5: Publish a Package Locally (Optional Advanced)**

Configure a local PyPI repo using:

```
python -m http.server
```

Upload your wheel file and install via:

```
pip install --index-url http://localhost:8000/ mycalculator
```

---

# 🧠 **3. Practice Questions (Interview + Practical)**

### **Short Answers**

1. What is a virtual environment and why do we use it?
2. Difference between `pip install` and `pip install -r`?
3. What does `pip freeze` do?
4. What is a wheel file?
5. What is `__init__.py` used for?
6. How do you check from where a package is imported?

### **Hands-On Coding Questions**

1. Write a script that prints all installed packages and their versions.
2. Write a script that checks if `requests` is installed; if not, installs it using `subprocess`.
3. Create a venv, install `boto3`, and write a Python script that prints all S3 buckets (only if AWS CLI is already configured).
4. Modify your `setup.py` to include author and description fields.
5. Create a custom CLI command for your package using entry points.

---

# 💡 **4. Real DevOps Use Cases**

* Isolated environments for deployment scripts
* Packaging internal tools (like cleanup scripts, monitoring utilities)
* Using `requirements.txt` in CI/CD pipelines
* Reproducible builds across dev/stage/prod
* Lambda function dependencies packaged with venv

---

# 📌 **5. Submission Checklist**

Before ending Day-13, make sure you have:

✔ Created & activated a venv
✔ Installed & managed packages
✔ Generated `requirements.txt`
✔ Created your first Python package
✔ Built a wheel file
✔ Installed your package locally

---


