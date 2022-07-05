class Solution:
    def reverse(self, x: int) -> int:
        s = f'{x}'[::-1]
        if s[-1] == '-':
            s = '-' + s[:-1]
        result = int(s)
        return result if (result > (-2**31) and result < (2**31) -1) else 0

        

if __name__ == '__main__':
    solution = Solution()
    print(solution.reverse(-53))