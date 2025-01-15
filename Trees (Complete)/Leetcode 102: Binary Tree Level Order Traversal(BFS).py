from typing import Optional, List
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def create_bst(self, values: List[int]) -> Optional[TreeNode]:
        if not values or values[0] is None:
            return None

        root = TreeNode(values[0])
        queue = [root]
        i = 1

        while queue and i < len(values):
            node = queue.pop(0)

            if i < len(values) and values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1

            if i < len(values) and values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1

        return root

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # we need to init the result arr
        res = []

        # The Queue
        q = collections.deque()
        q.append(root)

        while q:
            # we get the length of the q, one level at a time
            qLen = len(q)
            level = []
            # loop for each val in q
            for i in range(qLen):
                # FIFO
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            # make sure level is non-empty
            if level:
                res.append(level)
        return res

    def sol(self) -> None:
        root = [1, 2, 3, 4, 5, 6, 7]
        root2 = []

        r1, r2 = self.create_bst(root), self.create_bst(root2)
        sol, sol2 = self.levelOrder(r1), self.levelOrder(r2)

        print(f"Level order for Solution 1: {sol}")
        print(f"Level order for Solution 2: {sol2}")


solution = Solution()

solution.sol()
