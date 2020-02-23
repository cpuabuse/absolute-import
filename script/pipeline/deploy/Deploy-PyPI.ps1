Copy-Item -Path "src/*" -Destination "build/deploy" -Recurse -Force

# Create distribution
python setup.py sdist

# Upload distribution
twine upload dist/*