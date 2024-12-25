import collections
from typing import Optional, List


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

    def rightSide(self, root: Optional[TreeNode]) -> List[int]:
        # We will use BFS (Level order traversal) So array and queue
        res = []
        q = collections.deque([root])

        while q:
            # set right to none
            rightSide = None
            qLen = len(q)

            # for this level, we go through every element, pop it, and add the children the queue
            for i in range(qLen):
                # pop from left, add from right
                node = q.popleft()
                # if not null...
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                res.append(rightSide.val)
        return res

    def sol(self) -> None:
        root1 = [1, 2, 3]
        root2 = [1, 2, 3, 4, 5, 6, 7]

        r1, r2 = self.create_bst(root1), self.create_bst(root2)

        sol1, sol2 = self.rightSide(r1), self.rightSide(r2)  # sol1 = [1,3], sol2 = [1,3,7]

        print(f"The right side of binary tree 1 is : {sol1} " +
              f"\nThe right side of binary tree 2 is : {sol2}")


'''
Been a while since I added a comment because I believe you all are weathered to know how this program functions from the code...
But I'll add quick comment as my Christmas gift to you!
So it is nature when tasked with displaying one side of an Binary Tree to just iterate and output "The right"...
But there are edge cases that will null this process. So if you use Breath First Search (AKA Level Order Traversal)...
you can keep track of two things, 1) the level of the node and 2) the left v right node. We add the values to a Queue.
In the Queue, we can keep track of the root, left, right, and subsequent children. We update the result array with the right side...
while popping that value from the Queue. Included in this code it the helper function "create_bst" to build the binary tree.
If you have any questions, please consult Neetcode's video "Leetcode 199: Right Side of Binary Tree". 
Merry Christmas guys, (I should probably not have done work today, but I know this will pay off one day)


'''
solution = Solution()

solution.sol()
