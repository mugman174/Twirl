from twirl.errors import PackageNotFoundError
from twirl.core.debug import logging
from twirl import localdb

def pkg(name, version=None):

    package = localdb.get_pkg(name)
    if not package:
        raise PackageNotFoundError(name)
    logging.info(f"Attempting to install {name} (version {package.version})")
    #for file in package.files:
    #    print(file[0])

    print(f"{package.name}: {package.depends}")
    for dep in package.depends:
        print(dep)
        if ">=" in dep:
            pkg(dep.split(">=")[0], dep.split(">=")[1])
        elif "=" in dep:
            pkg(dep.split("=")[0], dep.split("=")[1])
        elif ".so" in dep:
            continue
        else: pkg(dep)