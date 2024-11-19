from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # pointers
        l, r = 1, max(piles)
        res = r  # the result will always default to the max val of piles

        while l <= r:
            # calc the middle
            k = (l + r) // 2
            hours = 0
            # start going through piles in input array
            for p in piles:
                # we can divide pile p by k
                hours += math.ceil(p / k)
            if hours <= h:  # condition to update res and right pointer
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res

    def output(self) -> None:

        piles1 = [1, 4, 3, 2]
        h1 = 9
        piles2 = [25, 10, 23, 4]
        h2 = 4

        print(self.minEatingSpeed(piles1, h1))  # output: 2
        print(self.minEatingSpeed(piles2, h2))  # output: 25


solution = Solution()
print(solution.output())
