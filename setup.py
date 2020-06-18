#
# Copyright (C) 2020 Arihant Parsoya
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requires = [
    'PyQt5',
]

setuptools.setup(
    name="ProcessingQt", # Replace with your own username
    version="1.0.0",
    author="Arihant Parsoya",
    author_email="parsoyaarihant@gmail.com",
    description="Python library for Processing software. Built on top of Qt5",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/parsoyaarihant/ProcessingQt",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        'Intended Audience :: Developers',
        'Intended Audience :: Education',

        'Topic :: Artistic Software',
        'Topic :: Education',

        'Topic :: Multimedia',
        'Topic :: Multimedia :: Graphics',

        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=requires,
)