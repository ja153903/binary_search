from typing import List


class Solution:
    def solve(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)

        even_nums = [num for num in sorted_nums if num % 2 == 0]
        odd_nums = [num for num in sorted_nums if num % 2 == 1][::-1]

        relative_position = [0 if num % 2 == 0 else 1 for num in nums]

        result = []

        i, j = 0, 0

        for position in relative_position:
            if position == 0:
                result.append(even_nums[i])
                i += 1

            if position == 1:
                result.append(odd_nums[j])
                j += 1

        return result
