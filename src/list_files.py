import sys
import re

import click
from botocore.exceptions import ClientError

from aws_client import aws_client
from exceptions import CredentialsError


@click.command(name='list')
@click.option('--bucket', required=True, help='The name of the S3 bucket.')
@click.option('--regex', required=False, help='Specify a file regex filter.')
def list_files(bucket, regex):
    """List all files in an S3 bucket."""
    try:
        s3 = aws_client.get_client()

        response = s3.list_objects_v2(Bucket=bucket)
        if 'Contents' in response:
            if regex:
                pattern = re.compile(regex)
                for obj in response['Contents']:
                    if pattern.match(obj['Key']):
                        print(obj['Key'])
            for obj in response['Contents']:
                print(obj['Key'])
        else:
            print(f"No files found in bucket '{bucket}'.")
    except ClientError as e:
        print(f"Error listing files: {e}")
        sys.exit(1)
    except CredentialsError as e:
        print(e)
        sys.exit(1)
