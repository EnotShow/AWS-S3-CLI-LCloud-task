import click


from src.auth import auth


@click.group()
def cli():
    """AWS S3 CLI"""
    pass


def add_commands():
    cli.add_command(auth)


if __name__ == '__main__':
    add_commands()
    cli()

