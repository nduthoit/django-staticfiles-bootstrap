from distutils.core import setup
import os

# Stolen from django-registration
# Compile the list of packages available, because distutils doesn't have
# an easy way to do this.
packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir:
    os.chdir(root_dir)

for dirpath, dirnames, filenames in os.walk('bootstrap'):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'):
            del dirnames[i]
    if '__init__.py' in filenames:
        pkg = dirpath.replace(os.path.sep, '.')
        if os.path.altsep:
            pkg = pkg.replace(os.path.altsep, '.')
        packages.append(pkg)
    elif filenames:
        prefix = dirpath[len('boostrap/'):]
        for f in filenames:
            data_files.append(os.path.join(prefix, f))


setup(
    name='django-staticfiles-jquery',
    version=open("./VERSION").read(),
    description='jQuery meets Django staticfiles',
    author='Nathan Duthoit',
    author_email='nathan.duthoit@gmail.com',
    url='http://github.com/nduthoit/django-staticfiles-jquery/',
    packages=packages,
    package_data={'bootstrap': data_files},
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
)