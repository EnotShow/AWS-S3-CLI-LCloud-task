import boto3

from src.exceptions import CredentialsError


class AWSClient:
    aws_access_key_id = None
    aws_secret_access_key = None

    def auth(self, aws_access_key_id, aws_secret_access_key):
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key

    def get_client(self):
        if not self.aws_access_key_id or not self.aws_secret_access_key:
            raise CredentialsError("Credentials not provided")

        return boto3.client(
            's3',
            aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key
        )


aws_client = AWSClient()
