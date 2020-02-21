#!/usr/bin/env pwsh
# To be run from a repository root

param([ValidateNotNullOrEmpty()][string]$FilePath = (Join-Path -Path "." -ChildPath "requirements.txt"))

pip install -r $FilePath; if (-not $?) { throw }