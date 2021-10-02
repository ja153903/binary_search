from typing import List


class Solution:
    def solve(self, nums: List[int]) -> List[int]:
        """
        delete last occurence which means that for each
        number we can keep track of its first and last occurence
        if the number's first and last occurence are the same then we don't remove it
        else we remove the last time we see the number
        """

        occurences = {}

        for i, num in enumerate(nums):
            if num not in occurences:
                occurences[num] = {"first": i, "last": i}
            else:
                occurences[num]["last"] = i

        indices_to_remove = set()
        for obj in occurences.values():
            if obj["first"] != obj["last"]:
                indices_to_remove.add(obj["last"])

        return [num for i, num in enumerate(nums) if i not in indices_to_remove]
