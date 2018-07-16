import click
from renew import RenewTool


@click.option('--config', default='config.json', help='Specify directory for config file (include filename).')
@click.group()
def cli(config):
    global rt
    rt = RenewTool(config)


@click.command(help='Creates backup of primary trial key.')
@click.argument('program', default='all')
def backup(program):
    if program == 'all':
        rt.backup_all()
    else:
        rt.backup(program)


@click.command(help='Creates and replaces actual trial key.')
@click.option('--key', default=False, type=click.STRING, help='Use this to provide your own 24 digit trial key.')
@click.argument('program', default='all')
def renew(program, key):
    if program == 'all':
        rt.renew_all()
    else:
        if key:
            rt.renew(program, key)
        else:
            rt.renew(program)


@click.command(help='Restores backed-up trial key.')
@click.argument('program', default='all')
def restore(program):
    if program == 'all':
        rt.restore_all()
    else:
        rt.restore(program)


cli.add_command(backup)
cli.add_command(renew)
cli.add_command(restore)

if __name__ == '__main__':
    cli()
