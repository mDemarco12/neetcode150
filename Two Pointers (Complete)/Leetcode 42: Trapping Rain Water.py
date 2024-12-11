class Solution:
    '''
    How does this algo work? We need two pointers, right and left. We need to compare keep track of the max height of either.
    Then we compare the max height of the pointer to the input array (Equation: Max[l/r] - i).
    Update the value of max by comparing Max of the pointer to the input array ("max(lMax, height[l]")
    The difference between the max height and the input is the "water". Note: Think of it as the water from Minecraft.
    To move the pointers, we compare the max between left and right with the lowest being the one that travels.
    Append the result after each comparison till pointers meet, then return the result.
    '''


    def trap(self, height):
        # edge case
        if not height:
            return 0
        l, r = 0, len(height) - 1
        lMax, rMax = height[l], height[r]
        res = 0

        while l < r:
            if lMax < rMax:
                l += 1
                lMax = max(lMax, height[l])
                res += lMax - height[l]
            else:
                r -= 1
                rMax = max(rMax, height[r])
                res += rMax - height[r]
        return res


solution = Solution()

height1 = [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]  # output 9
height2 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]  # output 6

print(solution.trap(height1))
print(solution.trap(height2))
