from typing import List
import math


class Solution:
    def solve(self, n: int) -> List[int]:
        if n < 2:
            return []

        # Sieve Algorithm
        # https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
        is_prime = [True for _ in range(n + 1)]
        is_prime[0] = False
        is_prime[1] = False

        for i in range(2, int(math.sqrt(n)) + 1):
            if is_prime[i]:
                j = i * i

                while j <= n:
                    is_prime[j] = False
                    j += i

        return [i for i, val in enumerate(is_prime) if val]
