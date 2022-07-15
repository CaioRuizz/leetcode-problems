from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        result = []
        self._generateParenthesis(n, n, "", result)
        return result

    def _generateParenthesis(self, left, right, temp, result):
        if left == 0 and right == 0:
            result.append(temp)
            return
        if left>0:
            self._generateParenthesis(left - 1, right, temp + '(', result)
        if right > left:
            self._generateParenthesis(left, right - 1, temp + ')', result)

if __name__ == '__main__':
    solution = Solution()
    print(solution.generateParenthesis(3))