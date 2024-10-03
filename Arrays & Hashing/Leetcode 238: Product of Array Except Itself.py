class Solution:
    #Test Cases:
    nums1 = [1, 2, 3, 4]
    nums2 = [-1, 0, 1, 2, 3]
    nums3 = [21, 0, 4, 34, 11111]

    def productExceptSelf(nums):
        '''We mult every value expect the nums value and return it
        answer[i] is equal to the product of all elements of nums except nums[i]
        input: [1,2,3,4]; output -> [24,12,8,6] 1 = 2*3*4 -> 24, 2= 3*4 -> 12

        WE NEED TO SOLVE IN O(n) AND WE CANT USE DIVISION OPERATOR
        get the product before and after nums, then mult the two for our product

        Compute prefix and postfix product of nums, add to answer[i]
        '''
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] += prefix
            prefix += nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix += nums[i]
        return res



    '''
   Example 1:
   Input: nums = [1,2,4,6]
       Output: [48,24,12,8]

   Example 2:
   Input: nums = [-1,0,1,2,3]
       Output: [0,-6,0,0,0]
   '''
    print(productExceptSelf(nums1))
    print(productExceptSelf(nums2))
    print(productExceptSelf(nums3))