#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='fastjsonschema',
    version='1.1+monetate1',
    packages=['fastjsonschema'],

    extras_require={
        "test": [
            "colorama",
            "enum34;python_version<'3.4'",
            "jsonschema",
            "json-spec",
            "pathlib2;python_version<'3.4'",
            "pytest",
            "validictory",
        ],
    },

    url='https://github.com/seznam/python-fastjsonschema',
    author='Michal Horejsek',
    author_email='horejsekmichal@gmail.com',
    description='Fastest Python implementation of JSON schema',
    license='BSD',

    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
