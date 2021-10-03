from typing import List


class RangeSum:
    def __init__(self, nums: List[int]):
        # keep track of the running sums
        self.sums = self._compute_running_sum(nums)

    def total(self, i: int, j: int) -> int:
        if i == 0:
            return self.sums[j - 1]

        return self.sums[j - 1] - self.sums[i - 1]

    def _compute_running_sum(self, nums: List[int]) -> List[int]:
        result = list(nums)

        for i in range(1, len(result)):
            result[i] += result[i - 1]

        return result
