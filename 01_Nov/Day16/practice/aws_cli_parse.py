import subprocess
import json

def list_instance_ids():
    cmd = [
            "aws", "ec2", "describe-instances",
            "--query", "Reservations[].Instances.InstanceId"
            ]
    result = subporcess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print("command failed:", result.stderr)
        return
    instance_ids = json.loads(result.stdout)
    print("/n--- EC2 Instances from CLI (parsed in python)  ---\n")

    for inst in instance_ids:
        print(inst)


if __name__ == "__main__":
    list_instance_ids()
