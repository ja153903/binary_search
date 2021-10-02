import pytest

from binary_search.easy.shortest_string import Solution

s = Solution()

test_cases = [("11000", 1), ("101010", 0)]


@pytest.mark.parametrize("string,expected", test_cases)
def test_shortest_string(string, expected):
    assert s.solve(string) == expected
