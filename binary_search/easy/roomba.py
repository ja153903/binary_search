from typing import List


class Solution:
    def solve(self, moves: List[str], x: int, y: int) -> bool:
        directions = {
            "NORTH": (0, 1),
            "SOUTH": (0, -1),
            "EAST": (1, 0),
            "WEST": (-1, 0),
        }

        cx, cy = 0, 0

        for move in moves:
            dx, dy = directions[move]

            cx += dx
            cy += dy

        return cx == x and cy == y
