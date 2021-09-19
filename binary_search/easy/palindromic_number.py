"""
Given a non-negative integer num, return whether it is a palindrome.

Bonus: Can you solve it without using strings?

Constraints
* num < 2 ** 31
"""
class Solution:
    def solve(self, num: int) -> bool:
        num_copy = num
        rev = 0
        
        while num_copy > 0:
            rev = rev * 10 + num_copy % 10
            num_copy = num_copy // 10

        return rev == num

