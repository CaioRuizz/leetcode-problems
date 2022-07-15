from typing import List, Optional
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

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        while None in lists:
            lists.remove(None)


        if lists == []:
            return None

        if len(lists) == 1:
            return lists[0]
        
        response = ListNode()

        node = response

        while True:
            node.next = ListNode()
            min_index = 0
            ls = lists[1:]
            min_val = lists[0].val
            min_index = 0
            for i, l in enumerate(ls):
                if l.val < min_val:
                    min_val = l.val
                    min_index = i + 1

            node.val = lists[min_index].val

            if lists[min_index].next == None:
                lists = lists[:min_index] + lists[min_index + 1:]
            else:
                lists[min_index] = lists[min_index].next

            if len(lists) > 1:
                node = node.next
            else:
                break
        
        node.next = lists[0]

        return response



def listToNode(nums):
    if len(nums) > 0:
        node = ListNode(nums[0], listToNode(nums[1:]))
        return node
    return None

if __name__ == '__main__':
    solution = Solution()
    l = [[]]
    l = [listToNode(i) for i in l]
    print(solution.mergeKLists(l))