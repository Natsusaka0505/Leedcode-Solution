from typing import List


# Time: 3 ms (89.99%), Space: 19.36 MB (25.00%)
from collections import deque
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        m,n = len(isConnected),len(isConnected[0])
        adjList = [[] for _ in range(n)]
        for i in range(m):
            for j in range(n):
                if isConnected[i][j]==1 and i!=j:
                    adjList[i].append(j)
                    adjList[j].append(i)
        vis = [False]*n
        res = 0
        for i in range(n):
            if not vis[i]:
                qu = deque()
                qu.append(i)
                vis[i] = True
                while qu:
                    node = qu.popleft()
                    for adj in adjList[node]:
                        if not vis[adj]:
                            vis[adj] = True
                            qu.append(adj)
                res+=1
        return res

sol = Solution()
inputList = [[1,1,0],[1,1,0],[0,0,1]]
print(sol.findCircleNum(inputList))
