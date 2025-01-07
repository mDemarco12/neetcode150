from typing import List
import time


class Solution:

    def minPathSumNC(self, grid: List[List[int]]) -> float:
        ROWS, COLS = len(grid), len(grid[0])

        # Initialize the cols to infinity
        res = [[float("inf")] * (COLS + 1) for r in range(ROWS + 1)]
        # Initialize the bottom right of the 2d Matrix to zero
        res[ROWS - 1][COLS] = 0

        # Iterate through the grid bottom up and calc the value for reach pos
        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                # for a pos in result, we need to take val @ position,
                # and add it to the min cost of the val below and to the right
                res[r][c] = grid[r][c] + min(res[r + 1][c], res[r][c + 1])
            # return the sum at first row and col
        return res[0][0]

    def minPathSumIF(self, grid: List[List[int]]) -> int:
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if row == 0 and col == 0:
                    continue
                if row == 0 or col == 0:
                    if row == 0:
                        grid[row][col] += grid[row][col - 1]
                    elif col == 0:
                        grid[row][col] += grid[row - 1][col]
                else:
                    grid[row][col] += min(grid[row][col - 1], grid[row - 1][col])
        return grid[-1][-1]

    def sol(self) -> None:
        list1 = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
        list2 = [[1, 2, 3], [4, 5, 6]]

        # Time NeetCode solution
        start_nc1 = time.perf_counter()
        sol1, sol2 = self.minPathSumNC(list1.copy()), self.minPathSumNC(list2.copy())
        end_nc1 = time.perf_counter()

        # Time IF solution
        start_if2 = time.perf_counter()
        sol3, sol4 = self.minPathSumIF(list1.copy()), self.minPathSumIF(list2.copy())
        end_if2 = time.perf_counter()

        totalTime1, totalTime2 = (end_nc1 - start_nc1) * 1000, (end_if2 - start_if2) * 1000

        print("Neetcode Solution:")
        print(f"The following matrix {list1} has a min path sum of {sol1}")
        print(f"The following matrix {list2} has a min path sum of {sol2}")
        print(f"Execution time: {totalTime1:.5f} seconds\n")

        print("IF and Else Solution:")
        print(f"The following matrix {list1} has a min path sum of {sol3}")
        print(f"The following matrix {list2} has a min path sum of {sol4}")
        print(f"Execution time: {totalTime2:.5f} seconds\n")

        bestTime = min(totalTime1, totalTime2)

        if totalTime1 > totalTime2:
            print(f"Solution 2 is the most efficient with exec time {bestTime:.5f} seconds")
        else:
            print(f"Solution 1 is the most efficient with exec time {bestTime:.5f} seconds")



solution = Solution()

solution.sol()