# Day 1: Linux Basics for DevOps - Files, Permissions, and Environment Variables

## 🧭 Overview
Today’s focus is on understanding how the Linux filesystem, permissions, and environment variables work — the foundation for every DevOps engineer working with automation or CI/CD pipelines.

### 📘 Topics Covered
1. **Linux Filesystem Overview**
   - Understanding directory structure (`/bin`, `/etc`, `/home`, `/var`, etc.)
   - Absolute vs relative paths
   - Hidden files and configuration files

2. **File Permissions**
   - Ownership: user, group, others
   - Permission types: read (r), write (w), execute (x)
   - Changing permissions using `chmod`
   - Changing ownership using `chown`
   - Recursive permission changes (`chmod -R`)

3. **Environment Variables**
   - Listing environment variables: `env`, `printenv`
   - Setting temporary and permanent environment variables
   - The difference between `.bashrc`, `.bash_profile`, `.profile`
   - Exporting variables for child processes

4. **Why Shell Matters in DevOps**
   - Core to automation: used in Jenkins, CI/CD, Kubernetes scripts, and cloud automation
   - Lightweight, fast, and universal across all Linux systems
   - Interacts natively with system commands and configurations

5. **Practical Tasks**
   - Create and list files with different permissions
   - Write a simple `env_info.sh` script that prints system information
   - Create a symbolic link to `env_info.sh`
   - Change permissions recursively for a folder

6. **References**
   - [Bash Scripting Tutorial - TutorialsPoint](https://www.tutorialspoint.com/unix/shell_scripting.htm)
   - [GNU Bash Manual](https://www.gnu.org/software/bash/manual/bash.html)
   - [Linux File Permissions - Red Hat](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/securing_networks/understanding-linux-file-permissions_securing-networks)

---

### ✅ Deliverables
- `env_info.sh` script
- Symbolic link test
- Recursive permission exercise
- Interview preparation notes

