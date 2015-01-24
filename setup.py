#!/usr/bin/env python

from setuptools import find_packages
from setuptools import setup

setup(
    name='celery-janitor',
    version='0.1.0',
    description="Clean up unused queues from your Celery broker",
    long_description=open('README.rst').read(),
    keywords='celery queue clenaup',
    author='Andrei Coman',
    author_email='comandrei@gmail.com',
    url='https://github.com/comandrei/celery-janitor',
    license='MIT License',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    setup_requires=['wheel'],
    classifiers=["Development Status :: 3 - Alpha",
                 "Intended Audience :: Developers",
                 "License :: OSI Approved :: MIT License",
                 "Operating System :: OS Independent",
                 "Topic :: Internet",
                 "Programming Language :: Python :: 2.7",
                 "Programming Language :: Python :: 3.4"],
)
