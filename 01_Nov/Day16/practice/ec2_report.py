import json
import boto3

def ec2_status_report():
    ec2 = boto.client("ec2")
    response = ec2.describe_instances()


    report = { "running":0, "stopped":0, "terminated":0 }

    for reservation in response["Reservations"]:
        for instance 
