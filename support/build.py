"""
Builds the version of Bootstrap that's in vendor/bootstrap and packages
it as a Django app for use with Django staticfiles.
"""
import subprocess
import sys

DEFAULT_VERSION = "v2.1.1"


def cp(src):
    cmd = [
        "cp -R vendor/bootstrap/%s bootstrap/static/bootstrap/" % src,
    ]
    subprocess.call(cmd, shell=True)


def main():
    args = {
        "version": DEFAULT_VERSION if len(sys.argv) is 1 else sys.argv[1],
    }
    subprocess.call(["mkdir -p ./bootstrap/static/bootstrap"], shell=True)
    subprocess.call(
            ["cd vendor/bootstrap && git checkout %(version)s && make bootstrap" %
                args],
            shell=True)
    cp("bootstrap/*")
    cp("LICENSE")
    # Cleanup
    subprocess.call(["rm -Rf vendor/bootstrap/bootstrap"], shell=True)

    with open("./VERSION", "w") as f:
        f.write(args["version"])


if __name__ == "__main__":
    main()
