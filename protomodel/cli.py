import click

@click.group()
def cli():
    pass

@cli.command()
def generate():
    click.echo("Generating file...")

if __name__ == "__main__":
    cli()