import sys

import click
from aws_client import aws_client
from exceptions import CredentialsError


def prompt_for_credentials():
    """
    Prompts the user interactively for AWS Access Key ID and Secret Access Key.
    """
    access_key = click.prompt('Please enter your AWS Access Key ID', type=str)
    secret_key = click.prompt('Please enter your AWS Secret Access Key', type=str, hide_input=True)
    return access_key, secret_key


@click.command()
def auth():
    """
    Returns an S3 client using interactively prompted credentials.
    Supports optional role assumption.
    """
    try:
        access_key, secret_key = prompt_for_credentials()
        if not access_key or not secret_key:
            raise CredentialsError("Access Key ID or Secret Access Key not provided")
        aws_client.auth(access_key, secret_key)
    except CredentialsError as e:
        print(e)
        sys.exit(1)
