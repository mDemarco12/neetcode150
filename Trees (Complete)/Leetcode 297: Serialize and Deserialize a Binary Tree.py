from typing import Optional, List
from collections import deque


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

    def treeToArray(self, root):
        """
        Convert a binary tree to an array representation.
        The array representation follows LeetCode's format where null nodes are represented as None.
        """
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            level_has_value = False  # Flag to check if we should keep adding nulls

            for _ in range(level_size):
                node = queue.popleft()

                if node is None:
                    result.append(None)
                    queue.append(None)
                    queue.append(None)
                else:
                    result.append(node.val)
                    level_has_value = True
                    queue.append(node.left)
                    queue.append(node.right)

            # If this level had no actual nodes, remove all nulls from this level
            if not level_has_value:
                while result and result[-1] is None:
                    result.pop()
                break

        # Remove trailing nulls if any
        while result and result[-1] is None:
            result.pop()

        return result

    def serialize(self, root: Optional[TreeNode]) -> str:
        # set result to an array (we will insert strings here)
        res = []

        # define preorder dfs function
        def dfs(node):
            if not node:
                res.append("N")
                return

            # we append b/f dfs, then convert int to string, then append res
            res.append(str(node.val))

            # recursive call on left and right
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        # join the result using comma's as a delimiter
        return ",".join(res)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        # split data
        vals = data.split(",")
        # create g.pointer, start @ first values
        self.i = 0

        def dfs():
            if vals[self.i] == ("N"):
                # increment i
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))

            # increment global i
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()

    def sol(self) -> None:
        tree1, tree2 = [1, 2, 3, None, None, 4, 5], []

        bt1, bt2 = self.create_bst(tree1), self.create_bst(tree2)

        serial1, serial2 = self.serialize(bt1), self.serialize(bt2)
        deserial1, deserial2 = self.deserialize(serial1), self.deserialize(serial2)
        ds1, ds2 = self.treeToArray(deserial1), self.treeToArray(deserial2)

        print(f"Serial and Deserialization of a Binary Tree:\nTree 1: {tree1}")
        print(f"Serialization of the tree is: {serial1}")
        print(f"Deserialization of the tree is: {ds1}")

        print(f"\nTree 2: {tree2}")
        print(f"Serialization of the tree is: {serial2}")
        print(f"Deserialization of the tree is: {ds2}\n")


solution = Solution()
solution.sol()
