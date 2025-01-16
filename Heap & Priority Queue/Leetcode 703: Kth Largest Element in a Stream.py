import heapq
from typing import List, Any


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        # minHeap with K largest ints
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)

        # use while-loop to adjust size of heap to int k
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        # add value to our minHeap
        heapq.heappush(self.minHeap, val)

        # edge case: heap has less than k elements
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]  # min value is stored in 0

    @staticmethod
    def handle_commands(commands: List[Any]) -> List[Any]:
        """Handles commands and operations for KthLargest class."""
        # Ensure initialization command is correct
        if commands[0] != "KthLargest":
            raise ValueError("First command must initialize the KthLargest class.")

        # Parse the initialization arguments
        k, nums = commands[1]
        obj = KthLargest(k, nums)
        results = [None]  # Constructor does not return a result

        # Process remaining commands
        for i in range(2, len(commands), 2):
            command = commands[i]
            arg = commands[i + 1]

            if command == "add":
                results.append(obj.add(arg[0]))
            else:
                raise ValueError(f"Unknown command: {command}")

        return results


    def output(self) -> None:
        list1 = ["KthLargest", [3, [1, 2, 3, 3]], "add", [3], "add", [5],
                 "add", [6], "add", [7], "add", [8]]
        results = KthLargest.handle_commands(list1)
        print(f"The Kth Largest element:\nList 1: {results}")


solution = KthLargest(3,  [1, 2, 3, 3])
solution.output()
