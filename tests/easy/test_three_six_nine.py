import pytest

from binary_search.easy.three_six_nine import Solution

@pytest.fixture
def simple_test_case():
    return 16, ["1", "2", "clap", "4", "5", "clap", "7", "8", "clap", "10", "11", "clap", "clap", "14", "clap", "clap"]

s = Solution()

def test_three_six_nine(simple_test_case):
    arg, expected = simple_test_case

    assert s.solve(arg) == expected
