# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='tox-tags',
    url='https://github.com/AndreLouisCaron/tox-tags',
    description='Adds tags for running subsets of Tox environments.',
    maintainer='Andre Caron',
    maintainer_email='andre.l.caron@gmail.com',
    version='0.1.0',
    py_modules=[
        'tox_tags',
    ],
    entry_points={
        'tox': [
            'tags = tox_tags',
        ],
    },
    install_requires=[
        'tox>=2.0',
    ],
)
