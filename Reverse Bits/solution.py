class Solution:
    def reverseBits(self, n: int) -> int:
        b_str = f'{n:b}'
        b_str = ('0' * (32 - len(b_str))) + b_str
        b_str = b_str[::-1]
        return int(b_str, 2)

if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseBits(2))