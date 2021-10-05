import pytest

from binary_search.easy.ancient_astronaut_theory import Solution

s = Solution()

test_cases = [("acb", "aaaa h ccc i bbb", True), ("acb", "aaaacccbc", False)]


@pytest.mark.parametrize("dictionary,string,expected", test_cases)
def test_ancient_astronaut_theory(dictionary, string, expected):
    assert s.solve(dictionary, string) == expected
