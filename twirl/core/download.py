from pyalpm import Handle
from twirl import core
import time
def pkg(name):
    handle = Handle("/", "/var/lib/pacman")
    localdb = handle.get_localdb()
    package  = localdb.get_pkg(name)

    for attr in dir(package):
        if "__" not in attr and "files" not in attr:
            print(f"{attr}: {getattr(package, attr)}")
        elif "date" in attr:
            print(f"{attr}: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1347517370))}")
