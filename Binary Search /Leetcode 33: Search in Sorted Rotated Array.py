from typing import List


class Solution:

    def search(self, nums: List[int], target: int) -> int:
        # init pointers
        l, r = 0, len(nums) - 1

        while l <= r:
            # middle
            m = (l + r) // 2
            # edge case
            if target == nums[m]:
                return m
            # we are in left sorted-portion of array
            if nums[l] <= nums[m]:
                if target < nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    # search left, update right portion
                    r = m - 1
            # we are in right portion
            else:
                # if the target is less than mid or greater than right-most value...
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        # Target value DNE
        return -1


    def output(self) -> None:
        nums1 = [3, 4, 5, 6, 1, 2]
        nums2 = [3, 5, 6, 0, 1, 2]
        t1 = 1
        t2 = 4

        print(self.search(nums1, t1))
        print(self.search(nums2, t2))


solution = Solution()

print(solution.output())
