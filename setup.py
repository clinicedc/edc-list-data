# -*- coding: utf-8 -*-
import os

from os.path import abspath, dirname, join
from setuptools import setup
from setuptools import find_packages

with open(join(dirname(__file__), "README.rst")) as readme:
    README = readme.read()

with open(join(dirname(__file__), "VERSION")) as f:
    VERSION = f.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(join(abspath(__file__), os.pardir)))


setup(
    name="edc-list-data",
    version=VERSION,
    author=u"Erik van Widenfelt",
    author_email="ew2789@gmail.com",
    packages=find_packages(),
    url="http://github.com/clinicedc/edc-list-data",
    license="GPL license, see LICENSE",
    description="Populate list data and other static model data on startup",
    long_description=README,
    include_package_data=True,
    zip_safe=False,
    keywords="django Edc action items reminders",
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    install_requires=[],
    python_requires=">=3.7",
    test_suite="runtests.main",
)
