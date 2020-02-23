#!/usr/bin/env python3

# Metadata
from pathlib import Path
from sys import path
package_path: str = Path(__file__).parent.joinpath("src").as_posix()
if package_path not in path:
	path.append(package_path)

# Imports
from os.path import sep
from setuptools import setup, find_packages

with open("README.md", "r") as readme:
	setup(
		name="absolute-import",
		version="0.3",
		author="cpuabuse.com",
		author_email="pypi@cpuabuse.com",
		description="A package to automate setting up absolute imports and namespace.",
		long_description=readme.read(),
		long_description_content_type="text/markdown",
		url="https://github.com/cpuabuse/absolute-import",
		package_dir={"absolute_import": "src"},
		packages=find_packages("src"),
		classifiers=[
			"Intended Audience :: Developers",
			"License :: OSI Approved :: ISC License (ISCL)",
			"Natural Language :: English",
			"Operating System :: OS Independent",
			"Programming Language :: Python :: 3",
			"Programming Language :: Python :: 3.6",
			"Programming Language :: Python :: 3.7",
			"Programming Language :: Python :: 3.8",
			"Topic :: Software Development :: Libraries",
			"Topic :: Software Development :: Libraries :: Python Modules",
			"Typing :: Typed"
		],
		python_requires=">=3.6"  # Due to typing
	)
