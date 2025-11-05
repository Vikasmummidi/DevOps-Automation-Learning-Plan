

---

# 🚀 **systemctl Cheat Sheet — DevOps Edition**

## ✅ **Service Management**

| Action                               | Command                        |
| ------------------------------------ | ------------------------------ |
| Start service                        | `sudo systemctl start nginx`   |
| Stop service                         | `sudo systemctl stop nginx`    |
| Restart service                      | `sudo systemctl restart nginx` |
| Reload config without restart        | `sudo systemctl reload nginx`  |
| Enable service on boot               | `sudo systemctl enable nginx`  |
| Disable autostart                    | `sudo systemctl disable nginx` |
| Check service status                 | `systemctl status nginx`       |
| Check if service is active (running) | `systemctl is-active nginx`    |
| Check if enabled on boot             | `systemctl is-enabled nginx`   |
| View logs (journal logs)             | `journalctl -u nginx`          |

---

## ✅ **Powerful Status/Check Commands**

| Purpose                      | Command                               |
| ---------------------------- | ------------------------------------- |
| Check running state silently | `systemctl is-active --quiet nginx`   |
| Check if enabled silently    | `systemctl is-enabled --quiet nginx`  |
| List all services            | `systemctl list-units --type=service` |
| List failed services         | `systemctl --failed`                  |

---

## ✅ **System / OS level**

| Task                  | Command                        |
| --------------------- | ------------------------------ |
| Reboot server         | `sudo systemctl reboot`        |
| Shutdown server       | `sudo systemctl poweroff`      |
| Reload systemd config | `sudo systemctl daemon-reload` |

*(Used after editing .service files)*

---

## ✅ **Working With Service Files**

| Task                         | Command                                       |
| ---------------------------- | --------------------------------------------- |
| Service unit files directory | `/etc/systemd/system/*.service`               |
| View unit file               | `systemctl cat nginx`                         |
| Edit custom service file     | `sudo nano /etc/systemd/system/myapp.service` |
| Reload configs               | `sudo systemctl daemon-reload`                |
| Start after change           | `sudo systemctl restart myapp`                |

---

## ✅ **journalctl (logs)**

| Task                    | Command                  |
| ----------------------- | ------------------------ |
| Show logs for a service | `journalctl -u nginx`    |
| Show latest logs        | `journalctl -u nginx -f` |
| Logs since boot         | `journalctl -b`          |

---

## ✅ **Example: Health Check Script**

```bash
#!/bin/bash
service=$1

if systemctl is-active --quiet "$service"; then
    echo "$service running ✅"
else
    echo "$service NOT running ❌"
    exit 1
fi
```

---

## ✅ **Real DevOps Use Cases**

| Scenario                    | Usage                                          |
| --------------------------- | ---------------------------------------------- |
| EC2 startup scripts         | enable/start web app services                  |
| Jenkins pipelines           | restart app after deploy                       |
| System health automation    | check services before deployment               |
| Autoscaling lifecycle hooks | verify service before marking instance healthy |
| Kubernetes node prep        | enable Docker/Containerd service               |
| Ansible roles               | manage services via `systemd` module           |

---

## ✅ **Interview Questions**

| Question                                                            | Expected Answer Key                                   |
| ------------------------------------------------------------------- | ----------------------------------------------------- |
| How do you check if a service is running without displaying output? | `systemctl is-active --quiet service`                 |
| Difference between restart and reload                               | restart restarts process; reload reloads config only  |
| How do you reload systemd after editing service file?               | `systemctl daemon-reload`                             |
| Where are unit files stored?                                        | `/etc/systemd/system/` and `/usr/lib/systemd/system/` |

---

## 🎯 Quick Memory Trick

**Start / Stop / Restart / Status**

```
S S R S
start
stop
restart
status
```

**Enable / Disable / Daemon Reload**

```
E D R
enable
disable
daemon-reload

```
---

