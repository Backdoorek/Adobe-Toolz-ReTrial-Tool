import json
import click


class RenewTool:
    def __init__(self, config):
        self.__configpath = config
        self.reload_config()

    def reload_config(self):
        self.__config = json.load(open(self.__configpath, encoding='utf-8'))

    def renew(self, program, custom_key=False):
        click.echo('Renewing trial key for {}'.format(program))

        path = self.__config['Programs\' paths'][program]
        amt_file = open(path, encoding='utf-8', mode='r')
        file_content = amt_file.read()
        i = file_content.index('<Data key="TrialSerialNumber">') + 30

        old_trial_key = file_content[i:(i + 24)]
        click.echo('Old key loaded ({})'.format(old_trial_key))

        if custom_key:
            new_trial_key = custom_key
            click.echo('New key created (user request, {})'.format(custom_key))
        else:
            new_trial_key = str(int(old_trial_key) + 1)
            click.echo('New key created ({})'.format(new_trial_key))

        file_content = file_content.replace(old_trial_key, new_trial_key)
        click.echo('Key replaced')

        click.echo('Saving...')
        open(path, encoding='utf-8', mode='w').write(file_content)
        click.echo('Saved!')
        click.echo('{} -> {} | Old key replaced, now you can use your copy of {}'.format(
            new_trial_key,
            old_trial_key,
            program
        ))

    def renew_all(self):
        for program in self.__config['Enabled']:
            self.renew(program)

    def backup(self, program):
        click.echo('Selected program {}'.format(program))

        path = self.__config['Programs\' paths'][program]
        amt_file = open(path, encoding='utf-8', mode='r')
        file_content = amt_file.read()
        i = file_content.index('<Data key="TrialSerialNumber">') + 30

        trial_key = file_content[i:(i + 24)]
        click.echo('Key loaded')
        click.echo(trial_key, color='blue')

        click.echo('Saving...')
        self.__config['Default keys'][program] = trial_key
        open(self.__configpath, mode='w+').write(json.dumps(self.__config, indent=1))
        click.echo('Saved!')

        self.reload_config()
        click.echo('Config reloaded')

    def backup_all(self):
        for program in self.__config['Enabled']:
            self.backup(program)

    def restore(self, program):
        click.echo('Restoring original key for {}'.format(program))

        backup_key = self.__config['Default keys'][program]
        click.echo('Original key loaded ({})'.format(backup_key))

        self.renew(program, custom_key=backup_key)

    def restore_all(self):
        for program in self.__config['Default keys']:
            self.restore(program)

    def enable(self, program):
        if not program in self.__config["Programs' paths"]:
            click.echo('Program {} not recognized!!!'.format(program))
            return
        if program in self.__config['Enabled']:
            click.echo('{} exists on "Enabled" list! Skipping...'.format(program))
        else:
            click.echo('Enabling {}...'.format(program))
            self.__config['Enabled'].append(program)

            open(self.__configpath, encoding='utf-8', mode='w').write(json.dumps(self.__config, indent=2))
            click.echo('Enabled!')

            self.reload_config()
            click.echo('Config reloaded')

    def disable(self, program):
        if not program in self.__config['Enabled']:
            click.echo('Program {} is not enabled!!!'.format(program))
        else:
            click.echo('Disabling {}...'.format(program))
            del self.__config['Enabled'][program]

            open(self.__configpath, encoding='utf-8', mode='w').write(json.dumps(self.__config, indent=2))
            click.echo('Disabled!')

            self.reload_config()
            click.echo('Config reloaded')

    def enabled(self):
        click.echo('Showing {} products'.format(self.__config['Enabled'].__len__()))
        for program in self.__config['Enabled']:
            click.echo(program)


if __name__ == '__main__':
    k = RenewTool('config.json')
    k.renew('Photoshop')
