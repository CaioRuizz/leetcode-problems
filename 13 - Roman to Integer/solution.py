class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        # instead of creating conditions to detect subtractions like IV, i will just replace then with other symbol

        # IV
        values['4'] = 4
        s = s.replace('IV', '4')

        # IZ
        values['9'] = 9
        s = s.replace('IX', '9')

        # XL
        values['F'] = 40
        s = s.replace('XL', 'F')

        # XC
        values['N'] = 90
        s = s.replace('XC', 'N')

        # CD
        values['Q'] = 400
        s = s.replace('CD', 'Q')

        # CM
        values['Z'] = 900
        s = s.replace('CM', 'Z')

        result = 0

        for char in s:
            result += values[char]

        return result

if __name__ == '__main__':
    solution = Solution()
    result = solution.romanToInt('MCMXCIV')
    print(result)