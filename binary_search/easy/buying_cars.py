from typing import List


class Solution:
    def solve(self, prices: List[int], k: int) -> int:
        prices.sort()

        # We can implement a greedy algorithm and just take the smallest
        # prices
        cars = 0
        i = 0
        while k > 0 and i < len(prices):
            if k >= prices[i]:
                k -= prices[i]
                cars += 1

            i += 1

        return cars
