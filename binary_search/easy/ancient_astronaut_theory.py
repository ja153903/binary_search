class Solution:
    def solve(self, dictionary: str, s: str) -> bool:
        # convert each character in the dictionary into an index
        # then convert each value in the string into an index
        # if the value does not exist within the dictionary, then filter it out
        # we can the check if any values are less than the other
        mp = {char: idx for idx, char in enumerate(dictionary)}
        chars = [mp[c] for c in s if c in mp]

        for i in range(1, len(chars)):
            if chars[i] < chars[i - 1]:
                return False

        return True
