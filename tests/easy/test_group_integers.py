import pytest

from binary_search.easy.group_integers import Solution

s = Solution()

test_cases = [
    ([2, 3, 5, 8, 3, 2, 5, 8], True),
    ([3, 0, 0, 3, 3, 3], True),
    ([2, 2, 2], True),
    ([1], False),
    ([1, 2], False),
]


@pytest.mark.parametrize("nums,expected", test_cases)
def test_group_integers(nums, expected):
    assert s.solve(nums) == expected
