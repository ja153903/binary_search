from typing import List


class Solution:
    def solve(self, nums: List[int]) -> bool:
        nums.sort()

        nums = [num * num for num in nums]

        # Fix the end of the array
        for i in range(len(nums) - 1, 1, -1):
            # Use two pointer solution for the rest of the array
            j = 0
            k = i - 1

            while j < k:
                if nums[j] + nums[k] == nums[i]:
                    return True

                if nums[j] + nums[k] < nums[i]:
                    j += 1
                else:
                    k -= 1
        return False
