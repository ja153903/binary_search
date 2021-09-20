import math
from typing import List


class Solution:
    def solve(self, n: int) -> List[int]:
        # pretty much need to get all the 2s
        result = []

        while n % 2 == 0:
            result.append(2)
            n = n // 2

        # This is to break down composite numbers
        # Skip by 2 because we only want to look at odd numbers
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            while n % i == 0:
                result.append(i)
                n = n // i

        # need to add here if prime
        if n > 2:
            result.append(n)

        return result
