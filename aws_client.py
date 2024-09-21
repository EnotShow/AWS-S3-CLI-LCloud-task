import os

import boto3

from exceptions import CredentialsError


class AWSClient:

    def auth(self, aws_access_key_id, aws_secret_access_key):
        os.environ['AWS_ACCESS_KEY_ID'] = aws_access_key_id
        os.environ['AWS_SECRET_ACCESS_KEY'] = aws_secret_access_key

    def get_client(self):
        access_key = os.getenv('AWS_ACCESS_KEY_ID')
        secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')

        if not access_key or not secret_key:
            raise CredentialsError("Credentials not provided")

        return boto3.client(
            's3',
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key
        )


aws_client = AWSClient()
