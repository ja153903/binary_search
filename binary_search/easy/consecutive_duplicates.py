class Solution:
    def solve(self, s: str) -> str:
        if len(s) <= 1:
            return s

        prev = s[0]
        ans = [prev]

        for i in range(1, len(s)):
            if s[i] != prev:
                ans.append(s[i])

            prev = s[i]

        return "".join(ans)
