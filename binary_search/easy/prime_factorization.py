import math
from typing import List


class Solution:
    def solve(self, n: int) -> List[int]:
        # pretty much need to get all the 2s
        result = []

        while n % 2 == 0:
            result.append(2)
            n = n // 2

        for i in range(3, int(math.sqrt(n)) + 1, 2):
            while n % i == 0:
                result.append(i)
                n = n // i

        if n > 2:
            result.append(n)

        return result
