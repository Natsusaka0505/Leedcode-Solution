import collections
import heapq
from typing import List
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

# Time: 24 ms (98.41%), Space: 17.91MB (6.64%)
class Solution:
    def guess(n : int):
        pass
    def guessNumber(self, n: int) -> int:
        low, high = 1, n

        while low <= high:
            mid = (low + high) // 2
            resCode = self.guess(mid)

            if resCode == 0:
                return mid
            elif resCode == -1:
                high = mid - 1
            else:           
                low = mid + 1

        return 0      

        


sol = Solution()
print(sol.totalCost(n=10, pick=6))
