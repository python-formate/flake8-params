========
Usage
========

This library provides the Flake8 plugin ``flake8-params`` mismatches between function signatures and docstring params.


Flake8 codes
--------------

.. flake8-codes:: flake8_params

	PRM001
	PRM002
	PRM003



Pre-commit hook
----------------

``flake8-params`` can also be used as a ``pre-commit`` hook
See `pre-commit <https://github.com/pre-commit/pre-commit>`_ for instructions

Sample ``.pre-commit-config.yaml``:

.. pre-commit:flake8:: 0.0.0
