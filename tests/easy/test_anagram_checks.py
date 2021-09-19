import pytest

from binary_search.easy.anagram_checks import Solution

s = Solution()

test_cases = [
   ("listen", "silent", True),
   ("bedroom", "bathroom", False),
]

@pytest.mark.parametrize("s0,s1,expected", test_cases)
def test_anagram_checks(s0, s1, expected):
    assert s.solve(s0, s1) == expected
