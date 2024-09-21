import sys
import re

import click
from botocore.exceptions import ClientError

from aws_client import aws_client
from exceptions import CredentialsError


@click.command(name='delete')
@click.option('--bucket', required=True, help='The name of the S3 bucket.')
@click.option('--regex', required=True, help='Regex pattern to match files to delete.')
@click.option('--prefix', required=False, help='Prefix to match files to delete.')
def delete_files(bucket, regex, prefix):
    """Delete all files matching a regex."""
    try:
        s3 = aws_client.get_client()
        response = s3.list_objects_v2(Bucket=bucket, Prefix=prefix)
        if 'Contents' in response:
            pattern = re.compile(regex)
            delete_keys = [{'Key': obj['Key']} for obj in response['Contents'] if pattern.match(obj['Key'])]
            if delete_keys:
                s3.delete_objects(Bucket=bucket, Delete={'Objects': delete_keys})
                print(f"Deleted files: {', '.join([d['Key'] for d in delete_keys])}")
            else:
                print("No files matching the regex were found.")
        else:
            print(f"No files found in bucket '{bucket}'.")
    except ClientError as e:
        print(f"Error deleting files: {e}")
        sys.exit(1)
    except CredentialsError as e:
        print(e)
        sys.exit(1)
