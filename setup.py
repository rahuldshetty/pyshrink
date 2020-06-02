#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

requirements = [ ]

setup(
    author="Rahul D Shetty",
    author_email='35rahuldshetty@gmail.com',
    python_requires='>=3.5',
    description="Compression algorithms implemented in pure Python.",
    install_requires=requirements,
    license="MIT license",
    keywords='pyshrink',
    name='pyshrink',
    packages=find_packages(include=['pyshrink', 'pyshrink.*']),
    url='https://github.com/rahuldshetty/pyshrink',
    version='0.0.1',
    zip_safe=False,
)
