import click

from lcloud.commands.delete_files import delete_files
from lcloud.commands.upload_file import upload_file
from lcloud.commands.auth import auth
from lcloud.commands.list_files import list_files


@click.group()
def cli():
    """AWS S3 CLI"""
    pass


def add_commands():
    cli.add_command(auth)
    cli.add_command(list_files)
    cli.add_command(upload_file)
    cli.add_command(delete_files)


def main():
    add_commands()
    cli()


if __name__ == '__main__':
    main()
