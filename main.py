import click

from src.delete_files import delete_files
from src.upload_file import upload_file
from src.auth import auth
from src.list_files import list_files


@click.group()
def cli():
    """AWS S3 CLI"""
    pass


def add_commands():
    cli.add_command(auth)
    cli.add_command(list_files)
    cli.add_command(upload_file)
    cli.add_command(delete_files)


if __name__ == '__main__':
    add_commands()
    cli()

