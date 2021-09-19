import pytest

from binary_search.easy.pythagorean_triplets import Solution

s = Solution()

test_cases = [
    ([5, 1, 7, 4, 3], True),
    ([51, 52, 68, 85], True),
]


@pytest.mark.parametrize("nums,expected", test_cases)
def test_pythagorean_triplets(nums, expected):
    assert s.solve(nums) == expected
