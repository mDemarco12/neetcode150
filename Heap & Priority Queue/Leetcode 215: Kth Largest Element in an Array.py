from typing import List
import time


class Solution:
    def findKthLargestSort(self, nums: List[int], k: int) -> int:
        # sort the array, and return the (length of nums - k) index of nums
        # this is dead easy
        nums.sort()
        return nums[len(nums) - k]

    def findKthLargestMaxHeap(self, nums: List[int], k: int) -> int:
        # declare k
        k = len(nums) - k

        # recursive quick-select algo
        def quickSelect(l, r):
            # pivot is the nums of right, p is value that separates left (least values)
            pivot, p = nums[r], l
            for i in range(l, r):
                # set nums[p] = i
                nums[p], nums[i] = nums[i], nums[p]
                # if we swap p, we need to increment the p pointer
                # we want to increment p to keep track of index for next swap
                p += 1
            nums[p], nums[r] = nums[r], nums[p]  # swap the pivot(right-most val) with what is in nums[p]

            # now we evaluate our pivot scenarios!
            if p > k:
                return quickSelect(l, p - 1)
            elif p < k:
                return quickSelect(p + 1, r)
            else:
                return nums[p]  # this test case is if p == k

        return quickSelect(0, len(nums) - 1)

    def sol(self) -> None:
        nums1, k1 = [2, 3, 1, 5, 4], 2
        nums2, k2 = [2, 3, 1, 1, 5, 5, 4], 3

        start_nc1 = time.perf_counter()
        solution1, solution2 = (self.findKthLargestSort(nums1, k1),
                                self.findKthLargestSort(nums2, k2))
        end_nc1 = time.perf_counter()

        start_nc2 = time.perf_counter()
        solution3, solution4 = (self.findKthLargestMaxHeap(nums1, k1),
                                self.findKthLargestMaxHeap(nums2, k2))
        end_nc2 = time.perf_counter()

        sortTime = (end_nc1 - start_nc1)
        heapTime = (end_nc2 - start_nc2)

        print("Kth Largest Element in an Array: MaxHeap v. Sort")
        print(f"The Kth, k = {k1} Largest Element in an Array 1, {nums1}, is {solution1}")
        print(f"The Kth, k = {k2} Largest Element in an Array 2, {nums2}, is {solution2}\n")
        print(f"The run time for Sort is: {sortTime:.3e} ms\n"
              f"The run time for MaxHeap is: {heapTime:.3e} ms")

        if sortTime < heapTime:
            print("The Sort has a faster execution time!")
        else:
            print("The Heap has a faster execution time!")


# Good coding practice: Write if __name__ to isolate what our coding is doing...
# where it is doing it, and when!
if __name__ == '__main__':
    solution = Solution()
    solution.sol()
