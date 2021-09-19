class Solution:
    def solve(self, s: str) -> int:
        if not s:
            return 0

        current_char = s[0]
        max_len = 0
        current_len = 1

        for i in range(1, len(s)):
            if current_char == s[i]:
                current_len += 1
            else:
                max_len = max(max_len, current_len)
                current_len = 1
                current_char = s[i]

        return max_len if max_len > current_len else current_len

