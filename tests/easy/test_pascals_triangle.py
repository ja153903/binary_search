import pytest

from binary_search.easy.pascals_triangle import Solution

s = Solution()

test_cases = [
    (0, [1]),
    (1, [1, 1]),
    (2, [1, 2, 1]),
    (3, [1, 3, 3, 1]),
]


@pytest.mark.parametrize("n,expected", test_cases)
def test_pascals_triangle(n, expected):
    assert s.solve(n) == expected
