#!/usr/bin/env python3

import boto3
from botocore.exceptions import ClientError, NoCredentialsError


def demo_s3(bucket_name, file_name):
    s3 = boto3.client("s3")

    try:
        # 1. Create bucket (safe to ignore if exists)
        print(f"[INFO] Ensuring bucket '{bucket_name}' exists...")
        try:
            s3.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'}
            )
        except ClientError as e:
            if e.response['Error']['Code'] != 'BucketAlreadyOwnedByYou':
                raise e

        # 2. Upload
        print("[INFO] Uploading file...")
        s3.upload_file(file_name, bucket_name, file_name)

        # 3. List objects
        print("[INFO] Listing objects...")
        objects = s3.list_objects_v2(Bucket=bucket_name)
        for obj in objects.get('Contents', []):
            print(" -", obj["Key"])

        # 4. Download
        print("[INFO] Downloading back...")
        s3.download_file(bucket_name, file_name, f"downloaded-{file_name}")

        # 5. Delete
        print("[INFO] Deleting uploaded object...")
        s3.delete_object(Bucket=bucket_name, Key=file_name)

        print("[SUCCESS] S3 automation completed!")

    except NoCredentialsError:
        print("ERROR: No AWS credentials found. Run 'aws configure'.")
    except ClientError as e:
        print(f"ERROR: AWS error: {e}")


if __name__ == "__main__":
    demo_s3("vikas-demo-bucket-12345", "test.txt")
