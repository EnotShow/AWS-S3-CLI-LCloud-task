import boto3
import keyring

from exceptions import CredentialsError


class AWSClient:
    def __init__(self, service_name="aws_s3"):
        self.service_name = service_name

    def auth(self, aws_access_key_id, aws_secret_access_key):
        """
        Store AWS credentials securely using the keyring.
        """
        keyring.set_password(self.service_name, "AWS_ACCESS_KEY_ID", aws_access_key_id)
        keyring.set_password(self.service_name, "AWS_SECRET_ACCESS_KEY", aws_secret_access_key)

    def get_client(self):
        """
        Retrieve AWS credentials from keyring and create a boto3 client.
        """
        access_key = keyring.get_password(self.service_name, "AWS_ACCESS_KEY_ID")
        secret_key = keyring.get_password(self.service_name, "AWS_SECRET_ACCESS_KEY")

        if not access_key or not secret_key:
            raise CredentialsError("Credentials not found in keyring. Please authenticate first.")

        return boto3.client(
            's3',
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key
        )


aws_client = AWSClient()
