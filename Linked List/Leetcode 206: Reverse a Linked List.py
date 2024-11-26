from typing_extensions import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # create link list constructor
    def list_to_listnode(self, lst: list) -> Optional[ListNode]:
        if not lst:
            return None
        head = ListNode(lst[0])
        current = head
        for val in lst[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    def listnode_to_list(self, head: Optional[ListNode]) -> list:
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result
    # end of link list constructor section
    def reverseListTwoPointers(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # variables
        prev, curr = None, head

        # while curr is not null...
        while curr:
            nxt = curr.next  # update next
            curr.next = prev  # save the link between curr and prev
            prev = curr  # update previous pointer to curr
            curr = nxt  # update curr pointer to next
        return prev

    def reverseListRecursion(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # edge case
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseListRecursion(head.next)
            head.next.next = head  # reverse the link between next node and head
        head.next = None  # if head is first in list, set to null

        return newHead

    def sol(self) -> None:
        input1 = [0, 1, 2, 3]
        input2 = []

        # Convert input lists to ListNode
        head1 = self.list_to_listnode(input1)
        head2 = self.list_to_listnode(input2)

        # two pointers
        reversed1 = self.reverseListTwoPointers(head1)
        reversed2 = self.reverseListTwoPointers(head2)
        print(self.listnode_to_list(reversed1))  # Will print [3, 2, 1, 0]
        print(self.listnode_to_list(reversed2))  # Will print []

        # Convert input lists to ListNode again (since previous lists are now reversed)
        head1 = self.list_to_listnode(input1)
        head2 = self.list_to_listnode(input2)

        # recursion
        reversed1 = self.reverseListRecursion(head1)
        reversed2 = self.reverseListRecursion(head2)
        print(self.listnode_to_list(reversed1))  # Will print [3, 2, 1, 0]
        print(self.listnode_to_list(reversed2))  # Will print []


solution = Solution()
solution.sol()
