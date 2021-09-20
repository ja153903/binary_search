import pytest

from binary_search.easy.mixed_sorting import Solution

s = Solution()

test_cases = [([8, 13, 11, 90, -5, 4], [4, 13, 11, 8, -5, 90])]


@pytest.mark.parametrize("nums,expected", test_cases)
def test_mixed_sorting(nums, expected):
    assert s.solve(nums) == expected
