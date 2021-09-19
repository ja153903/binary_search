class Solution:
    def solve(self, n: int) -> int:
        as_bits = "{0:b}".format(n)
        return len([i for i in as_bits if i == "1"])
