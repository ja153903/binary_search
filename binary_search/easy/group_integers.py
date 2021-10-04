import collections
from typing import List


class Solution:
    def solve(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False

        counter = collections.Counter(nums)

        # if there is only one group, then we return True
        if len(counter) == 1:
            return True

        # all groups have to have an even number or all the same count
        same_count = True
        prev = None
        for _, value in counter.items():
            if prev is None:
                prev = value

            if prev is not None and value != prev:
                same_count = False
                break
            elif prev is not None:
                prev = value

        if same_count and prev >= 2:
            return True

        for _, value in counter.items():
            if value < 2 or value % 2 == 1:
                return False

        return True
