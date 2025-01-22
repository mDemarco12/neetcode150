from typing import List
import heapq, time


class Solution:
    def kClosestHeap(self, points: List[List[int]], k: int) -> List[List[int]]:
        # we will use a minHeap, which is initially an array() or list []
        minHeap, res = [], []

        for x, y in points:
            # compute distance
            dist = (x ** 2) + (y ** 2)

            # append the list and include distance
            minHeap.append([dist, x, y])
        # turn our list into a heap
        heapq.heapify(minHeap)

        while k > 0:
            # keep popping from heap and append
            dist, x, y = heapq.heappop(minHeap)

            # append our result, we don't include dist at this point
            res.append([x, y])

            # decrement k til 0
            k -= 1
        return res

    def kClosestSort(self, points: List[List[int]], k: int) -> List[List[int]]:
        # note, lambda's take on whatever format as listed; [x**2 + y**2]
        # lambda's also allow inline expressions that otherwise trigger "invalid syntax"
        points.sort(key=lambda p: p[0] ** 2 + p[1] ** 2)
        return points[:k]

    def sol(self) -> None:
        points1, k1 = [[0, 2], [2, 2]], 1
        points2, k2 = [[0, 2], [2, 0], [2, 2]], 2

        # heap
        start_nc1 = time.perf_counter()
        p1, p2 = self.kClosestHeap(points1, k1), self.kClosestHeap(points2, k2)
        end_nc1 = time.perf_counter()

        # sort
        start_if1 = time.perf_counter()
        p3, p4 = self.kClosestSort(points1, k1), self.kClosestHeap(points2, k2)
        end_if1 = time.perf_counter()

        timeHeap = ((end_nc1 - start_nc1) * 2)
        timeSort = ((end_if1 - start_if1) * 2)

        formatHeap = f"The total execution time for Heap is {timeHeap:.3e} ms."
        formatSort = f"The total execution time for Sort is {timeSort:.3e} ms."

        print("K Closest Points to Origin: Heap & Sort")
        print(f"The first List: {points1} has the closest(s) point to origin at {p1}.\n" +
              f"The second List: {points2} has the closest(s) point to origin at {p2}.\n")
        print("Execution Time:\n" + formatHeap + "\n" + formatSort)

        if timeHeap > timeSort:
            print("The Heap is more efficient than the Sort.")
        else:
            print("The Sort is more efficient than the Heap.")


solution = Solution()
solution.sol()
