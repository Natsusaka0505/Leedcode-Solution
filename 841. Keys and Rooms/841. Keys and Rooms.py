from typing import List

# Time: 0 ms (100%), Space: 18.12 MB (74.91%)

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        #Init
        res = [False] * len(rooms)
        res[0] = True
        stack = [0]
        
        #Loop the rooms
        while stack:
            room = stack.pop()
            for key in rooms[room]:
                if not res[key]:
                    res[key] = True
                    if key not in stack:
                        stack.append(key)
            
        return all(res)
    
sol = Solution()
inputList = [[1],[2],[3],[]]
print(sol.canVisitAllRooms(inputList))


