import collections
import heapq
from typing import List

# Time: 99 ms (85.92%), Space: 26.75MB (99.67%)
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        left = []
        right = []
        numWorkers = len(costs)
        total = 0
        numChosen = 0
        
        if candidates * 2 > numWorkers:
            heapq.heapify(costs)
            while numChosen < k:
                total += heapq.heappop(costs)
                numChosen += 1
            return total


        for i in range(candidates):
            heapq.heappush(left, costs[i])
        for i in range(numWorkers - 1, numWorkers - candidates - 1, -1):
            heapq.heappush(right, costs[i])
        
        left_index = candidates
        right_index = numWorkers - candidates - 1

        # O(N log M)
        while numChosen < k:
            # print(left, right, left_index, right_index)
            if (not right) or (left and left[0] <= right[0]):
                total += heapq.heappop(left)
                if left_index <= right_index:
                    heapq.heappush(left, costs[left_index])
                    left_index += 1
            else:
                total += heapq.heappop(right)
                if right_index >= left_index:
                    heapq.heappush(right, costs[right_index])
                    right_index -= 1
            numChosen += 1

        return total
        
sol = Solution()
costs = [17,12,10,2,7,2,11,20,8]
k = 3
candidates = 4 

print(sol.totalCost(costs, k, candidates))