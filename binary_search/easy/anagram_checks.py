import collections


class Solution:
    def solve(self, s0: str, s1: str) -> bool:
        counter = collections.Counter(s0)

        for char in s1:
            if char not in counter or counter[char] == 0:
                return False

            counter[char] -= 1

        return sum(counter.values()) == 0
