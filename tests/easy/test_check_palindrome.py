import pytest

from binary_search.easy.check_palindrome import Solution

s = Solution()

test_cases = [("racecar", True), ("evilolive", True), ("palindrome", False)]


@pytest.mark.parametrize("string,expected", test_cases)
def test_check_palindrome(string, expected):
    assert s.solve(string) == expected
