import collections
import heapq
from typing import List, Tuple
import numpy

# Time: 112 ms (98.92%), Space: 36.40MB (99.74%)
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)
        sorted_ind = sorted(range(n), key = lambda i: nums2[i],reverse = True)
        print(sorted_ind)

        min_heap = []
        sum_nums1 = 0
        
        for i in sorted_ind[:k]:
            heapq.heappush(min_heap,nums1[i])
            print(min_heap)
            sum_nums1 += nums1[i]
        ans = sum_nums1 * nums2[i]

        for i in sorted_ind[k:]:
            if nums1[i] > min_heap[0]:
                sum_nums1 += nums1[i]
                sum_nums1 -= heapq.heappushpop(min_heap,nums1[i])
                print(min_heap)
                ans = max(ans, sum_nums1 * nums2[i])
        return ans  
    
sol = Solution()
nums1 = [1,3,3,2]
nums2 = [2,1,3,4]
k = 3
print(sol.maxScore(nums1, nums2, k))