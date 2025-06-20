#include <stdio.h>

int mySqrt(int x) {
    if (x == 1) return 1;
    long aux = 1;
    long sum = 0;
    int counter = 0;
    while(1) {
        sum += aux;
        if (sum > x) {
            return counter;
        }
        aux += 2;
        counter++;
    }
}

int main() {
    printf("%d\n", mySqrt(9));
}