#!/usr/bin/env python3
import subprocess

def run_cmd(cmd):
    result=subprocess.run(cmd, capture_output=True,text=True)
    return result.stdout.strip(), result.returncode

def check_disk():
    output, _ = run_cmd(["df", "-h","/"])
    print("==== Disk Info ====\n", output)

def check_cpu():
    output, _ = run_cmd(["top","-bn1"])
    print("==== CPU Usage ====\n", output.splitlines()[2])

def check_service(service):
    _,code = run_cmd(["systemctl","is-active",service])
    print(f"{service}:{'Running ✅' if code == 0 else 'Not Running ❌'}")


if __name__=="__main__":
    check_disk()
    check_cpu()
    check_service("nginx")

