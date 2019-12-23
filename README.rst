Recollecing
###########


Usage
*****
In debian you can use systemctl by executing ``install.debian.sh``
once to install it.

Then, to manage it:
- ``systemctl --user start/stop/status/restart recollecing``
- ``journalctl --user recollecing``

You need to sign in with the user after boot to start the program.

More here: https://github.com/torfsen/python-systemd-tutorial
