#!\usr\bin\env \python3
import subprocess
import sys

def run_cmd(cmd):
    """Run system command safely and return output """
    output=subprocess.run(cmd,capture_output=True,text=True)
    if output.returncode != 0:
        print(f"[ERROR] command failed: {''.join(cmd)}")
        print(output.stderr)
        sys.exit(1)
    return output.stdout.strip()


def build_image(tag="myapp:latest"):
    print("[INFO] Building image...")
    run_cmd(["docker","build","-t",tag,"."])
    print("[SUCCESS] image built.")
    
def run_container(tag="myapp:latest"):
    print("[INFO] Running container...")
    cid=run_cmd(["docker","run","-d",tag])
    print("[INF0] containerID:", cid)
    return cid

def show_logs(container_id):
    print("[INFO] Logs:")
    logs=run_cmd(["docker","logs",container_id])
    print(logs)

def stop_container(container_id):
    print("[INFO] Stopping container...")
    run_cmd(["docker","stop",container_id])
    print("[INFO] removing container...")
    run_cmd(["docker","rm",container_id])
    print("[SUCCESS] container cleaned up.")

if __name__ == "__main__":
    build_image()
    cid = run_container()
    show_logs(cid)
    stop_container(cid)



