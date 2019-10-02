# Adobe-Toolz-ReTrial-Tool

## THIS METHOD DOESN'T WORK ON CC 2019! Use 2018 versions or older! [All 2018 CC downloads](https://prodesigntools.com/adobe-cc-2018-direct-download-links.html)

[Download latest release](https://github.com/Backdoorek/Adobe-Toolz-ReTrial-Tool/releases/latest)

[Wiki](https://github.com/Backdoorek/Adobe-Toolz-ReTrial-Tool/wiki)

Basic Usage
```
D:\Toolz\ATRT>cli.py --help
Usage: cli.py [OPTIONS] COMMAND [ARGS]...

Options:
  --config TEXT  Specify directory for config file (include filename).
  --help         Show this message and exit.

Commands:
  backup   Creates backup of primary trial key.
  renew    Creates and replaces actual trial key.
  restore  Restores backed-up trial key.

D:\Toolz\ATRT>cli.py renew --help
Usage: cli.py renew [OPTIONS] [PROGRAM]

  Creates and replaces actual trial key.

Options:
  --key TEXT  Use this to provide your own 24 digit trial key.
  --help      Show this message and exit.

D:\Toolz\ATRT>cli.py renew
Renewing trial key for Photoshop
Old key loaded (911987057659283838047469)
New key created (911987057659283838047470)
Key replaced
Saving...
Saved!
```
