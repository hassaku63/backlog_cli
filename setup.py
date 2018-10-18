#!/usr/bin/env python3
# coding: utf-8

from setuptools import setup, find_packages

setup(
    name='backlogcli',
    version='0.1',
    description='backlog nulab',
    author='hassaku63',
    author_email='takuyahashimoto1988@gmail.com',
    url='',
    scripts=[
        'bin/backlog'
    ],
    packages=find_packages(exclude=['tests*'])
)