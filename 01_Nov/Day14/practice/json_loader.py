import json
import os
import sys

def load_config(file_path, requried_keys=None):
    if not os.path.exists(file_path):
        print(f"ERROR: config file not found: {file_path}")
        return None

    try:
        with open(file_path,"r") as f:
            config = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format in {file_path}")
        print(f"Details: {e}")
        return None

    except Exception as e:
        print(f"ERROR: could not read file {file_path}")
        print(f"Details: {e}")
        return None

    if requried_keys:
        for key in requried_keys:
            if key not in config:
                print(f"ERROR: Missing required key '{key}' in config file.")
                return None

    return config


if __name__ == "__main__":
    required = ["path", "threshold", "email_alert"]

    config = load_config("config.json", required)


    if config is None:
        print("configuration load failed. Exiting.")
        sys.exit(1)

    print("config loaded successfully:", config)
