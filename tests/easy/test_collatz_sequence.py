import pytest

from binary_search.easy.collatz_sequence import Solution

s = Solution()

test_cases = [(11, 15)]


@pytest.mark.parametrize("n,expected", test_cases)
def test_collatz_sequence(n, expected):
    assert s.solve(n) == expected
