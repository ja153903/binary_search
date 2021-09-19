import pytest

from binary_search.easy.number_of_bits import Solution

s = Solution()


@pytest.mark.parametrize("n,expected", [(0, 0), (1, 1), (2, 1), (3, 2)])
def test_number_of_bits(n, expected):
    assert s.solve(n) == expected
