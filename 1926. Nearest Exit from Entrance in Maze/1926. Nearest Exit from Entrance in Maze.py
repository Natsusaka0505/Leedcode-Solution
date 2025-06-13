from typing import List, Tuple
from collections import deque


# Time: 64 ms (71.24%), Space: 19.17MB (79.76%)
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        rows, cols = len(maze), len(maze[0])

        x0, y0 = entrance
        queue = deque([(x0, y0, 0)])
        maze[x0][y0] = '+'

        while queue:
            x, y, steps = queue.popleft()

            for dx, dy in directions:
                next_x, next_y = x + dx, y + dy

                if (0 <= next_x < rows and 0 <= next_y < cols) and maze[next_x][next_y] == '.':
                    if next_x in [0, rows - 1] or next_y in [0, cols - 1]:
                        return steps + 1  
                    maze[next_x][next_y] = '+'
                    queue.append((next_x, next_y, steps + 1))

        return -1


sol = Solution()
maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]]
entrance = [1,2]

print(sol.nearestExit(maze, entrance))