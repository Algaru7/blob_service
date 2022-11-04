#!/usr/bin/env python3

from setuptools import setup

setup(
    name='blob_service',
    version='0.1',
    description=__doc__,
    packages=['blob_service', 'blob_service_scripts'],
    entry_points={
        'console_scripts': [
            'blob_service_server=blob_server_scripts.server:main',
            'blob_service_client=blob_server_scripts.client:main'
        ]
    }
)