"""
Performs an integration test for absolute_import.py.
"""

# Bootstrap for package import
from pathlib import Path
from sys import path
target_path: str = str(Path(__file__).parent.joinpath("..").joinpath("..").joinpath("src").resolve())
if target_path not in path:
	path.insert(1, target_path) # Inserting to ensure the use of local package

# Importing from __init__.py
from absolute_import import absolute_import

"""
Integration test for absolute-import.
"""
class TestAbsoluteImportAndNamespace:
	def test_import(self):
		# Set the absolute import
		absolute_import(file=__file__, name=__name__, path=[Path(__file__).parent.as_posix()])

		# Import aux module; Disabling the pylint due to inability to set .env in a crossplatform way for multiple targets
		from _input.success import success # pylint: disable=import-error

		# Assert import was successful
		assert success()
