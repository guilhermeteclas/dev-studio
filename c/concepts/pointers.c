#include <stdio.h>

int multiply(int *a, int *b) { return (*a) * (*b); }

void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

void bubbleSort(int *arr, int n)
{
    for (int i = 0; i < n - 1; i++)
    {
        for (int j = 0; j < n - i - 1; j++)
        {
            if (*(arr + j) > *(arr + j + 1))
            {
                swap(&arr[j], &arr[j + 1]);
            }
        }
    }
}

void printArray(int *arr, int size)
{
    for (int i = 0; i < size; i++)
    {
        printf("%d ", *(arr + i));
    }
    printf("\n");
}

int main()
{
    int num = 10;
    int *ptr = &num;

    printf("Address of num: %p\n", (void *)&num);
    printf("Value of ptr (address of num): %p\n", (void *)ptr);
    printf("Value at ptr (value of num): %d\n", *ptr);

    *ptr = 20;

    printf("New value of num: %d\n", num); // num is now 20
    printf("New value at ptr: %d\n", *ptr);

    int num1 = 7, num2 = 8;
    int result = multiply(&num1, &num2);
    printf("The product of %d and %d is: %d\n", num1, num2, result);

    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("Array lenght : %d\n", n);

    printf("Original array: ");
    printArray(arr, n);

    bubbleSort(arr, n);

    printf("Sorted array: ");
    printArray(arr, n);

    return 0;
}
