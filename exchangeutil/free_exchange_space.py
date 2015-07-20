from poplib import POP3, POP3_SSL
from datetime import datetime, timedelta
from argparse import ArgumentParser

from etaprogress.progress import ProgressBar

from .config import load as load_config

MAX_DELETE = 1000


def main():
    parser = ArgumentParser()
    parser.add_argument('--debug', action='store_true')
    args = parser.parse_args()

    cfg = load_config()
    cfg.debug = args.debug

    popfunc = POP3_SSL if cfg.pop3.ssl else POP3
    pop = popfunc(cfg.pop3.host)
    pop.user(cfg.pop3.user)
    pop.pass_(cfg.pop3.passwd)

    num = len(pop.list()[1])
    n_delete = 0

    bar = ProgressBar(num)

    for i in range(1, num+1):
        bar.numerator = i - 1
        if not cfg.debug:
            print(bar, end='\r')
        mail = pop.retr(i)[1]
        if to_delete(mail, cfg):
            n_delete += 1
            if cfg.debug:
                print("Mark {} to be delete".format(i))
            pop.dele(i)
            if n_delete == MAX_DELETE:
                break

    answer = input("Okay to delete {} mails? (y/N) ".format(n_delete))
    if answer != 'y':
        pop.rset()

    pop.quit()

    if n_delete == MAX_DELETE:
        print("There may be more mails to delete.  You may want to re-run this script.")


def to_delete(mail, cfg):
    old = None
    mine = None
    date_threshold = datetime.today() - timedelta(days=cfg.keepdays)

    for line in mail:
        try:
            line = line.decode('utf8')
        except UnicodeDecodeError:
            continue

        if line.startswith('Date: '):
            try:
                dt = datetime.strptime(' '.join(line.split()[1:-1]),
                                       '%a, %d %b %Y %H:%M:%S')
            except ValueError:
                # unknown date format, do not delete it for safe
                old = False

            if cfg.debug:
                print("Date:", dt)
            old = dt < date_threshold

        elif line.startswith('From: '):
            mine = cfg.pop3.user.lower() in line.lower()
            if cfg.debug:
                print(line)

    if old is None:
        print("unknown date")
        return False

    if mine is None:
        print("Unknown from")
        return False

    if cfg.keepmine:
        return old and not mine
    else:
        return old
