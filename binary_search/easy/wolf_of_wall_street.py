from typing import List


class Solution:
    def solve(self, prices: List[int]):
        if not prices:
            return 0

        min_buy = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i] < min_buy:
                min_buy = prices[i]

            max_profit = max(max_profit, prices[i] - min_buy)

        return max_profit
