from pyalpm import Handle
from twirl import core

def pkg(name):
    handle = Handle("/", "/var/lib/pacman")
    localdb = handle.get_localdb()
    package  = localdb.get_pkg(name)