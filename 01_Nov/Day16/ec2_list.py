import boto3
from botocore.exceptions import NoCredentialsError, ClientError


def list_ec2_instances():
    ec2 = boto3.client("ec2")

    try:
        response = ec2.describe_instances()
    except NoCredentialsError:
        print("ERROR: AWS credentials not configured. Run 'aws configure'.")
        return
    except ClientError as e:
        print(f"ERROR: AWS error: {e}")
        return

    print("\n--- EC2 Instance List ---\n")
    count = 0

    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            instance_id = instance["InstanceId"]
            state = instance["State"]["Name"]
            print(f"Instance: {instance_id} | State: {state}")
            count += 1

    print(f"\nTotal Instances Found: {count}")


if __name__ == "__main__":
    list_ec2_instances()
