class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ']': '[',
            ')': '(',
            '}': '{',
        }
        openingChar = []
        for char in s:
            if char in ['(', '{', '[']:
                openingChar.append(char)
            else:
                if openingChar == []:
                    return False
                if openingChar.pop() != pairs[char]:
                    return False
        return len(openingChar) == 0

if __name__ == '__main__':
    solution = Solution()
    print(solution.isValid('{}()({)'))