import collections


class Solution:

    def maxSlidingWindow(nums: int, k):
        output = []
        q = collections.deque()
        l = r = 0

        while r < len(nums):
            # make sure no smaller values exists
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # if left value is out of bounds
            # remove left value from window
            if l > q[0]:
                q.popleft()
            # edge case
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output


solution = Solution()
nums1 = [1, 3, -1, -3, 5, 3, 6, 7]  # output: 3,3,5,5,6,7
nums2 = [1, 1, 1, 1, 1, 4, 5]  # output: 4,5
k1 = 3
k2 = 6
print(solution.maxSlidingWindow(nums1, k1))
print(solution.maxSlidingWindow(nums2, k2))
