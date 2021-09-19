import pytest

from binary_search.easy.buying_cars import Solution

s = Solution()

test_cases = [
    ([90, 30, 20, 40, 90], 95, 3),
    ([60, 90, 55, 75], 50, 0),
]


@pytest.mark.parametrize("prices,k,expected", test_cases)
def test_buying_cars(prices, k, expected):
    assert s.solve(prices, k) == expected
