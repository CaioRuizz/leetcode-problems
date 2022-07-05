class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binary = f'{n:b}'
        last = None
        for char in binary:
            if char == last:
                return False
            last = char
        return True

if __name__ == '__main__':
    solution = Solution()
    print(solution.hasAlternatingBits(5))