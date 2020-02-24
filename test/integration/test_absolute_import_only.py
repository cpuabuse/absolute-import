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


class TestAbsoluteImportOnly:
	"""
	Integration test for absolute-import.
	"""

	def test_import(self):
		"""
		Test the import of success module.
		"""

		# Set the absolute import
		absolute_import(file=__file__)

		# Import aux module; Disabling the pylint due to inability to set .env in a crossplatform way for multiple targets
		from _input.success import success # pylint: disable=import-error

		# Assert import was successful
		assert success()
