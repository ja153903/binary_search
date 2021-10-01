from typing import List


class Solution:
    """
    You are given a list of integers nums of length n representing the current score of swimmers in a competition.
    There is one more round to swim and the first place winner for this round gets n points, second place n-1 points,
    etc. and the last place gets 1 point

    Return the number of swimmers that can still win the competition after the last round.
    If you tie for first in points, this still counts as winning.

    Solution:

    * Maybe we should think about this from the lens of what is the minimum score
      a swimmer needs to win.
    * We can sort the array first and suppose that the current number receives the first place amount of points
    * We can then start backtracking by updating the rest of the possible scores.
    """

    def solve(self, nums: List[int]) -> int:
        nums.sort()
