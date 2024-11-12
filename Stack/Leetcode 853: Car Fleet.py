from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # stack for pairs: use list comprehension
        pair = [[p, s] for p, s in zip(position, speed)]
        stack = []

        for p, s in sorted(pair)[::-1]:
            # decimal division
            stack.append((target - p) / s)
            # does val overlap? Top of stack == -1: -2 is the destination
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)


solution = Solution()
target1 = 10
position1 = [1, 4]
speed1 = [3, 2]
target2 = 10
position2 = [4, 1, 0, 7]
speed2 = [2, 2, 1, 1]

print(solution.carFleet(target1, position1, speed1))  # output: 1
print(solution.carFleet(target2, position2, speed2))  # output: 3
