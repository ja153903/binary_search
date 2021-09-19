from typing import List


class Solution:
    def solve(self, n: int) -> List[int]:
        rows = [[1], [1, 1]]

        if n <= 1:
            return rows[n]

        for i in range(2, n + 1):
            current = []
            for j in range(0, i + 1):
                if j == 0 or j == i:
                    current.append(1)
                else:
                    current.append(rows[i - 1][j] + rows[i - 1][j - 1])

            rows.append(current)

        return rows[n]
