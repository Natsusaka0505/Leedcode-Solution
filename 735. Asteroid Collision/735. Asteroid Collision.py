from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []

        for asteroid in asteroids:
            while res and res[-1] > 0 and asteroid < 0:
                if res[-1] + asteroid == 0:
                    res.pop()
                    asteroid = 0
                elif res[-1] + asteroid < 0:
                    res.pop()
                else:
                    asteroid = 0
            if asteroid:
                res.append(asteroid)

        return res


sol = Solution()

# asteroids = [5, 10, -5]
# asteroids = [8,-8]
asteroids = [10, 2, -5]
print(sol.asteroidCollision(asteroids))
