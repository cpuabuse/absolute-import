"""
A package for setting up absolute import and namespaces.
"""

# Bootstrap to be able to perform absolute imports as standalone code
from pathlib import Path
from sys import path
parent_path: str = Path(__file__).parent.joinpath("..").as_posix()
if parent_path not in path:
	path.append(parent_path)

# Namespace
from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)

# Import metadata
from absolute_import.version import __version__

# For export
from absolute_import.absolute_import import absolute_import
