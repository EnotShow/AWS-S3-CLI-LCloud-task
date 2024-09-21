import sys

import click
from lcloud.aws_client import aws_client
from lcloud.exceptions import CredentialsError


def prompt_for_credentials():
    """
    Prompts the user interactively for AWS Access Key ID and Secret Access Key.
    """
    access_key = click.prompt('Please enter your AWS Access Key ID', type=str)
    secret_key = click.prompt('Please enter your AWS Secret Access Key', type=str, hide_input=True)
    return access_key, secret_key


@click.command()
@click.option('--access-key', required=False, help='The AWS Access Key ID.')
@click.option('--secret-key', required=False, help='The AWS Secret Access Key.')
def auth(access_key, secret_key):
    """
    Authenticates the AWS client with prompted credentials.
    """
    try:
        if not access_key or not secret_key:
            access_key, secret_key = prompt_for_credentials()
        if not access_key or not secret_key:
            raise CredentialsError("Access Key ID or Secret Access Key not provided")
        aws_client.auth(access_key, secret_key)
    except CredentialsError as e:
        print(e)
        sys.exit(1)
