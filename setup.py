"""setup.py.

Set up details for ``pip install qusetta`` or ``pip install -e .`` if
installing by source.

"""

import setuptools


with open('README.rst') as f:
    README = f.read()

with open("requirements.txt") as f:
    REQUIREMENTS = [line.strip() for line in f if line.strip()]

# get __version__, __author__, etc.
with open("qusetta/_version.py") as f:
    exec(f.read())


setuptools.setup(
    name="qusetta",
    version=__version__,
    author=__author__,
    author_email=__authoremail__,
    description=__description__,
    long_description=README,
    long_description_content_type='text/x-rst',
    url=__sourceurl__,
    license=__license__,
    packages=setuptools.find_packages(exclude=("tests", "docs")),
    test_suite="tests",
    install_requires=REQUIREMENTS,
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    project_urls={
        "Source": __sourceurl__
    }
)
