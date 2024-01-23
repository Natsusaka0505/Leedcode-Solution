from collections import deque


# one queue solution
# Time: 796 ms (11.14%), Space: 16.73 MB (74.07%)
class Solution1:
    def predictPartyVictory(self, senate: str) -> str:
        senates = deque(senate)

        while len(senates) > 1:
            s = senates.popleft()
            try:
                senates.remove("R" if s == "D" else "D")
                senates.append(s)
            except ValueError:
                pass

        return "Radiant" if senates.popleft() == "R" else "Dire"


# Two queue solution
# Time: 35 ms (99.52%), Space: 16.97 MB (59.64%)
class Solution2:
    def predictPartyVictory(self, senate: str) -> str:
        rad = deque()
        dir = deque()

        n = len(senate)

        for idx, s in enumerate(senate):
            if s == "R":
                rad.append(idx)
            else:
                dir.append(idx)

        while len(rad) and len(dir):
            if rad.popleft() > dir.popleft():
                dir.append(n)
            else:
                rad.append(n)

            n += 1

        return "Radiant" if len(rad) else "Dire"


sol = Solution2()
# senate = "RD"
senate = "RDD"
print(sol.predictPartyVictory(senate))
