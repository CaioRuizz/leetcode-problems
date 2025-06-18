from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pivot = strs[0]
        prefix = ''
        for char in pivot:
            case = prefix + char
            if all([s.startswith(case) for s in strs]):
                prefix = case
            else:
                break
        return prefix

if __name__ == '__main__':
    solution = Solution()
    print(solution.longestCommonPrefix(["flower","flow","flight"]))