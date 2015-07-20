import os
from getpass import getpass

import lya

cfgpath = os.path.expanduser('~/.config/exchangeutil/config.yaml')
cfg = None


def load():
    global cfg

    if cfg is None:
        cfg = lya.AttrDict.from_yaml(cfgpath)
        passwd = getpass("POP3 password for {}: ".format(cfg.pop3.user))
        cfg.pop3.passwd = passwd

    return cfg
