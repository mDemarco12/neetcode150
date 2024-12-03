from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = x
        self.next = next
        self.random = random

    # this formats the output of our Linked List
    def __str__(self):
        # Create string representation
        values = []
        current = self
        while current:
            values.append(str(current.val))
            current = current.next
        return "->".join(values) + "->None"


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # create hashmap to copy nodes
        oldToCopy = {None: None}

        # fist pass: Clone the linked list nodes
        cur = head
        while cur:
            # create a copy of cur node
            copy = Node(cur.val)
            # map this copy to Hashmap
            oldToCopy[cur] = copy
            # increment cur
            cur = cur.next

        # second pass: Link each pointer
        cur = head
        while cur:
            # set pointers
            copy = oldToCopy[cur]
            # for cur, set pointers
            copy.next = oldToCopy[cur.next] # this maps copy.next to oldToCopy
            copy.random = oldToCopy[cur.random] # ditto, except copy.random
            cur = cur.next

        return oldToCopy[head]

    def create_linked_list(self, arr):

        if not arr:
            return None
        head = Node(arr[0])
        current = head
        for val in arr[1:]:
            current.next = Node(val)
            current = current.next
        return head

    def sol(self) -> None:
        head1 = self.create_linked_list([[3,None],[7,3],[4,0],[5,1]])
        head2 = self.create_linked_list([[1,None],[2,2],[3,2]])

        print(self.copyRandomList(head1))
        print(self.copyRandomList(head2))


solution = Solution()

print(solution.sol())
