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
from pkg_resources import parse_requirements

with open("README.md", "r") as readme, open("requirements" + sep + "prod.txt", "r") as requirements:
	setup(
		name="absolute-import", # Replace with your own username
		version="0.0.dev1",
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
			"Programming Language :: Python :: 3.3",
			"Programming Language :: Python :: 3.4",
			"Programming Language :: Python :: 3.5",
			"Programming Language :: Python :: 3.6",
			"Programming Language :: Python :: 3.7",
			"Programming Language :: Python :: 3.8",
			"Topic :: Software Development :: Libraries",
			"Topic :: Software Development :: Libraries :: Python Modules",
			"Typing :: Typed"
		],
		python_requires=">=3.3"  # Due to https://www.python.org/dev/peps/pep-0420/
	)
