import os
from setuptools import setup


def read(f_name):
    return open(os.path.join(os.path.dirname(__file__), f_name)).read()

setup(
    name="technical-challenge",
    version="0.0.1",
    author="DanielMorales9",
    author_email="dnlmrls9@gmail.com",
    description=("Aylien Technical Challenge"),
    keywords="technical-challenge",
    url="http://packages.python.org/an_example_pypi_project",
    install_requires=['appdirs', 'click', 'Flask', 'itsdangerous', 'Jinja2',
                      'MarkupSafe', 'packaging', 'prometheus.yml-client', 'pyparsing',
                      'six', 'Werkzeug', 'parameterized'],
    packages=['app'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
    ],
)