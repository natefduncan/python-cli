import click

@click.group()
def cli():
    pass

@cli.command
@click.argument('input', type=click.File('rb'))
def command1(input):
    click.echo(input)

@cli.command
def command2():
    click.echo('Command2')

if __name__=='__main__':
    cli()
