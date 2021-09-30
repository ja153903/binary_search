import pytest

from binary_search.easy.split_list import Solution

s = Solution()

test_cases = [
    ([5, 3, 2, 7, 9], True),
    ([1, 5, 6, 9, 4, 3], False),
    ([0, 3, 0, 1], False),
    ([0, 2, 1], True),
    ([0, 0], False),
]


@pytest.mark.parametrize("nums,expected", test_cases)
def test_split_list(nums, expected):
    assert s.solve(nums) == expected
