class Solution:
    nums1, nums2 = 0, 0
    '''
    Given an array of integers nums, return the length of the longest consecutive sequence of elements.
    A consecutive sequence is a sequence of elements in which each element is exactly... 
        ...1 greater than the previous element.
    
    You must write an algorithm that runs in O(n) time.
    '''

    def longestConsecutive(nums):
        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if it's the start of a sequence
            if (n - 1) not in numSet:  # if there is no left neighbor to value
                length = 0
                while (n + length) in numSet:  # check current number
                    length += 1  # check each consecutive num
                longest = max(length, longest)  # update longest by taking the max of current value compared to previous
        return longest

    nums1 = [2, 20, 4, 10, 3, 4, 5]  # should print 4
    nums2 = [0, 3, 2, 5, 4, 6, 1, 1]  # should print 7

    print(longestConsecutive(nums1))
    print(longestConsecutive(nums2))
