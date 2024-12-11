from typing import List


class Solution:

    def findMin(self, nums: List[int]) -> int:
        # declare values
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            # if we get to a sorted sub-arr...update result
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            # declare middle and res
            m = (l + r) // 2
            res = min(res, nums[m])
            # is this mid-value of the left sorted portion?
            if nums[m] >= nums[l]:
                l = m + 1
            # right
            else:
                r = m - 1
        return res

    def output(self) -> None:
        nums1 = [3, 4, 5, 6, 1, 2]
        nums2 = [4, 5, 0, 1, 2, 3]
        nums3 = [4, 5, 6, 7]

        print(self.findMin(nums1))  # output: 1
        print(self.findMin(nums2))  # output: 2
        print(self.findMin(nums3))  # output: 4


solution = Solution()
print(solution.output())
