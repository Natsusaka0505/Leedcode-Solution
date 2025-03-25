from typing import List
from collections import deque

# Time: 3 ms (89.99%), Space: 19.36 MB (25.00%)
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node,d,v):
            v[node]=True
            for i in d[node]:
                if (not v[i]):
                    dfs(i,d,v)
        n=len(isConnected)
        d = {i: [] for i in range(n)}
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]==1 and i!=j:               
                    d[i].append(j)
                    d[j].append(i)
        v=[False]*n
        ans=0
        for i in range(n):
            if (not v[i]):
                ans += 1 
                dfs(i,d,v)
        return ans

sol = Solution()
inputList = [[1,1,0],[1,1,0],[0,0,1]]
print(sol.findCircleNum(inputList))
