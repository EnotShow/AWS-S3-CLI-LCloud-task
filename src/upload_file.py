import sys

import click
from botocore.exceptions import ClientError

from aws_client import aws_client
from exceptions import CredentialsError


@click.command(name='upload')
@click.option('--bucket', required=True, help='The name of the S3 bucket.')
@click.option('--file', required=True, type=click.Path(exists=True), help='Path to the local file.')
def upload_file(bucket, file, key):
    """Upload a local file to a defined location in the bucket with prompted credentials."""
    try:
        s3 = aws_client.get_client()
        s3.upload_file(file, bucket, key)
        print(f"File '{file}' uploaded to bucket '{bucket}' at '{key}'.")
    except FileNotFoundError:
        print("The file was not found.")
        sys.exit(1)
    except ClientError as e:
        print(f"Error uploading file: {e}")
        sys.exit(1)
    except CredentialsError as e:
        print(e)
        sys.exit(1)
