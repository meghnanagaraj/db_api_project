from setuptools import setup
import sys

with open("requirements.txt") as f:
    req_pkgs=f.read().splitlines()
    print(req_pkgs)
setup(
    name='dbfetch',
    version='0.1.0',
    install_requires=req_pkgs,
    entry_points={
        'console_scripts': ['dbfetch=fetch:query']
    }
)
