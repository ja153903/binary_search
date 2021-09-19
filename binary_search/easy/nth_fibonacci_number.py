class Solution:
    def solve(self, n: int) -> int:
        if n < 2:
            return 1

        a, b = 1, 1

        for _ in range(1, n):
            a, b = b, a + b

        return a
