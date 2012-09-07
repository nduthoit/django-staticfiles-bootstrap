"""
Builds the version of Bootstrap that's in vendor/bootstrap and packages
it as a Django app for use with Django staticfiles.
"""
import subprocess
import sys

DEFAULT_VERSION = "v2.1.1"


def cp(src, dest="."):
    # if dest != ".":
    #     dest += "/"
    cmd = [
        "cp -R vendor/bootstrap/{src} bootstrap/static/bootstrap/{dest}".format(src=src, dest=dest)
    ]
    subprocess.call(cmd, shell=True)


def main():
    args = {
        "version": DEFAULT_VERSION if len(sys.argv) is 1 else sys.argv[1],
    }
    subprocess.call(["mkdir -p ./bootstrap/static/bootstrap"], shell=True)
    subprocess.call(["mkdir -p ./bootstrap/static/bootstrap/less"], shell=True)
    subprocess.call(["mkdir -p ./bootstrap/static/bootstrap/js"], shell=True)
    # Run `make bootstrap`
    subprocess.call(
            ["cd vendor/bootstrap && git checkout %(version)s && make bootstrap" %
                args],
            shell=True)
    # Copy the results (compiled css, combined and uglified js)
    cp("bootstrap/*")
    # Include the less files as well
    cp("less/*.less", "less")
    # Include the js
    cp("js/bootstrap*.js", "js")
    cp("LICENSE")
    # Cleanup
    subprocess.call(["rm -Rf vendor/bootstrap/bootstrap"], shell=True)

    with open("./VERSION", "w") as f:
        f.write(args["version"])


if __name__ == "__main__":
    main()
