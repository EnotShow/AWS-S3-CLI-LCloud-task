import click


from src.auth import auth
from src.list_files import list_files


@click.group()
def cli():
    """AWS S3 CLI"""
    pass


def add_commands():
    cli.add_command(auth)
    cli.add_command(list_files)


if __name__ == '__main__':
    add_commands()
    cli()

