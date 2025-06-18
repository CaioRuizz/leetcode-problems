from itertools import combinations
from timeit import repeat
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []

        letters = {
            "2" : ["a", "b", "c"],
            "3" : ["d", "e", "f"],
            "4" : ["g", "h", "i"],
            "5" : ["j", "k", "l"],
            "6" : ["m", "n", "o"],
            "7" : ["p", "q", "r", "s"],
            "8" : ["t", "u", "v"],
            "9" : ["w", "x", "y", "z"],
        }

        amount_of_combinations = 1

        for digit in digits:
            amount_of_combinations *= len(letters[digit])

        combinations = ['' for _ in range(amount_of_combinations)]

        repeat = amount_of_combinations

        for _, digit in enumerate(digits):
            pointer = 0
            amount_of_letters = len(letters[digit])
            repeat //= amount_of_letters
            while pointer < amount_of_combinations:
                letter_position = (pointer // repeat) % amount_of_letters
                combinations[pointer] += letters[digit][letter_position]
                pointer += 1

        return combinations
        

if __name__ == '__main__':
    solution = Solution()
    print(solution.letterCombinations("234"))