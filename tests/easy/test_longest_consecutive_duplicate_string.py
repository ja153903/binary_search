import pytest

from binary_search.easy.longest_consecutive_duplicate_string import Solution

s = Solution()

test_cases =[
    ("abbbba", 4),
    ("aaabbb", 3),
]

@pytest.mark.parametrize("string,expected", test_cases)
def test_longest_consecutive_duplicate_string(string, expected):
    assert s.solve(string) == expected
