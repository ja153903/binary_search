class Solution:
    def solve(self, start: int, end: int) -> int:
        count = 0

        while end > start:
            if end & 1:
                end -= 1
            else:
                end //= 2

            count += 1

        return count + start - end
