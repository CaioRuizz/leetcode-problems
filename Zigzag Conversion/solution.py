class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        splited_result = [[] for _ in range(numRows)]

        index = 0

        positive = True

        for char in s:
            splited_result[index].append(char)
            if positive:
                index += 1
            else:
                index -= 1
            if index == 0 or index == numRows - 1:
                positive = not positive

        result = ''

        for row in splited_result:
            result += ''.join(row)

        return result

        

if __name__ == '__main__':
    solution = Solution()
    print(solution.convert("PAYPALISHIRING", 4))