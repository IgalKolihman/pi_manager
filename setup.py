"""Setup file for handling packaging and distribution."""
from __future__ import absolute_import
from setuptools import setup, find_packages


__version__ = "0.1.0"

setup(
    name='pi_manager',
    version=__version__,
    description="Raspberry Pi managing library",
    long_description=open("README.rst").read(),
    author="IgalKolihman",
    keywords="",
    install_requires=[
    ],
    packages=find_packages("pi_manager"),
    zip_safe=False,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: MacOS',
    ],
)
