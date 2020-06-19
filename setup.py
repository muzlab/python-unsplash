#!/usr/bin/env python
# coding=utf-8

import pathlib
import pkg_resources
import setuptools

with pathlib.Path('requirements.txt').open() as requirements_txt:
    install_requires = [str(
        requirement) for requirement in pkg_resources.parse_requirements(requirements_txt)]

setuptools.setup(
    name="python-unsplash",
    version="1.0.0",
    description="A Python client for the Unsplash API.",
    license="MIT",
    author="Yakup Adaklı",
    author_email="yakup.adakli@gmail.com",
    url="http://github.com/yakupadakli/python-unsplash.git",
    packages=setuptools.find_packages(exclude=["tests"]),
    install_requires=install_requires,
    keywords="unsplash library",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    zip_safe=True,
)
