from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # matrix is always going to be non-empty
        rows, cols = len(matrix), len(matrix[0])
        top, bottom = 0, rows - 1

        # begin 1st part of binary search
        while top <= bottom:
            # calculate row
            row = (top + bottom) // 2
            # look at right most value, [-1]
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:  # row has less than smallest val in row
                bottom = row - 1
            else:
                break
            # if we didn't find a middle, return False
        if not (top <= bottom): return False

        # second part of binary search
        l, r = 0, rows - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False

    def returnClass(self) -> None:
        matrix1 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        target1 = 3

        matrix2 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        target2 = 13

        print(self.searchMatrix(matrix1, target1))  # Output: True
        print(self.searchMatrix(matrix2, target2))  # Output: False


solution = Solution()
print(solution.returnClass())
