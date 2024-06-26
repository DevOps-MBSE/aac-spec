# aac-spec

Specification and requirement tracing plugins for Architecture-as-Code

## PYTHON VERSION COMPATIBILITY

Currently, Python version 3.9.13 is required to avoid certain dependency version issues.

## pyproject.toml vs setup.py

Previously, this project was built with dependency information kept in a setup.py script.
However, the preferred method is to use pyproject.toml to set the project-level options.
Required modules are kept in the dependency sections of the pyproject.toml, and then the
pip-compile command is used to add hashes to the requirements.txt file for enhanced security
(see additional instructions below).

To coincide with these changes, some changes to tox.ini and the addition of a MANIFEST.ini file were also necessary.

These lines were added to tox.ini:
   isolated_build = True
   skipsdist = True

A MANIFEST file with these lines was added:
   graft src
   graft tests
   include tox.ini
   include src/puml/.aac

## TO BUILD FROM TERMINAL

cd python
pip install -e .

## TO TEST FROM TERMINAL

cd python
pip install -e .
python -m unittest

## Generate a requirements.txt file populated with hashes

pip install pip-tools
pip-compile --generate-hashes pyproject.toml
