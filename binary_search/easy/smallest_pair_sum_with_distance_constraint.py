from typing import List


class Solution:
    def solve(self, nums: List[int]) -> int:
        minimum_up_to = list(nums)

        for i in range(1, len(nums)):
            minimum_up_to[i] = min(nums[i], minimum_up_to[i - 1])

        ans = float("inf")

        for i in range(2, len(nums)):
            ans = min(ans, nums[i] + minimum_up_to[i - 2])

        return ans
