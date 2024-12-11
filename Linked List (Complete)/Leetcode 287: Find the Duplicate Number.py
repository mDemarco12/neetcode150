from typing import List


class Solution:

    def findDuplicate(self, nums: List[int]) -> int:
        # we will use Floyd's Cycle Detection Algorithm
        fast, slow = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast: break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2: return slow

    def sol(self) -> None:

        list1 = [1, 2, 3, 2, 2] # 2
        list2 = [1, 2, 3, 4, 4] # 4

        print(self.findDuplicate(list1))
        print(self.findDuplicate(list2))


solution = Solution()

solution.sol()
