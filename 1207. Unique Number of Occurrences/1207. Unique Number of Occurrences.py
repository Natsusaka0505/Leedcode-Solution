from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashMap = {}

        for ele in arr:
            if ele in hashMap:
                hashMap[ele] += 1
            else:
                hashMap[ele] = 1

        hashSet = set()
        flag = True

        for count in hashMap.values():
            if count in hashSet:
                flag = False
            else:
                hashSet.add(count)

        return flag


arr = [1, 2, 2, 1, 1, 3]
sol = Solution()
print(sol.uniqueOccurrences(arr))
