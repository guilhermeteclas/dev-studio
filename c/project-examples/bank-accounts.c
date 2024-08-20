#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <time.h>

typedef struct
{
    int id;
    char name[50];
    float balance;
} Account;

char filename[100];

char *getDateTime()
{
    time_t now = time(NULL);
    struct tm *tm = localtime(&now);
    static char buffer[80];
    strftime(buffer, sizeof(buffer), "%d/%m/%Y %H:%M:%S", tm);
    return buffer;
}

void createFile(Account acc)
{
    strcpy(filename, acc.name);
    strcat(filename, ".txt");

    FILE *file = fopen(filename, "w");
    char *now = getDateTime();

    if (file != NULL)
    {
        fprintf(file, ":: %s\n", now);
        fprintf(file, "Account ID: %d\n", acc.id);
        fprintf(file, "Account Name: %s\n", acc.name);
        fprintf(file, "Balance: %.2f\n", acc.balance);
        fprintf(file, "\n");
        fclose(file);
    }
    else
    {
        printf("Error opening file.\n");
    }
}

void createAccount(Account *acc)
{
    acc->id = rand();
    printf("Enter account name: ");
    scanf("%s", acc->name);
    acc->balance = 0.0;
    createFile(*acc);
}

void deposit(Account *acc, float amount)
{
    acc->balance += amount;
    printf("Deposited: %.2f\n", amount);

    FILE *file = fopen(filename, "a");
    char *now = getDateTime();

    fprintf(file, ":: %s\n", now);
    fprintf(file, "Deposit: %.2f\n", amount);
    fprintf(file, "Balance: %.2f\n", acc->balance);
    fprintf(file, "\n");
    fclose(file);
}

void withdraw(Account *acc, float amount)
{
    if (amount > acc->balance)
    {
        printf("Insufficient funds!\n");
    }
    else
    {
        acc->balance -= amount;
        printf("Withdrew: %.2f\n", amount);

        FILE *file = fopen(filename, "a");
        char *now = getDateTime();

        fprintf(file, ":: %s\n", now);
        fprintf(file, "Withdraw: %.2f\n", amount);
        fprintf(file, "Balance: %.2f\n", acc->balance);
        fprintf(file, "\n");
        fclose(file);
    }
}

void printAccount()
{
    char search[50];
    char filename[60];

    printf("Search account name: ");
    scanf("%s", search);

    strcpy(filename, search);
    strcat(filename, ".txt");

    FILE *file = fopen(filename, "r");

    if (file != NULL)
    {
        printf("Account found ->\n");
        char line[100];
        while (fgets(line, sizeof(line), file) != NULL)
        {
            printf("%s", line);
        }
        printf("\n");
        fclose(file);
    }
    else
    {
        printf("Not found.\n");
    }
}

int main()
{
    Account myAccount;
    int option;
    int isRunning = 1;
    float amount;

    while (isRunning == 1)
    {
        printf(":: BANK MENU ::\n");
        printf("1 - Create\n");
        printf("2 - Deposit\n");
        printf("3 - Withdraw\n");
        printf("4 - View\n");
        printf("0 - Exit\n");
        scanf("%d", &option);
        printf("You entered: %d\n", option);

        switch (option)
        {
        case 1:
            createAccount(&myAccount);
            break;
        case 2:
            printf("Value:\n");
            scanf("%f", &amount);
            deposit(&myAccount, amount);
            break;
        case 3:
            printf("Value:\n");
            scanf("%f", &amount);
            withdraw(&myAccount, amount);
            break;
        case 4:
            printAccount();
            break;
        case 0:
            printf("App closed.\n");
            isRunning = 0;
            break;
        default:
            printf("Invalid option. Try again.\n");
        }
    }

    return 0;
}