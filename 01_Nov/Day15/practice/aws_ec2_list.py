#!/usr/bin/env python3
import boto3
from botocore.exceptions import NoCredentialsError, ClientError

def list_instances():
    ec2=boto3.client("ec2")

    try:
        response = ec2.describe_instances()
    except NoCredentialsError:
        print("[ERROR] AWS credentials not configured. Run 'aws configure' .")
        return
    except ClientError as e:
        print(f"[ERROR] AWS error:{e}")
        return

    print("\n====EC2 Instances===\n")

    count = 0

    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            instance_id = instance["InstanceId"]
            state = instance["State"]["Name"]

            print(f"Instance: {instance_id}")
            print(f"State: {state}")
            print("-" * 30)

            count += 1

    print(f"\n Total instances: {count}")

def list_running_instances():
    ec2=boto3.client("ec2")
    response = ec2.describe_instances(
                    Filters=[{"Name": "instance-state-name", "Values": ["running"]}]
                )

    print(f"response: {response}")
    print("\n===Running Instances====\n")

    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            print(f"Running Instance: {instance['InstanceId']}")

if __name__ == "__main__":
    list_instances()
    list_running_instances()


