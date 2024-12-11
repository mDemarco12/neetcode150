from typing import Optional


class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next

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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # include the vars
        dummy = ListNode(0, head)
        groupPrev = dummy

        # loop
        while True:
            # we need the kth node to determine group size
            kth = self.getKth(groupPrev, k)
            # edge case
            if not kth:
                break
            groupNext = kth.next

            # now we need to reverse the list via two pointers!
            prev, curr = kth.next, groupPrev.next

            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            temp = groupPrev.next  # this stores the first node of group
            groupPrev.next = kth  # put the kth at the beginning of the group
            groupPrev = temp  # update the previous
        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

    def create_linked_list(self, arr):

        if not arr:
            return None
        head = ListNode(arr[0])
        current = head
        for val in arr[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    def sol(self) -> None:
        # examples
        l1, k1 = self.create_linked_list([1, 2, 3, 4, 5, 6]), 3
        l2, k2 = self.create_linked_list([1, 2, 3, 4, 5]), 3

        print(self.reverseKGroup(l1, k1))
        print(self.reverseKGroup(l2, k2))


solution = Solution()

solution.sol()
