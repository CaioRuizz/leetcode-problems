from typing import *
from urllib import response

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        node = self
        response = ''
        while node:
            response += f'{node.val}, '
            node = node.next

        response = response[:-2]
        return response

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        response = None
        temp = None
        carry = 0
        while l1 is not None or l2 is not None:
            sum_value = carry
            
            if l1 is not None:
                sum_value += l1.val
                l1 = l1.next
            if l2 is not None:
                sum_value += l2.val
                l2 = l2.next
            
            node = ListNode(sum_value % 10)
            
            carry = sum_value // 10

            if temp is None:
                temp = response = node

            else:
                temp.next = node
                temp = temp.next

        if carry > 0:
            temp.next = ListNode(carry)
        
        return response


if __name__ == '__main__':
    a = ListNode(
        2,
        ListNode(
            4,
            ListNode(
                3,   
            )   
        )
    )

    b = ListNode(
        5,
        ListNode(
            6,
            ListNode(
                4,   
            )   
        )
    )

    solution = Solution()

    print(solution.addTwoNumbers(a, b))