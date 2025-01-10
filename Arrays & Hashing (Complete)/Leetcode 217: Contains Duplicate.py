import time
from typing import List


class Solution:
    def containsDuplicateHashSet(self, nums: List[int]) -> bool:
        hs = set()
        for n in nums:
            if n in hs:
                return True
            hs.add(n)
        return False

    def containsDuplicateHashMap(self, nums: List[int]) -> bool:
        hs = []
        for n in nums:
            if n in hs:
                return True
            hs.append(n)
        return False

    def output(self) -> None:
        list1, list2 = [1, 1, 1, 2, 3, 3, 4], [1, 2, 3, 4]

        # Time NeetCode solution
        start_nc1 = time.perf_counter()
        sol1, sol2 = self.containsDuplicateHashSet(list1), self.containsDuplicateHashSet(list2)
        end_nc1 = time.perf_counter()

        # Time IF solution
        start_if2 = time.perf_counter()
        sol3, sol4 = self.containsDuplicateHashMap(list1), self.containsDuplicateHashMap(list2)
        end_if2 = time.perf_counter()

        totalTime1, totalTime2 = round((end_nc1 - start_nc1) * 1000, 5), round((end_if2 - start_if2) * 1000, 5)

        print("Contains Duplicate HashSet:")
        print(f"Set 1: {sol1}\nSet 2: {sol2}")
        print(f"The total time it took to execute using a Hash Set was {totalTime1} seconds.")
        print("\nContains Duplicate HashMap:")
        print(f"Set 1: {sol3}\nSet 2: {sol4}")
        print(f"The total time it took to execute using a Hash Map was {totalTime2} seconds.")

        if totalTime1 > totalTime2:
            print(f"\nThe HashMap has a faster execution time of {totalTime2} seconds.")
        else:
            print(f"\nThe HashSet has a faster execution time of {totalTime1} seconds.")


'''
What did this exercise teach me? 
Hash Maps are blistering quick and the saying is true...
"If you don't know what to do, it probably needs a Hashmap"
Remember, Hashmaps are created using "[]" while set is "set()"
You "append" Hashmaps while you "add" to Hashsets
Hashmaps are dead easy to implement, traverse, and call from. Please make working with them a habit.
'''

solution = Solution()

solution.output()
