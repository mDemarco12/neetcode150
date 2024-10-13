class Solution:
    def maxArea(self, heights):
        # Brute Force
        res = 0

        for l in range(len(heights)):
            for r in range(l + 1, len(heights)):
                area = (r - 1) * min(heights[l], heights[r])
                res = max(res, area)
        return res


solution = Solution()
heights1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
heights2 = [2, 2, 2]

print(solution.maxArea(heights1))  # Out: 49
print(solution.maxArea(heights2))  # Out: 2
