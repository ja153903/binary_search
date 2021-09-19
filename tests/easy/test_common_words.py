import pytest

from binary_search.easy.common_words import Solution

s = Solution()

test_cases = [("hello world hello oyster", "world is your oyster", 2)]


@pytest.mark.parametrize("s0,s1,expected", test_cases)
def test_common_words(s0, s1, expected):
    assert s.solve(s0, s1) == expected
