from typing import List


class Solution:

    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []  # pair: (index, height)

        for i, h in enumerate(heights):
            # height starts at i
            start = i
            # check if the stack is !empty & top value's height > h
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, index * (i - index))  # i - index is width
                start = index  # we can extend index backwards
            stack.append((start, h))
        # check entries in our stack
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea
''''
class solution(Solution):
    def solution(self)
        h1 = [7, 1, 7, 2, 2, 4]
        h2 = [1, 3, 7]

        print(self.largestRectangleArea(h1))  # output: 8
        print(self.largestRectangleArea(h2))  # output: 7
'''

solution = Solution()

h1 = [7, 1, 7, 2, 2, 4]
h2 = [1, 3, 7]

print(solution.largestRectangleArea(h1))  # output: 8
print(solution.largestRectangleArea(h2))  # output: 7


