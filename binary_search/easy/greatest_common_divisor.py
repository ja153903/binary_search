from typing import List


class Solution:
    def solve(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        gcd = self._gcd(nums[0], nums[1])

        for i in range(2, len(nums)):
            gcd = self._gcd(gcd, nums[i])

        return gcd

    # https://www.geeksforgeeks.org/python-program-for-gcd-of-more-than-two-or-array-numbers/
    # Euclidean algorithm for greatest common divisor
    def _gcd(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b

        return a
