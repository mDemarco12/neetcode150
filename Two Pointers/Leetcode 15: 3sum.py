class Solution:
    def threeSum(self, nums, target):
        res = []
        nums.sort()  # We need to sort the array to group duplicates

        for i, a in enumerate(nums):
            # if i isn't first value in input arr and a is == to the neighbor value
            if i > 0 and a == nums[i - 1]:
                continue  # Skip this value and keep reading


            # This is the solution to two sum plus value a
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    # append our answer to result
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[
                        l - 1] and l < r:  # if nums[]l is the same as neighbor, and we are still in bounds...
                        l += 1
        return res


solution = Solution()
nums1 = [-2, 0, 1, 2, -1, -4]
nums2 = [-3, 0, 3, -3, 1, 2]

print(solution.threeSum(nums1, 0))  # [[-2, 0, 2], [-1, 0, 1]]
print(solution.threeSum(nums2, 0))  # [[-3, 0, 3], [-3, 1, 2]]
