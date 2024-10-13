class Solution:
    def maxArea(self, heights):
        # Linear Solution
        res = 0
        l, r = 0, len(heights) - 1

        while l < r:
            area = (r - 1) * min(heights[l], heights[r])
            res = max(res, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return res


solution = Solution()
heights1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
heights2 = [2, 2, 2]

print(solution.maxArea(heights1))  # Out: 49
print(solution.maxArea(heights2))  # Out: 2
