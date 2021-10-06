class Solution:
    def solve(self, n: int) -> int:
        while n >= 10:
            current = 0

            while n > 0:
                current += n % 10
                n //= 10

            n = current

        return n
