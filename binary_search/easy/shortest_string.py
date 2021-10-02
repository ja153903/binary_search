class Solution:
    def solve(self, s: str) -> int:
        """
        11000 => 1 left
        """
        num_ones, num_zeros = 0, 0
        for digit in s:
            if digit == "1":
                num_ones += 1
            else:
                num_zeros += 1

        return abs(num_ones - num_zeros)
