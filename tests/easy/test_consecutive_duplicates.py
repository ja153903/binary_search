import pytest

from binary_search.easy.consecutive_duplicates import Solution

s = Solution()

test_cases = [("YYYXYXX", "YXYX"), ("", ""), ("X", "X"), ("XX", "X")]


@pytest.mark.parametrize("string,expected", test_cases)
def test_consecutive_duplicates(string, expected):
    assert s.solve(string) == expected
