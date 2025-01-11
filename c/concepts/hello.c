#include <stdio.h>

int number = 7;
float temperature = 23.5;
char scale = 'C';
char name[] = "Celsius";

void show_temperature()
{

    if (scale == 'C')
    {
        printf("Temperature: %.1f %c \n", temperature, scale);
    }
    else
    {
        printf("Scale not found.\n");
    }
}

typedef struct
{
    char name[50];
    int age;
    float height;
} Person;

void printPerson(Person p)
{
    printf("Name: %s\n", p.name);
    printf("Age: %d\n", p.age);
}

int main()
{
    show_temperature();

    Person me = {"Guilherme", 34};
    Person her = {"Bea", 27};
    printPerson(me);
    printPerson(her);

    int numbers[5] = {1, 2, 3, 4, 5};
    for (int i = 0; i < 5; i++)
    {
        printf("%d\n", numbers[i]);
    }

    // Pointers
    int value = 10;
    int *ptr = &value;

    printf("Value: %d\n", *ptr);

    // File I/O
    FILE *file = fopen("example.txt", "w");
    

    if (file != NULL)
    {
        fprintf(file, "Hello, File!\n");
        fclose(file);
    }
    else
    {
        printf("Error opening file.\n");
    }

    return 0;
}