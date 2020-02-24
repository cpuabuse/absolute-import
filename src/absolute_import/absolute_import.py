"""
A package for creating a pre-commit hook.
"""

from pathlib import Path
from sys import path as sys_path
from pkgutil import extend_path

def absolute_import(file: str = None, path: str = None, name: str = None):
	# File must be provided
	if file == None:
		raise ValueError

	# Namespace
	if path != None and name != None:
		__path__ = extend_path(path, name)
	elif path != None or name != None:
		raise ValueError

	# Bootstrap to be able to perform absolute imports as standalone code
	parent_path: str = str(Path(file).parent.joinpath("..").resolve())
	if parent_path not in sys_path:
		sys_path.append(parent_path)
