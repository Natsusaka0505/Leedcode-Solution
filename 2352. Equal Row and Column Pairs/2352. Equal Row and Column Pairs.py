from typing import List
from collections import Counter


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        pairs = 0
        cnt = Counter(tuple(row) for row in grid)
        print(cnt)
        for tpl in zip(*grid):
            print(f"tpl:{tpl}, cnt: {cnt[tpl]}")
            pairs += cnt[tpl]
        return pairs


class mySolution:
    def equalPairs(self, grids: List[List[int]]) -> int:
        cols_start_list = grids[0]

        cols = [[] for _ in cols_start_list]

        for row in grids:
            for idx, ele in enumerate(row):
                cols[idx].append(ele)

        res = 0

        for row in grids:
            for idx, ele in enumerate(cols_start_list):
                if row[0] == ele:
                    if row == cols[idx]:
                        res += 1

        return res


sol = Solution()
grid = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]
print(sol.equalPairs(grid))
