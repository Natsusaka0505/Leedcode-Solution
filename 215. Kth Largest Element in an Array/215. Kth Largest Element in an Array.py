import collections
from typing import List, Tuple
import numpy

# Time: 3 ms (82.18%), Space: 18.02MB (5.97%)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return int(numpy.partition(nums, -k)[-k])


    #nums = [3, 2, 1, 5, 6, 4]
    #k = 2
    # numpy.partition(nums, -2) → 例如: [3, 2, 1, 4, 5, 6]
    # 最後一個位置（-2）是第 2 大：5
    # [-2] 就是 5


sol = Solution()
nums = [3,2,1,5,6,4], k = 2

print(sol.findKthLargest(nums, k))
