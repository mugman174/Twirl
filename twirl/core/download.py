from twirl.errors import PackageNotFoundError
from twirl.core.debug import logging
from pyalpm import Handle

def pkg(name):
    handle = Handle("/", "/var/lib/pacman")
    localdb = handle.get_localdb()
    package  = localdb.get_pkg(name)
    if not package:
        raise PackageNotFoundError(name)
    logging.info(f"Attempting to install {name} (version {package.version})")