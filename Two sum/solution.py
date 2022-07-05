class Solution:
    def twoSum(self, nums: list , target: int) -> list:
        hashTable = []

        for i, element in enumerate(nums):
            sumMinusElement = target - element

            if (sumMinusElement in hashTable): 
                return [i, nums.index(sumMinusElement)][::-1]

            hashTable.append(element)
            


if __name__ == '__main__':
    solution = Solution()
    result = solution.twoSum([0,4,3,0], 0)
    print(result)