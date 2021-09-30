import pytest

from binary_search.easy.roomba import Solution

test_cases = [(["NORTH", "EAST"], 1, 1, True)]

s = Solution()


@pytest.mark.parametrize("moves,x,y,expected", test_cases)
def test_roomba(moves, x, y, expected):
    assert s.solve(moves, x, y) == expected
