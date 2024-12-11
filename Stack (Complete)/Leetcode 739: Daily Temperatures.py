from typing import List


class Solution:

    def dailyTemperatures(self, temperature: List[int]) -> List[int]:
        # init default values in res to 0
        res = [0] * len(temperature)
        stack = []  # pair: [temp, index]

        # i is index, t is temp
        for i, t in enumerate(temperature):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                # the result of the index is equal to the current index temp (i) - index we popped
                res[stackInd] = (i - stackInd)
            stack.append([t, i])
        return res
'''
Our stack is in Monotonic Decreasing order, meaning it will it decrease over its domain. 
So we fill values in the stack, and we compare the next value to current. If next > current, pop stack, and calcuate the different in values
If the value is lesser than current, keep it in stack and compare to next value.
All values in stack should be popped, if not, the default value is 0.
'''

solution = Solution()

temperature1 = [30, 38, 30, 36, 35, 40, 28]
temperature2 = [22, 21, 20]

print(solution.dailyTemperatures(temperature1))  # output: [1,4,1,2,1,0,0]
print(solution.dailyTemperatures(temperature2))  # output: [0,0,0]
