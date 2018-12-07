#!/usr/bin/env python

from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as readme_file:
    readme = readme_file.read()

setup(
    name='WiPy',
    version="1.0.0",
    description="Python Wireless Library",
    long_description=readme,
    long_description_content_type='text/markdown',
    url="https://github.com/wifiphisher/WiPy",
    author="Dale Patterson",
    maintainer="Brian Smith",
    license="GPLv3",
    python_requires=">=3.6.0",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators', 'Topic :: Security',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries', 'Topic :: Security',
        'Topic :: System :: Networking', 'Topic :: Utilities',
        'Operating System :: POSIX :: Linux', 'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.5'
    ],
    keywords=
    'Linux Python nl80211 iw iwconfig ifconfig wireless WLAN WiFi pentest',
    packages=find_packages(exclude=('tests', )),
    package_data={'pyric': ['nlhelp/*.help', 'utils/data/*.txt']})
