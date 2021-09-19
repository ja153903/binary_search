from binary_search.easy.wolf_of_wall_street import Solution

s = Solution()

def test_wolf_of_wall_street():
    prices = [9, 11, 8, 5, 7, 10]
    assert s.solve(prices) == 5

    prices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert s.solve(prices) == 8

    prices = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert s.solve(prices) == 0
