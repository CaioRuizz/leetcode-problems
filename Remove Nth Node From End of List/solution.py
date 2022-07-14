from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        node = self
        response = f'{node.val}, '
        while node.next:
            node = node.next
            response += f'{node.val}, '
        return response[:-2]

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pointer = 0
        length = 1

        node = head

        while node.next:
            node = node.next
            length += 1

        print(length)

        print(n, length)

        if n == length:
            return head.next

        node = head

        while pointer < (length - 1) - n:
            node = node.next
            pointer += 1
        
        node.next = node.next.next

        return head

def listToNode(nums):
    if len(nums) > 0:
        node = ListNode(nums[0], listToNode(nums[1:]))
        return node
    return None


if __name__ == '__main__':
    case = listToNode([1, 2, 3, 4 , 5, 6])
    print(case)
    solution = Solution()
    print(solution.removeNthFromEnd(case, 4))
