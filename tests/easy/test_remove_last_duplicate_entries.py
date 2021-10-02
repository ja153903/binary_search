import pytest

from binary_search.easy.remove_last_duplicate_entries import Solution

s = Solution()

test_cases = [([1, 3, 4, 1, 3, 5], [1, 3, 4, 5])]


@pytest.mark.parametrize("nums,expected", test_cases)
def test_remove_last_duplicate_entries(nums, expected):
    assert s.solve(nums) == expected
