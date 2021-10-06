import pytest

from binary_search.easy.repeated_addition import Solution


s = Solution()

test_cases = [(8835, 6)]


@pytest.mark.parametrize("n,expected", test_cases)
def test_repeated_addition(n, expected):
    assert s.solve(n) == expected
