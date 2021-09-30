from typing import List


class Solution:
    def solve(self, nums: List[int]) -> bool:
        left_sublist = [0 for _ in range(len(nums))]
        right_sublist = [0 for _ in range(len(nums))]

        left_sublist[0] = nums[0]
        right_sublist[-1] = nums[-1]

        for i in range(1, len(nums)):
            left_sublist[i] = max(left_sublist[i - 1], nums[i])

        for i in range(len(nums) - 2, -1, -1):
            right_sublist[i] = min(right_sublist[i + 1], nums[i])

        for i in range(0, len(nums) - 1):
            if left_sublist[i] < right_sublist[i + 1]:
                return True

        return False
