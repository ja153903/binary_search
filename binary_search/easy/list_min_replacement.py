from typing import List


"""
Given a list of integers nums, replace every nums[i] with
the smallest integer left of i. Replace nums[0] with 0
"""


class Solution:
    def solve(self, nums: List[int]) -> List[int]:
        current_min = nums[0]
        nums[0] = 0

        if len(nums) == 1:
            return nums

        for i in range(1, len(nums)):
            current_num = nums[i]
            nums[i] = current_min
            current_min = min(current_min, current_num)

        return nums
