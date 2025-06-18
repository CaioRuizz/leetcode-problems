#include <stdio.h>
#include <stdlib.h>

void quicksort(int* nums, int left, int right) {
    if (left >= right) return;
    int pivot = nums[right];
    int i = left, j;
    for (j = left; j < right; j++) {
        if (nums[j] < pivot) {
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
            i++;
        }
    }
    int temp = nums[i];
    nums[i] = nums[right];
    nums[right] = temp;
    quicksort(nums, left, i - 1);
    quicksort(nums, i + 1, right);
}

int threeSumClosest(int* nums, int numsSize, int target) {
    int left;
    int right;
    int currentSum;
    int currentDiff;
    int minimumDiff = __INT16_MAX__;
    int closestSum = __INT16_MAX__;
    
    if (numsSize == 3) {
        return nums[0] + nums[1] + nums[2];
    }

    quicksort(nums, 0, numsSize -1);

    for (int i = 0; i < numsSize -2; i++) {
        left = i + 1;
        right = numsSize - 1;

        while (left < right) {
            currentSum = nums[i] + nums[left] + nums[right];
            currentDiff = abs(currentSum - target);

            if (currentDiff < minimumDiff) {
                minimumDiff = currentDiff;
                closestSum = currentSum;
            }

            if (currentSum < target) {
                left++;
            } else {
                right--;
            }
        }
    }
    return closestSum;
}

int main() {
    int nums[] = {-1, 2, 1, -4};
    int numsSize = sizeof(nums) / sizeof(nums[0]);
    int target = 1;
    int result = threeSumClosest(nums, numsSize, target);
    printf("Output: %d\n", result); // Esperado: 2
    return 0;
}