# author: Andre Alves
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


# Get the long description from the README file
with open("README.md", "r") as f:
    long_description = f.read()


setup(
    name="argval",
    version="0.1.0",
    license="MIT",
    description="A simple package for argument validation in python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="André Alves",
    author_email="easycv.developers@gmail.com",
    url="https://github.com/1cybersheep1/argval",
    download_url="https://github.com/1cybersheep1/argval/archive/v0.1.0.tar.gz",
    keywords=["python", "validation", "programming", "software"],
    setup_requires=["setuptools>=38.6.0"],
    packages=find_packages(),
    python_requires=">=3.4",
    install_requires=[],
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
