import pytest

from binary_search.easy.list_min_replacement import Solution

s = Solution()

test_cases = [([10, 5, 7, 9], [0, 10, 5, 5])]


@pytest.mark.parametrize("nums,expected", test_cases)
def test_list_min_replacment(nums, expected):
    assert s.solve(nums) == expected
