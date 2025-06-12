from typing import List, Tuple
from collections import deque


# Time: 0 ms (100%), Space: 18.13MB (7.84%)
class Solution:
    def dfs(
        self, node: str, dest: str, gr: dict, vis: set, ans: List[float], temp: float
    ) -> None:
        if node in vis:
            return

        vis.add(node)
        if node == dest:
            ans[0] = temp
            return

        for nextNode, val in gr[node].items():
            self.dfs(nextNode, dest, gr, vis, ans, temp * val)

    def buildGraph(self, equations: List[List[str]], values: List[float]) -> dict:
        gr = {}

        for i in range(len(equations)):
            dividend, divisor = equations[i]
            value = values[i]

            if dividend not in gr:
                gr[dividend] = {}
            if divisor not in gr:
                gr[divisor] = {}

            gr[dividend][divisor] = value
            gr[divisor][dividend] = 1.0 / value

        return gr

    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        res = []
        gr = self.buildGraph(equations, values)

        for i in range(len(queries)):
            dividend, divisor = queries[i]

            if dividend not in gr or divisor not in gr:
                res.append(-1.0)
            elif dividend == divisor:
                res.append(1.0)
            else:
                via = set()
                ans = [-1.0]
                temp = 1

                self.dfs(dividend, divisor, gr, via, ans, temp)
                res.append(ans[0])
        return res


sol = Solution()
equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]

print(sol.calcEquation(equations, values, queries))