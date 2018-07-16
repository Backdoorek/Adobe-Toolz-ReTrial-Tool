import click
from renew import RenewTool


@click.option('--config', default='config.json', help='Specify directory for config file (include filename).')
@click.group()
def cli(config):
    global rt
    rt = RenewTool(config)


@click.command(help='Creates backup of primary trial key.')
@click.argument('adobe_product', default='all')
def backup(adobe_product):
    if adobe_product == 'all':
        rt.backup_all()
    else:
        rt.backup(adobe_product)


@click.command(help='Creates and replaces actual trial key.')
@click.option('--key', default=False, type=click.STRING, help='Use this to provide your own 24 digit trial key.')
@click.argument('adobe_product', default='all')
def renew(adobe_product, key):
    if adobe_product == 'all':
        rt.renew_all()
    else:
        if key:
            rt.renew(adobe_product, key)
        else:
            rt.renew(adobe_product)


@click.command(help='Restores backed-up trial key.')
@click.argument('adobe_product', default='all')
def restore(adobe_product):
    if adobe_product == 'all':
        rt.restore_all()
    else:
        rt.restore(adobe_product)

@click.command(help='Allow to manage with enabled Adobe software.')
@click.option('--enable', default=False, type=click.STRING, help='Enable selected product.')
@click.option('--disable', default=False, type=click.STRING, help='Disable selected product.')
def manage(enable, disable):
    if not enable and not disable:
        rt.enabled()
    else:
        if enable:
            rt.enable(enable)
        if disable:
            rt.disable(disable)


cli.add_command(backup)
cli.add_command(renew)
cli.add_command(restore)
cli.add_command(manage)

if __name__ == '__main__':
    cli()
