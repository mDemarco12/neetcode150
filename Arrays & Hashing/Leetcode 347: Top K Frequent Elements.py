'''
Given an integer array nums and an integer k, return the k most frequent elements within the array.
The test cases are generated such that the answer is always unique.
You may return the output in any order.
    Example 1:
        Input: nums = [1,2,2,3,3,3], k = 2
        Output: [2,3]
    Example 2:
        Input: nums = [7,7], k = 1
        Output: [7]
'''


def topKFrequent(nums, k):
    count = {}  # this is your hashmap
    freq = [[] for i in range(len(nums) + 1)]  # array as input arr

    for n in nums:  # for each number in nums
        count[n] = 1 + count.get(n, 0)  # count n is equal to the pos of count at n, 0 if it does not exist, + 1
    for n, c in count.items():  # count.items returns key value pair
        freq[c].append(n)

    res = []
    for i in range(len(freq) - 1, 0, -1):  # len of freq - 1, go up to 0, decrement by -1
        for n in freq[i]:  # Go through each n value in freq
            res.append(n)  # and append n
            if len(res) == k:  # If res is = k we are done.
                return res


print(topKFrequent([1, 2, 2, 3, 3, 3], 2))
print(topKFrequent([7, 7], 1))
