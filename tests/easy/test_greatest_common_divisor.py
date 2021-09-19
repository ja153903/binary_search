import pytest

from binary_search.easy.greatest_common_divisor import Solution

s = Solution()

test_cases = [
    ([6, 12, 9], 3),
    ([6, 7, 9], 1),
]


@pytest.mark.parametrize("nums,expected", test_cases)
def test_greatest_common_divisor(nums, expected):
    assert s.solve(nums) == expected
