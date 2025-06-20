#include <stdio.h>

int pivotInteger(int n) {
    if (n == 1) {
        return 1;
    }
    
    int left = 1;
    int right = (n * (n + 1)) / 2;

    int pivot = 2;

    while (pivot < n) {
        if (left == right) return --pivot;
        left += pivot;
        right -= pivot - 1;
        pivot++;
    }

    return -1;
}

int main() {
    printf("%d\n", pivotInteger(8));
}