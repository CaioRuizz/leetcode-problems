from typing import Optional

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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            if list2:
                return list2
            return None
        if list2 is None:
            return list1
        
        node1 = list1
        node2 = list2

        result = ListNode()

        node = result

        while node1 and node2:
            if node1.val < node2.val:
                node.val = node1.val
                node1 = node1.next
                if node1:
                    node.next = ListNode()
                    node = node.next
            else:
                node.val = node2.val
                node2 = node2.next
                if node2:
                    node.next = ListNode()
                    node = node.next


        if node1:
            node.next = node1

        if node2:
            node.next = node2

        return result



def listToNode(nums):
    if len(nums) > 0:
        node = ListNode(nums[0], listToNode(nums[1:]))
        return node
    return None


if __name__ == '__main__':
    solution = Solution()
    print(solution.mergeTwoLists(listToNode([1,2,4]), listToNode([1,3,4])))