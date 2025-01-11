#include <stdio.h>

int main() {
    int num = 10;
    int *ptr = &num;  // &num gives the address of num, which is stored in ptr

    printf("Address of num: %p\n", (void*)&num);
    printf("Value of ptr (address of num): %p\n", (void*)ptr);
    printf("Value at ptr (value of num): %d\n", *ptr);

    *ptr = 20;  // Modify the value at the address pointed to by ptr

    printf("New value of num: %d\n", num);  // num is now 20
    printf("New value at ptr: %d\n", *ptr);

    return 0;
}
