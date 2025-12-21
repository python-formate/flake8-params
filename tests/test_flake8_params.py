# stdlib
import ast
import sys
from typing import List

# 3rd party
import pytest
from coincidence.regressions import AdvancedFileRegressionFixture
from domdf_python_tools.paths import PathPlus

# this package
from flake8_params import Plugin

example_code = PathPlus(__file__).parent.joinpath("example_code.py").read_text()


def results(s: str) -> List[str]:
	return ["{}:{}: {}".format(*r) for r in Plugin(ast.parse(s)).run()]


@pytest.mark.skipif(sys.version_info >= (3, 12), reason="Line numbers are offset on earlier versions")
def test_plugin(advanced_file_regression: AdvancedFileRegressionFixture):
	res = results(example_code)
	advanced_file_regression.check('\n'.join(res))
