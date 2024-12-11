from typing import List


class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # we have two arrays
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        # Edge Case: we make sure A is smaller of the two
        if len(B) < len(A):
            # swap a and b
            A, B = B, A
        # run binary search on A
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2  # mid-value for A
            j = (half - i) - 2  # mid-value for B

            # find value and determine median
            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # partition if correct
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright)

                # even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:  # Aleft is t0o big...
                r = i - 1

            else: l = i + 1

    def sol(self) -> None:
        nums11 = [1, 2]
        nums21 = [3]

        nums12 = [1, 3]
        nums22 = [2, 4]

        print(self.findMedianSortedArrays(nums11, nums21)) # output: 2
        print(self.findMedianSortedArrays(nums12, nums22)) # output: 2.5


solution = Solution()

print(solution.sol())
