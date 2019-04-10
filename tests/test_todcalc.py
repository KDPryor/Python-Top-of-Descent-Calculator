# coding=utf-8
"""Default unittests to automate functional testing of flight module code."""
# !/usr/bin/env python
import unittest
from click.testing import CliRunner

from flight.todcalc import cli, calculate_descent_rate


class UserModelCase(unittest.TestCase):
    """Unittests automated flight decent rate test case framework."""

    def test_decent_rate(self):
        """Authentication unit test function."""
        return_data = calculate_descent_rate(1500, 5500, 300)
        self.assertEqual(return_data['time'], 13)
        self.assertEqual(return_data['distance'], 12.0)

    def test_cli_decent_rate(self):
        """Authentication unit test function."""
        runner = CliRunner()
        result = runner.invoke(
            cli, ["--target", "1500", "--start", "5500", "--descent_rate", "300"])
        assert not result.exception


if __name__ == '__main__':
    unittest.main(verbosity=2)
