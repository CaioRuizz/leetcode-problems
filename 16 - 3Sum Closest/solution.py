import math
from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) == 3:
            return sum(nums)
        
        nums.sort()

        final = len(nums)
        
        minimum_diff = math.inf

        closest_sum = math.inf

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                current_diff = abs(current_sum - target)

                if current_diff < minimum_diff:
                    minimum_diff = current_diff
                    closest_sum = current_sum

                if current_sum < target:
                    left += 1
                else:
                    right -= 1
        
        return closest_sum


if __name__ == '__main__':
    solution = Solution()
    print(solution.threeSumClosest([-1,2,1,-4], 1))

        