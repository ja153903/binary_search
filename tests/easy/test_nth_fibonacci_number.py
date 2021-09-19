from binary_search.easy.nth_fibonacci_number import Solution

s = Solution()

def test_nth_fibonacci_number():
    assert s.solve(1) == 1
    assert s.solve(6) == 8
    assert s.solve(7) == 13
