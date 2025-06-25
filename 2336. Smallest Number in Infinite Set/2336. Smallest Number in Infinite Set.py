import collections
from typing import List, Tuple
import numpy

# Time: 9 ms (92.69%), Space: 15.87MB (33.68%)
class SmallestInfiniteSet:

    def __init__(self):
        self.SmallestInfiniteSet  = set()
        self.cur = 1

    def popSmallest(self) -> int:
        if self.SmallestInfiniteSet:
            res = min(self.SmallestInfiniteSet)
            self.SmallestInfiniteSet.remove(res)
            return res
        else:
            self.cur += 1
            return self.cur - 1

    def addBack(self, num: int) -> None:
        if (self.cur > num):
            self.SmallestInfiniteSet.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)