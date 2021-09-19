from typing import Set


class Solution:
    def solve(self, s0: str, s1: str) -> int:
        if s0 == "" or s1 == "":
            return 0

        s0_set = self._parse_sentence_into_unique_words(s0)
        s1_set = self._parse_sentence_into_unique_words(s1)

        return len(s0_set.intersection(s1_set))

    def _parse_sentence_into_unique_words(self, s: str) -> Set[str]:
        return set(s.lower().split(" "))
