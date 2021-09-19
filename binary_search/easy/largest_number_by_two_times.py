from typing import List


class Solution:
    def solve(self, nums: List[int]) -> bool:
        if not nums or len(nums) < 2:
            return False
        
        largest_number = max(nums)
        nums.remove(largest_number)
        second_largest_number = max(nums)

        return largest_number > second_largest_number * 2
