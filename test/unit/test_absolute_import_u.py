"""
Tests absolute_import.py.
"""

# Bootstrap for package import
from pathlib import Path
from sys import path
target_path: str = Path(__file__).parent.joinpath("..").joinpath("..").joinpath("src").as_posix()
if target_path not in path:
	path.append(target_path)

# Imports
from absolute_import.absolute_import import absolute_import
from pytest import raises

class TestAbsoluteImport:
	def test_no_file_arg(self):
		with raises(ValueError):
			absolute_import()

	def test_inconsistent_namespace_args(self):
		with raises(ValueError):
			absolute_import(name="abc")
		with raises(ValueError):
			absolute_import(path="abc")