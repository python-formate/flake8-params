# stdlib
import ast
from typing import List

# 3rd party
from coincidence.regressions import AdvancedFileRegressionFixture
from domdf_python_tools.paths import PathPlus

# this package
from flake8_params import Plugin

example_code = PathPlus(__file__).parent.joinpath("example_code.py").read_text()


def results(s: str) -> List[str]:
	return ["{}:{}: {}".format(*r) for r in Plugin(ast.parse(s)).run()]


def test_plugin(advanced_file_regression: AdvancedFileRegressionFixture):
	res = results(example_code)
	advanced_file_regression.check('\n'.join(res))
