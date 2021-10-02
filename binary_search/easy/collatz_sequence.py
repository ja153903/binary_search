class Solution:
    def solve(self, n: int) -> int:
        seq_len = 1

        while n != 1:
            if n % 2 == 0:
                n //= 2
            else:
                n = 3 * n + 1

            seq_len += 1

        return seq_len
