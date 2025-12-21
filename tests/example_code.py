def missing_in_docstring(foo, bar, baz):
	"""
	Does something.

	:param foo:
	:param bar:
	"""


def has_self(self, foo, bar, baz):
	"""
	Does something.

	:param foo:
	:param bar:
	:param baz:
	"""


def missing_in_docstring_with_self(self, foo, bar, baz):
	"""
	Does something.

	:param bar:
	:param baz:
	"""


def docstring_wrong_order(self, foo, bar, baz):
	"""
	Does something.

	:param bar:
	:param foo:
	:param baz:
	"""


@classmethod
def is_classmethod(cls, foo, bar, baz):
	"""
	Does something.

	:param foo:
	:param bar:
	:param baz:
	"""


@classmethod
def missing_in_docstring_with_classmethod(cls, foo, bar, baz):
	"""
	Does something.

	:param foo:
	:param baz:
	"""


def missing_in_signature(foo, bar):
	"""
	Does something.

	:param foo:
	:param bar:
	:param baz:
	"""


def missing_in_signature_with_self(self, foo, bar):
	"""
	Does something.

	:param foo:
	:param bar:
	:param baz:
	"""


@classmethod
def missing_in_signature_with_classmethod(cls, foo, baz):
	"""
	Does something.

	:param foo:
	:param bar:
	:param baz:
	"""


@property
def a_property(self):
	"""
	A property.
	"""


@a_property.setter
def a_property(self, val):
	"""
	A property.
	"""


# 3rd party
import click  # type: ignore


@click.argument("-f", "--foo")
@click.command()
def a_command(foo):
	"""
	Command line entry point.
	"""


def no_docstring(foo, bar, baz):
	pass
