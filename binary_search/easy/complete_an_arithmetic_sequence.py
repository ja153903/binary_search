from typing import List


class Solution:
    def solve(self, nums: List[int]) -> int:
        """
        T(N) = a + (N - 1) * d
        """
        start, end = nums[0], nums[-1]
        expected_len = len(nums)
        jump = (end - start) // expected_len

        if jump == 0:
            return start

        expected_set = set([i for i in range(start, end, jump)])
        current_set = set(nums)

        missing_no = expected_set.difference(current_set)

        return list(missing_no)[0]
