# absolute-import

## About

Package providing a one-line functionality to set up a project for ability to perform absolute imports both after setup and with plain download. Additionally, provides namespaces support.

## Usage

### Absolute import

1. In the root `__init__.py`.

	```python
	from absolute_import import absolute_import

	absolute_import(file=__file__)
	```

1. In the root `__main__.py` or root directly executable python files.

	```python
	from absolute_import import absolute_import

	if __name__ == "__main__":
		absolute_import(file=__file__)
	```

### Absolute import and namespace

1. In the root `__init__.py`.

	```python
	from absolute_import import absolute_import

	absolute_import(file=__file__, name=__name__, path=__path__)
	```

1. In the root `__main__.py` or root directly executable python files.

	```python
	from absolute_import import absolute_import

	if __name__ == "__main__":
		absolute_import(file=__file__, name=__name__, path=__path__)
	```
