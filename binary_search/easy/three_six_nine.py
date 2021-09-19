"""
Given an integer n, return a list with each number from 1 to n, except if it's a multiple of 3 or has a 3, 6, or 9 in the number, it should be the string "clap".

Note: return the number as a string.
"""
from typing import List


class Solution:
    def solve(self, n: int) -> List[str]:
        result = []

        for i in range(1, n + 1):
            as_int = i
            as_str = str(i)

            if as_int % 3 == 0 or self._has_three_six_nine(as_str):
                result.append("clap")
            else:
                result.append(as_str)

        return result

    def _has_three_six_nine(self, as_str: str) -> bool:
        for num in ("3", "6", "9"):
            if num in as_str:
                return True

        return False
