import setuptools
import re

VERSIONFILE="random_emoji/__init__.py"
getversion = re.search( r"^__version__ = ['\"]([^'\"]*)['\"]", open(VERSIONFILE, "rt").read(), re.M)
if getversion:
    new_version = getversion.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))

with open("README.rst", "r") as r:
    long_description = r.read()
    setuptools.setup(
        name='random_unicode_emoji',
        python_requires='>=3',
        version=new_version,
        license='MIT',
        author="Nic Jones",
        author_email='nic@nicpjones.com',
        description='A simple Python package to retrieve a random Unicode emoji. 😄',
        long_description=long_description,
        packages=setuptools.find_packages(),
        url='https://github.com/NicPWNs/random-unicode-emoji',
        download_url ='https://github.com/NicPWNs/random-unicode-emoji/releases',
        keywords='random unicode emoji',
    )
