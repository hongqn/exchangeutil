# Exchange Utils

## Installation

### Mac OS X (via [Homebrew](http://brew.sh)'ed Python)

1. `brew install python3`
2. `pip3 install -e 'git+https://github.com/hongqn/exchangeutil#egg=exchangeutil'`
3. `hash -r`
4. `mkdir -p ~/.config/exchangeutil/`
5. `vi ~/.config/exchangeutil/config.yaml`  # see config example

## Config example

```yaml
pop3:
  ssl: true   # use POP3_SSL or not?
  host: email.example.com  # POP3 host
  user: user@example.com   # POP3 account

keepdays: 50    # mails older than this will be deleted
keepmine: true  # keep mails sent from me or not?
```

## Utils

### free-exchange-space

Run `free-exchange-space` to delete old mails.

It will ask for POP3 password and scan all mails to find what to delete.  After scanning, it prints number of mails to delete and ask for permission.

### More utils

...is comming (or not).

## Known Issues

1. Slow.

2. It can only scan for mails in Inbox folder.  Can not delete those in other folders (e.g. Archive).
