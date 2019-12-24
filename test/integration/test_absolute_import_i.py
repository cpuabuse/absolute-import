"""
Performs an integration test for absolute_import.py.
"""

# Bootstrap for package import
from pathlib import Path
from sys import path
target_path: str = Path(__file__).parent.joinpath("..").joinpath("..").joinpath("src").as_posix()
if target_path not in path:
	path.append(target_path)

# Imports
from absolute_import.absolute_import import absolute_import

class TestAbsoluteImport:
	def test_import(self):
		# Set the absolute import
		absolute_import(file=__file__)

		# Import aux module; Disabling the pylint due to inability to set .env in a crossplatform way for multiple targets
		from integration.test_module import success # pylint: disable=import-error

		# Assert import was successful
		assert success()