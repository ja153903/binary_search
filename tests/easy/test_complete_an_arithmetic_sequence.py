import pytest

from binary_search.easy.complete_an_arithmetic_sequence import Solution

s = Solution()

test_cases = [([1, 3, 5, 9], 7), ([-8, 0], -4), ([2, 0], 1), ([0, 0], 0)]


@pytest.mark.parametrize("nums,expected", test_cases)
def test_complete_an_arithmetic_sequence(nums, expected):
    assert s.solve(nums) == expected
