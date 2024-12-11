from typing import List


class Solution:

    def search(self, nums: List[int], target: int) -> int:
        # pointers
        l, r = 0, len(nums) - 1

        # binary search uses while-loops
        while l <= r:
            # find the median point
            m = (l + r) // 2
            # compare r and left pointers to target
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        # if the value does not exist, return - 1
        return -1


'''
Welcome to Binary Search. We have come far, haven't we? 
Binary search works through a couple of ways.
First, we use a while loop to iterate through the entire array.
Second, we use two-pointers (remember that section? Very useful)...
and compare the left value to the right. 
We compare and try to the median (middle value) of the array by dividing L + r // 2
We split, compare, and adjust the position of left and right till we find our value.
If the value DNE (does not exist) we return 0. 
'''

solution = Solution()
nums1 = [-1, 0, 2, 4, 6, 8]
target1 = 4
nums2 = [-1, 0, 2, 4, 6, 8]
target2 = 3

print(solution.search(nums1, target1))  # output: 3
print(solution.search(nums2, target2))  # output: -1
