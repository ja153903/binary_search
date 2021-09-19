from typing import List


class Solution:
    def solve(self, nums: List[int], k: int) -> List[int]:
        lst_len = len(nums)
        k = k % lst_len

        if k == 0:
            return nums

        result = list(nums)

        for i in range(len(nums)):
            # Rotating to the left means the following
            # i => (i - k)
            # this only works in Python
            result[(i - k) % lst_len] = nums[i]

        return result
