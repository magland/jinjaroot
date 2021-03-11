from setuptools import setup, find_packages

setup(
    packages=find_packages(),
    scripts=['bin/jinjaroot'],
    install_requires=['pyyaml', 'jinja2', 'click']
)