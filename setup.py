import os
from setuptools import setup


def read(file):
    return open(os.path.join(os.path.dirname(__file__), file)).read()


setup(
    name="roboclone",
    version="0.0.1",
    packages=['roboclone'],
    author="Simon Andrews",
    description=("A script for cloning FRC robot projects and configuring them for Eclipse"),
    license="MIT",
    url="https://github.com/Team4761/roboclone",
    long_description=read("README.md"),
    install_requires=['Jinja2'],
    scripts=['bin/roboclone'],
)
