import collections
from typing import List, Tuple

# Time: 3 ms (82.18%), Space: 18.02MB (5.97%)
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = grid
        row, col = len(grid), len(grid[0])
        countFreshOrange = 0
        queue = collections.deque()

        #init 
        for i in range(row):
            for j in range(col):
                if visited[i][j] == 2:
                    queue.append((i, j))
                elif visited[i][j] == 1:
                    countFreshOrange += 1

        if countFreshOrange == 0:
            return 0
        if not queue:
            return -1

        res = -1
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while queue:
            # x, y = queue.popleft()
            size = len(queue)
            while size > 0:
                x, y = queue.popleft()
                size -= 1
                for next_x, next_y in directions:
                    nx, ny = x + next_x, y + next_y

                    if 0 <= nx < row and 0 <= ny < col and visited[nx][ny] == 1:
                        visited[nx][ny] = 2
                        countFreshOrange -= 1
                        queue.append((nx, ny))
            res += 1
        if countFreshOrange == 0:
            return res

        return -1



sol = Solution()
grid = [[2,1,1],[1,1,0],[0,1,1]]

print(sol.orangesRotting(grid))
