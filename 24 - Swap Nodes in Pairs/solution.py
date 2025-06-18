from typing import Optional
from urllib import response

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

    def __repr__(self) -> str:
        return str(self.val)

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None

        if head.next == None:
            return head

        node = head

        l = [node]

        while node.next:
            node = node.next
            l.append(node)

        times_to_iter = len(l) // 2

        print(times_to_iter)

        for i in range(times_to_iter):
            l[i * 2], l[i * 2 + 1] = l[i * 2 + 1], l[i * 2]

        response = l[0]

        node = response

        for i in l[1:]:
            node.next = i
            node = node.next

        node.next = None

        return response



def listToNode(nums):
    if len(nums) > 0:
        node = ListNode(nums[0], listToNode(nums[1:]))
        return node
    return None

if __name__ == '__main__':
    solution = Solution()
    l = listToNode([1,2,3,4])
    print(solution.swapPairs(l))