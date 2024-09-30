'''
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
Return the answer with the smaller index first.
    Example 1:
    Input: nums = [3,4,5,6], target = 7
    Output: [0,1]
        Explanation: nums[0] + nums[1] == 7, so we return [0, 1].
    Example 2:
    Input: nums = [4,5,6], target = 10
    Output: [0,2]
'''


def twoSum(nums, target):
    # Start with an empty hashmap, and go through the nums array
    # Subtract the target from the value in the nums array, add to empty set if it is not present
    # When you subtract a num that is in the empty array, return the two indices
    prevMap = {}

    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i
    return True

print(twoSum([3, 4, 5, 6], 7))
