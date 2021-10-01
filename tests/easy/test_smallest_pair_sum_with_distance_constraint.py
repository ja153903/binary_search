import pytest

from binary_search.easy.smallest_pair_sum_with_distance_constraint import Solution

s = Solution()

test_cases = [([2, 3, 1, 1, 3], 3), ([1, 0, 1, 0], 0)]


@pytest.mark.parametrize("nums,expected", test_cases)
def test_smallest_pair_sum_with_distance_constraint(nums, expected):
    assert s.solve(nums) == expected
