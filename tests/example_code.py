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


class ClassMissingDocstring:
	"""
	A class.

	:param foo:
	:param bar:
	"""

	def __init__(self, foo, bar, baz):
		pass

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


class ClassMissingSignature:
	"""
	A class.

	:param foo:
	:param bar:
	:param baz:
	"""

	def __init__(self, foo, bar):
		pass


class ClassWrongOrder:
	"""
	A class.

	:param bar:
	:param foo:
	:param baz:
	"""

	def __init__(self, foo, bar, baz):
		pass


class ClassNoInit:
	"""
	A class.

	:param foo:
	:param bar:
	:param baz:
	"""


class ClassNoDocstring:

	def __init__(self, foo, bar, baz):
		pass


class ClassInitDocstring:

	def __init__(self, foo, bar, baz):
		"""
		Setup the function.

		:param foo:
		:param bar:
		:param baz:
		"""


class GoodClass:
	"""
	A class.

	:param foo:
	:param bar:
	:param baz:
	"""

	def __init__(self, foo, bar, baz):
		pass


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


async def missing_in_docstring_async(foo, bar, baz):
	"""
	Does something.

	:param foo:
	:param bar:
	"""


async def has_self_async(self, foo, bar, baz):
	"""
	Does something.

	:param foo:
	:param bar:
	:param baz:
	"""


async def missing_in_docstring_with_self_async(self, foo, bar, baz):
	"""
	Does something.

	:param bar:
	:param baz:
	"""


async def docstring_wrong_order_async(self, foo, bar, baz):
	"""
	Does something.

	:param bar:
	:param foo:
	:param baz:
	"""


async def missing_in_signature_async(foo, bar):
	"""
	Does something.

	:param foo:
	:param bar:
	:param baz:
	"""


async def missing_in_signature_with_self_async(self, foo, bar):
	"""
	Does something.

	:param foo:
	:param bar:
	:param baz:
	"""


class AsyncClass:
	"""
	A class.
	"""

	@classmethod
	async def is_classmethod(cls, foo, bar, baz):
		"""
		Does something.

		:param foo:
		:param bar:
		:param baz:
		"""

	@classmethod
	async def missing_in_docstring_with_classmethod(cls, foo, bar, baz):
		"""
		Does something.

		:param foo:
		:param baz:
		"""

	@classmethod
	async def missing_in_signature_with_classmethod(cls, foo, baz):
		"""
		Does something.

		:param foo:
		:param bar:
		:param baz:
		"""


async def no_docstring_async(foo, bar, baz):
	pass


def missing_args(foo, bar, *baz):
	"""
	Does something.

	:param foo:
	:param bar:
	"""


def has_args(foo, bar, *baz):
	r"""
	Does something.

	:param foo:
	:param bar:
	:param \*baz:
	"""


def missing_kwargs(foo, bar, **baz):
	"""
	Does something.

	:param foo:
	:param bar:
	"""


def has_kwargs(foo, bar, **baz):
	r"""
	Does something.

	:param foo:
	:param bar:
	:param \*\*baz:
	"""


def keyword_only(foo, bar, *, baz=None):
	"""
	Does something.

	:param foo:
	:param bar:
	:param baz:
	"""


def positional_only(foo, /, bar, baz):
	"""
	Does something.

	:param foo:
	:param bar:
	:param baz:
	"""


# stdlib
from typing import Tuple


class MyTuple(Tuple[int, str, int]):  # noqa: SLOT001

	def __new__(cls, a: int, b: str, c: int = 0) -> "MyTuple":
		"""
		Create a new :class:`~.MyTuple`.

		:rtype: :class:`~.MyTuple`.
		"""

		return super().__new__((a, b, c))  # type: ignore[arg-type]


# stdlib
from abc import ABC


class MyABC(ABC):

	def __init_subclass__(cls, swallow, **kwargs) -> None:
		r"""
		Setup something in the subclass.

		:param \*\*kwargs:
		"""


# 3rd party
import pytest  # type: ignore


@pytest.fixture()
def a_fixture(foo) -> str:
	"""
	A pytest fixture .
	"""

	return "abc"


click_command = click.command


@click.argument("-f", "--foo")
@click_command()
def another_command(foo):
	"""
	Command line entry point.
	"""
