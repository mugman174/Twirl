from pyalpm import Handle
from twirl import core
import time
def pkg(name):
    handle = Handle("/", "/var/lib/pacman")
    localdb = handle.get_localdb()
    package  = localdb.get_pkg(name)
    if not package:
        print("Package not found.")
        exit()
    print(f"""Name: {name}
Requires: {package.depends}
License: {package.licenses[0]}
Description: {package.desc}
Hash: {package.md5sum}
Optional Dependencies: {package.optdepends}
Url: {package.url}
""")