'''
Given an array of integers numbers that is sorted in non-decreasing order.
Return the indices (1-indexed) of two numbers, [index1, index2],
such that they add up to a given target number target and index1 < index2.
    Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.
Also:
    There will always be exactly one valid solution.
    Your solution must use O(1) additional space.
'''


class Solution:
    def twoSum(self, numbers, target: int):
        l, r = 0, len(numbers) - 1  # right will always be equal to the length of arr - 1 index value

        while l < r:
            curSum = numbers[l] + numbers[r]  # curSum is equal to left and right index [l,r]

            if curSum > target:  # if our right is too high,move pointer left
                r -= 1
            elif curSum < target:  # if our left is too low,move pointer right
                l += 1
            else:  # if we are spot on, our output is l,r plus 1
                return [l + 1, r + 1]
        return []


solution = Solution()

number1 = [1, 2, 3, 4]  # Expected output: [1,2]
number2 = [1, 3, 4, 5, 7, 10, 11]  # Expected output: [3,4]

print(solution.twoSum(number1, 3))
print(solution.twoSum(number2, 9))
