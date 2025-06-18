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

    def __repr__(self) -> str:
        return str(self.val)

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        list = self.nodeToList(head)
        len_list = len(list)

        if k == 1:
            return head

        if len_list < k:
            return head

        if k == len_list:
            return self.listToNode(list[::-1])

        result = []
        previous = 0

        for i in range(k, len_list + 1, k):
            result += list[previous:i][::-1]
            previous = i

        module = len_list % k
        if module != 0:
            result += list[-module:]

        return self.listToNode(result)
            


    def listToNode(self, nums):
        if len(nums) > 0:
            node = ListNode(nums[0], self.listToNode(nums[1:]))
            return node
        return None

    def nodeToList(self, node):
        result = [node.val]
        while node.next:
            node = node.next
            result.append(node.val)
        return result

if __name__ == '__main__':
    solution = Solution()
    l = solution.listToNode([1,2,3,4,5,6])
    print(solution.reverseKGroup(l, 2))