import heapq, time
from typing import List


class Solution:
    def lastStoneWeightSort(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            cur = stones.pop() - stones.pop()
            if cur:
                stones.append(cur)
        return stones[0] if stones else 0

    def lastStoneWeightHeap(self, stones: List[int]) -> int:
        # we need to implement a maxHeap using a minHeap...
        # because python does not support maxHeaps
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            # if second is greater than first...
            if second > first:
                # take the diff b/w the two and add to heap
                heapq.heappush(stones, first - second)
        # edge case: if heap is empty, return 0
        # if there is a val in 0, leave it
        stones.append(0)

        # since we are dealing with neg values(due to minHeap)...
        # we need to return the absolute value of stones[0]
        return abs(stones[0])

    def output(self) -> None:
        stones1, stones2, stones3 = [2, 3, 6, 2, 4], [2, 7, 4, 1, 8, 1], []  # output: 1, 1

        # sort
        start_nc1 = time.perf_counter()
        sort1, sort2, sort3 = (self.lastStoneWeightSort(stones1[:]), self.lastStoneWeightHeap(stones2),
                               self.lastStoneWeightHeap(stones3))
        end_nc1 = time.perf_counter()

        # heap
        start_if1 = time.perf_counter()
        heap1, heap2, heap3 = (self.lastStoneWeightHeap(stones1[:]), self.lastStoneWeightHeap(stones2),
                               self.lastStoneWeightHeap(stones3))
        end_if1 = time.perf_counter()

        sortTime, heapTime = (round((end_nc1 - start_nc1) * 1000, 4),
                              round((end_if1 - start_if1) * 1000, 4))

        print(f"The Last Stone Weight: Sort\nStack 1: {stones1}, Output: {sort1}")
        print(f"Stack 2: {stones2}, Output: {sort2}")
        print(f"Stack 3: {stones3}, Output: {sort3}")
        print(f"Total Time of Operation: {sortTime} ms\n")

        print(f"The Last Stone Weight: Heap\nStack 1: {stones1}, Output: {heap1}")
        print(f"Stack 2: {stones2}, Output: {heap2}")
        print(f"Stack 3: {stones3}, Output: {heap3}")
        print(f"Total Time of Operation: {heapTime} ms\n")

        if heapTime < sortTime: print("The Heap has superior performance")
        else: print("The Sort has superior performance")


solution = Solution()

solution.output()
