import heapq
from typing import List, Deque
from collections import deque, Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # each task is 1 unit, and minimize idle time
        # declare vars
        time: int = 0
        q: Deque = deque()

        # count occurrences of char in input
        count = Counter(tasks)
        # maxHeap using counts... we have to take negative of count to adjust for Python's minHeap
        maxHeap = [-cnt for cnt in count.values()]
        # sort our heap
        heapq.heapify(maxHeap)

        while maxHeap or q:
            # increment time
            time += 1
            # if heap is not empty
            if maxHeap:
                # increment index and pop
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            # if is != empty and idle time has been reached
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time

    def main(self) -> None:
        tasks1, n1 = ["X", "X", "Y", "Y"], 2
        task2, n2 = ["A", "A", "A", "B", "C"], 3
        s1 = self.leastInterval(tasks1, n1)
        s2 = self.leastInterval(task2, n2)

        print(f"The least interval of Task 1, {tasks1} is: {s1}\n"
              f"The least interval of Task 2, {task2} is: {s2}\n")


if __name__ == '__main__':
    solution = Solution()
    solution.main()
