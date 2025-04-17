from typing import List, Tuple
from collections import deque

# Time: 23 ms (97.37%), Space: 38.22 MB (97.81%)
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # Initialize a set to track visited cities
        seen = {0}
        # Counter for the number of roads that need to be reversed
        ans = 0
        
        while len(seen) < n:
            check = []
            for path in connections:
                if path[1] in seen:
                    seen.add(path[0])
                elif path[0] in seen:
                    seen.add(path[1])
                    ans += 1
                else:
                    check.append(path)
            # Reverse the order of unprocessed connections for the next iteration
            connections = check[::-1]
        
        return ans

sol = Solution()
inputList = [[0,1],[1,3],[2,3],[4,0],[4,5]]
print(sol.minReorder(6, inputList))

