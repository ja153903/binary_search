from typing import List, Tuple


class RunLengthDecodedIterator:
    def __init__(self, s):
        self.decoded = RunLengthDecodedIterator._decode(s)

    @staticmethod
    def _decode(encoded_str: str) -> List[Tuple[str, int]]:
        expanded = []

        i = 0
        current_count = 0

        while i < len(encoded_str):
            while encoded_str[i].isdigit():
                current_count = current_count * 10 + int(encoded_str[i])
                i += 1

            expanded.append((encoded_str[i], current_count))
            current_count = 0
            i += 1

        return expanded

    def next(self):
        front = self.decoded[0]
        char, count = front

        if count - 1 == 0:
            self.decoded.pop(0)
        else:
            self.decoded[0] = (char, count - 1)

        return char

    def hasnext(self):
        return len(self.decoded) > 0
