from pyalpm import Handle

handle = Handle("/", "/var/lib/pacman")
localdb = handle.get_localdb()
